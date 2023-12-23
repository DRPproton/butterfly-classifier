# Multi-Class Butterfly Classifier

This Butterfly Classifier API was created for my daughter, who loves these colorful insects. I would like to use the API on a web or mobile app. This API uses advanced image recognition technology to classify various species of butterflies from web images. The aim is to provide a simple, effective tool for butterfly enthusiasts (my daughter), researchers, and app developers who wish to integrate this functionality into web or mobile applications

This repository contains a Jupyter Notebook, `Butterfly-Classification.ipynbb`, 
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
   Navigate to project directory it using the terminal.

   ```bash
   cd project_directory
   ```

3. **Initialize a New Environment and Install Dependencies**:
   Inside your project directory, run the following command to create a new environment and install Python packages and dependencies for your project using `pip install -r requirements.txt`.
   
   ```bash
     python3 -m venv virtual-environment-name
   ```


4. **Activate the enviroment:**

   ```bash
      source env/bin/activate
   ```
   Your terminal prompt will change to indicate that you are now working within the  virtual environment.

   - Install dependencies
   ```
      pip install -r requirements.txt
   ```
   

5. **Run Python Scripts**:
   You can now run your Python scripts within the Pipenv virtual environment. For example, if you have a script named `my_script.py`, you can run it with:
    
   ```bash
   python predict.py
   ```
   
6. **Run Jupyter Notebook**:
   You can now run the Notebook within the Pipenv virtual environment. For example, you can run it with:
    
   ```bash
   jupyter lab
   ```

   Any packages installed using `pipenv install` will be available for your scripts within the virtual environment.

## Run Flask API Locally and testing

1. **Run Python Scripts**:
   You can now run your Flask scripts within the Pipenv virtual environment.
   ```bash
   python predict.py
   ```
   
2. **Test APIs**:
   Open a new shell with the enviroment activated and run the script bellow to test the api.
   The test_api.py file have a sample of a patiente, feel free to change the parameters to see how the changes affect the result. 
  ```bash
   python test_api.py
   ```

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
   docker run -it --rm -p 9696:9696 [containerName]
   ```
   The `-d` flag runs the container in detached mode. You can access the running container using its name.

5. **Test your application run Python Test Scripts**:
   Open a new shell with the enviroment activated and run the script bellow.
   ```bash
   python test_api.py
   ```
> ***Due to that we are using a free version for deployment sometimes take more than 30 seconds to get the result***

## Testing the live API
1. **Open files**:
   Open a new shell with the enviroment activated and run the script bellow.
   Open the file test_api.py in your IDE
   Uncomment lines 15 and 16 and comment line 19
3. **Test your application run Python Test Scripts**:
   Save file and run it on the shell using the command bellow.
   ```bash
   python test_api.py
   ```
> Deployed API in this address:  https://cirrhosis-outcomes-prediction.onrender.com/predict
   
## Deploy a Docker container in AWS Lamvda, follow these steps:


<img width="1000" alt="" src="Screenshot 2023-12-11 at 2.24.10 PM.png" />
