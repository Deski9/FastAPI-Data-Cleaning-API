from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
import io, json
import pandas as pd
from schemas import CleaningConfig
from services.transform_service import apply_cleaning

app = FastAPI(title="FastAPI Data Cleaning API")

@app.post("/clean")
async def clean_data_endpoint(
    file: UploadFile = File(...),
    config: str = Form(...),
    preview: bool = Form(False)   # toggle between CSV download and JSON preview
):
    try:
        
        config_dict = json.loads(config)
        cleaning_config = CleaningConfig(**config_dict)

        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
    
        df_cleaned = apply_cleaning(io.BytesIO(contents), cleaning_config)

        if preview:
            return df_cleaned.head(10).to_dict(orient="records")
        else:
            stream = io.StringIO()
            df_cleaned.to_csv(stream, index=False)
            stream.seek(0)
            return StreamingResponse(
                iter([stream.getvalue()]),
                media_type="text/csv",
                headers={"Content-Disposition": "attachment; filename=cleaned.csv"}
            )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
