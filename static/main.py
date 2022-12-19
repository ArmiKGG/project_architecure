
import numpy as np
import tensorflow as tf


class_names = ["sitting", "standing"]


img_height = 180
img_width = 180

TF_MODEL_FILE_PATH = 'model.tflite'

interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)

classify_lite = interpreter.get_signature_runner('serving_default')


def prep_img(path):
    img = tf.keras.utils.load_img(
        path, target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    return img_array


def predict(img_array):
    predictions_lite = classify_lite(sequential_1_input=img_array)['outputs']
    score_lite = tf.nn.softmax(predictions_lite)
    stringged = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score_lite) - 1], 100 * np.max(score_lite))
    return stringged


img = prep_img('./700-nw.jpg')
preds = predict(img)

print(preds)