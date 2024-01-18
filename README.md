# Building a Scalable Image Classification app using AWS Services

## 1. Overview
In this project, an image classification model will be built using AWS Sagemaker to distinguish bicycles from motorcycles. AWS Lambda functions are used to build supporting services and AWS Step Functions will be orchestrating the composition of the model and services into an event-driven application. The end of this project is a scalable, machine learning-enabled AWS application.

The project approaches image classification from a logistics point of view by building an image classification model that can automatically detect which kind of vehicle delivery drivers have, in order to route them to the correct loading bay and orders. Assigning delivery professionals who have a bicycle to nearby orders and giving motorcyclists orders that are farther

The goal is to ship a scalable and safe model. The model must scale to meet demand, and safeguards are in place to monitor and control for drift or degraded performance.

## 2. Project steps
- Step 1: Data staging
- Step 2: Model training and deployment
- Step 3: Lambdas and step function workflow
- Step 4: Testing and evaluation

## 3. Getting Started
The project is extensively detailed and explained step by step in the main.ipynb Jupyter notebook and within each lambda function. The following is just an overview.

### 3.1 Dataset Used
The CIFAR-100 dataset was used for this project. It consists of 60000 32x32 color images in 10 classes, with 6000 images per class. The CIFAR dataset is open source and generously hosted by the University of Toronto at: https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz

### 3.2 Project files
**1. `main.ipynb`:** Jupyter notebook with detailed steps and explanations of implementing the workflow for Image Classification. This includes the necessary preprocessing of the CIFAR-100 dataset, model training, deployment, and monitoring using Amazon SageMaker and other associated AWS Services

**2. `main.html`:** Web page displaying the main.ipynb Jupyter notebook

**3. `lambda 1 - Image Serialization.py`:** A Lambda function (serializeImageData) designed to serialize target data from an S3 bucket, converting image data to base64 format for subsequent processing within an AWS Step Function

**4. `lambda 2 - Image Classification.py`:** A Lambda function utilizing SageMaker for image classification, decoding base64 image data, making predictions using a deployed model, and returning results to a Step Function.

**5. `lambda 3 - Filtering low confidence.py`:** A Lambda function (Filtering_low_confidence) that checks if any inference values in the given event exceed a specified threshold (0.93), and raises an error if the threshold confidence is not met.

**4. `Working Step Functions Graph and example.png`:** screen capture of the working step function.

**5. `MyStateMachine-hs53ltoxf.asl.json`:** Step Function exported to JSON

### 3.3 Dependencies
The project was built using Amazon SageMaker. Dependencies within SageMaker are as follow:
```
Python 3 (Data Science) - v3.7.10 kernel
ml.t3.medium instance
Python 3.8 runtime for the AWS Lambda Functions
```

## 4. The BIG picture
### 4.1 Data Processing, Training, and Deploying a Machine Learning Model
Performing a **complete ETL (extract, transform, load)** on the CIFAR-100 dataset, training an image classifier using `sagemaker.estimator.Estimator`, and constructing a **unique endpoint API** used for predictions 

### 4.2 Building a full machine learning workflow
Three lambda functions were created to automate the predictions of images and to filter low confidence rates (*3.2 Check project files section for more details*). These lambda functions were put together in a single workflow using AWS Step Functions

![Working Step Functions Graph and example.png](https://github.com/Kshishtawy/Scalable-Image-Classification-application-on-Amazon-Sagemaker/blob/main/Working%20Step%20Functions%20Graph%20and%20example.png?raw=true)
*A screenshot of the working step function utilizing the lambda function in a workflow*

### 4.3 Monitoring the model's performance and errors
Monitoring data was extracted from S3 and visualizations were created to check performance, capture errors, and make sure everything was working as expected.
![Visualization example](https://github.com/Kshishtawy/Scalable-Image-Classification-application-on-Amazon-Sagemaker/blob/main/Confidence%20levels%20visualization.png?raw=true)
*One of the visualizations created to check the model's performance*

## This was the Fourth project of the "Udacity Machine Learning Fundamentals Nandegree" offered by AWS as part of the "AWS AI & ML scholarship"
Confirmation  link: [link](https://graduation.udacity.com/confirm/e/ba2b0610-ee8f-11ed-8e43-fbdc25fcc49f)
![Certificate](https://github.com/Kshishtawy/Developing-a-Handwritten-Digits-Classifier-with-PyTorch/blob/main/Certificate/Udacity%20-%20Machine%20Learning%20Fundamentals.png?raw=true)
