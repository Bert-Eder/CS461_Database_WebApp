import tkinter as tk
import psycopg2


# Executes when user presses 'Login' button
def login():
    global usr_name
    global usr_passwd
    usr_name = ent_usr.get()
    usr_passwd = ent_passwd.get()
    tk.Toplevel(win_login)

# Not used yet, it is for returning to login screen
def show_login():
    win_login.deiconify()
    tk.Toplevel(win_login)
    win_login.update()

# Executes after user presses 'Login' button
def show_master():
    win_master.deiconify()
    tk.Toplevel(win_master)
    win_master.update()

# Master window with query options
win_master = tk.Tk()
win_master.geometry("500x500")
win_master.title("Pharmaceutical Database")
win_master.withdraw()

# Inserting Drugs Window (halfway done)
win_insert_drug = tk.Tk()
win_insert_drug.geometry("500x500")
win_insert_drug.title("Add Drug to Database")
labels = ["Drug ID", "Scientific Name", "Drug Name", "Dosage", "Storage Temp", "Manufacturer ID",
          "Batch Number", "Expiration Date", "Quantity"]
# List of drug labels and entries
lbl_drug_list = []
ent_drug_list = []

# Pack all the labels and text boxes onto the drug form
for i in range(len(labels)):
    lbl_drug_list.append(tk.Label(master=win_insert_drug, text=labels[i], anchor="w"))
    ent_drug_list.append(tk.Entry(master=win_insert_drug, width=20))
    lbl_drug_list[i].pack()
    ent_drug_list[i].pack()

# Executes when user clicks 'Add drugs' button
def add_drugs():
    entry_list = []
    for item in ent_drug_list:
        entry_list.append(item.get())

    # Connect ot database, use your credentials
    conn = psycopg2.connect(dbname="pharmacy", user="", password="")
    cur = conn.cursor()

    # execute query
    cur.execute(
        'INSERT INTO drug(drug_id, scientific_name, drug_name, dosage, storage_temp, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s)',
        (entry_list[0], entry_list[1], entry_list[2], entry_list[3], entry_list[4], entry_list[5]))

    ### THIS IS TEMP FOR TESTING
    cur.execute("""
        SELECT * FROM drug WHERE drug_id = '00001111'
        """
    )

    print(cur.fetchall())
    conn.close()

# executes when user selects 'Insert Drugs' from the master window
def show_insert_drug():
    win_insert_drug.deiconify()
    tk.Toplevel(win_insert_drug)
    win_insert_drug.update()

# Button for sending the insert drugs query
btn_insert_drugs = tk.Button(master=win_insert_drug, text="Add Drug", anchor="w", command=add_drugs)
btn_insert_drugs.pack()

# Button for opening the insert drugs window
btn_master_a = tk.Button(master=win_master, text="Insert Drugs", anchor="w", command=show_insert_drug)
btn_master_a.pack()

# Create Login Window
win_login = tk.Tk()
win_login.title("Login")
win_login.geometry("300x300")

# Frames
frm_master_a = tk.Frame(master=win_master)

frm_login_a = tk.Frame(master=win_login)  # user info here
frm_login_b = tk.Frame(master=win_login)  # password here
frm_login_c = tk.Frame(master=win_login)  # button here

# ***** LABELS *******
# Master form

# User Login Form
lbl_usr = tk.Label(master=frm_login_a, text="Login", anchor="w")
lbl_usr.pack()
lbl_passwd = tk.Label(master=frm_login_b, text="Password", anchor="w")
lbl_passwd.pack()

# Entries
ent_usr = tk.Entry(master=frm_login_a, width=50)
ent_usr.pack()
ent_passwd = tk.Entry(master=frm_login_b, width=50)
ent_passwd.pack()

# **** BUTTONS ****
btn_select_usr_login = tk.Button(
    master=frm_master_a,
    text="Employee Login",
    command=show_login,
)
btn_select_usr_login.pack()

# Login button
tk.Button()
btn_login = tk.Button(
    master=frm_login_c,
    text="Login",
    command=show_master
)
btn_login.pack()

frm_master_a.pack()
frm_login_a.pack()
frm_login_b.pack()
frm_login_c.pack()

win_insert_drug.withdraw()

win_login.mainloop()