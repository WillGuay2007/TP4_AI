import tensorflow as tf
import samva.config as cfg

def get_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(cfg.IMG_WIDTH, cfg.IMG_HEIGHT, 3)),
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(cfg.NUM_CATEGORIES, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model