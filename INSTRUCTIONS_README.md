# **Developer Instructions README**

Welcome to the developer documentation for this project and how to install and run the code. 

---

## Getting Started

To contribute to this project or run this package, follow these steps to set up your development environment.

### 1. Clone the repository to your local machine

```bash
git https://github.com/KaysHaydock/VisTool.git
cd VisTool
```

2. Set up the environment

You can set up the development environment using conda.

```bash
conda env create -f binder/environment.yml
conda activate vistool_env
```

3. Install the package

For local development, you can install the package in editable mode for local development:

```bash
pip install -e .
```

4. Run the Example Notebook

Navigate to the notebooks/ folder and open example_usage.ipynb:

```bash
jupyter notebook notebooks/example_usage.ipynb
```

5. Project Structure
```bash
project/
├── LICENSE
├── binder/
│   └── environment.yml
├── pyproject.toml
├── README.md
├── INSTRUCTIONS_README.md
├── .gitignore
├── analysis_package/
│   ├── init.py
│   ├── combine.py
│   ├── download.py
│   ├── visualize.py
│   ├── wrangle.py
│   └── data/
│       ├── titanic3.xls
│       └── monthly_ae_attendances_nov_2024
├── tests/
│   ├── test_model.py
│   ├── test_combine.py
│   ├── test_download.py
│   ├── test_visualize.py
│   └── test_wrangle.py
│   └── functional_testing.xlsx
├── notebooks/
│   ├── example_usage.ipynb
│   ├── advanced_example_usage.ipynb
│   └── documentation.ipynb
```
