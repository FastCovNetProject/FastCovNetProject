# ChestCovNet

In this section the objective is to develop an architecture that we call **ChestCovNet**, which will be based on some existing network architecture and must be able to perform our task of interest: to predict if a patient has COVID-19 or not based on its chest radiograph. For this task, which is a binary classification problem based on images, we rely on deep convolutional networks, drawing inspiration from the work by Tang, YX., Tang, YB., Peng, Y. et al. *Automated abnormality classification of chest radiographs using deep convolutional neural networks*. This paper is an overview that shows that several convolutional architectures like VGG, ResNet, DenseNet etc. achieve high or very high accuracies (ROC AUC) in this type of binary classification task with radiographs. We have selected three architectures as our baseline, following a higher-performance criteria. 

It is worth highlighting that our target variable (COVID19 positive/negative) is different to the one employed in the mentioned paper (general "abnormality" in the chest radiograph), and that in a good portion of cases, a COVID19 positive patient does not show any abnormality in its chest radiograph that is perceptible for humans (i.e., the ground truth is not a radiologist's veredict, but the PCR test). For this reason, one of the first hypothesis that we set is that the accuracies we will obtain will be lower than those showed in the paper. This is confirmed by our experiments. Still, we also set the hypothesis that the networks will be able to "see more" than the human eye, which also seems to be confirmed by the experiments.

--------------------------------------

## The architectures and strategies
We select three architectures, ResNet, DenseNet, and GoogLeNet, following a criteria of performance in the aforementioned study. In all the three cases we have employed a network pretrained on Imagenet (i.e., transfer learning approach), and we have adapted the last layer (fully connected, for classification) to our task, with one single output neuron followed by a Sigmoid operation and the Binary Cross Entropy Loss as the loss function. Alternatively, we have tried employing two neurons for the output (one for each class) and the Cross Entropy Loss (i.e., a Softmax operation and the Negative Log Likelihood Loss). There is no significative difference between these two approaches, as they represent essentially the same. 

Both the Adam and the SGD optimizers with different parameters have been tried. We have not found significative differences in the final performances of the networks depending on this choice, although some differences in the trainig behavior have been observed.

Our original dataset was very unbalanced, with many more controls than cases. We have opted for manually balancing the dataset, by sampling a number of controls equal to the number of cases. This is due to the fact that, as should be expected, we have observed worst metrics for the minority class when employing the whole dataset. This approach is slightly "wasteful", as many images are not employed, but we have allowed ourselves to do it under the premise that the balanced dataset was still big enough for the task. Other more involved approaches like moving the decision threshold for the prediction of case and control could be employed.

--------------------------------------

## Experiments and results:

For each network, the winner metrics of precission and recall for both classes (cases and controls) are showed. In addition, we include graphs of the evolution of loss and ROC AUC during training. 


### ResNet
![ResNet training](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/COVID%20Classification/ChestCovNet/Experiments/ResNet/Exp5_Adam.jpg)

Model: ResNet; Training epochs: 39; Batch size: 40; Results: 

                 precision    recall  f1-score   support      
        Case        0.8280    0.7945    0.8109       618
     Control        0.8084    0.8401    0.8240       638

    accuracy                            0.8177      1256
    macro avg       0.8182    0.8173    0.8174      1256
    weighted avg    0.8181    0.8177    0.8175      1256

The graph above shows how the network starts to overfit to the training data from approximately epoch 15 on, when the loss in the validation set starts to increase. Nevertheless, the ROC AUC metric still improves a bit until a few epochs after.

### DenseNet
![Densenet training](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/COVID%20Classification/ChestCovNet/Experiments/DenseNet/Exp2.jpg)

Model: DenseNet; Training epochs: 39; Batch size: 40; Results: 

                 precision    recall  f1-score   support
        Case        0.8083    0.8188    0.8135       618
     Control        0.8222    0.8119    0.8170       638

    accuracy                            0.8153      1256
    macro avg       0.8153    0.8153    0.8153      1256
    weighted avg    0.8154    0.8153    0.8153      1256

This graph also shows a very clear case of overfit from around epoch 8 on. We have not been able to overcome this by hyperparameter tuning, but the metrics are still reasonably good.

### GoogleNet
![GoogleNet training with ADAM optimizer](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/COVID%20Classification/ChestCovNet/Experiments/GoogLeNet/Exp2.jpg)![GoogleNet training with SGD optimizer](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/COVID%20Classification/ChestCovNet/Experiments/GoogLeNet/Exp3_sgd.jpg)


Model: GoogLeNet; Training epochs: 23; Batch size: 40; Results: 

                  precision    recall  f1-score   support
        Case         0.7977    0.7718    0.7845       618
     Control         0.7857    0.8103    0.7978       638

    accuracy                             0.7914      1256
    macro avg        0.7917    0.7911    0.7912      1256
    weighted avg     0.7916    0.7914    0.7913      1256

The main difference between these two graphs is the noise in the loss of the validation set. This may be due to differences in the batch size and also in the optimizer, as the network in the graph above has been trained with Adam while the one below has been trained with SGD.

All the results of this section (and also some not included) are in the [Experiments](/Experiments/) folder.

--------------------------------------

## Conclusions

As it can be seen, the three networks achieve similar values for these metrics, around the 80%. GoogLeNet slightly underperforms the other two networks, but it is significantly faster to train (taking around a third of the time required by ResNet and a fourth of the time required by DenseNet). This may be due to GoogLeNet's architecture, that is able to provide a better depth-computational efficiency tradeoff. This difference in training time has meant that in practice GoogLeNet has been our "prototyping" network for changes, for instance in hyperparameters, in the absence of more time to perform all the experiments with all the combinations over all the networks. Given these results, there is not a clear "winner" candidate for our ChestCovNet, but we have selected GoogLeNet for the aforementioned reasons.

The results obtained with this approach support the hypothesis that detecting COVID-19 with high accuracy based solely in chest radiographs is difficult. In most asymptomatic cases, no abonormality can be detected by humans in those radiographs. Despite we have not quantified it, we believe the proportion of asymptomatic individuals in our cohort is big enough to say that the network has been able to detect some of them based solely on the radiograph, which is a good result. In addition, we believe that further fine-tuning of the hyperparameters of the networks could lead to a higher precission and recall in the control class.

The results in this section motivate further and pave the way for FastCovNet, the multimodal approach.

#### References

* [Tang, YX., Tang, YB., Peng, Y. et al. Automated abnormality classification of chest radiographs using deep convolutional neural networks. npj Digit. Med. 3, 70 (2020).](https://doi.org/10.1038/s41746-020-0273-z)
