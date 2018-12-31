import os
import cv2
import numpy as np
from PIL import Image
from keras.models import model_from_json
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# This is class mainly recognizes the operand patterns drawn on the canvas based on the pre-trained model
class OperandRecogniton:
    def __init__(self):
        json_file = open('operand_model.json', 'r')
        self.loaded_model_json = json_file.read()
        json_file.close()
        self.loaded_model = model_from_json(self.loaded_model_json)
        self.loaded_model.load_weights("operand_model.h5")

    def recognition(self, img):
        self.loaded_model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img,(100,100))
        img = img.reshape(1,100,100,1)
        result = str(np.argmax(self.loaded_model.predict(img)))
        if (result == "0"):
            result = "/"
        elif (result == "1"):
            result = "-"
        elif(result == "2"):
            result = "*"
        else:
            result = "+"
        return result

if __name__ == '__main__':
    OR = OperandRecogniton()
    img = Image.open("plus.png")
    res = OR.recognition(img)
    print(res)