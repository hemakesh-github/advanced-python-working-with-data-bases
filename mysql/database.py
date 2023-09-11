import mysql.connector as mysql

def connect(db_name):
    try:
        return mysql.connect(host = "localhost",
                   user = "root",
                   password = "hemakesh@mysql",
                   database = db_name)
    except:
        print("error")

def add_project(cursor, project_title, project_description, tasks):
    project_data = (project_title, project_description)
    cursor.execute("INSERT INTO PROJECTS(title, description) VALUES (%s, %s)", project_data)
    tasks_data = []
    for task in tasks:
        task_data =(cursor.lastrowid, task)
        tasks_data.append(task_data)
    cursor.executemany("INSERT INTO tasks(project_id, description) VALUES(%s, %s)",tasks_data)


if __name__ == "__main__":
    db = connect("projects")
    cursor = db.cursor()
    

    tasks = ["clean bathroom", "clean kitchen", "clean living room"]
    add_project(cursor, "Clean house", "Clean house by room", tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    cursor.execute("SELECT * FROM tasks")
    project_tasks = cursor.fetchall()
    print(project_records,project_tasks, sep = "\n")
    db.close()
