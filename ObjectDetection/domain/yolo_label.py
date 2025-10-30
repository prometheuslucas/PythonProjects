from domain.exceptions.yolo_label_exception import InvalidYoloLabelException


class YoloLabel:
    """
    Domain primitive for a single YOLO-format label.
    """
    def __init__(self, class_identifier: int, x_center: float, y_center: float, width: float, height: float):
        self.class_identifier = class_identifier
        self.x_center = x_center
        self.y_center = y_center
        self.width = width
        self.height = height
        if not self.is_valid():
            raise InvalidYoloLabelException(f"Invalid YOLO label values: {self.__dict__}")

    @classmethod
    def from_list(cls, values):
        if len(values) != 5:
            raise InvalidYoloLabelException("YOLO label must have 5 values.")
        return cls(int(values[0]), values[1], values[2], values[3], values[4])

    def is_valid(self) -> bool:
        return 0 <= self.x_center <= 1 and 0 <= self.y_center <= 1 and 0 < self.width <= 1 and 0 < self.height <= 1
