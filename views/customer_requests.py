import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
      "id": 1,
      "name": "Elizabeth Witt",
    },
    {
      "id": 2,
      "name": "Jeff Stever",
    },
    {
      "id": 3,
      "name": "Jeff Adams",
    },
    {
      "id": 4,
      "name": "Sage Klein",
    },
    {
      "id": 5,
      "name": "Ani Osborne",
    },
    {
      "id": 6,
      "name": "Susan Wiens",
    },
    {
      "id": 7,
      "name": "Josh Wiens",
    },
    {
      "id": 8,
      "name": "Tori Gedvillas",
    },
    {
      "id": 9,
      "name": "Chris Honiball",
    },
]

def create_customer(customer):
    '''
    this is the docstring
    '''
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    '''
    docstring
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))

def update_customer(id, new_customer):
    '''
    docstring
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Customer
            SET
                name = ?,
                address = ?,
                email = ?,
                password = ?,
        WHERE id = ?
        """, (new_customer['name'], new_customer['address'],
              new_customer['email'], new_customer['password'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def get_all_customers():
    '''
    this is the docstring
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name
        FROM customer c
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            customer = Customer(row['id'], row['name'], row['address'])

            customers.append(customer.__dict__)

    return json.dumps(customers)

def get_single_customer(id):
    '''
    this is the docstring
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name
        FROM customer c 
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'])

        return json.dumps(customer.__dict__)

def get_customer_by_email(email):
    '''
    docstring
    '''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'],row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
