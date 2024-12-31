import tkinter as tk
from tkinter import messagebox

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")
        self.root.geometry("400x500")
        self.root.configure(bg="#f4f4f4")

        self.transactions = []

        # Header
        self.header = tk.Label(root, text="Finance Tracker", bg="#4caf50", fg="white", font=("Arial", 16, "bold"), pady=10)
        self.header.pack(fill=tk.X)

        # Input fields
        self.input_frame = tk.Frame(root, bg="#f4f4f4", pady=10)
        self.input_frame.pack(fill=tk.X, padx=20)

        self.description_label = tk.Label(self.input_frame, text="Description", bg="#f4f4f4", font=("Arial", 12))
        self.description_label.pack(anchor="w")
        self.description_entry = tk.Entry(self.input_frame, font=("Arial", 12))
        self.description_entry.pack(fill=tk.X, pady=5)

        self.amount_label = tk.Label(self.input_frame, text="Amount", bg="#f4f4f4", font=("Arial", 12))
        self.amount_label.pack(anchor="w")
        self.amount_entry = tk.Entry(self.input_frame, font=("Arial", 12))
        self.amount_entry.pack(fill=tk.X, pady=5)

        # Buttons frame
        self.button_frame = tk.Frame(root, bg="#f4f4f4", pady=10)
        self.button_frame.pack(fill=tk.X, padx=20)

        self.add_income_button = tk.Button(self.button_frame, text="Add Income", bg="#4caf50", fg="white", font=("Arial", 12), command=self.add_income)
        self.add_income_button.grid(row=0, column=0, padx=5, pady=5)

        self.add_expense_button = tk.Button(self.button_frame, text="Add Expense", bg="#f44336", fg="white", font=("Arial", 12), command=self.add_expense)
        self.add_expense_button.grid(row=0, column=1, padx=5, pady=5)

        self.view_summary_button = tk.Button(self.button_frame, text="View Summary", bg="#2196f3", fg="white", font=("Arial", 12), command=self.view_summary)
        self.view_summary_button.grid(row=1, column=0, padx=5, pady=5)

        self.clear_transactions_button = tk.Button(self.button_frame, text="Clear Transactions", bg="#ff9800", fg="white", font=("Arial", 12), command=self.clear_transactions)
        self.clear_transactions_button.grid(row=1, column=1, padx=5, pady=5)

        self.exit_button = tk.Button(root, text="Exit", bg="#9e9e9e", fg="white", font=("Arial", 12), command=root.quit)
        self.exit_button.pack(pady=10)

    def add_transaction(self, description, amount):
        self.transactions.append({"description": description, "amount": amount})

    def add_income(self):
        description = self.description_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Income must be greater than zero.")
            self.add_transaction(description, amount)
            messagebox.showinfo("Success", "Income added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        finally:
            self.description_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)

    def add_expense(self):
        description = self.description_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Expense must be greater than zero.")
            self.add_transaction(description, -amount)
            messagebox.showinfo("Success", "Expense added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        finally:
            self.description_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)

    def view_summary(self):
        total_income = sum(txn['amount'] for txn in self.transactions if txn['amount'] > 0)
        total_expense = sum(txn['amount'] for txn in self.transactions if txn['amount'] < 0)
        balance = total_income + total_expense

        summary = (
            f"Total Income: Rp{total_income:.2f}\n"
            f"Total Expense: Rp{abs(total_expense):.2f}\n"
            f"Balance: Rp{balance:.2f}\n\n"
            "Transaction History:\n"
        )

        for i, txn in enumerate(self.transactions, 1):
            summary += f"{i}. {txn['description']} (Rp{txn['amount']:.2f})\n"

        messagebox.showinfo("Summary", summary)

    def clear_transactions(self):
        self.transactions = []
        messagebox.showinfo("Success", "All transactions have been cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    root.mainloop()