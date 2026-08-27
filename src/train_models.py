import joblib
import os


def save_model(model, filename):

    os.makedirs(
        "models",
        exist_ok=True
    )

    path = os.path.join(
        "models",
        filename
    )

    joblib.dump(
        model,
        path
    )

    print(
        f"Model saved successfully: {path}"
    )
