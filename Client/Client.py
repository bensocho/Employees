import requests

isOpen = True
def test_server():
    pass
def add_employee():
    pass
def get_employee_by_id():
    pass
def get_employee_by_name():
    pass
def get_all_employees():
    pass
def update_employee():
    pass
def delete_employee():
    pass
def import_employees_from_csv():
    pass
def export_employees_to_csv():
    pass
functions = {
    0: test_server,
    1: add_employee,
    2: get_employee_by_id,
    3: get_employee_by_name,
    4: get_all_employees,
    5: update_employee,
    6: delete_employee,
    7: import_employees_from_csv,
    8: export_employees_to_csv,
    9: exit
}




def printMenu():
    pass


def main():
    print("Welcome")
    while(isOpen):
        printMenu()
        choice = int(input())

if __name__ == "__main__":
    main()