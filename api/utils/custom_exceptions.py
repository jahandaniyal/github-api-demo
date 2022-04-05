class ResourceNotAvailable(Exception):
    """Exception raised for GitHub API calls.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message, status_code=404):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

