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

def get_all_customers():
    '''
    this is the docstring
    '''
    return CUSTOMERS

def get_single_customer(id):
    '''
    this is the docstring
    '''
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

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
    this is the docstring
    '''
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    '''
    this is the docstring
    '''
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
