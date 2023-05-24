import requests
from Employee import Employee
import ast
url = "http://127.0.0.1:5000"


def is_open():
    if requests.exceptions.ConnectionError:
        return False
    return True


def test_server():
    response = requests.get('/test')
    print(response.text)


def add_employee():
    f_name, l_name = input("Enter employee full name: ").split()
    emp_id = input("Enter employee id: ")
    department = input("Enter employee department: ")
    salary = input("Enter employee salary: ")
    age = input("Enter employee age: ")
    gender = input("Enter employee gender [F/M]: ").upper()
    emp = Employee(emp_id, f_name, l_name, department, salary, age, gender)
    response = requests.post(url=url + '/add_employee', json=emp.__dict__, data="")
    print(response.text)


def get_employee_by_id():
    emp_id = input("Enter id of the employee you would like to view: ")
    response = requests.get(url=url + '/get_emp_by_id?id={}'.format(emp_id))
    print(response.status_code)


def get_employee_by_name():
    emp_name = input("Enter full name of the employee you would like to view: ").replace(' ', '-')
    # print(emp_name.split(sep='-')[0], emp_name.split(sep='-')[1])
    response = requests.get(url=url + '/get_emp_by_name?name={}'.format(emp_name))
    print(response.text)


def get_all_employees():
    res = requests.get(url + '/get_all_emps')
    tuple_from_res_text = ast.literal_eval(res.text)
    for t in tuple_from_res_text:
        print(t)


def update_employee():
    pass


def delete_employee():
    emp_id = int(input("Enter id of employee to delete: "))
    res = requests.delete(url + f'/delete_employee?id={emp_id}')
    print(res.text)


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
    for item in functions:
        print(item, str(functions[item]).split()[1])


def main():
    print("Welcome")
    while(is_open):
        printMenu()
        choice = int(input())
        functions[choice]()


if __name__ == "__main__":
    main()
