from.data import load_data
from pathlib import Path

DATASET_PATH = r"C:\Users\willb\Downloads\gtsrb"

def main():
    print("Main!")
    images, labels = load_data(Path(DATASET_PATH))