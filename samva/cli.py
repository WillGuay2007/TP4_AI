from .data import load_data
from .model import get_model
from sklearn.model_selection import train_test_split
import numpy
import sys
import tensorflow as tf
from pathlib import Path

MODEL_SAVE_PATH = "model.keras"
TEST_SIZE = 0.2
EPOCHS = 10

def main():
    dataset_path = sys.argv[1] if len(sys.argv) > 1 else ""
    if len(dataset_path) == 0:
        print("Please enter dataset path")
        return
    images, labels = load_data(Path(dataset_path))
    print("Loading images and labels...")
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
    numpy.array(images), numpy.array(labels), test_size =
    TEST_SIZE)
    model = get_model()
    print("Training model...")
    model.fit(x_train, y_train, epochs=EPOCHS)
    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
    print("Test loss:", test_loss)
    print("Test accuracy:", test_accuracy)

    model.save(MODEL_SAVE_PATH)
