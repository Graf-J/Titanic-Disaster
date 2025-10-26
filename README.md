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


## 🧠 Notes
If you’re interested in the data cleaning, preprocessing, and model selection workflow, you can find the corresponding scripts inside the `src/python` and `src/r` folders.  
These files are provided for transparency and exploration purposes only. They are **excluded from the Docker build** to keep the container size small and build times short.

If you’d like to perform the analysis yourself:
1. Create a folder named `data` inside the `src` directory.
2. Place the downloaded `train.csv` and `test.csv` files inside `src/data/`.

---

### 🐍 Python

To explore or modify the Jupyter notebooks in the `src/python` folder, install the required development dependencies:

```bash
$ pip install -r requirements.dev.txt
```