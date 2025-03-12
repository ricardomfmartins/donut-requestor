class BoxIsFullException(Exception):
    def __init__(self, message: str, code=400):
        super().__init__(message)
        self.code = code
