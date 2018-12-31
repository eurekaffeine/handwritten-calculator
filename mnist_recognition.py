from keras import backend as K
from keras.models import load_model
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# This is class mainly recognizes the digit patterns drawn on the canvas based on the pre-trained model

class mnist_recognition:

    # Load the pre-trained ConvNet model
    def __init__(self):
        K.set_image_dim_ordering('th')
        self.my_model = load_model('mnist_model.h5')

    # Feed in the drawn image and get the predicted result back
    def read_img(self, img):

        img = img.resize((28, 28))
        w, h = img.size
        img = img.convert("L")
        # print(img)
        data = img.getdata()
        data = np.matrix(data, dtype='float') / 255.0
        new_data = np.reshape(data * 255.0, (w, h))
        new_data = new_data[np.newaxis, np.newaxis, :]
        pred = self.my_model.predict(new_data)
        res = np.argmax([pred[0]])
        return res

# if __name__ == '__main__':
    # img = Image.open('digit.png')
    # Recognition().read_img(img)