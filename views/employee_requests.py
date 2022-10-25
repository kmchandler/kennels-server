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
    docstring
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    '''
    docstring
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                address = ?,
                location_id = ?,
        WHERE id = ?
        """, (new_employee['name'], new_employee['address'],
              new_employee['locationId'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

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
            e.name,
            e.location_id
        FROM employee e
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['id'], row['name'], row['location_id'])

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
            l.name,
            l.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['location_id'])

        return json.dumps(employee.__dict__)

def get_employee_by_location(location_id):
    '''
    get employee by location
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.location_id
        FROM employee a
        WHERE a.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)
