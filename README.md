Image Classification Using a Pretrained Model
Internship Project
Organization: CodeOrbit Tech
Project: Image Classification Using a Pretrained Model

1.Project Overview

This project demonstrates image classification using  a pretrained deep learning model. Instead of training a model from Scratch, the project uses MobileNetV2, a pretrained model available through PyTorch and Torchvision.

The model takes an input image, processes it, and predicts the most likely object or category present in the image.

2.Objective

The objective of this project is to understand how a pretrained image-classification model can be used to classify new images and display the predicted class along with its confidence score.

3. Technologies Used

Python
PyTorch
Tochvision 
Pillow(PIL)
MobileNetV2

4. How the project works

The Pretrained MobileNetV2 model is loaded.
The input image is loaded using Pillow.
The image is resized and normalized using the preprocessing steps provided by the model.
The processed image is passed to MobileNetV2.
The model predicts the most likely class.
SoftMax is used to calculate the prediction probability.
The predicted class and confidence percentage are displayed.

5. Pretrained Model

MobileNetV2 is a lightweight convolutional neural network designed for efficient image classification.

A pretrained model has already learned useful visual patterns from large dataset. This allows us to use the model for classifying new images without training the entire model from beginning.

I selected MobileNetV2 because it is lightweight, efficient, and suitable for running on a CPU-based system.

6. Sample Result

The model successfully classified the sample image.

Example Output:

Predicted class:  golden retriever
Confidence: 35.88%

The prediction may vary depending on the input image.

7. Project Files

CodeOrbit_Image_Classification
|
|--- image_classifier.py
|--- sample.jpg
|--- README.md

8. How to Run

Make sure Python, PyTorch, Torchvision, and Pillow are installed.

Open Command Prompt in the project folder and run:

py image_classifier.py

The program will display the predicted class and confidence percentage.

9. Conclusion

This project helped me understand the basic workflow of image classification using a pretrained deep learning model. I learned how to load a pretrained model, preprocess an image, perform prediction, and calculate the confidence of the prediction. 

