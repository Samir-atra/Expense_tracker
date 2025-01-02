"""
load the images in the given directory and predict the classes 
of the images using the model saved
"""

import pathlib
import os
import sys
import tensorflow as tf
import numpy as np


def predict_image():
    """
    predict the classes of the images using the model saved in the full_mode_saving_path

    Returns:
        pred_dict: a dictionary of the classes and the number of images predicted to be in each
    """
    path = os.getcwd()
    pred_dict = {
        "ADVE": 0,
        "Email": 0,
        "Empty_papers": 0,
        "Form": 0,
        "Letter": 0,
        "Memo": 0,
        "News": 0,
        "Note": 0,
        "Receipts": 0,
        "Report": 0,
        "Resume": 0,
        "Scientific": 0,
    }

    model_path = input(
        "Please input the full path to the h5 model to be used for prediction."
    )
    # "/home/samer/Desktop/Beedoo/Expenses_tracker_stuff/expenses_tracker_model.h5"
    full_model_saving_path = pathlib.Path(model_path)
    loaded_model = tf.keras.models.load_model(full_model_saving_path, compile=True)
    pred_img_path = pathlib.Path(f"{path}/Images/")

    loaded_model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=0.0005
        ),  # compiling with low learning rate
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"],
        run_eagerly=False,
    )
    try:
        dataset_pathy = tf.keras.utils.image_dataset_from_directory(
            pred_img_path,
            labels="inferred",
            seed=1,
            batch_size=1,
            image_size=(300, 300),
            color_mode="rgb",
            shuffle=False,
        )
    except ValueError:
        sys.exit("Please, add images to the directory, to be classified")

    sample_list = []  # creating a list of sample(s)
    for sample, _ in dataset_pathy:
        sample_list.append(sample)
        continue

    class_dict = {
        0: "ADVE",
        1: "Email",
        2: "Empty_papers",
        3: "Form",
        4: "Letter",
        5: "Memo",
        6: "News",
        7: "Note",
        8: "Receipts",
        9: "Report",
        10: "Resume",
        11: "Scientific",
    }

    sample_list = np.array(sample_list)

    for sample in sample_list:
        predictions = loaded_model.predict(sample)
        pred = np.argmax(predictions, axis=1)
        pred_dict.update(
            {class_dict.get(pred[0]): pred_dict[class_dict.get(pred[0])] + 1}
        )

    return pred_dict


if __name__ == "__main__":
    predict_image()
