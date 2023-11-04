import tkinter as tk
from tkinter import ttk
import mysql.connector

def open_editor_window():
    def fetch_data():
        for record in data_tree.get_children():
            data_tree.delete(record)

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2618",
            database="admin"
        )

        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM empsal")
        data = cursor.fetchall()
        mydb.close()

        for record in data:
            data_tree.insert("", "end", values=record)

    def update_data():
        emp_id = emp_id_entry.get()
        name = name_entry.get()
        surname = surname_entry.get()
        field = field_entry.get()
        salary = salary_entry.get()
        bonus = bonus_entry.get()
        total = total_entry.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2618",
            database="admin"
        )

        cursor = mydb.cursor()

        update_query = "UPDATE empsal SET"
        updates = []

        if name:
            updates.append(f"name = '{name}'")
        if surname:
            updates.append(f"surname = '{surname}'")
        if field:
            updates.append(f"field = '{field}'")
        if salary:
            updates.append(f"salary = '{salary}'")
        if bonus:
            updates.append(f"bonus = '{bonus}'")
        if total:
            updates.append(f"total = '{total}'")

        if updates:
            update_query += " " + ", ".join(updates)
            update_query += f" WHERE empid = {emp_id}"
            cursor.execute(update_query)
            mydb.commit()
            mydb.close()
            status_label.config(text="Data updated successfully", fg="green")
        else:
            status_label.config(text="No fields to update", fg="red")

        # Fetch updated data and display
        fetch_data()

    def delete_data():
        emp_id = emp_id_entry.get()
        
        if not emp_id:
            status_label.config(text="Enter Emp ID for deletion", fg="red")
            return

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2618",
            database="admin"
        )

        cursor = mydb.cursor()

        delete_query = f"DELETE FROM empsal WHERE empid = {emp_id}"
        cursor.execute(delete_query)
        mydb.commit()
        mydb.close()
        
        status_label.config(text="Data deleted successfully", fg="green")
        fetch_data()

    editor_window = tk.Toplevel()
    editor_window.geometry("1080x690")
    editor_window.title("Editor")

    # Create a frame for the main content (editor_frame)
    editor_frame = tk.Frame(editor_window, relief="solid", borderwidth=1)
    editor_frame.pack(fill="both", expand=True)

    # Create a header frame with text
    header_frame = tk.Frame(editor_frame, bg="black", height=70, relief="raised", borderwidth=1)
    header_frame.pack(fill="x")

    header_label = tk.Label(header_frame, text="Data Editor", font=("Arial", 20), bg="black", fg="gold")
    header_label.pack()

    # Add padding between the header and other frames
    padding_y = 10

    # Create data frame
    data_frame = tk.Frame(editor_frame, padx=10, pady=10)
    data_frame.pack(fill="both", expand=True, side="left")

    # Create a "Fetch Data" button at the top
    fetch_data_button = tk.Button(data_frame, text="Fetch Data", command=fetch_data)
    fetch_data_button.pack()

    # Create a treeview widget to display the table
    data_tree = ttk.Treeview(data_frame, columns=["empid", "name", "surname", "field", "salary", "bonus", "total"])
    data_tree.heading("#1", text="Emp ID", anchor="center")
    data_tree.heading("#2", text="Name", anchor="center")
    data_tree.heading("#3", text="Surname", anchor="center")
    data_tree.heading("#4", text="Field", anchor="center")
    data_tree.heading("#5", text="Salary", anchor="center")
    data_tree.heading("#6", text="Bonus", anchor="center")
    data_tree.heading("#7", text="Total", anchor="center")

    data_tree.pack(fill="both", expand=True)

    # Set column widths to 30 pixels
    for col in data_tree['columns']:
        data_tree.column(col, width=50)

    # Editor Frame
    editor_data_frame = tk.Frame(editor_frame, padx=10, pady=10)
    editor_data_frame.pack(fill="both", expand=True, side="right")

    # Create an editor section
    editor_label = tk.Label(editor_data_frame, text="Edit Data")
    editor_label.pack()

    # Input fields
    emp_id_label = tk.Label(editor_data_frame, text="Emp ID:")
    emp_id_label.pack()
    emp_id_entry = ttk.Entry(editor_data_frame)
    emp_id_entry.pack()
    
    emp_id_label = tk.Label(editor_data_frame, text="Choose the Empid of Row You Want To Edit")
    emp_id_label.pack()

    separator_label = tk.Label(editor_data_frame, text="----------------------------")
    separator_label.pack()
    emp_id_label = tk.Label(editor_data_frame, text="Now when you have chosen the row now you can edit the information")
    emp_id_label.pack()
    emp_id_label = tk.Label(editor_data_frame, text="Choose one or more fields to edit; leave the rest empty")
    emp_id_label.pack()
    name_label = tk.Label(editor_data_frame, text="Name:")
    name_label.pack()
    name_entry = ttk.Entry(editor_data_frame)
    name_entry.pack()

    surname_label = tk.Label(editor_data_frame, text="Surname:")
    surname_label.pack()
    surname_entry = ttk.Entry(editor_data_frame)
    surname_entry.pack()

    field_label = tk.Label(editor_data_frame, text="Field:")
    field_label.pack()
    field_entry = ttk.Entry(editor_data_frame)
    field_entry.pack()

    salary_label = tk.Label(editor_data_frame, text="Salary:")
    salary_label.pack()
    salary_entry = ttk.Entry(editor_data_frame)
    salary_entry.pack()

    bonus_label = tk.Label(editor_data_frame, text="Bonus:")
    bonus_label.pack()
    bonus_entry = ttk.Entry(editor_data_frame)
    bonus_entry.pack()

    total_label = tk.Label(editor_data_frame, text="Total:")
    total_label.pack()
    total_entry = ttk.Entry(editor_data_frame)
    total_entry.pack()

    # Update button
    update_button = ttk.Button(editor_data_frame, text="Update Data", command=update_data)
    update_button.pack()

    # Add a "Delete Data" button
    separator_label = tk.Label(editor_data_frame, text="----------------------------")
    separator_label.pack()

    emp_id_label = tk.Label(editor_data_frame, text="Emp ID:")
    emp_id_label.pack()
    emp_id_entry = ttk.Entry(editor_data_frame)
    emp_id_entry.pack()
        
    delete_button = ttk.Button(editor_data_frame, text="Delete Data", command=delete_data)
    delete_button.pack()

    # Status label
    status_label = tk.Label(editor_data_frame, text="", fg="green")
    status_label.pack()

    editor_window.mainloop()

def open_chart_window():
   
    root = tk.Tk()
    root.title("Employee Salary Manager")

    # Header Frame
    header_frame = tk.Frame(root, bg="black")
    header_frame.pack(fill="x")

    header_label = tk.Label(header_frame, text="Employee Salary Manager", font=("Arial", 20), bg="black", fg="gold")
    header_label.pack()

    # Sidebar Frame
    sidebar_frame = tk.Frame(root, width=250, bg="blue", relief="sunken", borderwidth=2)
    sidebar_frame.pack(fill="y", side="left")

    # Create buttons for sidebar
    chart_button = ttk.Button(sidebar_frame, text="Chart", command=open_chart_window)
    editor_button = ttk.Button(sidebar_frame, text="Editor", command=open_editor_window)

    chart_button.pack(pady=10)
    editor_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main":
    open_chart_window()
