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

Insertar esqeuma de GradCAM. 

#### 2nd Hypotesis: GradCAM limiations might be affecting the interpretation in our experiment: GradCAM++
Features causing class activation in chest radiographs might be more than one (for example multilobar pneumonia) and Grad-CAM has shown limitations to properly localize objects in an image if the image contains multiple occurrences of the same class activation. In addition another consequence of an unweighted average of partial derivatives is that the localization map might not correspond to the entire features but bits and parts of it. 
If there were multiple occurrences of an object with slightly different orientations or views (or parts of an object that excite different feature maps), different feature maps may be activated with differing spatial footprints, and the feature maps with lesser footprints fade away in the final saliency map.
Grad-CAM++ could be considered a generalized formulation of Grad-CAM that tries to fix this problem by taking a weighted average of the pixel-wise gradients. For this the target layer's scores are passed through an exponential function. We try this approach in an attempt to improve our visual explanation maps. 

(ilustración de la diferencia).


### GuidedBackpropagation
#### 3rd Hypotesis: Pixel-space gradient visualizations might work better for our problem: Guided Backpropagation 
Guided Backpropagation visualizes gradients with respect to the image where negative gradients are suppressed when backpropagating through ReLU layers. This aims
to capture pixels detected by neurons. The resulted visualization maos are high-resolution and highlight fine-grained details in the image. They have the limitation of not being class-discriminative but might provide us a better understanting of the estructures that our model is targeting. 

##Conclusion2## 
In our experiment the model correctly detects the anatomic elements in the chest radiograph related to mediastinal structures(heart, pulmonary vessels and great vessels like aorta and cava vein), lung limits and extratoracic bone structures, however, it fails to be informative about with of the structures is more relevant for class activation. 

### Guided GradCAM
#### 4rd Hypotesis: Our problem needs a method that is both hight resolution and class discriminative: Guided GradCAM. 
Combination of the two methods might provide us with the intended insight. The fusion of the outputs of Guided Backpropagation and Grad-CAM visualizations via
element-wise multiplication might keep the benefits of both methods. 

##Conclusion##
GuidedGradCAM is both high-resolution identifing the anatomical structures of the chest xray and class-discriminative hightlinghting some regions of the image that are suposed to be relevant for class activation. However the hightlighted regions and anatomical structures change greatly in the various experiments with no understandable pattern. The model is capable of detecting anormality but doesn't behave in a robust fashion. 
