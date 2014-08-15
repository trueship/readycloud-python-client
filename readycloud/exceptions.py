from requests.exceptions import HTTPError


class ReadyCloudServerError(HTTPError):
    pass
