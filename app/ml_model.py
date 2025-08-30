import random

def predict(apk_features: dict):
    """
    Dummy prediction function for APK analysis.
    In the real system, this will use a trained ML model.
    """
    result = random.choice(["Legitimate", "Fake"])

    explanation = (
        "Flagged due to suspicious permissions" if result == "Fake" 
        else "No issues found"
    )

    return {
        "prediction": result,
        "explanation": explanation
    }
