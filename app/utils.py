import random
import string

def extract_features(file_path: str):
    """Fake feature extractor for now"""
    features = {
        "dangerous_permissions": random.randint(0, 5),
        "network_calls": random.randint(0, 10),
        "suspicious_apis": random.randint(0, 3),
    }
    return features

def generate_apk_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
