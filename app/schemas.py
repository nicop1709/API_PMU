from pydantic import BaseModel
from datetime import datetime

class DataRequest(BaseModel):
    table_name: str
    start_date: datetime
    end_date: datetime
