from domain.image_data import ImageData
from domain.yolo_label import YoloLabel
from domain.exceptions.image_data_exception import InvalidImageDataException
from domain.exceptions.yolo_label_exception import InvalidYoloLabelException
import numpy as np

def test_image_data_valid():
    print("Running test_image_data_valid...")
    arr = np.zeros((100, 100, 3))
    img = ImageData("test.jpg", arr)
    assert img.is_valid()
    assert img.get_shape() == (100, 100, 3)
    print("test_image_data_valid passed.")

def test_image_data_invalid():
    print("Running test_image_data_invalid...")
    try:
        img = ImageData("test.jpg", None)
    except InvalidImageDataException:
        print("test_image_data_invalid passed.")

def test_yolo_label_valid():
    print("Running test_yolo_label_valid...")
    label = YoloLabel(0, 0.5, 0.5, 0.2, 0.2)
    assert label.is_valid()
    print("test_yolo_label_valid passed.")

def test_yolo_label_invalid():
    print("Running test_yolo_label_invalid...")
    try:
        label = YoloLabel(0, 1.5, 0.5, 0.2, 0.2)
    except InvalidYoloLabelException:
        print("test_yolo_label_invalid passed.")

def test_yolo_label_from_list():
    print("Running test_yolo_label_from_list...")
    label = YoloLabel.from_list([0, 0.5, 0.5, 0.2, 0.2])
    assert label.is_valid()
    print("test_yolo_label_from_list passed.")

if __name__ == "__main__":
    test_image_data_valid()
    test_image_data_invalid()
    test_yolo_label_valid()
    test_yolo_label_invalid()
    test_yolo_label_from_list()
    print("All domain primitive tests completed.")

