##Where is my CNN looking at?##

###Introduction###
Media y desviación stándard de la muestra para casos y controles en dataset
Primeras pruebas 77f1, alrededor de 80%precision/recall. 
Buenos resultados pero no lógicos para radiólogo torácico. 
Decisión de buscar métodos de interpretabilidad.
We detect the problem of non interpretable predictions

###Hypotesis1###
1. Predictions from model cam be explainable by regional gradient weighted activation maps: GradCAM
1.1 Features causing class activation in chest radiographs might be more than one (for example bilateral pneumonia) and Grad-CAM has shown limitations to properly localize objects
in an image if the image contains multiple occurrences of the same class activation. GradCAM++.

##Conclusion1## GradCam and GradCam++ give features activation maps that include wide areas of the radiography. Moreover we are using posteroanterior chest x-ray with are a bidimensional representation of a wide varienty of anatomical structures. GradCAM and GradCAM++ fail in providing more detailed information of the elements causing class activation. 

##Hypoteisis2## 
2. Pixel-space gradient visualizations such as Guided Backpropagation are high-resolution and highlight fine-grained details in the image. They have the limitation of not being class-discriminative but might provide us a better understanting of the estructures that our model is targeting. 

##Conclusion2## 
Guided Backpropagation visualizes gradients with respect to the image where negative gradients are suppressed when backpropagating through ReLU layers. This aims
to capture pixels detected by neurons. In our experiment the model correctly detects the anatomic elements in the chest radiograph related to mediastinal (heart, pulmonary vessels and great vessels like aorta and cava veing) lung limits and extratoracic bone structures, however, it fails to be informative about with of the structures is more relevant for class activation. 

##Hypotesis3## 
3. Combination of the two methods might provide us with the intended insight. The fusion of the outputs of Guided Backpropagation and Grad-CAM visualizations via
element-wise multiplication might keep the benefits of both methods. 

##Conclusion##
GuidedGradCAM is both high-resolution identifing the anatomical structures of the chest xray and class-discriminative hightlinghting some regions of the image that are suposed to be relevant for class activation. However the hightlighted regions and anatomical structures change greatly in the various experiments with no understandable pattern. The model is capable of detectign anormality but focuses.....
