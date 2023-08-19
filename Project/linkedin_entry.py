import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Import the DateEntry widget

lan = ['Blekinge län', 'Dalarnas län', 'Gotlands län', 'Gävleborgs län', 'Hallands län', 'Jämtlands län', 'Jönköpings län', 'Kalmar län', 'Kronobergs län', 'Norrbottens län', 'Skåne län', 'Stockholms län', 'Södermanlands län', 'Uppsala län', 'Värmlands län', 'Västerbottens län', 'Västernorrlands län', 'Västmanlands län', 'Västra Götalands län', 'Örebro län', 'Östergötlands län']

def submit_data():
    results = {}
    selected_item = dropdown_var.get()
    data = [entry.get() for entry in input_entries]
    date = date_entry.get() 
    results[selected_item] = {'data': data, 'date': date}  # Save data and date
   

    for entry in input_entries:
        entry.delete(0, 'end')
    print(results)
    print(selected_item[:2])
    print(results[selected_item]['data'][3])

app = tk.Tk()
app.title("Data Collection")

# Dropdown list
dropdown_var = tk.StringVar()
dropdown_label = ttk.Label(app, text="Select Item:")
dropdown_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
dropdown = ttk.Combobox(app, textvariable=dropdown_var)
dropdown['values'] = ('10 Elektriker', '9  Ingenjör', '8  Logistiker', '7  Läkare', '6  Lärare', '5  Operatör', '4  Projektledare', '3  Sjuksköterska', '2  Tekniker', '1  Utvecklare')
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