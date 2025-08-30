# APK Analyzer FastAPI Project

This project is a simple **APK Analyzer** built with **FastAPI** and **Androguard**. It allows you to upload an APK file and extracts its metadata such as app name, package name, version, and permissions.

---

## Requirements

- Python 3.10+
- Virtual environment (recommended)

### Python Packages

```text
fastapi==0.95.2
uvicorn==0.22.0
androguard==3.5.5
```

## Installation Steps

1. **Clone or copy the project folder** to your local machine.

2. **Create a virtual environment** (recommended):

```bash
python -m venv venv
```

3. **Activate the virtual environment**:

- **Windows:**

```bash
venv\Scripts\activate
```

- **Linux/macOS:**

```bash
source venv/bin/activate
```

4. **Install dependencies**:

```bash
pip install -r requirements.txt
```

5. **Ensure project structure:**

```
project-cyber-hackathon/
│
├─ app/                # optional for future routes
├─ uploads/            # uploaded APKs will be stored temporarily
├─ main.py             # FastAPI main app
├─ requirements.txt
```

## Running the Application

1. **Start the FastAPI server:**

```bash
uvicorn main:app --reload
```

2. **Open Swagger UI in your browser:**

```
http://127.0.0.1:8000/docs
```

3. **Upload an APK** using the `/analyze_apk/` POST endpoint and get the JSON response containing:
   - `app_name`
   - `package`
   - `version`
   - `permissions`

## Notes

- Make sure you are using **androguard version 3.5.5**, otherwise some methods may not exist.
- Uploaded APKs are temporarily stored in a temp file and deleted after analysis.
- You can expand the project to save uploaded APKs or add further analysis features.

---

## Example Response

```json
{
  "app_name": "F-Droid",
  "package": "org.fdroid.fdroid",
  "version": "1.21.1",
  "permissions": [
    "android.permission.INTERNET",
    "android.permission.ACCESS_WIFI_STATE",
    "android.permission.CAMERA"
  ]
}
```
