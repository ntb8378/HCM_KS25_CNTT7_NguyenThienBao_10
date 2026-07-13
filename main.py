from fastapi import FastAPI, Depends
from models import EmployeesModels
from database import Base, engine, get_db
from sqlalchemy.orm import Session
import employees_service
from schemas import EmployeesCreate

app = FastAPI(
    title="Quản lý thông tinh nhân viên"
)

Base.metadata.create_all(bind = engine)

@app.get("/")
def test_root():
    return {
        "message": "sever đang hoạt động"
    }

@app.get("/employees",tags=["test"])
def get_employees(db:Session = Depends(get_db)):
    return employees_service.get_employees(db)

@app.get("/get_employees/search/{department}",tags=["employees"])
def get_employees_search_department(department:str, db:Session = Depends(get_db)):
    return employees_service.get_employees_search_department(db, department)

@app.get("/employees/{employees_id}",tags=["employees"])
def get_employees_by_id(employees_id:int, db:Session = Depends(get_db)):
    return employees_service.get_employees_by_id(db,employees_id)

@app.post("/employees",tags=["employees"])
def post_employees(addemployees: EmployeesCreate, db:Session = Depends(get_db)):
    return employees_service.post_employees(db, addemployees)
    
@app.put("/employees/{employee_id}",tags=["employees"])
def put_employees(employees_id:int, employees: EmployeesCreate, db:Session = Depends(get_db)):
    return employees_service.put_employees(db,employees_id,employees)

@app.delete("/employees/{employee_id}",tags=["employees"])
def delete_employees(employees_id:int, db:Session = Depends(get_db)):
    return employees_service.delete_employees(db, employees_id)