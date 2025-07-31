# FastAPI Data Cleaning API

A FastAPI service that reuses the transformation logic from my [python-data-pipeline](https://github.com/Deski9/python-data-pipeline) project.  
Upload a CSV file and a JSON config to automatically clean and transform your dataset.  
The API applies modular transformations and returns the cleaned data as a downloadable CSV or a JSON preview.

## 🔧 Features
- ♻️ Reuses proven transform logic from [python-data-pipeline](https://github.com/Deski9/python-data-pipeline)
- 📂 CSV file upload via multipart form-data  
- ✅ JSON config validation with Pydantic  
- 🧹 Supported transformations:  
  - Drop columns  
  - Rename columns  
  - Fill missing values (mean, median, mode, constant)  
  - Encode categorical variables (label / one-hot)  
- 📤 Flexible output: download cleaned CSV or preview JSON  
- ⚡ Auto-generated Swagger docs at `/docs`  

## 📁 Project Structure
```
fastapi-data-cleaning-api/
├── main.py                  # FastAPI app entrypoint
├── schemas.py               # Pydantic models for config
├── services/
│   └── transform_service.py # Wrapper for cleaning logic
├── transform.py             # Core transformation functions
├── sample_config.json       # Example configuration file
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

```bash
git clone https://github.com/Deski9/FastAPI-Data-Cleaning-API.git
cd FastAPI-Data-Cleaning-API
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API.

## 📤 Example Request

```bash
curl -X POST "http://127.0.0.1:8000/clean" \
-F "file=@titanic.csv" \
-F 'config={
    "fillna": {"strategy": "mean"},
    "drop": ["Cabin"],
    "rename": {"Survived": "IsSurvived"},
    "encode": {"columns": ["Sex"], "method": "label"}
}'
```

Or use the interactive Swagger UI.

## 🧠 Example Config

```json
{
  "fillna": {"strategy": "mean"},
  "drop": ["Cabin"],
  "rename": {"Survived": "IsSurvived"},
  "encode": {"columns": ["Sex"], "method": "label"}
}
```
