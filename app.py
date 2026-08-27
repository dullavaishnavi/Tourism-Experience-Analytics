import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Tourism Experience Analytics",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Tourism Experience Analytics")

st.write(
    "Classification, Rating Prediction and Recommendation System"
)

# Load models safely
@st.cache_resource
def load_model(path):
    if os.path.exists(path):
        return joblib.load(path)
    return None


regression_model = load_model(
    "models/best_regression_model.joblib"
)

classification_model = load_model(
    "models/best_classification_model.joblib"
)


st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose a feature",
    [
        "Home",
        "Rating Prediction",
        "Visit Mode Prediction",
        "Recommendations"
    ]
)


# HOME

if page == "Home":

    st.header("Welcome!")

    st.write("""
    This application uses Machine Learning to analyze
    tourism experiences.
    """)

    st.subheader("Features")

    st.write("⭐ Predict attraction ratings")

    st.write("🧳 Predict visit mode")

    st.write("🎯 Recommend tourist attractions")


# RATING PREDICTION

elif page == "Rating Prediction":

    st.header("⭐ Attraction Rating Prediction")

    st.info(
        "The trained regression model will predict the expected attraction rating."
    )

    if regression_model is None:

        st.warning(
            "Regression model is not available yet."
        )

    else:

        st.success(
            "Regression model loaded successfully!"
        )


# CLASSIFICATION

elif page == "Visit Mode Prediction":

    st.header("🧳 Visit Mode Prediction")

    st.info(
        "The classification model predicts the user's visit mode."
    )

    if classification_model is None:

        st.warning(
            "Classification model is not available yet."
        )

    else:

        st.success(
            "Classification model loaded successfully!"
        )


# RECOMMENDATIONS

elif page == "Recommendations":

    st.header("🎯 Attraction Recommendations")

    matrix_path = "models/user_item_matrix.joblib"

    if os.path.exists(matrix_path):

        user_item_matrix = joblib.load(matrix_path)

        user_id = st.selectbox(
            "Select User ID",
            user_item_matrix.index
        )

        n = st.slider(
            "Number of Recommendations",
            1,
            10,
            5
        )

        if st.button("Get Recommendations"):

            user_ratings = user_item_matrix.loc[user_id]

            visited = user_ratings.dropna().index

            recommendations = (
                user_item_matrix.mean()
                .drop(visited, errors="ignore")
                .sort_values(ascending=False)
                .head(n)
            )

            st.subheader("Recommended Attractions")

            st.dataframe(
                recommendations
            )

    else:

        st.warning(
            "Recommendation data is not available yet."
        )
