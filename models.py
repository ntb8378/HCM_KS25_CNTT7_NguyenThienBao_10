from database import Base
from sqlalchemy import Column, Integer, String, Float

class EmployeesModels(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    department = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)
    salary = Column(Float, nullable=False)