## Where is ChestCOVNet looking at?

### Introduction
Media y desviación stándard de la muestra para casos y controles en dataset
Primeras pruebas 77f1, alrededor de 80%precision/recall. 
Buenos resultados pero no lógicos para radiólogo torácico. 
Decisión de buscar métodos de interpretabilidad.
We detect the problem of non interpretable predictions

### GradCAM and GradCAM++
#### 1st Hypotesis: A visual explanation with gradient weighted class activation maps can be useful to interpret predictions from our model: GradCAM 

Grad-CAM uses the gradient information flowing into the last convolutional layer of the CNN to assign importance values to each neuron for a particular decision of interest. The last convolutional layer of the model is the best suited for this task, due to it's convolutional nature it will retain spatial information about the input and being the deeper layer it will capture higher level semantic class-specific information. 
To obtain the class-discriminative localization map, Grad-CAM computes the gradient of the score for the target class with respect to feature map activations of a convolutional layer (the last convolutional layer in our experiments). These gradients flowing back are global-average-pooled over the width and height dimensions to obtain the neuron importance weights. This weights capture the ‘importance’ of the feature map for the target class. Then a weighted combination of forward activation maps is computed, followed a ReLU to obtain the heatmap.

![GradCAM](/Interpretability/Images/gradcam.png)

#### 1st Experiment:

[](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Interpretability/Images/egradCAM.png)

#### Conclusion from 1st Experiment:
The first heatmaps that we obtained didn't look very informative nor very consistent. They were able to detect obvious abnormality but focused mainly on the center of the image and the diafragm.

#### 2nd Hypotesis: GradCAM limitions might be affecting the interpretation in our experiment: GradCAM++
Features causing class activation in chest radiographs might be more than one (for example multilobar pneumonia) and Grad-CAM has shown limitations to properly localize objects in an image if the image contains multiple occurrences of the same class activation. Another described limitation is that the localization map might not correspond to the entire features but bits and parts of it, consequence of how it's computed as an unweighted average of partial derivatives. If there were multiple occurrences of an object with slightly different orientations or views (or parts of an object that excite different feature maps), different feature maps may be activated with differing spatial footprints, and the feature maps with lesser footprints fade away in the final saliency map.

In an attempt to overcome this issue we tried GradCAM++. GradCAM++ which could be considered a generalized reformulation of Grad-CAM that tries to fix this problem by taking a weighted average of the pixel-wise gradients. For this the target layer's scores are passed through an exponential function. We tried this approach in order to improve our visual explanation maps.

![GradCAM++](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Interpretability/Images/gradcam%2B%2B.JPG)

#### 2nd Experiment: 

[](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Interpretability/Images/eGradCAM%20y%20%2B%2B.PNG)

#### Conclusion from 2nd Experiment:
The GradCAM++ obtained do look more intense in some of our experiments while in other stay the same. The heatmaps still have wide areas of the image marked as important for the prediction of the target class with many involved structures. Successive attempts don't show robustness in the selected areas for the target class. 

### GuidedBackpropagation
#### 3rd Hypotesis: Pixel-space gradient visualizations might work better for our problem: Guided Backpropagation 
The heatmap obtained so far include wide hot areas in the image which are not very informative nor robust. We need to take into consideration that a chest x-ray is a bidimensional representation of several trimimensional structures. Our heatmaps pointing at mediastinal structures might be focusing on all the structures that collude in the radiological representation of it wich include bone structures, vessels and the heart among others. When the heatmap is hotter at the bases of the radiography might be focusing both in the diaphragm, the upper abdominal structures or the lower lung segments. Therefore we need a method with higher resolution. 

Guided Backpropagation visualizes gradients with respect to the image where negative gradients are suppressed when backpropagating through ReLU layers. This aims
to capture pixels detected by neurons. The resulted visualization maos are high-resolution and highlight fine-grained details in the image. They have the limitation of not being class-discriminative but might provide us a better understanting of the estructures that our model is targeting. 

![GBP](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Interpretability/Images/gbp.JPG)

#### 3rd Experiment:

[](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Interpretability/Images/eGBp.PNG)

#### Conclusion from 3er Experiment:
In our experiment the model correctly detects the anatomic elements in the chest radiograph related to mediastinal structures(heart, pulmonary vessels and great vessels like aorta and cava vein), lung limits and extratoracic bone structures, however, it fails to be informative about with of the structures is more relevant for class activation. 

We surely have contributed to this limitation since we were not able to inplement the method in the deeper layers of the model. [Springerberg et al](https://arxiv.org/pdf/1412.6806.pdf) state that it is possible to perform guided backpropagation even in the last layers of the model. After several attempts we obtained non informative outputs.  This is a clear inprovement area for the project that we would like to complete in the future. 

### Guided GradCAM
#### 4rd Hypotesis: Our problem needs a method that is both hight resolution and class discriminative: Guided GradCAM. 
Combination of the two methods might provide us with the intended insight. The fusion of the outputs of Guided Backpropagation and Grad-CAM visualizations via
element-wise multiplication might keep the benefits of both methods. 

![GuidedGradCAM](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Interpretability/Images/gradcam%20y%20guidedbp.png)

#### 4th Experiment:

#### Conclusion from 4th Experiment:
GuidedGradCAM is both high-resolution identifing the anatomical structures of the chest xray and class-discriminative hightlinghting some regions of the image that are suposed to be relevant for class activation. While this method is more informative about the areas of the image that the model is targeting for prediction, the hightlighted regions change greatly in the various experiments with no understandable pattern. The model is capable of detecting anormality but doesn't behave in a robust fashion. 
When presenting the model with previously chosen inputs, cases with obvious pneumonia findings
