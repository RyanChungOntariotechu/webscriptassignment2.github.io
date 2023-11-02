#Ryan Chung #100867856

from tkinter import *
import math

class BMI_Calculator:
    def __init__(self, master):
        # GUI initiation
        self.master = master
        master.title("BMI Calculator")
        
        # input label and field creation
        

        self.label_height = Label(master, text="Enter height (m): ")
        self.label_height.grid(row=0, column=0)

        self.entry_height = Entry(master)
        self.entry_height.grid(row=0, column=1)
        
        self.label_weight = Label(master, text="Enter weight (kg): ")
        self.label_weight.grid(row=1, column=0)

        self.entry_weight = Entry(master)
        self.entry_weight.grid(row=1, column=1)
        
        # create calculate button
        self.button_calculate = Button(master, text="Calculate BMI", command=self.calculate_bmi_number)
        self.button_calculate.grid(row=2, column=0)

        # create label to display result
        self.label_bmi_result = Label(master, text="")
        self.label_bmi_result.grid(row=2, column=1)

    def calculate_bmi_number(self):
        # BMI calculations
        height = float(self.entry_height.get())
        weight = float(self.entry_weight.get())
        
        bmi = weight / (height**2)
        self.label_bmi_result.config(text=f"BMI: {bmi:.2f} ({self.get_bmi_status_description(bmi)})")

    def get_bmi_status_description(self, bmi_value):
        # returing BMI description
        if bmi_value < 5:
            return "Underweight"
        elif bmi_value < 24.9 and bmi_value>=5:
            return "Healthy Weight"
        else:
            return "Overweight"

        
    
# GUI creation 
root = Tk()

# BMI calculator initialization
my_gui = BMI_Calculator(root)

# GUI loop
root.mainloop()

#End