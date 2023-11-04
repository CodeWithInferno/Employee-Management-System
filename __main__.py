# import mysql.connector
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import pyfiglet
# from chart import open_chart_window
# from edit import open_editor_window

# # Global variables
# entries = {}
# screen_width = 0
# screen_height = 0
# sidebar_width = 0
# main_frame = None

# # Database initialization
# def Sql():
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="2618"
#     )
#     cur = mydb.cursor()


# # Security functions (Login, Register, Admin Panel)
# def Security():
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="2618"
#     )
#     cur = mydb.cursor()
#     # cur.execute("CREATE DATABASE IF NOT EXISTS admin")
#     cur.execute("use admin")
#     cur.execute("CREATE TABLE IF NOT EXISTS admin(Name varchar(25), User varchar(25), Password varchar(25))")
    
#     # User input (Login or Register)
#     a = int(input("""
#     •) Login    == 1
#     •) Register == 2
#     •) Enter Your Choice:- """))
    
#     # Define a function for submitting data to the database
#     def submit_data():
#         # Fetch data from entry fields
#         name = entries['name'].get()
#         surname = entries['surname'].get()
#         field = entries['field'].get()
#         salary = entries['salary'].get()
#         bonus = entries['bonus'].get()
#         total = entries['total'].get()

#         # Insert Data
#         cur.execute("INSERT INTO empsal (name, surname, field, salary, bonus, total) VALUES (%s, %s, %s, %s, %s, %s)",
#                     (name, surname, field, salary, bonus, total))
#         mydb.commit()
#         print("Data Submitted To Database")
        
#         # Field cleaner
#         for entry in entries.values():
#             entry.delete(0, tk.END)

#     # Login process
#     if a == 1:
#         print("-=-=-=-=- Admin Panel Login -=-=-=-=-=-")
#         u = input("Enter Your Username: ")
#         p = input("Enter Password: ")
#         cur.execute("SELECT * FROM admin WHERE User = %s AND Password = %s", (u, p))
#         result = cur.fetchone()
#         if result:
#             print(f"Admin Logged in as {u}")
            
#             # Define a function to open the salary input window
#             def open_salary_window():
#                 salary_window = tk.Toplevel()
                
#                 # Calculate the dimensions to fit the available space
#                 salary_window.geometry(f"{screen_width - 40}x{screen_height - 90}")
#                 salary_window.title("Employee Salary Form")

#                 # Basic form
#                 form_labels = ['name', 'surname', 'field', 'salary', 'bonus', 'total']
                
#                 for i, label_text in enumerate(form_labels):
#                     label = tk.Label(salary_window, text=label_text.capitalize())
#                     label.grid(row=i, column=0, padx=10, pady=10, sticky="w")
#                     entry = tk.Entry(salary_window, width=20)
#                     entry.grid(row=i, column=1, padx=10, pady=10, sticky="e")
#                     entries[label_text] = entry  # Store the entry widgets in the global dictionary

#                 submit_button = tk.Button(salary_window, text="Submit", command=submit_data)
#                 submit_button.grid(row=len(form_labels), columnspan=2, padx=10, pady=10)

#             root = tk.Tk()
#             # Update screen width and height
#             global screen_width, screen_height, sidebar_width, main_frame
#             screen_width = root.winfo_screenwidth()
#             screen_height = root.winfo_screenheight()
#             sidebar_width = 40  # Assign the sidebar width

#             root.geometry("{0}x{1}+0+0".format(screen_width, screen_height))
#             root.title("Employee Salary Manager")

#             # Create a header frame with text
#             header_frame = tk.Frame(root, bg="black", height=90, relief="raised", borderwidth=1)
#             header_frame.pack(fill="x")

#             # Create a label with the header text
#             header_label = tk.Label(header_frame, text="Employee Salary Manager", font=("Arial", 20), bg="black", fg="gold")
#             header_label.pack(expand=True, fill='both')

#             # Create a frame for the sidebar
#             sidebar_frame = tk.Frame(root, bg="darkgray", relief="solid", borderwidth=1, padx=10, pady=10)
#             sidebar_frame.pack(fill="y", side="left")

#             # Set the width of the sidebar
#             sidebar_frame.config(width=sidebar_width)

#             # Buttons within the sidebar with fixed width and padding
#             button1 = tk.Button(sidebar_frame, text="Salary", bg="gold", fg="black", width=10, command=open_salary_window)
#             button1.pack(fill="x", padx=10, pady=10)
            
#             button2 = tk.Button(sidebar_frame, text="Chart", bg="gold", fg="black", width=10, command=open_chart_window)
#             button2.pack(fill="x", padx=10, pady=10)
            
#             button3 = tk.Button(sidebar_frame, text="Editor", bg="gold", fg="black", width=10, command=open_editor_window)
#             button3.pack(fill="x", padx=10, pady=10)

#             # Create a frame for the main content (main_frame)
#             main_frame = tk.Frame(root, relief="solid", borderwidth=1)
#             main_frame.pack(fill="both", expand=True)

#             # Call the set_main_frame_image function to display the image in the main_frame
#             set_main_frame_image(main_frame)

#             root.mainloop()

#         else:
#             print("Wrong username or password")

#     # Registration process
#     if a == 2:
#         print("-=-=-=-=- Admin Panel Register -=-=-=-=-=-")

# # Banner and image display
# def Banner():
#     result = pyfiglet.figlet_format("Employee Salary Manager")
#     print(result)

# def set_main_frame_image(main_frame):
#     # Load the image and resize it to fit the main_frame
#     img = Image.open("hotel images/myh.jpg")
#     img = img.resize((screen_width - sidebar_width - 40, screen_height - 90))
#     photo = ImageTk.PhotoImage(img)

#     # Create a label to display the image
#     image_label = tk.Label(main_frame, image=photo)
#     image_label.image = photo
#     image_label.pack(fill="both", expand=True)

# # Entry point and execution
# def Executer():
#     Sql()
#     Banner()
#     Security()

# if __name__ == "__main__":
#     Executer()



# Import required libraries
import mysql.connector
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pyfiglet
from chart import open_chart_window
from edit import open_editor_window

# Global variables
entries = {}
screen_width = 0
screen_height = 0
sidebar_width = 0
main_frame = None

# Database initialization
def Sql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2618"
    )
    cur = mydb.cursor()

# Security functions (Login, Register, Admin Panel)
def Security():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2618"
    )
    cur = mydb.cursor()
    # cur.execute("CREATE DATABASE IF NOT EXISTS admin")
    cur.execute("use admin")
    cur.execute("CREATE TABLE IF NOT EXISTS admin(Name varchar(25), User varchar(25), Password varchar(25))")
    
    # User input (Login or Register)
    a = int(input("""
    •) Login    == 1
    •) Register == 2
    •) Enter Your Choice:- """))
    
    # Define a function for submitting data to the database
    def submit_data():
        # Fetch data from entry fields
        name = entries['name'].get()
        surname = entries['surname'].get()
        field = entries['field'].get()
        salary = entries['salary'].get()
        bonus = entries['bonus'].get()
        total = entries['total'].get()

        # Insert Data
        cur.execute("INSERT INTO empsal (name, surname, field, salary, bonus, total) VALUES (%s, %s, %s, %s, %s, %s)",
                    (name, surname, field, salary, bonus, total))
        mydb.commit()
        print("Data Submitted To Database")
        
        # Field cleaner
        for entry in entries.values():
            entry.delete(0, tk.END)

    # Login process
    if a == 1:
        print("-=-=-=-=- Admin Panel Login -=-=-=-=-=-")
        u = input("Enter Your Username: ")
        p = input("Enter Password: ")
        cur.execute("SELECT * FROM admin WHERE User = %s AND Password = %s", (u, p))
        result = cur.fetchone()
        if result:
            print(f"Admin Logged in as {u}")
            
            # Define a function to open the salary input window
            def open_salary_window():
                salary_window = tk.Toplevel()
                
                # Calculate the dimensions to fit the available space
                salary_window.geometry(f"{screen_width - 40}x{screen_height - 90}")
                salary_window.title("Employee Salary Form")

                # Basic form
                form_labels = ['name', 'surname', 'field', 'salary', 'bonus', 'total']
                
                for i, label_text in enumerate(form_labels):
                    label = tk.Label(salary_window, text=label_text.capitalize())
                    label.grid(row=i, column=0, padx=10, pady=10, sticky="w")
                    entry = tk.Entry(salary_window, width=20)
                    entry.grid(row=i, column=1, padx=10, pady=10, sticky="e")
                    entries[label_text] = entry  # Store the entry widgets in the global dictionary

                submit_button = tk.Button(salary_window, text="Submit", command=submit_data)
                submit_button.grid(row=len(form_labels), columnspan=2, padx=10, pady=10)

            root = tk.Tk()
            # Update screen width and height
            global screen_width, screen_height, sidebar_width, main_frame
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            sidebar_width = 40  # Assign the sidebar width

            root.geometry("{0}x{1}+0+0".format(screen_width, screen_height))
            root.title("Employee Salary Manager")

            # Create a header frame with text
            header_frame = tk.Frame(root, bg="black", height=90, relief="raised", borderwidth=1)
            header_frame.pack(fill="x")

            # Create a label with the header text
            header_label = tk.Label(header_frame, text="Employee Salary Manager", font=("Arial", 20), bg="black", fg="gold")
            header_label.pack(expand=True, fill='both')

            # Create a frame for the sidebar
            sidebar_frame = tk.Frame(root, bg="darkgray", relief="solid", borderwidth=1, padx=10, pady=10)
            sidebar_frame.pack(fill="y", side="left")

            # Set the width of the sidebar
            sidebar_frame.config(width=sidebar_width)

            # Buttons within the sidebar with fixed width and padding
            button1 = tk.Button(sidebar_frame, text="Salary", bg="gold", fg="black", width=10, command=open_salary_window)
            button1.pack(fill="x", padx=10, pady=10)
            
            button2 = tk.Button(sidebar_frame, text="Chart", bg="gold", fg="black", width=10, command=open_chart_window)
            button2.pack(fill="x", padx=10, pady=10)
            
            button3 = tk.Button(sidebar_frame, text="Editor", bg="gold", fg="black", width=10, command=open_editor_window)
            button3.pack(fill="x", padx=10, pady=10)

            # Create a frame for the main content (main_frame)
            main_frame = tk.Frame(root, relief="solid", borderwidth=1)
            main_frame.pack(fill="both", expand=True)

            # Call the set_main_frame_image function to display the image in the main_frame
            set_main_frame_image(main_frame)

            root.mainloop()

        else:
            print("Wrong username or password")

    # Registration process
    if a == 2:
        print("-=-=-=-=- Admin Panel Register -=-=-=-=-=-")

# Banner and image display
def Banner():
    result = pyfiglet.figlet_format("Employee Salary Manager")
    print(result)

def set_main_frame_image(main_frame):
    # Load the image and resize it to fit the main_frame
    img = Image.open("employee payment\myh.jpg")
    img = img.resize((screen_width - sidebar_width - 40, screen_height - 90))
    photo = ImageTk.PhotoImage(img)

    # Create a label to display the image
    image_label = tk.Label(main_frame, image=photo)
    image_label.image = photo
    image_label.pack(fill="both", expand=True)

# Entry point and execution
def Executer():
    Sql()
    Banner()
    Security()

if __name__ == "__main__":
    Executer()
