from application.exceptions.yolo_dataset_loader_exception import YoloDatasetLoaderException

def test_yolo_dataset_loader_exception():
    with pytest.raises(YoloDatasetLoaderException):
        raise YoloDatasetLoaderException("This is a test exception")

