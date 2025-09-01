from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile
from androguard.core.bytecodes.apk import APK

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "APK Analyzer API is running. Go to /docs to test."}

# Suspicious permissions ka list
SUSPICIOUS_PERMISSIONS = [
    "android.permission.READ_SMS",
    "android.permission.SEND_SMS",
    "android.permission.RECEIVE_SMS",
    "android.permission.CALL_PHONE",
    "android.permission.RECEIVE_BOOT_COMPLETED",
    "android.permission.READ_CONTACTS",
    "android.permission.WRITE_CONTACTS",
    "android.permission.RECORD_AUDIO",
    "android.permission.CAMERA",
    "android.permission.READ_CALL_LOG",
    "android.permission.WRITE_CALL_LOG"
]

def analyze_apk(apk_path: str):
    try:
        apk = APK(apk_path)

        package = apk.get_package()
        app_name = apk.get_app_name()
        version = apk.get_androidversion_name()
        permissions = apk.get_permissions()

        flagged = [p for p in permissions if p in SUSPICIOUS_PERMISSIONS]

        result = {
            "package": package,
            "app_name": app_name,
            "version": version,
            "permissions": permissions,
            "suspicious_permissions": flagged,
            "is_suspicious": len(flagged) > 0
        }
        return result
    except Exception as e:
        return {"error": str(e)}

@app.post("/analyze_apk/")
async def analyze_apk_endpoint(file: UploadFile = File(...)):
    try:
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".apk") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        analysis = analyze_apk(tmp_path)
        return JSONResponse(content=analysis)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
