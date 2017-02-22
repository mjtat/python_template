import attr

@attr.s
class BostonAnalyticsExampleError(Exception):
    """
    Base class for exceptions in this module
    """
    pass


@attr.s
class InvalidDataCollectionYAMLFileSchema(BostonAnalyticsExampleError):
    """
      The yaml document provided does not match the expected
    schema
    """


@attr.s
class RequestFailure(BostonAnalyticsExampleError):
    """
     There was an issue reading the request
    """
    message = attr.ib()


@attr.s
class S3ConnectionNotFound(BostonAnalyticsExampleError):
    """
     an S3 connection was required and not provided.
    """