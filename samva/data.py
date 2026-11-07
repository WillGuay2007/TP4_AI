import numpy

IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43

from pathlib import Path
import cv2

def load_data(dataset_path: Path) -> tuple[list[numpy.ndarray], list[int]]:

    category_list = []
    img_list = []

    for category in range(NUM_CATEGORIES):
        category_path = dataset_path / str(category)
        for file in category_path.iterdir():
            img = cv2.imread(str(file))
            if img is None:
                continue
            resized = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            normalized = resized / 255
            category_list.append(category)
            img_list.append(normalized)

    return img_list, category_list
