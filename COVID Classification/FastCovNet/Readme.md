# FastCovNet

In this section, we present the FastCovNet architecture, the experiments and their results. FastCovNet should be an architecture capable of intaking chest X-ray images and tabular, structured data from a patiend (i.e., multimodal data) and predict the target variable, COVID19 positive or negative. The tabular data are several variables from the patient, ranging from sex and age to to blood levels of potasium or eosinophils. 

The motivation for trying to develop this architecture is two-fold: on one hand, we think that it would be cool to do Deep Learning with a mixture of image data and tabular data, and on the other hand, we expect this architecture to improve the classification metrics. This approach is not unique, as we can see in [this](https://github.com/naity/image_tabular) and [this](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7150512/pdf/main.pdf) examples, but it is not too common either. We believe one of the main reasons for not being more widespread is the data scarcity, especially in healthcare settings.

-------------------------------------

## The architecture

Below we present a scheme of FastCovNet's architecture:
![FastCovNet Architecture](FastCovNet.PNG)

As it can be seen, it consists of two parts, an image processing part and a tabular data processing part. The image processing part is the result of the previous step of the project, the ChestCovNet architecture, while the tabular data processing part consists of two fully connected layers with a ReLU activation between them. These two independent modules output the image features vector and the tabular features vector. These two vectors are then concatenated (an operation that is *backprop-able*) and passed through a linear layer with one single output neuron (followed by a sigmoid operation) acting as the classifier. The reason for putting a hidden layer in the tabular module is to give that module the oportunity to learn nonlinearities in the tabular data. The architecture within the image module (ChestCovNet) is GoogLeNet, for reasons previously explained in the corresponding [section](https://github.com/FastCovNetProject/FastCovNetProject/tree/main/COVID%20Classification/ChestCovNet). For logistic reasons we have decided not to re-train this module while training the whole network, and thus it has been "frozen" during training.

As mentioned, one of the first hypothesis regarding the experiments with FastCovNet is that it will be able to outperform ChestCovNet. Prior evidence supporting this idea is the fact that an XGBoost classifier trained over the tabular data alone is able to predict the target variable with high accuracy (above 80%). Unfortunately, we have not been able to see this results in our experiments, as it is shown in the following section. In addition, basic hyperparameter search and fine-tuning has been carried on, due to limited remaining time of the project.

-------------------------------------

## Experiments, results and conclusions

![FastCovNet training](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/COVID%20Classification/FastCovNet/Experiments/Fastcovnet/Exp4.jpg)

Model: MultiModalNet; Training epochs: 99; Batch size: 40; Results: 

                  precision    recall  f1-score   support
        Case         0.8000    0.7143    0.7547        28
     Control         0.6000    0.7059    0.6486        17

    accuracy                             0.7111        45
    macro avg        0.7000    0.7101    0.7017        45
    weighted avg     0.7244    0.7111    0.7146        45

This is the best result obtained with FastCovNet. As it can be seen, precision and recall metrics are not as good as in the ChestCovNet section, where they were around 80%. It must be highlighted that the available time for testing this architecture has been very limited, and thus that we still believe that our hypothesis holds (that this architecture or some variation of it should be able to outperform ChestCovNet), but that simply we have not been able to fine-tune the net properly. It also should be taken into consideration the small amount of datapoints available for training and testing this network, due to difficulties in the data-collecting process, as well as to our extreme caution with potential data leakage between train and validation/test sets (we have excluded data from the same patient, despite not being the same image, etc.).

We consider further optimization of this architecture an interesting line of future work.


-------------------------------------

#### References

* [Gessert N, Nielsen M, Shaikh M, Werner R, Schlaefer A. Skin lesion classification using ensembles of multi-resolution EfficientNets with meta data. MethodsX. 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7150512/pdf/main.pdf)
