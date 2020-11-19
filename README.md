# FastCovNetProject

### Multimodal Deep Learning for COVID19 Diagnosis

------------------------

#### Outline:
[1. Introduction](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/README.md)

[2. Infrastructure](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Infrastructure%20%26%20Software/)

[3. Tensorboard](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Tensorboard/)

[4. Preprocessing](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Preprocessing/)

[5. COVID19 Classification](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/COVID%20Classification/)

[6. Interpretability](https://github.com/FastCovNetProject/FastCovNetProject/blob/main/Interpretability/)

------------------------

#### Motivation

The COVID19 pandemic has posed a great challenge for health organizations everywhere. COVID19 is a new and poorly known infectious disease that has proven to be transmissible by air so cohortization of patients was of great importance. For diagnosis of COVID19 the Gold Standard test is the PCR (polymerase-chain-reaction) of a nasopharyngeal swab. In many places the increasing number of incoming patients exceeded the resources of the health system, slowed down the diagnostic flow and made it necessary to develop innovative strategies. 

In Barcelona, at Bellvitge University Hospital, a fast system for decision making was put in place. Patients with COVID19 suspicion would be separated from the rest and taken to a fast circuit where they would undertake a clinical assessment, blood test, chest X-ray and a PCR test. The clinical assessment, blood test results and radiology report would give a fast prediction of COVID-19 presence or absence and severity. According to this prediction the patient would be either hospitalized or sent home for confinement while waiting for the PCR result.

With this project we aim to solve the described problem using a deep learning approach. Deep learning, and more in particular convolutional neural networks, have shown good performance in computer vision tasks such as pneumonia detection. Recent studies have proven these algorithms useful in the detection of COVID19 pneumonia from non-COVID19 pneumonia and from normal chest-X rays with good sensibility and specificity. We believe that a multimodal approach, that includes not only radiological information but also blood test parameters and clinical parameters such as temperature and oxygen saturation could improve performance for COVID19 diagnosis.
 

------------------------

#### Objectives

1.	Obtain two curated datasets for training, testing and evaluation of the network:
	- Silver dataset: SISCAT databases
	- Golden dataset: Bellvitge Hospital COVID19 'Fast Diagnosis Circuit'

2.	Develop ChestCovNet: a CNN capable of processing X-ray images and classify them in COVID19 positive or negative. 

3.	Develop FastCovNet: Adapt the network for multimodal data (chest X-ray images and tabular data from clinical an laboratory features). 

4.	Fine-tune FastCovNet for improving the performance over the unimodal version. 

------------------------

#### Data

For this project we have worked with public health system data. For accessing and using public health data we needed to present the project protocol to the Bellvitge University Hospital Research Ethics Committee. Our protocol was approved on July 9th with reference code 'Proyecto FastCovNET PR254/20'.

*Silver Dataset*

Following protocol approval a petition was sent to Padris Program for imaging data:
- COVID19 group: Patients with a COVID19 positive PCR test and a Chest X Ray. 
- No-COVID19 group: Previous (before 2020) chest X Rays from patients in COVID19 group, chest X Rays of patients with different lung conditions. 

*Gold Dataset*

Following protocol approval we began a retrospective data collection from the Bellvitge COVID19 'Fast Diagnosis Circuit'. 
Gold dataset included 1078 individuals with following data:
- PCR
- Chest Xray report
- Age and sex
- Blood test parameters: Inflammation biomarkers, coagulation biomarkers and kidney function biomarkers among others. 
- Clinical parameters: cardiac rate, temperature and oxygen saturation. 
- Codified final diagnosis.
- Destination at discharge from the ER 

Data was handled to Padris for anonymization, codification and association with imaging data. 


------------------------

#### References

* [Li L, Qin L, Xu Z, Yin Y, Wang X, Kong B, et al. Artificial Intelligence Distinguishes
COVID19 from Community Acquired Pneumonia on Chest CT. Radiology. May 2020.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7233473/pdf/radiol.2020200905.pdf)

* [Mei X, Lee H-C, Diao K, Huang M, Lin B, Liu C, et al. Artificial intelligence–
enabled rapid diagnosis of patients with COVID-19. Nature Medicine. May 2020; 1-5.](https://www.nature.com/articles/s41591-020-0931-3)

* [Rajpurkar P, Irvin J, Zhu K, Yang B, Mehta H, Duan T, et al. CheXNet: Radiologist-
Level Pneumonia Detection on Chest X-Rays with Deep Learning.](http://arxiv.org/abs/1711.05225)

* [Zhang J, Xie Y, Li Y, Shen C, Xia Y. COVID-19 Screening on Chest X-ray Images
Using Deep Learning based Anomaly Detection. March 2020](http://arxiv.org/abs/2003.12338)

* [Asnaoui KE, Chawki Y. Using X-ray images and deep learning for automated
detection of coronavirus disease. Journal of Biomolecular Structure and
Dynamics. May 2020;0(0):1-12.](https://www.tandfonline.com/doi/full/10.1080/07391102.2020.1767212)

* [Murphy K, Smits H, Knoops AJG, Korst MBJM, Samson T, Scholten ET, et al.
COVID-19 on the Chest Radiograph: A Multi-Reader Evaluation of an AI System.
Radiology. May 2020;201874.](https://pubs.rsna.org/doi/pdf/10.1148/radiol.2020201874)
