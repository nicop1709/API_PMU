from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

# Exemple de table, à adapter selon tes besoins
class ExampleTable(Base):
    __tablename__ = "example_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    timestamp = Column(DateTime, index=True)
