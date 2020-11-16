# FastCovNetProject
##### Multimodal Deep Learning for COVID19 Diagnosis

The COVID19 pandemic has posed a great challenge for health organizations everywhere. COVID19 is a new and poorly known infectious disease that has proven to be transmissible by air so cohortization of patients was of great importance. For diagnosis of COVID19 the Gold Standard test is the PCR (polymerase-chain-reaction) of a nasopharyngeal swab. In many places the increasing number of incoming patients exceeded the resources of the health system, slowed down the diagnostic flow and made it necessary to develop innovative strategies. 
In Barcelona, at Bellvitge University Hospital, a fast system for decision making was put in place. Patients with COVID19 suspicion would be separated from the rest and taken to a fast circuit where they would undertake a clinical assessment, blood test, chest X-ray and a PCR test. The clinical assessment, blood test results and radiology report would give a fast prediction of COVID-19 presence or absence and severity. According to this prediction the patient would be either hospitalized or sent home for confinement while awaiting for the PCR result. 

With this project we aim to solve the described problem using a deep learning approach. Deep learning, and more in particular convolutional neural networks, have shown good performance in computer vision tasks such as pneumonia detection. Recent studies have proven this algorithms useful in the detection of COVID19 pneumonia from non-COVID19 pneumonia and from normal chest-Xrays with good sensibility and specificity. We believe that a multimodal approach, that includes not only radiolígical information but also blood test parameters and clínical parameters such as temperature and oxygen saturation could improve performance for COVID19 diagnosis. 




We believe that a deep learning model could be very helpful for a similar task, so for this project we plan to build a multimodal deep learning model that we call FastCovNet, which will take both images and tabular data as an input and it will classify patients in COVID19 positive or negative.

