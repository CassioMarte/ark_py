from sqlalchemy import Column, String, Integer, ForeignKey
from src.models.settings.sqlite.base import Base  
from src.utils.generate_uuid import generate_uuid

class PeopleTable(Base):  # pylint: disable=too-few-public-methods
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False, default=generate_uuid)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    pet_uuid = Column(String(36), ForeignKey('pets.uuid'), nullable=True)
