# TODO inherit desc from this error in whatever the Python way is.
class PuckError(Exception):
    """
    Generic Exception for errors in this project.

    Attributes:
        desc -- short message describing error
    """
    def __init__(self, desc):
        self.desc = desc


class MalformedSubscriptionError(PuckError):
    """
    Exception raised for badly formatted Subscription object.

    Attributes:
        desc -- short message describing error
    """
    def __init__(self, desc):
        self.desc = desc


class UnreachableFeedError(PuckError):
    """
    Exception raised for unreachable feeds.

    Attributes:
        desc -- short message describing error
        code -- HTTP error code, if applicable
        name -- HTTP error name, if applicable
    """
    def __init__(self, desc, code=None, name=None):
        self.desc = desc
        self.code = code
        self.name = name


class MalformedFeedError(PuckError):
    """
    Exception raised for malformed feeds that trips feedparser's bozo alert.

    Attributes:
        desc    -- short message describing error
        bozo_msg -- bozo exception message
    """
    def __init__(self, desc, bozo_msg):
        self.desc = desc
        self.bozo_msg = bozo_msg


class InvalidConfigError(PuckError):
    """
    Exception raised when the config file provides invalid options and we can't recover.

    Attributes:
        desc    -- short message describing error
    """
    def __init__(self, desc):
        self.desc = desc