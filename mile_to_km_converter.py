from tkinter import Tk, Label, Button, Entry, Checkbutton


def calculate_miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609344,1)
    km_value_label.config(text=f"{km}")
    
    
    

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=50,pady=60)

# creating a label

miles_label = Label(text="Miles", font=("Arial",25,))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial",25,))
km_label.grid(column=2, row=1)

equal_label = Label(text="is equal to", font=("Arial",25))
equal_label.grid(column=0, row=1)

km_value_label = Label(text=0, font=("Arial", 25))
km_value_label.grid(column=1, row=1)



#creating a button

calculate_button = Button(text="Calculate", command=calculate_miles_to_km)
calculate_button.grid(row=2, column=1)


# creating inputs

miles_input = Entry(width=10)
miles_input.grid(row=0, column = 1)






window.mainloop()


