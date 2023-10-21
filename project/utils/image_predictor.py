import tensorflow as tf
import pathlib
import numpy as np

def predict_image():

    pred_dict = {"ADVE":0,
    "Email":0,         
    "Empty_papers":0,
    "Form":0,          
    "Letter":0,        
    "Memo":0,          
    "News":0,
    "Note":0,          
    "Receipts":0,      
    "Report":0,        
    "Resume":0,
    "Scientific":0,}

    full_model_saving_path = pathlib.Path('/home/samer/Desktop/Beedoo/Expenses_tracker_stuff/expenses_tracker_model.h5')
    loaded_model = tf.keras.models.load_model(full_model_saving_path, compile=True)
    pred_img_path = pathlib.Path('/home/samer/Desktop/Beedoo/Expenses_tracker/project/utils/Images/')


    loaded_model.compile(
        optimizer = tf.keras.optimizers.Adam(learning_rate = 0.0005),        # compiling with low learning rate
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits= True),
        metrics=['accuracy'],
        run_eagerly = False)

    dataset_pathy = tf.keras.utils.image_dataset_from_directory(
        pred_img_path,
        labels= 'inferred',
        seed= 1,
        batch_size=1,
        image_size=(300, 300),
        color_mode="rgb",
        shuffle=False)


    sample_list = []                                                        # creating a list of sample(s)
    for sample, _ in dataset_pathy:
        sample_list.append(sample)
        continue

    class_dict = {0:"ADVE",
    1:"Email",         #
    2:"Empty_papers",
    3:"Form",          #
    4:"Letter",        #
    5:"Memo",          #
    6:"News",
    7:"Note",          #
    8:"Receipts",      #
    9:"Report",        #
    10:"Resume",
    11:"Scientific",}

    sample_list = np.array(sample_list)
    for sample in sample_list:
        predictions = loaded_model.predict(sample)
        pred = np.argmax(predictions, axis=1)
        pred_dict.update({class_dict.get(pred[0]):pred_dict[class_dict.get(pred[0])]+1})

    return pred_dict

if __name__ == "__main__":
    predict_image()
    
