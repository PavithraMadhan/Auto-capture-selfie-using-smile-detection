# Auto-capture-selfie-using-smile-detection
Objective : To auto capture a selfie when a smile is detected while using a camera

Approach : Haar Cascade algorithm and Adaboost

Haar Cascade is an ML object detection algorithm used to identify objects in an image (treated as a matrix i.e. 2D grid here).In this algorithm, a cascade function is trained from a lot of positive and negative images which is then used to detect objects in other images. It can be trained to identify almost any object. In this project, pre-trained files are used.

The algorithm has four steps:
1. Haar Feature Selection
2. Creating  Integral Images
3. Adaboost Training
4. Cascading Classifiers

Tools used : OpenCV and Haar Cascade model

OpenCV is an open-source library for computer vision, with a focus on real-time applications. It focuses mainly on video capture/processing, image processing, and analysis (like face and object detection). It has many built-in functions and pre-trained models, so we don’t have to worry about training and testing of algorithms.

In the best case scenario an accuracy of 95.5% can be achieved.

This project was done in collaboration with https://github.com/smth-27, check out his profile.
Ref : https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08

