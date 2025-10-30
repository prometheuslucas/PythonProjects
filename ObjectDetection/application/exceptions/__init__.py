# Application exceptions package init
#
# Project Features and Major Changes (since creation):
#
# Features:
# - Object detection project initialization
# - YOLO dataset loader implemented as a class
# - Domain primitives: ImageData and YoloLabel classes
# - Custom exception classes for domain primitives (InvalidImageDataException, InvalidYoloLabelException)
# - Custom exception class for application layer (YoloDatasetLoaderException)
# - Modular folder structure: domain/, application/, loader/, tests/
# - Test suite for domain and application primitives
# - Script to run all tests and print results
#
# Refactors and Improvements:
# - Moved exception classes to their own files and folders
# - Cleaned up duplicate and obsolete files
# - Ensured all folders are Python packages with __init__.py
# - Updated naming conventions for clarity and SOLID principles
# - Verified all tests pass and imports are correct
#
# (This comment documents the main features and refactors since project creation)
