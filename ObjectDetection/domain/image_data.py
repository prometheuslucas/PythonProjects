from typing import Optional
from domain.exceptions.image_data_exception import InvalidImageDataException

class ImageData:
    """
    Domain primitive for image data and related operations.
    """
    def __init__(self, image_path: str, image_array: Optional[any]):
        self.image_path = image_path
        self.image_array = image_array
        if not self.is_valid():
            raise InvalidImageDataException(f"Invalid image data for path: {image_path}")

    def is_valid(self) -> bool:
        return self.image_array is not None

    def get_shape(self):
        if self.is_valid():
            return self.image_array.shape
        return None
