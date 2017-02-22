import arrow
import attr
import os

import requests
import yaml
from boston_analytics_example.errors import InvalidDataCollectionYAMLFileSchema, RequestFailure, S3ConnectionNotFound
from cerberus import Validator
import hashlib
import jsonpickle


def collect_data(data_source):
    data_source = DataSource.from_json(data_source)
    if not data_source.authRequired:
        print(f'Requesting data from: {data_source.source}')
        result = get_public_request(data_source)
        return result

    else:
        raise NotImplementedError


def store_data(response):
    print(f'Received a response from a data sources')
    response = Response.from_json(response)
    print(f'Preparing to write data from {response.data_source}')
    writer = ResponseWriter()
    writer.save_locally(response)


@attr.s
class Response(object):
    data_source = attr.ib()
    created = attr.ib()
    content = attr.ib()
    id = attr.ib(init=False)

    def hash_id(self):
        h = hashlib.sha256()
        h.update(str(self.created.timestamp).encode('utf-8'))
        h.update(self.data_source.source.encode('utf-8'))
        h.update(self.data_source.url.encode('utf-8'))
        return h.hexdigest()

    def __attrs_post_init__(self):
        self.id = self.hash_id()

    def get_key(self, prefix=None):
        if prefix is None:
            prefix = self.data_source.source
        response_id = self.id
        response_type = self.data_source.responseType
        return f"{prefix}-{response_id}.{response_type}"

    def to_json(self):
        return jsonpickle.encode(self)

    @staticmethod
    def from_json(response):
        return jsonpickle.decode(response)

@attr.s
class ResponseWriter(object):
    bucket = attr.ib(default=None)
    s3conn = attr.ib(default=None)
    local_file_dir = attr.ib(default='/tmp/')

    def save_to_s3(self, bucket=None):
        if self.s3conn is not None:
            pass
        else:
            raise S3ConnectionNotFound

    def save_locally(self, response):
        full_path = f"{self.local_file_dir}/{response.get_key()}"
        with open(full_path, 'w') as f:
            f.write(str(response.content))




@attr.s
class DataCollectionSources(object):
    sources = attr.ib()


@attr.s
class DataSource(object):
    source = attr.ib()
    url = attr.ib()
    responseType = attr.ib()
    authRequired = attr.ib(validator=attr.validators.instance_of(bool))
    apiKey = attr.ib()
    _key = attr.ib(default=None)

    def _load_api_key(self):
        if self.authRequired:
            self._key = os.environ.get(self.apiKey)

    def to_json(self):
        return jsonpickle.encode(self)

    @staticmethod
    def from_json(data):
        return jsonpickle.decode(data)

def load_data_collection(document):
    document = yaml.safe_load(document)
    sources = []
    expected_yaml_schema = {
        'data_sources': {
            'type': 'dict',
            'valueschema': {
                'type': 'dict',
                'schema': {
                     'url': {'type': 'string', 'required': True},
                     'authRequired': {'type': 'boolean', 'required': True},
                     'apiKey': {'required': False, 'type': 'string'},
                    'responseType': {'required': True,
                                     'type': 'string',
                                     'allowed': ['xml', 'json']}
                 }

            }
        }
    }
    v = Validator(expected_yaml_schema)
    if v.validate(document):
        for source, data in document["data_sources"].items():
            data = DataSource(source=source,
                              url=data.get('url', None),
                              authRequired=data.get('authRequired', False),
                              apiKey=data.get('apiKey', None),
                              responseType=data.get('responseType', None))
            sources.append(data)
        return sources
    else:
        raise InvalidDataCollectionYAMLFileSchema


def get_public_request(data_source, timeout=30):
    try:
        r = requests.get(data_source.url, timeout=timeout)
        return Response(data_source, arrow.utcnow(), r.content)
    except Exception as err:
        raise RequestFailure(err)


def get_auth_request(data_source):
    return Exception