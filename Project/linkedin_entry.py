import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Import the DateEntry widget
from db.insert import insert_linkedin
from datetime import datetime
from os.path import exists
from sys import platform

lan = ['blekinge län', 'dalarnas län', 'gotlands län', 'gävleborgs län', 'hallands län', 'jämtlands län', 'jönköpings län', 'kalmar län', 'kronobergs län', 'norrbottens län', 'skåne län', 'stockholms län', 'södermanlands län', 'uppsala län', 'värmlands län', 'västerbottens län', 'västernorrlands län', 'västmanlands län', 'västra Götalands län', 'örebro län', 'östergötlands län']

def find_db_path():
        if(platform == "linux"):
            return "Project/db/echo.db"
        elif(platform == "darwin"):
            return "Project/db/echo.db"
        else:
            return "Project\db\echo.db"

def convert_date_format(input_date):
    try:
        # Parse input date in MM/DD/YY format
        parsed_date = datetime.strptime(input_date, '%m/%d/%y')
        
        # Convert to YYYY-MM-DD format
        converted_date = parsed_date.strftime('%Y-%m-%d')
        
        return converted_date
    except ValueError:
        return "Invalid date format"

def submit_data():
    results = {}
    selected_item = dropdown_var.get()
    data = [entry.get() for entry in input_entries]
    date = date_entry.get() 
    results[selected_item] = {'data': data, 'date': date}  # Save data and date
   

    for entry in input_entries:
        entry.delete(0, 'end')
    print(results)
    print(selected_item.split()[0])
    print(results[selected_item]['data'][3])
    print(str(date))
    print(convert_date_format(date))
    cntrl = True
    for nb in results[selected_item]['data']:
        if nb == '':
            cntrl = False

    if cntrl:
        for i in range(21):
            insert_linkedin(results[selected_item]['data'][i], selected_item.split()[0], lan[i], convert_date_format(date),find_db_path())


app = tk.Tk()
app.title("Data Collection")

# Dropdown list
dropdown_var = tk.StringVar()
dropdown_label = ttk.Label(app, text="Select Item:")
dropdown_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
dropdown = ttk.Combobox(app, textvariable=dropdown_var)
dropdown['values'] = ('10 Elektriker', '9 Ingenjör', '8 Logistiker', '7 Läkare', '6 Lärare', '5 Operatör', '4 Projektledare', '3 Sjuksköterska', '2 Tekniker', '1 Utvecklare')
dropdown.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Input boxes
input_entries = []
for i in range(21):
    label = ttk.Label(app, text=f"{lan[i]}:")
    label.grid(row=i+2, column=0, padx=10, pady=5)
    entry = ttk.Entry(app)
    entry.grid(row=i+2, column=1, padx=10, pady=5)
    input_entries.append(entry)

# Date input box
date_label = ttk.Label(app, text="Select Date:")
date_label.grid(row=23, column=0, padx=10, pady=5)
date_entry = DateEntry(app)
date_entry.grid(row=23, column=1, padx=10, pady=5)

# Submit button
submit_button = ttk.Button(app, text="Submit", command=submit_data)
submit_button.grid(row=24, column=0, columnspan=2, padx=10, pady=10)

# Dictionary to store results
results = {}

app.mainloop()