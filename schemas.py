from pydantic import BaseModel

class EmployeesCreate(BaseModel):
    full_name : str 
    department : str 
    position : str 
    salary : float