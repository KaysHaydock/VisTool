# **Developer README**

Welcome to the developer documentation for this project. This guide provides an in-depth overview of the development workflow, project structure, and best practices, including unit testing with `pytest`.

---

## **1. Project Structure**

The following structure outlines the layout of the project:

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


