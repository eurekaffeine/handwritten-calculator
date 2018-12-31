# handwritten-calculator
## Introduction
* This is the course project of ECE-6183 DSP Lab.
* We design a real-time handwritten calculator which can recognize handwritten digits as well as 4 basic operands, namely plus, minus, divide and mutiply. 
* We utilize Convolutional Neural Network to not only train the MNIST dataset but also our self-generated dataset of operands.
* We implement our project with `keras` frame based on `tensorflow` backend.
* The Graphic User Interface is mainly realized by `Tkinter` library.
* The interactive hand-writing and drawing part are realized with `PIL` library.

## Installation
* We compile and debug our project mainly on `python 3.6`
* The detailed installation tutorial of `keras` and `tensorflow` can be found in [keras](https://keras.io/) and [Tensorflow]( https://www.tensorflow.org/).
* In order to show the GUI and functionality of our calculator, please run the `main.py`.

## Descriptions
There are several `.py` files in our project. The detailed descriptions can be seen as follow:
* `main.py`: Main function of our project containing the GUI component
* `mnsit_train.py`: Training the dataset of MNIST and saving as a `mnist_model.h5` file for further usage.
* `mnist_recognition.py`: Recognition base on the `mnist_model.h5` file.
* `operand_train.py`: Training the dataset of MNIST and saving as `operand_model.h5` and `operand_model.json` files for further usage.
* `operand_recognition.py`: Recognition base on the `operand_model.h5` and `operand_model.json`file.

## Self-generated Dataset
* In this project, we generate the operand dataset by ourselves in the folder `data`.
* Its structure follows the recommendation of image preprocessing in keras. Please visit [here](https://keras.io/preprocessing/image/) for further information.