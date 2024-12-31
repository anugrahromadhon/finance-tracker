import os

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, description, amount):
        self.transactions.append({"description": description, "amount": amount})

    def view_summary(self):
        total_income = sum(txn['amount'] for txn in self.transactions if txn['amount'] > 0)
        total_expense = sum(txn['amount'] for txn in self.transactions if txn['amount'] < 0)
        balance = total_income + total_expense

        print("\n--- Financial Summary ---")
        print(f"Total Income  : Rp{total_income:.2f}")
        print(f"Total Expense : Rp{abs(total_expense):.2f}")
        print(f"Balance       : Rp{balance:.2f}")
        print("\n--- Transaction History ---")
        for i, txn in enumerate(self.transactions, 1):
            print(f"{i}. {txn['description']} (Rp{txn['amount']:.2f})")

    def clear_transactions(self):
        self.transactions = []
        print("\nAll transactions have been cleared.")


def main():
    tracker = FinanceTracker()

    while True:
        print("\n--- Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Clear Transactions")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            description = input("Enter income description: ")
            try:
                amount = float(input("Enter income amount: "))
                if amount <= 0:
                    raise ValueError("Income must be greater than zero.")
                tracker.add_transaction(description, amount)
                print("Income added successfully.")
            except ValueError as e:
                print(f"Invalid input: {e}")
        elif choice == "2":
            description = input("Enter expense description: ")
            try:
                amount = float(input("Enter expense amount: "))
                if amount <= 0:
                    raise ValueError("Expense must be greater than zero.")
                tracker.add_transaction(description, -amount)
                print("Expense added successfully.")
            except ValueError as e:
                print(f"Invalid input: {e}")
        elif choice == "3":
            tracker.view_summary()
        elif choice == "4":
            tracker.clear_transactions()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
