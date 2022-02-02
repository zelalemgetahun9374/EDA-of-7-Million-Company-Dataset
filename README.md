# EDA-of-7-Million-Company-Dataset
An explanatroy data analysis on 7+ Million Company Dataset with the objective of learning insights from business names.

**Table of Contents**

- [EDA-of-7-Million-Company-Dataset](#EDA-of-7-Million-Company-Dataset)
  - [Overview](#overview)
  - [Objective](#objective)
  - [Approach](#approach)
  - [Project Structure](#project-structure)
    - [data:](#data)
    - [notebooks](#notebooks)
    - [scripts](#scripts)
    - [root folder](#root-folder)
  - [Installation guide](#installation-guide)

## Overview
In this repository I have analyzed company names dataset. You can find this dataset on [kaggle](https://www.kaggle.com/peopledatalabssf/free-7-million-company-dataset).
## Objective
The objective of this project is to extract insights from company names.

## Approach
The project is implemented in the following phases.
1. Data cleaning
2. Univariate analysis
3. Feature engineering
4. Bivariate analysis
5. Filtering data and answering business questions

## Project Structure
The repository has a number of files including python scripts, a jupyter notebook, and text files. Here is their structure with a brief explanation.

### data:
- the folder where the dataset csv file is stored. I have not included the dataset here because it is over 1gb. You can download it from [here](https://www.kaggle.com/peopledatalabssf/free-7-million-company-dataset).

### notebooks:
- `Company Names EDA.ipynb`: a jupyter notebook that performs exploratory data analysis.

### scripts
- `app_logger.py`: a python script for logging
- `file_handler.py`: a python script for handling reading and writing of csv files
- `df_cleaner.py`: a python script for cleaning pandas dataframes
- `df_overview.py`: a python script for displaying summary data of a pandas dataframe
- `df_visualizer.py`: a python script for plotting selected data

### root folder
- `requirements.txt`: a text file lsiting the project's dependancies.
- `README.md`: markdown text with a brief explanation of the project and the repository structure.

## Installation guide
```
git clone https://github.com/zelalemgetahun9374/EDA-of-7-Million-Company-Dataset.git
cd EDA-of-7-Million-Company-Dataset
pip install -r requirements.txt
```
