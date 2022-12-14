from typing import Dict, List, Tuple

from flask import current_app


class FilesizeLimitError(Exception):
    """Exception to handle exceed file limit"""

    def __init__(self, loc="file", msg="") -> None:
        self.loc = loc
        super().__init__(msg)

    def errors(self) -> List[Dict[str, str | Tuple]]:
        """Return error like pydantic `e.errors()` of type `List[DictErr]`"""
        filesize_limit = current_app.config["MAX_CONTENT_LENGTH"] / (1000 * 1000)
        return [
            {
                "loc": (self.loc,),
                "msg": f"File is too big. Limit is {filesize_limit}mb",
                "type": "type_error",
            }
        ]


class FormError(Exception):
    """Custom top level exception to agreggate lower level form errors"""

    def __init__(self, errors: List[Dict[str, List]], msg: str = ""):
        self.errors = errors
        self.msg = msg
        super().__init__(self.errors)

    def __str__(self) -> str:
        return str(self.errors)
