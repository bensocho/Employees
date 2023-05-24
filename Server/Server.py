from flaskext.mysql import MySQL
from flask import Flask, request
import json

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'employees_dev'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Aa123456'
app.config['MYSQL_DATABASE_DB'] = 'employees'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/test", methods=["GET"])
def health_check():
    return "healthy"


@app.route('/add_employee', methods=['POST'])
def add_employee():
    newEmp = request.json
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO employees (id, first_name, last_name, department, salary, age, gender) VALUES (%s, %s, %s, "
        "%s, %s, %s, %s)",
        (int(newEmp['_Employee__id']), newEmp['_Employee__first_name'], newEmp['_Employee__last_name'],
         newEmp['_Employee__department'], float(newEmp['_Employee__salary']), float(newEmp['_Employee__age']),
         newEmp['_Employee__gender'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return "A new employee was added: " + str(newEmp['_Employee__first_name']) + " " + str(
        newEmp['_Employee__last_name'])


@app.route('/get_emp_by_name', methods=["GET"])
def get_emp_by_name():
    emp_name = request.args.get('name')
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE first_name = %s AND last_name = %s",
                (emp_name.split(sep='-')[0], emp_name.split(sep='-')[1]))
    emp = cur.fetchone()
    cur.close()
    conn.close()
    return '{}, {}, {}, {}, {}, {}, {}'.format(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6])


@app.route('/get_emp_by_id', methods=["GET"])
def get_emp_by_id():
    emp_id = request.args.get('id')
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE id = %s", emp_id)
    emp = cur.fetchone()
    cur.close()
    conn.close()
    return f'{emp[0]}, {emp[1]}, {emp[2]}, {emp[3]}, {emp[4]}, {emp[5]}, {emp[6]}'


@app.route('/get_all_emps', methods=["GET"])
def get_all_emps():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    emps = cur.fetchall()
    cur.close()
    conn.close()
    return str(emps)


@app.route('/delete_employee', methods=['DELETE'])
def delete_employee():
    emp_id = int(request.args.get('id'))
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT first_name, last_name FROM employees WHERE id = %s", emp_id)
    emp = cur.fetchone()
    cur.execute("DELETE FROM employees WHERE id = %s", emp_id)
    cur.close()
    conn.close()
    if emp == None:
        return f"Employee with id {emp_id} not found", 400
    print(emp[0], emp[1])
    return f"1 employee deleted: {emp[0]} {emp[1]}", 200


if __name__ == "__main__":
    app.run(debug=True)
