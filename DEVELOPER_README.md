# **Developer README**

Welcome to the developer documentation for this project and how to set it up. This guide provides an in-depth overview of the development workflow. 
---

# Features

## To Do
-- Loading of Datasets --
1. Load a dataset in CSV file
2. Load a dataset in (other type format) file
3. Merging two datasets together
4. Concatenating two datasets together

-- Customise Visualisation of data --
1. Choosing two columns on a dataset to visualise on a graph - KH
2. Choosing what type of graph the user would like (Bar, Scatter etc) - KH
3. Apply more then one line of data on a graph (overlays)
4. Use PyWidgets to adjust graph types and configurations perhaps

-- Wrangling of Data --
1. Clean data (pre-processing): Rename any columns
2. Give the user option to remove any empty cells they do not want
3. Give the user option to fill in any empty cells with the average/mean
4. Dimension reduction of the dataset
5. If a user has categorical data, give the option to user to encode

-- Downloading of Data --
1. Option to download and save the data to a location on their PC

## In Progress


## Completed


## **1. Project Structure**

The following structure outlines the layout of the project:

```bash

## Getting Started

To contribute to this project, follow these steps to set up your development environment.

### 1. Clone the repository

```bash

git https://github.com/KaysHaydock/HPDM139_2.git
cd HPDM139_2

2. Set up the environment

You can set up the development environment using either conda.

Using Conda

Create and activate the conda environment:

conda env create -f binder/environment.yml
conda activate pypi_package_dev


2. Install the package

For local development, you can install the package in editable mode:

pip install -e .

Development Setup
project/
├── LICENSE
├── binder/
│   ├── environment.yml
├── pyproject.toml
├── README.md
├── .gitignore
├── analysis_package/
│   ├── init.py
│   ├── combine.py
│   ├── download.py
│   ├── visualize.py
│   ├── wrangle.py
│   └── data/
│       └── test_data.csv
├── tests/
│   ├── test_model.py
│   ├── test_combine.py
│   ├── test_download.py
│   ├── test_visualize.py
│   └── test_wrangle.py
├── notebooks/
│   └── example_usage.ipynb


The Health Data Tools project is organized into the following main components:
	•	LICENSE: Contains the project’s licensing terms.
	•	binder:/environment.yml Includes environment configuration for cloud platforms like Binder.
	•	pyproject.toml: Manages build system and dependencies.
	•	README.md: End-user documentation for installation and usage.
	•	.gitignore: Specifies files to exclude from version control.
	•	analysis_package/: The core package, containing modules for downloading, cleaning, merging, and visualizing data.
	•	tests/: Unit tests for each module in analysis_package/.
	•	notebooks/: Jupyter notebooks with examples of package usage.


