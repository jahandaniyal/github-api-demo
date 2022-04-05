class ResourceNotAvailable(Exception):
    """Exception raised for GitHub API calls.

    Attributes:
        message -- explanation of the error
        status_code -- HTTP_STATUS_CODE of the error. [Default: 404]
    """
    def __init__(self, message, status_code=404):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

