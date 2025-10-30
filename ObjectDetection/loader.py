import cv2
import glob
import os
from typing import List, Tuple, Optional
from domain.image_data import ImageData
from domain.yolo_label import YoloLabel

class YoloDatasetLoader:
    """
    Loads images and YOLO-format labels for object detection training.
    Follows SOLID principles for extensibility and maintainability.
    """
    def __init__(self, images_dir: str, labels_dir: str, img_exts: Tuple[str, ...] = (".jpg", ".png")):
        self.images_dir = images_dir
        self.labels_dir = labels_dir
        self.img_exts = img_exts

    def load(self) -> List[Tuple[ImageData, List[YoloLabel]]]:
        """
        Loads images and their YOLO-format labels.
        Returns:
            List of (ImageData, [YoloLabel, ...]) tuples.
        """
        dataset = []
        for ext in self.img_exts:
            for img_path in glob.glob(os.path.join(self.images_dir, f"*{ext}")):
                img = cv2.imread(img_path)
                image_data = ImageData(img_path, img)
                base = os.path.splitext(os.path.basename(img_path))[0]
                label_path = os.path.join(self.labels_dir, base + ".txt")
                labels = []
                if os.path.exists(label_path):
                    with open(label_path, "r") as f:
                        for line in f:
                            parts = line.strip().split()
                            if len(parts) == 5:
                                try:
                                    label = YoloLabel.from_list([float(p) for p in parts])
                                    if label.is_valid():
                                        labels.append(label)
                                except ValueError:
                                    pass  # Optionally log or handle invalid label
                dataset.append((image_data, labels))
        return dataset
