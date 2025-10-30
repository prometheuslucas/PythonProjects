# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from application.yolo_dataset_loader import YoloDatasetLoader


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def run_object_detection_application():
    """
    Main entry point for the object detection application.
    Uncomment and implement the following lines to run the full object detection pipeline.
    """
    images_directory = "images"  # Path to your images folder
    labels_directory = "labels"  # Path to your labels folder
    yolo_dataset_loader = YoloDatasetLoader(images_directory, labels_directory)
    dataset = yolo_dataset_loader.load()
    print(f"Loaded {len(dataset)} image-label pairs.")
    # TODO: Initialize and train YOLO model here
    # TODO: Run inference on new images
    # TODO: Evaluate results and visualize detections


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Entry point for the application
    run_object_detection_application()
    # To run tests, use: python tests/run_all_tests.py

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
