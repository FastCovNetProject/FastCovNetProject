# Tensorboard
Tensorboard is a web server to serve visualizations of the training progress of a neural network, it visualizes scalar values, images, text, etc; these information are saved as events in tensorflow. It’s a pity that other deep learning frameworks lack of such tool, so there are already packages letting users to log the events without tensorflow.


## Installation
We work on a JupyterLab, collaborative environment for python were Tensorboard for Pytorch have been installed.
https://pytorch.org/docs/stable/tensorboard.html
https://www.dlology.com/blog/how-to-run-tensorboard-for-pytorch-110-inside-jupyter-notebook/


## Create a summary writer
As a visualization toolkit for machine learning experimentation, TensorBoard allows tracking and visualizing metrics such as loss and accuracy, visualizing the model graph, viewing histograms, displaying images and much more.

Before logging anything, we need to create a writer instance. Writer will output to ./runs/ directory by default. Each subfolder will be treated as different experiments in tensorboard. Each time we re-run the experiment with different settings, we should change the name of the sub folder. Different types of data types can be log.


### Add scalar
Scalar value is the most simple data type to deal with. Mostly we save the **LOSS** value of each training step, or the accuracy after each epoch. We can look at the predictions the model made on arbitrary batches throughout learning. See the “Images” tab and scroll down under the “predictions vs. actuals” visualization. In addition,  the corresponding learning rate can be save as well.


### Add image
An image is represented as 3-dimensional tensor. The simplest case is save one image at a time. In this case, the image should be passed as a 3-dimension tensor of size [3, H, W]. The three dimensions correspond to R, G, B channel of an image

### Add histogram
Saving histograms is expensive. Both in computation time and storage. To save a histogram is necessary convert the array into numpy array save it.

### Add figure
A matplotlib figure can be save to tensorboard with the add_figure function.

### Add graph
To visualize a model, a model m and the input t is needed. t can be a tensor or a list of tensors depending on the model. 

### PR curves
Plotting a precision-recall curve lets us understand your model’s performance under different threshold settings. With this function, we provide the ground truth labeling (T/F) and prediction confidence for each target. The TensorBoard UI will let us choose the threshold interactively.

### Add embedding
Embeddings, high dimensional data, can be visualized and converted into human perceptible 3D data by tensorboard, which provides PCA and t-sne to project the data into low dimensional space. What we need to do is provide a bunch of points and tensorboard will do the rest for us. The bunch of points is passed as a tensor of size n x d, where n is the number of points and d is the feature dimension. The feature representation can either be raw data (a raw image) or a representation learned by your network (extracted feature).

### Add audio
To log a single channel audio a dimensional array have to be used, each element in the array represents the consecutive amplitude samples. 

