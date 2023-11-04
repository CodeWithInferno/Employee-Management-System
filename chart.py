import tkinter as tk
from tkinter import ttk
import mysql.connector

def open_chart_window():
    def fetch_data():
        search_text = search_entry.get()
        
        for record in data_tree.get_children():
            data_tree.delete(record)

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="2618",  # Replace with your MySQL password
            database="admin"
        )

        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM empsal")
        data = cursor.fetchall()
        mydb.close()

        for i, record in enumerate(data):
            if any(search_text.lower() in str(col).lower() for col in record):
                data_tree.insert("", "end", values=record, tags=("highlight",))
            else:
                data_tree.insert("", "end", values=record)

    chart_window = tk.Toplevel()
    chart_window.geometry("1080x690")
    chart_window.title("Chart")

    # Create a frame for the main content (chart_frame)
    chart_frame = tk.Frame(chart_window, relief="solid", borderwidth=1)
    chart_frame.pack(fill="both", expand=True)

    # Create a header frame with text
    header_frame = tk.Frame(chart_frame, bg="black", height=70, relief="raised", borderwidth=1)
    header_frame.pack(fill="x")

    header_label = tk.Label(header_frame, text="Salary Data", font=("Arial", 20), bg="black", fg="gold")
    header_label.pack()

    # Add padding between the header and other frames
    padding_y = 10

    # Create data frame
    data_frame = tk.Frame(chart_frame, padx=10, pady=10)
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

    # Define a tag for highlighting matching records
    data_tree.tag_configure("highlight", background="yellow")

    # Search Frame
    search_frame = tk.Frame(chart_frame, padx=10, pady=10)
    search_frame.pack(fill="both", expand=True, side="right")

    # Search Bar
    field_label = tk.Label(search_frame, text="Search Field:")
    field_label.pack()

    fields = ["empid", "name", "surname", "field", "salary", "bonus", "total"]
    field_combobox = ttk.Combobox(search_frame, values=fields)
    field_combobox.set(fields[0])
    field_combobox.pack()

    search_label = tk.Label(search_frame, text="Search Text:")
    search_label.pack()

    search_entry = ttk.Entry(search_frame)
    search_entry.pack()

    search_button = ttk.Button(search_frame, text="Search", command=fetch_data)
    search_button.pack()

    chart_window.mainloop()






