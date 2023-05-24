class Employee:

    def __init__(self, emp_id, first_name, last_name, department, salary, age, gender):
        self.__id = emp_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__department = department
        self.__salary = salary
        self.__age = age
        self.__gender = gender
    @property
    def get_first_name(self):
        return self.first_name

    @property
    def get_last_name(self):
        return self.last_name
    @property
    def get_id(self):
        return self.id
    @property
    def get_department(self):
        return self.department

    @property
    def get_salary(self):
        return self.salary

    @property
    def get_salary(self):
        return self.salary

    @property
    def get_gender(self):
        return self.gender
    def get_age(self, value):
        return self.age


    def __str__(self):
        return "id: {}, name: {}, department: {}, salary: {}, age: {}, gender: {}". format(self.id, self.name, self.department, self.salary, self.age, self.gender)


