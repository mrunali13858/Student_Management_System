import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2004",
    database="students"
)

if conn.is_connected():
    print("Database Connected Successfully!")

    cursor=conn.cursor()

    name=input("Enter  Name: ")
    age=int(input("Enter Age: "))
    course=input("Enter Course: ")
    mobile=input("Enter Mobile Number:")

    query="INSERT INTO students(name,age,course,mobile) VALUES(%s,%s,%s,%s)"
    values=(name,age,course,mobile)

    cursor.execute(query, values)
    conn.commit()
    print("Student Record Inserted Successfully!")

    query="SELECT * FROM students"
    cursor.execute(query)

    records=cursor.fetchall()
    print("\n------student List------")
    
    for row in records:
                 print(row)

    search_name=input("\nEnter Name to Search: ")
    query="SELECT  * FROM students WHERE name=%s"
    cursor.execute(query, (search_name,))
    result=cursor.fetchall()

    if result:
                print("\nstudent found:")
                print(result)
    else:
                print("\nStudent Not Found")

    update_name = input("\nEnter Name to Update: ")
    new_age = int(input("Enter New Age: "))

    query = "UPDATE students SET age=%s WHERE name=%s"
    cursor.execute(query, (new_age, update_name))
    conn.commit()

    if cursor.rowcount > 0:
                print("Student Record Updated Successfully!")
    else:
                print("Student Not Found!")

    delete_name = input("\nEnter Name to Delete: ")

    query = "DELETE FROM students WHERE name=%s"
    cursor.execute(query, (delete_name,))
    conn.commit()

    if cursor.rowcount > 0:
                print("Student Record Deleted Successfully!")
    else:
                print("Student Not Found!")

                
    

        
            