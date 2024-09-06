import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=200)
window.config(pady=10)

#first label
first_label = tkinter.Label(text="Enter Your Weight(kg)")
first_label.pack(side= "top")
first_label.config(pady=25)

#first entry
first_entry = tkinter.Entry(width=16)
first_entry.pack(side= "top")
first_entry.place(x=100, y=50)

#second label
first_label = tkinter.Label(text="Enter Your Height(cm)")
first_label.pack(side= "top")

#second entry
second_entry = tkinter.Entry(width=16)
second_entry.pack(side= "top")
second_entry.place(x=100, y=95)

def click_button():
    try:
        weight = float(first_entry.get())
        height = float(second_entry.get())
        new_height = height/100
        #BMI =weight/(height)^2
        BMI = weight / new_height ** 2
        result =  round(BMI,2)
        if BMI < 18.5:
            third_label.config(text=f"Your BMI is {result}. You are underweight.")
        elif BMI >= 18.5 and BMI <= 24.9:
            third_label.config(text=f"Your BMI is {result}. You are normal weight.")
        elif BMI >= 25.0 and BMI <= 29.9:
            third_label.config(text=f"Your BMI is {result}. You are Overweight.")
        else:
            third_label.config(text=f"Your BMI is {result}. You are Obesity.")
    except ValueError:  # Error:
        third_label.config(text="Enter your correct Height and Weight!!!")

#button
first_button = tkinter.Button(text="Calculate", width=10, command=click_button)
first_button.pack(side= "top")
first_button.place(x=110, y=120)


#third label
third_label = tkinter.Label(text="")
third_label.pack(side="top")
third_label.place(x=40,y=150)



window.mainloop()

