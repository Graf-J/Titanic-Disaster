from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

numeric_features = ["SibSp", "Parch"]
scale_features = ["Age", "Fare"]
sex_features = ["Sex"]
pclass_features = ["Pclass"]
embarked_features = ["Embarked"]

# Pipelines
numeric_pipeline = Pipeline([("passthrough", "passthrough")])

scale_pipeline = Pipeline(
    [("imputer", SimpleImputer(strategy="mean")), ("scaler", StandardScaler())]
)

sex_pipeline = Pipeline([("map", OneHotEncoder(drop="if_binary", dtype=int))])

pclass_pipeline = Pipeline(
    [("encoder", OneHotEncoder(drop="first", sparse_output=False))]
)

embarked_pipeline = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(drop="first", sparse_output=False)),
    ]
)

# Preprocessor
preprocessor = ColumnTransformer(
    [
        ("num", numeric_pipeline, numeric_features),
        ("scale", scale_pipeline, scale_features),
        ("sex", sex_pipeline, sex_features),
        ("pclass", pclass_pipeline, pclass_features),
        ("embarked", embarked_pipeline, embarked_features),
    ]
)

# Model Pipeline
model = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
    ]
)
