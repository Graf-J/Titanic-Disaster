# Titanic-Disaster 🚢
An interactive machine learning app to train a survival classifier on Titanic data and predict outcomes for new passengers.

This project is implemented in **Python** and **R**. Follow the instructions below to set up and run the project.

---

## 🧭 Run the Project

### 1) Download the Data
1. Navigate to the [Titanic competition page on Kaggle](https://www.kaggle.com/competitions/titanic/data)
2. Sign in or create a Kaggle account.
3. Click the **Download All** button to download the dataset.
4. Extract the files and save **train.csv** and **test.csv** on your local machine.


## Notes

For transparency, the **data cleaning, preprocessing, and model selection workflow** is provided in notebooks in the `src/python` and `src/r` folders. These files show how the models were trained and evaluated, including accuracy scores and intermediate steps.

> **Important:** In the Docker container, I intentionally **did not include print statements** for these intermediate steps. This was a deliberate choice:  
> 1. Print statements are not ideal in a production container.  
> 2. The Docker container includes the **final trained model** on the full dataset, which is cleaner and allows for more accurate predictions.  
> 3. Excluding the model-building scripts keeps the container size small and minimizes build times, while still allowing users to explore the workflow outside Docker.

If you want to perform the analysis yourself:

1. Create a folder named `data` inside the `src` directory.  
2. Place the downloaded `train.csv` and `test.csv` files inside `src/data/`.

---

### 🐍 Python

The Python workflow is provided as a Jupyter notebook:

- **File:** `src/python/build-model.ipynb`  
- **Purpose:** Demonstrates the full model-building process, including preprocessing, logistic regression fitting, and accuracy evaluation.

To run this notebook locally:

```bash
$ pip install -r requirements.dev.txt
```

### 🖥️ R

The Python workflow is provided as a Jupyter notebook:

- **File:** `src/r/build-model.qmd`  
- **Purpose:** Shows the R equivalent workflow for preprocessing, model training, and evaluation.

To run it locally, first install the development dependencies:

```r
$ source("src/r/install_packages_dev.R")
```

**Note:** GitHub does not render Quarto files directly. To make the analysis easy to view, the notebook has been rendered as src/r/build-model.pdf. This allows you to inspect the full workflow and results without running the code.