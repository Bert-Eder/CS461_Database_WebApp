import tkinter as tk
import psycopg2

# Globals
usr_name = None
usr_passwd = None

# Create Login Window (first window or root window)
win_login = tk.Tk()
win_login.geometry("300x200")
win_login.title("Login")
# win_login.configure(bg='blue')

""" # Executes when user presses 'Login' button
def login():
    global usr_name
    global usr_passwd
    usr_name = ent_usr.get()
    usr_passwd = ent_passwd.get()
    #tk.Toplevel(win_login)

# Not used yet, it is for returning to login screen
def show_login():
    win_login.deiconify()
    tk.Toplevel(win_login)
    win_login.update()
    win_login.destroy()
 """


# Executes after user presses 'Login' button
# Master window with query options
def show_master():
    win_master = tk.Toplevel(win_login)
    win_master.geometry("300x500")
    win_master.title("Pharmaceutical Database")
    # win_master.deiconify()
    # win_master.update()
    win_login.withdraw()

    # set window color
    win_master.configure(bg='#a4a7c7')

    # executes when user selects 'Insert Drugs' from the master window
    def show_insert_drug():
        win_insert_drug = tk.Toplevel(win_master)
        win_insert_drug.geometry("400x500")
        win_insert_drug.title("Add Drug to Database")
        # win_insert_drug.deiconify()
        # win_insert_drug.update()
        # win_insert_drug.withdraw()

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

        # Executes when user clicks 'Add drugs' button from the insert drug window
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
            cur.execute("""SELECT * FROM drug WHERE drug_id = '00001111'""")

            print(cur.fetchall())
            conn.close()

        # Button for submiting the insert drugs query
        btn_insert_drugs = tk.Button(master=win_insert_drug, text="Add Drug", anchor="w", command=add_drugs, bg='green',
                                     font='Ubuntu')
        btn_insert_drugs.pack()

    # executes when user selects '"quantity in stock" from the master window
    def show_qtyInStock():
        win_qtyInStock = tk.Toplevel(win_master)
        win_qtyInStock.geometry("500x100")
        win_qtyInStock.title("Quantity of a Drug in Storage")
        # win_insert_drug.deiconify()
        # win_qtyInStock.update()
        # win_qtyInStock.withdraw()

        # User Login Form
        lbl_qtyInStock = tk.Label(master=win_qtyInStock, text="Drug Name", anchor="w")
        lbl_qtyInStock.pack()

        # Entries
        ent_qtyInStock = tk.Entry(master=win_qtyInStock, width=50)
        ent_qtyInStock.pack()

        # Executes when user clicks 'submit' button
        def check_qtyInStock():
            # Connect ot database, use your credentials
            conn = psycopg2.connect(dbname="pharmacy", user="", password="")
            cur = conn.cursor()

            # execute query
            cur.execute(
                'SELECT  qty_in_stock FROM  drug, stored_drug WHERE drug.drug_name = %s AND stored_drug.drug_id = drug.drug_id',
                (ent_qtyInStock.get()))

            print(cur.fetchall())
            conn.close()

        # Button for checking the quantity of stock
        btn_submit_qtyInStock = tk.Button(master=win_qtyInStock, text="submit", anchor="w", command=check_qtyInStock,
                                          bg='green', font='Ubuntu')
        btn_submit_qtyInStock.pack()

    # Button for opening the insert drugs window
    btn_master_a = tk.Button(master=win_master, text="Insert Drugs", anchor="w", command=show_insert_drug, bg='green',
                             font='Ubuntu')
    btn_master_a.pack()

    # Button for checking the quantity of stock
    btn_qtyInStock = tk.Button(master=win_master, text="Quantity in Stock", anchor="w", command=show_qtyInStock,
                               bg='green', font='Ubuntu')
    btn_qtyInStock.pack()


# setting up the login window ----------------------------------------
# Frames -
""" frm_master_a = tk.Frame(master=win_master)
frm_login_a = tk.Frame(master=win_login)  # user info here
frm_login_b = tk.Frame(master=win_login)  # password here
frm_login_c = tk.Frame(master=win_login)  # button here
frm_master_a.pack()
frm_login_a.pack()
frm_login_b.pack()
frm_login_c.pack()
 """

# Master form (window)
# User Login Form
lbl_usr = tk.Label(master=win_login, text="Login", anchor="w", bg='green', font='Ubuntu')
lbl_usr.pack()
ent_usr = tk.Entry(master=win_login, width=50)
ent_usr.pack()

lbl_passwd = tk.Label(master=win_login, text="Password", anchor="w", bg='green', font='Ubuntu')
lbl_passwd.pack()
ent_passwd = tk.Entry(master=win_login, width=50)
ent_passwd.pack()

# Login button in master window
btn_login = tk.Button(master=win_login, text="Login", command=show_master, bg='green', font='Ubuntu')
btn_login.pack()

# Button in master window login, is this even being used?
# btn_select_usr_login = tk.Button(master=frm_master_a, text="Employee Login", command=show_login)
# btn_select_usr_login.pack()

win_login.mainloop()