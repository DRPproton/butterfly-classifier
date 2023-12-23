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
  python3 -m venv <virtual-environment-name>
   ```


4. **Activate the enviroment:

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
