EMPLOYEES = [
    {
      "name": "Jonathen",
      "locationId": 2,
      "animalId": 1,
      "id": 1
    },
    {
      "name": "Jonathens",
      "locationId": 1,
      "animalId": 1,
      "id": 2
    },
    {
      "name": "asd",
      "locationId": 1,
      "animalId": 2,
      "id": 3
    }
]
def get_all_employees():
    return EMPLOYEES
    # Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the Employees list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
def create_employees(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee