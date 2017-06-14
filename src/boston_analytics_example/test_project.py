import unittest
import boston_analytics_example
from boston_analytics_example import load_data_collection, Response, get_public_request, ResponseWriter
from boston_analytics_example.errors import InvalidDataCollectionYAMLFileSchema
import os
valid_document = """
data_sources:
   MARoadwayEvents:
      url: "https://www.massdot.state.ma.us/feeds/MARoadwayEventsXML.aspx"
      authRequired: False
      responseType: 'xml'
   MassDotRTTMFeed:
      url: "https://www.massdot.state.ma.us/feeds/traveltimes/RTTM_feed.aspx"
      authRequired: False
      responseType: 'xml'
   BostonPoliceIncidents:
      url: "https://data.cityofboston.gov/resource/29yf-ye7n.json"
      authRequired: False
      responseType: 'json'
   VisionZeroResidentSubmissions:
      url: "http://bostonopendata.boston.opendata.arcgis.com/datasets/5bed19f1f9cb41329adbafbd8ad260e5_0.geojson"
      authRequired: False
      responseType: 'json'
"""

broken_document = """
  hello_im_broken:
   MARoadwayEvents:
      authRequired: False
   MassDotRTTMFeed:
      url: "https://www.massdot.state.ma.us/feeds/traveltimes/RTTM_feed.aspx"
      authRequired: False
   BostonPoliceIncidents:
      authRequired: False
   VisionZeroResidentSubmissions:
      url: "http://bostonopendata.boston.opendata.arcgis.com/datasets/5bed19f1f9cb41329adbafbd8ad260e5_0.geojson"
"""


class LoadingDataSources(unittest.TestCase):
    def test_valid_document_is_parsed(self):
        parsed_data = load_data_collection(valid_document)
        for source in parsed_data:
            self.assertIsInstance(source, boston_analytics_example.DataSource)

    def test_broken_document(self):
        self.assertRaises(InvalidDataCollectionYAMLFileSchema,
                          load_data_collection, broken_document)


class QueryingDataSources(unittest.TestCase):
    def test_get_public_request(self):
        sources = load_data_collection(valid_document)
        self.assertIsInstance(get_public_request(sources[2]), Response)


class ResponsesWellFormed(unittest.TestCase):
    def setUp(self):
        self.sources = load_data_collection(valid_document)
        self.simple_response = get_public_request(self.sources[2])

    def test_key_evaluation(self):
        print(self.simple_response.get_key())
        self.assertIsInstance(self.simple_response.get_key(), str)


class ResponseWriterCanSave(unittest.TestCase):
    def setUp(self):
        self.sources = load_data_collection(valid_document)
        self.simple_response = get_public_request(self.sources[2])

    def test_save_locally(self):
        response_files = ResponseWriter()
        response_files.save_locally(self.simple_response)
        expected_key = f'{response_files.local_file_dir}/' \
                       f'{self.simple_response.get_key()}'
        self.assertTrue(os.path.isfile(expected_key))
