class ResponseError(Exception):
    """Raised when the bittrex API returns an
    error in the message response"""

class RequestError(Exception):
    """Raised when the request towards the bittrex
    API is incorrect or fails"""
