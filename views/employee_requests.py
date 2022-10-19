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

def get_all_employees():
    '''
    this is the docstring
    '''
    return EMPLOYEES

def get_single_employee(id):
    '''
    this is the docstring
    '''
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    '''
    this is the docstring
    '''
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee
