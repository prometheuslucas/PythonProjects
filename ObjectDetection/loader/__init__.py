# Loader package for infrastructure loaders (empty for now)
from typing import Optional

class ImageData:
    """
    Domain primitive for image data and related operations.
    """
    def __init__(self, path: str, data: Optional[any]):
        self.path = path
        self.data = data

    def is_valid(self) -> bool:
        return self.data is not None

