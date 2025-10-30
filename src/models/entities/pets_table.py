from sqlalchemy import Column, String, Integer
from src.models.settings.sqlite.base import Base  
from src.utils.generate_uuid import generate_uuid

class PetsTable(Base):  # pylint: disable=too-few-public-methods
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False, default=generate_uuid)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
