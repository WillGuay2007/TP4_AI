from .data import load_data
from .model import get_model
from sklearn.model_selection import train_test_split
import numpy
import tensorflow as tf
from pathlib import Path

DATASET_PATH = r"C:\Users\Willb\Downloads\gtsrb"
MODEL_SAVE_PATH = "model.keras"
TEST_SIZE = 0.2
EPOCHS = 10

def main():
    print("Main!")
    images, labels = load_data(Path(DATASET_PATH))
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
    numpy.array(images), numpy.array(labels), test_size =
    TEST_SIZE)
    model = get_model()
    model.summary()
    model.fit(x_train, y_train, epochs=EPOCHS)
    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
    print("Test loss:", test_loss)
    print("Test accuracy:", test_accuracy)

    model.save(MODEL_SAVE_PATH)
