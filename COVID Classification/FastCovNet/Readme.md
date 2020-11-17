### FastCovNet

In this section, we present the FastCovNet architecture, the experiments and their results. FastCovNet should be an architecture capable of intaking chest X-ray images and tabular, structured data from a patiend (i.e., multimodal data) and predict the target variable, COVID19 positive or negative. The tabular data are several variables from the patient, ranging from sex and age to to blood levels of potasium or eosinophils. 

The motivation for trying to develop this architecture is two-fold: on one hand, we think that it would be cool to do Deep Learning with a mixture of image data and tabular data, and on the other hand, we expect this architecture to improve the classification metrics. This approach is not unique, as we can see in [this](https://github.com/naity/image_tabular) and [this](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7150512/pdf/main.pdf) examples, but it is not too common either. We believe one of the main reasons for not being more widespread is the data scarcity, especially in healthcare settings.

## The architecture

Below we present a scheme of FastCovNet's architecture:
