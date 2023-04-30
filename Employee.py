class Employee:

    def __init__(self, name, emp_id, department, salary, age, seniority):
        self.name = name
        self.id = emp_id
        self.department = department
        self.salary = salary
        self.age = age
        self.seniority = seniority

    def __str__(self):
        return "id,    name,    department,    age,    salary,    seniority\n" \
               "{},    {},    {},    {},    {},    {}".format(self.id, self.name, self.department, self.age, self.salary, self.seniority)

emp1 = Employee("dave", 1234, "ops", 7000, 24, 2)
print(emp1)