from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from androguard.core.bytecodes.apk import APK
import tempfile
import shutil
import os

app = FastAPI()

@app.post("/analyze_apk/")
async def analyze_apk(file: UploadFile = File(...)):
    try:
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".apk") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        
        apk = APK(tmp_path)

        
        result = {
            "app_name": apk.get_app_name(),
            "package": apk.get_package(),
            "version": apk.get_version_name(),
            "permissions": apk.get_permissions(),
        }

        
        os.remove(tmp_path)

        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
