import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Kess Chandler",
    },
    {
        "id": 2,
        "name": "Elanor Chandler",
    },
    {
        "id": 3,
        "name": "Ryann Chandler",
    },
    {
        "id": 4,
        "name": "Kristen Chandler",
    },
    {
        "id": 5,
        "name": "James Chandler",
    },
    {
        "id": 6,
        "name": "Chud",
    },
    {
        "id": 7,
        "name": "BB Wee Wee",
    },
    {
        "id": 8,
        "name": "Blizzy B",
    },
]

def create_employee(employee):
    '''
    this is the docstring
    '''
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    '''
    this is the docstring
    '''
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    '''
    this is the docstring
    '''
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break

def get_all_employees():
    '''
    this is the docstring
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name
        FROM employee e
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['id'], row['name'])

            employees.append(employee.__dict__)

    return json.dumps(employees)

def get_single_employee(id):
    '''
    this is the docstring
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'])

        return json.dumps(employee.__dict__)
