import cv2  # OpenCV is a popular library for image processing. Install with: pip install opencv-python
import glob
import os
from typing import List, Tuple
from domain.image_data import ImageData
from domain.yolo_label import YoloLabel
from application.exceptions.yolo_dataset_loader_exception import YoloDatasetLoaderException

class YoloDatasetLoader:
    """
    Application service for loading images and YOLO-format labels for object detection training.
    Follows CLEAN and SOLID principles with descriptive naming and exception handling.
    """
    def __init__(self, images_directory: str, labels_directory: str, image_extensions: Tuple[str, ...] = (".jpg", ".png")):
        self.images_directory = images_directory
        self.labels_directory = labels_directory
        self.image_extensions = image_extensions

    def load(self) -> List[Tuple[ImageData, List[YoloLabel]]]:
        dataset = []
        for image_extension in self.image_extensions:
            for image_path in glob.glob(os.path.join(self.images_directory, f"*{image_extension}")):
                image_array = cv2.imread(image_path)
                try:
                    image_data = ImageData(image_path, image_array)
                except Exception as error:
                    raise YoloDatasetLoaderException(f"Failed to load image: {image_path}. Error: {error}")
                base_filename = os.path.splitext(os.path.basename(image_path))[0]
                label_path = os.path.join(self.labels_directory, base_filename + ".txt")
                yolo_labels = []
                if os.path.exists(label_path):
                    with open(label_path, "r") as label_file:
                        for line in label_file:
                            label_parts = line.strip().split()
                            if len(label_parts) == 5:
                                try:
                                    yolo_label = YoloLabel.from_list([float(part) for part in label_parts])
                                    yolo_labels.append(yolo_label)
                                except Exception as error:
                                    raise YoloDatasetLoaderException(f"Invalid label in {label_path}: {error}")
                dataset.append((image_data, yolo_labels))
        return dataset
