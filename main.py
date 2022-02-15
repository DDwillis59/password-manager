
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- SEARCH BUTTON ------------------------------- #
def search():
    web = Web_Input.get()
    try:
        with open('passwords.json', 'r') as info:
            data = json.load(info)
            for i in data.items():
                if i[0] == web.title():
                    newdata = i[1]
    except FileNotFoundError:
        messagebox.showerror(message='No passwords have been saved yet')
    else:
        try:
            email = newdata['email']
            password = newdata['password']
        
        except UnboundLocalError:
            messagebox.showerror(message='This password does not exist')
        else:
            messagebox.showinfo(title= web.title(), message=f'Website: {web.title()}\n Email: {email}\n Password: {password}')
    

    

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def genpass():
    Pass_Input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for i in range(nr_letters)]
    password_number = [random.choice(numbers) for i in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]

    password_list = password_letter + password_number + password_symbols
    random.shuffle(password_list)
    
    password = ''.join(password_list)
    pyperclip.copy(password)
    Pass_Input.insert(END, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def savepass():
    
    Website = Web_Input.get()
    Email = Email_Input.get()
    Password = Pass_Input.get()

    newdata = {
        Website.title(): {
            "email": Email,
            "password": Password
        }
    }

    if Website == '' or Password == '':
        messagebox.showerror(title='Error',message= 'Must put in password or website')
    else:

        box = messagebox.askokcancel(title=Website,message=f'Do you want to save this email and password \n Email : {Email} \n Password: {Password}')
        if box:
            try:
                with open('passwords.json', 'r') as data_file:
                    #reading
                    data1 = json.load(data_file)
                    #updating
                    data1.update(newdata)
            except FileNotFoundError:
                # AES Key

                #saving
                with open("passwords.json", 'w') as file:
                    json.dump(newdata, file, indent=4) 
                Web_Input.delete(0, END)
                Pass_Input.delete(0, END)
            else:
                #saving
                with open("passwords.json", 'w') as file:
                    json.dump(data1, file, indent=4) 
                Web_Input.delete(0, END)
                Pass_Input.delete(0, END)

        else:
            pass
    

    

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()

canvas = Canvas(height=200, width=200)
canvas.grid(column=2, row=1)
img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image= img)
root.config(padx=20, pady=20)
root.maxsize(height=360,width=500)
root.minsize(height=360,width=500)
root.title('Password Manager')

#buttons
add_button = Button(width=45, text='Add', command=savepass)
add_button.grid(column=2, row=5, columnspan=2,)

search_button = Button(text= 'Search' ,width=14, command=search)
search_button.grid(column=3, row=2)

gen_pass = Button(text='Generate Password',command=genpass)
gen_pass.grid(column=3, row=4)
#labels
website = Label(text="Website: ")
website.grid(column=1, row=2)

Email_Username = Label(text="Email/Username: ")
Email_Username.grid(column=1, row=3)

password = Label(text="Password: ")
password.grid(column=1, row=4)

#entries
Web_Input = Entry(width=35)
Web_Input.grid(column=2, row=2)
Web_Input.focus()

Email_Input = Entry(width=53)
Email_Input.grid(column=2, row=3, columnspan=2)
Email_Input.insert(END, '')

Pass_Input = Entry(width=35)
Pass_Input.grid(column=2, row=4)






root.mainloop()
