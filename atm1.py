import tkinter as tk
from tkinter import messagebox


password = 1234
balance = 5000
transaction_history = []


def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')


def login():
    entered_pin = pin_entry.get()
    if not entered_pin.isdigit():
        messagebox.showerror("Error", "Enter digits only.")
        return
    if int(entered_pin) == password:
        show_menu()
    else:
        messagebox.showerror("Error", "Wrong PIN")

def show_menu():
    login_frame.pack_forget()
    menu_frame.pack(pady=20)

def check_balance():
    messagebox.showinfo("Balance", f"Your Current Balance is ₹{balance}")

def withdraw():
    def do_withdraw():
        global balance
        amt = amt_entry.get()
        if amt.isdigit() and int(amt) > 0:
            amt = int(amt)
            if amt <= balance:
                balance -= amt
                transaction_history.append(f"Withdrawn ₹{amt}")
                messagebox.showinfo("Success", f"Withdrawn ₹{amt}\nNew Balance: ₹{balance}")
                withdraw_window.destroy()
            else:
                messagebox.showerror("Error", "Insufficient Balance")
        else:
            messagebox.showerror("Error", "Invalid amount")

    withdraw_window = tk.Toplevel(root, bg="#f9f9f9")
    withdraw_window.title("Withdraw")
    center_window(withdraw_window, 300, 150)
    tk.Label(withdraw_window, text="Enter Amount:", bg="#f9f9f9", font=("Arial", 12)).pack(pady=10)
    amt_entry = tk.Entry(withdraw_window, font=("Arial", 12))
    amt_entry.pack(pady=5)
    tk.Button(withdraw_window, text="Withdraw", font=("Arial", 11), bg="#f44336", fg="white", command=do_withdraw).pack(pady=10)

def deposit():
    def do_deposit():
        global balance
        amt = amt_entry.get()
        if amt.isdigit() and int(amt) > 0:
            amt = int(amt)
            balance += amt
            transaction_history.append(f"Deposited ₹{amt}")
            messagebox.showinfo("Success", f"Deposited ₹{amt}\nNew Balance: ₹{balance}")
            deposit_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid amount")

    deposit_window = tk.Toplevel(root, bg="#f9f9f9")
    deposit_window.title("Deposit")
    center_window(deposit_window, 300, 150)
    tk.Label(deposit_window, text="Enter Amount:", bg="#f9f9f9", font=("Arial", 12)).pack(pady=10)
    amt_entry = tk.Entry(deposit_window, font=("Arial", 12))
    amt_entry.pack(pady=5)
    tk.Button(deposit_window, text="Deposit", font=("Arial", 11), bg="#4CAF50", fg="white", command=do_deposit).pack(pady=10)

def show_transactions():
    history_window = tk.Toplevel(root, bg="#f0f0ff")
    history_window.title("Transaction History")
    center_window(history_window, 350, 250)
    if not transaction_history:
        tk.Label(history_window, text="No transactions yet.", bg="#f0f0ff", font=("Arial", 12)).pack(pady=10)
    else:
        for idx, txn in enumerate(transaction_history, start=1):
            tk.Label(history_window, text=f"{idx}. {txn}", bg="#f0f0ff", font=("Arial", 11)).pack(anchor="w", padx=20)

def change_pin():
    def update_pin():
        global password
        old = old_entry.get()
        new = new_entry.get()
        confirm = confirm_entry.get()
        if old != str(password):
            messagebox.showerror("Error", "Incorrect current PIN")
        elif new != confirm or len(new) != 4 or not new.isdigit():
            messagebox.showerror("Error", "New PIN mismatch or invalid format")
        else:
            password = int(new)
            messagebox.showinfo("Success", "PIN changed successfully!")
            pin_window.destroy()

    pin_window = tk.Toplevel(root, bg="#fff0f0")
    pin_window.title("Change PIN")
    center_window(pin_window, 300, 250)
    for lbl in ["Old PIN:", "New PIN:", "Confirm New PIN:"]:
        tk.Label(pin_window, text=lbl, bg="#fff0f0", font=("Arial", 12)).pack(pady=5)
    old_entry = tk.Entry(pin_window, show='*', font=("Arial", 12)); old_entry.pack()
    new_entry = tk.Entry(pin_window, show='*', font=("Arial", 12)); new_entry.pack()
    confirm_entry = tk.Entry(pin_window, show='*', font=("Arial", 12)); confirm_entry.pack()
    tk.Button(pin_window, text="Change", font=("Arial", 11), bg="#2196F3", fg="white", command=update_pin).pack(pady=10)

# Main Window
root = tk.Tk()
root.title("💳 ATM Simulator")
root.configure(bg="#e0f7fa")
center_window(root, 400, 450)

# Login Frame
login_frame = tk.Frame(root, bg="#e0f7fa")
tk.Label(login_frame, text="💳 Welcome to ATM", font=('Arial', 18, 'bold'), bg="#e0f7fa").pack(pady=20)
tk.Label(login_frame, text="Enter Your 4-digit PIN", font=('Arial', 14), bg="#e0f7fa").pack(pady=10)
pin_entry = tk.Entry(login_frame, show='*', font=('Arial', 14), justify="center")
pin_entry.pack(pady=10)
tk.Button(login_frame, text="Login", font=('Arial', 13), bg="#2196F3", fg="white", width=15, command=login).pack(pady=20)
login_frame.pack()

# Menu Frame
menu_frame = tk.Frame(root, bg="#e0f7fa")
tk.Label(menu_frame, text="🏧 ATM MENU", font=('Arial', 16, 'bold'), bg="#e0f7fa").pack(pady=15)
btn_style = {'width': 25, 'font': ('Arial', 12), 'padx': 5, 'pady': 4}
tk.Button(menu_frame, text="1. Check Balance", command=check_balance, bg="#80cbc4", **btn_style).pack(pady=5)
tk.Button(menu_frame, text="2. Withdraw", command=withdraw, bg="#ff8a65", **btn_style).pack(pady=5)
tk.Button(menu_frame, text="3. Deposit", command=deposit, bg="#aed581", **btn_style).pack(pady=5)
tk.Button(menu_frame, text="4. Change PIN", command=change_pin, bg="#ba68c8", **btn_style).pack(pady=5)
tk.Button(menu_frame, text="5. Transaction History", command=show_transactions, bg="#7986cb", **btn_style).pack(pady=5)
tk.Button(menu_frame, text="6. Exit", command=root.destroy, bg="#ef5350", **btn_style).pack(pady=10)

root.mainloop()
