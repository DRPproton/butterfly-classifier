# Multi-Class Butterfly Classifier

This Butterfly Classifier API was created for my daughter, who loves these colorful insects. I would like to use the API on a web or mobile app. This API uses advanced image recognition technology to classify various species of butterflies from web images. The aim is to provide a simple, effective tool for butterfly enthusiasts (my daughter), researchers, and app developers who wish to integrate this functionality into web or mobile applications

This repository contains a Jupyter Notebook, `Butterfly-Classification.ipynb`, 
which provides a predictive analysis, model construction, and selection. 

<hr />


## Installation

To run the Jupyter Notebook and perform the analysis, you'll need Python and some necessary libraries. You can set up your environment by following these steps:

1. Clone this repository to your local machine:

   git clone https://github.com/DRPproton/butterfly-classifier.git

1. **Install virtualenv (if not already installed)**:
   If you don't have virtualenv installed, you can do so using `pip`, the Python package manager. Open your terminal or command prompt and run the following command:

   ```bash
   pip install virtualenv
   ```

2. **Navigate to Project Directory**:
   Navigate to the project directory using the terminal.

   ```bash
   cd project_directory
   ```

3. **Initialize a New Environment and Install Dependencies**:
   Inside your project directory, run the following command to create a new environment and install Python packages and dependencies for your project using `pip install -r requirements.txt`.
   
   ```bash
     python3 -m venv virtual-environment-name
   ```


4. **Activate the environment:**

   ```bash
      source env/bin/activate
   ```
   Your terminal prompt will change to indicate that you are now working within the  virtual environment.

   - Install dependencies
   ```
      pip install -r requirements.txt
   ```

   
6. **Run Jupyter Notebook**:
   You can now run the Notebook within the Pipenv virtual environment. For example, you can run it with:
    
   ```bash
   jupyter lab
   ```


<hr />

## Creating a Docker image using a Dockerfile involves several steps. Below are the commands and steps to build a Docker image from a Dockerfile:

1. **Navigate to the ***deployment_code*** folder inside the main project**:

2. **Build the Docker image**:
   Use the `docker build` command to build an image based on the Dockerfile. Replace `your-image-name` with the name you want to give to your Docker image:

   ```bash
   docker build -t your-image-name .
   ```

   The `.` at the end of the command indicates that the Dockerfile is located in the current directory.

3. **Check the list of Docker images**:
   To verify that your image was successfully created, use the `docker images` command:

   ```bash
   docker images
   ```
   You should see your newly created image in the list.

4. **Run a container from the Docker image (optional)**:
   If you want to test your image, you can run a container based on it using the `docker run` command. Replace `your-container-name` with a name for your container:

   ```bash
   docker run -it --rm -p 8080:808 [containerName]
   ```

5. **Test your application by running Python Test Scripts**:
   Open a new shell with the environment activated and run the script below. after uncommenting line 4 and comment line 7
   ```bash
   python test.py
   ```

<hr />
## Testing the live API
1. **Open files**:
   Open a new shell with the environment activated and run the script below.
   Open the file test_api.py in your IDE
   Uncomment lines 7 and 16 and comment line 4
3. **Test your application running Python Test Scripts**:
   Save the file and run it on the shell using the command below.
   ```bash
   python test.py
   ```
> Deployed API on this address:  https://19kywrz8ek.execute-api.us-east-1.amazonaws.com/butterfly-classifier/predict

<hr />
## Deploy a Docker container in AWS Lamvda, follow these steps:

Deploying a Docker image as a Lambda function in AWS involves several steps, including creating a Docker image, pushing it to Amazon Elastic Container Registry (ECR), and then configuring AWS Lambda to use this image. Here's a step-by-step guide to help you through the process:

### 1. **Prepare Your Docker Image**

First, you must create a Docker image containing your application and its dependencies.

1. **Create a Dockerfile**: This file contains the instructions for building your Docker image. It should set up the necessary environment, install dependencies, and specify how your application will be executed.

   Example Dockerfile:
   ```Dockerfile
   FROM public.ecr.aws/lambda/python:3.10

   RUN pip install keras-image-helper
   RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
   
   COPY butterfly-model.tflite .
   COPY lambda_function.py.
   
   CMD [ "lambda_function.lambda_handler" ]
   ```

2. **Build the Docker Image**: Run the Docker build command to create your Docker image.
   ```bash
   docker build -t my-lambda-function .
   ```

### 2. **Push the Image to Amazon ECR**

Before you can deploy your Docker image to Lambda, you need to push it to Amazon Elastic Container Registry (ECR).

1. **Create a Repository in ECR**: Navigate to the Amazon ECR console and create a new repository for your Docker image.

2. **Authenticate Docker to Your ECR Registry**: Run the `aws ecr get-login-password` command to retrieve an authentication token and authenticate your Docker client to your registry.
   ```bash
   aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com
   ```

3. **Tag Your Docker Image**: Tag your image with your ECR repository's URI.
   ```bash
   docker tag my-lambda-function:latest your-account-id.dkr.ecr.your-region.amazonaws.com/my-lambda-function:latest
   ```

4. **Push the Image to ECR**: Push your Docker image to your newly created ECR repository.
   ```bash
   docker push your-account-id.dkr.ecr.your-region.amazonaws.com/my-lambda-function:latest
   ```

### 3. **Create and Configure Your Lambda Function**

Now, you can create your Lambda function using the Docker image you've just pushed to ECR.

1. **Open the Lambda Console**: Go to the AWS Lambda console.

2. **Create a New Function**: Choose to create a new Lambda function. Select the "Container image" option as your blueprint.

3. **Configure the Function**: Give your function a name and select the Docker image you pushed to ECR as the source of your Lambda function. Configure any additional settings like memory, timeout, triggers, and execution role as needed.

4. **Deploy the Function**: After configuring your function, deploy it.

5. **Test Your Function**: You can test your Lambda function directly in the AWS Lambda console to ensure it's working as expected.

### Additional Considerations

- **IAM Roles**: Ensure that your Lambda function has the necessary IAM roles and permissions to access other AWS services if needed.
- **Environment Variables**: Set any required environment variables through the Lambda console.
- **Networking**: Configure VPC settings if your Lambda function needs to access resources within a VPC.

By following these steps, you should be able to successfully deploy a Docker-based AWS Lambda function. Remember to regularly update both your Docker image and your Lambda function configuration as your application evolves.

