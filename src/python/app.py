import streamlit as st
import pandas as pd
from pipeline import model

# Page Config
st.set_page_config(page_title="Titanic Survival Classifier 🚢", page_icon="🚢")

# Title
st.title(":blue[Titanic Survival Classifier] 🚢")
st.write(
    "Train a logistic regression model to predict who survived the Titanic disaster."
)

st.markdown("---")

# Upload Training File
st.header("🧠 Train Your Model")
uploaded_train_file = st.file_uploader("Upload your `train.csv` file", type="csv")

if uploaded_train_file is not None:
    df_train = pd.read_csv(uploaded_train_file)
    if set(df_train.columns) != {
        "Age",
        "Cabin",
        "Embarked",
        "Fare",
        "Name",
        "Parch",
        "PassengerId",
        "Pclass",
        "Sex",
        "SibSp",
        "Survived",
        "Ticket",
    }:
        st.error(
            "❌ The uploaded training file does not match the expected structure.\n\n"
            "Please make sure it's the **original Kaggle Titanic `train.csv`** file "
            "with the following columns:\n\n"
            "`PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, "
            "`Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`."
        )
    else:
        X = df_train.drop("Survived", axis=1)
        y = df_train["Survived"]
        model.fit(X, y)
        st.success(
            "✅ Model trained successfully! You can now upload a test file to make predictions."
        )

# Upload Test File
df_result = None
if uploaded_train_file is not None:
    st.markdown("---")
    st.header("🔎 Make Predictions")
    uploaded_test_file = st.file_uploader("Upload your `test.csv` file", type="csv")
    if uploaded_test_file is not None:
        X_test = pd.read_csv(uploaded_test_file)
        if set(X_test.columns) != {
            "Age",
            "Cabin",
            "Embarked",
            "Fare",
            "Name",
            "Parch",
            "PassengerId",
            "Pclass",
            "Sex",
            "SibSp",
            "Ticket",
        }:
            st.error(
                "❌ The uploaded test file does not match the expected structure.\n\n"
                "Please make sure it's the **original Kaggle Titanic `test.csv`** file "
                "with the following columns:\n\n"
                "`PassengerId`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, "
                "`Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`."
            )
        else:
            y_pred = model.predict(X_test)
            df_result = pd.DataFrame(
                {"PassengerId": X_test["PassengerId"], "Survived": y_pred}
            )
            st.success("✅ Predictions generated successfully!")

            st.dataframe(df_result.head(), width="stretch")

# Download Predictions
if df_result is not None:
    st.markdown("---")
    st.download_button(
        label="💾 Download Predictions",
        data=df_result.to_csv(index=False).encode("utf-8"),
        file_name="predictions.csv",
        mime="text/csv",
        help="Click to download your prediction results as a CSV file.",
    )
