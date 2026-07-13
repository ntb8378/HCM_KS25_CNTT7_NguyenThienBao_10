from sqlalchemy.orm import Session
from models import EmployeesModels
from fastapi import HTTPException, status
from schemas import EmployeesCreate

def get_employees(db:Session):
    find = db.query(EmployeesModels).all()
    if not find:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Danh sách rỗng!")
    return {
        "statusCode": 200,
        "error": None,
        "message": "Lấy danh sách nhân viên thành công",
        "data": find
}

def get_employees_search_department(db:Session, Input_department:str):
    find_department = db.query(EmployeesModels).filter(EmployeesModels.department.like(f"%{Input_department}%")).first()
    if not find_department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy nhân viên!")
    return {
        "statusCode": 200,
        "error": None,
        "message": "tìm nhân viên theo phòng ban thành công",
        "data": find_department
}


def get_employees_by_id(db:Session, employees_id:int):
    find_id = db.query(EmployeesModels).filter(EmployeesModels.id == employees_id).first()
    if not find_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy nhân viên!")
    return {
        "statusCode": 200,
        "error": None,
        "message": "tìm nhân viên theo id thành công",
        "data": find_id
}

def post_employees(db:Session, employees:EmployeesCreate):
    new_employees = EmployeesModels(
        full_name = employees.full_name,
        department = employees.department,
        position = employees.position,
        salary = employees.salary
    )
    if not new_employees:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="thêm thất bại!")
    db.add(new_employees)
    db.commit()
    db.refresh(new_employees)

    return{
        "statusCode": 200,
        "error": None,
        "message": "thêm nhân viên thành công",
        "data": new_employees
}

def put_employees(db:Session, employees_id:int, updateemployees:EmployeesCreate):
    find_id = db.query(EmployeesModels).filter(EmployeesModels.id == employees_id).first()
    if not find_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy nhân viên!")
    
    find_id.full_name = updateemployees.full_name,
    find_id.department = updateemployees.department,
    find_id.position = updateemployees.position,
    find_id.salary = updateemployees.salary

    db.commit()

    return{
        "statusCode": 200,
        "error": None,
        "message": "thêm nhân viên thành công",
        "data": find_id
}

def delete_employees(db:Session, employees_id:int):
    find_id = db.query(EmployeesModels).filter(EmployeesModels.id == employees_id).first()
    if not find_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy nhân viên!")
    db.delete(find_id)
    db.commit()
    return {
        "statusCode": 200,
        "error": None,
        "message": "xóa nhân viên thành công",
        "data": find_id
}