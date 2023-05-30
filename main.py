from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list+= random.choice(letters)

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password5 = ""
    for char in password_list:
      password5 += char

    password.insert(0,password5)
    pyperclip.copy(password5)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    with open("data.txt","a") as f:
        website=website_form.get()
        email=email_username.get()
        password1=password.get()
        if len(website)==0 or len(password1)==0:
            messagebox.showinfo(title="OOps",message="Some fields are empty")
        else:
            yes=messagebox.askokcancel(title=website,message=f"These are the details that are entered: \nEmail:{email}\nPassword:{password1}")
            if yes:
                f.write(f"{website} || {email} || {password1}\n")
                website_form.delete(0,END)
                password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50,pady=50)



canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

label=Label(text="Website:")
label.grid(row=1,column=0)

website_form=Entry(width=35)
website_form.focus()
website_form.grid(row=1,column=1,columnspan=2)

label1=Label(text="Email/Username:")
label1.grid(row=2,column=0)

email_username=Entry(width=35)
email_username.grid(row=2,column=1,columnspan=2)
email_username.insert(0,"hello@gmail.com")

label2=Label(text="Password:")
label2.grid(row=3,column=0)

password=Entry(width=18)
password.grid(row=3,column=1)

button=Button(text="Generate Password",width=11,command=get)
button.grid(row=3,column=2)

button1=Button(text="Add",width=32,command=add)
button1.grid(row=4,column=1,columnspan=2)

window.mainloop()