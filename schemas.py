from typing import Dict, List, Optional
from pydantic import BaseModel

class FillNaConfig(BaseModel):
    strategy: str  # mean, median, mode, constant
    value: Optional[float] = None

class EncodeConfig(BaseModel):
    columns: List[str]
    method: str  # label, onehot

class CleaningConfig(BaseModel):
    fillna: Optional[FillNaConfig] = None
    drop: Optional[List[str]] = None
    rename: Optional[Dict[str, str]] = None
    encode: Optional[EncodeConfig] = None
