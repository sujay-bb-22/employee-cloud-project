import os
import sqlite3

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "employees.db")


def get_db_connection():
    """Create a new SQLite connection for each request."""
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Create the employees table automatically if it does not exist."""
    with get_db_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                department TEXT NOT NULL,
                position TEXT NOT NULL
            )
            """
        )
        connection.commit()


def validate_employee_form(form):
    name = form.get("name", "").strip()
    email = form.get("email", "").strip()
    department = form.get("department", "").strip()
    position = form.get("position", "").strip()

    employee = {
        "name": name,
        "email": email,
        "department": department,
        "position": position,
    }

    errors = []
    if not name:
        errors.append("Name is required.")
    if not email:
        errors.append("Email is required.")
    elif "@" not in email or "." not in email:
        errors.append("Enter a valid email address.")
    if not department:
        errors.append("Department is required.")
    if not position:
        errors.append("Position is required.")

    return employee, errors


def get_employee(employee_id):
    with get_db_connection() as connection:
        return connection.execute(
            "SELECT * FROM employees WHERE id = ?", (employee_id,)
        ).fetchone()


@app.route("/")
def index():
    with get_db_connection() as connection:
        employees = connection.execute(
            "SELECT * FROM employees ORDER BY id DESC"
        ).fetchall()

    return render_template(
        "index.html",
        employees=employees,
        message=request.args.get("message"),
    )


@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        employee, errors = validate_employee_form(request.form)

        if errors:
            return render_template("add.html", employee=employee, errors=errors)

        with get_db_connection() as connection:
            connection.execute(
                """
                INSERT INTO employees (name, email, department, position)
                VALUES (?, ?, ?, ?)
                """,
                (
                    employee["name"],
                    employee["email"],
                    employee["department"],
                    employee["position"],
                ),
            )
            connection.commit()

        return redirect(url_for("index", message="Employee added successfully."))

    return render_template("add.html", employee={}, errors=[])


@app.route("/edit/<int:employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):
    employee = get_employee(employee_id)

    if employee is None:
        return redirect(url_for("index", message="Employee not found."))

    if request.method == "POST":
        updated_employee, errors = validate_employee_form(request.form)

        if errors:
            updated_employee["id"] = employee_id
            return render_template(
                "edit.html", employee=updated_employee, errors=errors
            )

        with get_db_connection() as connection:
            connection.execute(
                """
                UPDATE employees
                SET name = ?, email = ?, department = ?, position = ?
                WHERE id = ?
                """,
                (
                    updated_employee["name"],
                    updated_employee["email"],
                    updated_employee["department"],
                    updated_employee["position"],
                    employee_id,
                ),
            )
            connection.commit()

        return redirect(url_for("index", message="Employee updated successfully."))

    return render_template("edit.html", employee=employee, errors=[])


@app.route("/delete/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id):
    employee = get_employee(employee_id)

    if employee is None:
        return redirect(url_for("index", message="Employee not found."))

    with get_db_connection() as connection:
        connection.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
        connection.commit()

    return redirect(url_for("index", message="Employee deleted successfully."))


init_db()


if __name__ == "__main__":
    app.run(debug=True)
