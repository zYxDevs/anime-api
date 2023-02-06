"""
File containing generic exceptions for all the apis.
"""
import typing


class ServerError(Exception):
    """
    Errors from the server.
    """

    def __init__(
        self, status_code: int, msg: typing.Optional[str] = None, *args, **kwargs
    ):
        super().__init__(
            f"The server returned an error{f': {msg}' if msg else '.'} (Status code: {status_code})",
            *args,
            **kwargs,
        )


class UploadLimitExceeded(Exception):
    """
    Error raised when the upload limit is exceeded. This error is not necesarily from
    the server.
    """


class UnsupportedFileType(Exception):
    """
    Error raised when the file type is not supported by the API.
    """


class Forbidden(Exception):
    """
    Error raised when the user is not authorized to perform the action.
    """


class NotFound(ServerError):
    """
    Error raised when the item is not found.
    """

    def __init__(self, msg: typing.Optional[str] = "Not found", *args, **kwargs):
        ServerError.__init__(self, 404, msg, *args, **kwargs)
