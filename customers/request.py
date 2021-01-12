CUSTOMERS = [
    {
      "email": "DawnOps@icloud.com",
      "password": "19972011",
      "name": "Kyle Nevels",
      "id": 1
    },
    {
      "email": "mauligan@hghg.com",
      "password": "13792",
      "name": "Kyle Nevels",
      "id": 2
    },
    {
      "email": "mcrib@gmail.com",
      "password": "143",
      "name": "Dawny Nevels",
      "id": 3
    }
]
def get_all_customers():
    return CUSTOMERS
    # Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the Customers list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer