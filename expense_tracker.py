"""Institute Expense Tracker.

A small command-line tool for recording daily institute expenses in a CSV file.
Expenses are loaded when the program starts and new records are appended so they
remain available the next time the program runs.
"""

import csv
import math
import os

EXPENSES_FILE = "expenses.csv"
FIELDNAMES = ["date", "item", "category", "amount"]


def load_expenses() -> list[dict]:
    """Load saved expenses from the CSV file.

    If the file does not exist, catch FileNotFoundError and return an empty
    list so the program can still be used for the first time.
    """
    try:
        with open(EXPENSES_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            expenses = []
            for row in reader:
                try:
                    amount = float(row["amount"])
                except (KeyError, TypeError, ValueError):
                    print(f"  Skipping malformed row: {row}")
                    continue

                if not math.isfinite(amount):
                    print(f"  Skipping non-numeric amount: {row}")
                    continue

                expenses.append(
                    {
                        "date": (row.get("date") or "").strip(),
                        "item": (row.get("item") or "").strip(),
                        "category": (row.get("category") or "").strip(),
                        "amount": amount,
                    }
                )
            return expenses

    except FileNotFoundError:
        print(f"  {EXPENSES_FILE} not found. Starting with an empty expense list.")
        return []

    except csv.Error as exc:
        print(f"  Could not read {EXPENSES_FILE}: {exc}. Starting with an empty list.")
        return []


def save_expense(expense: dict) -> None:
    """Append one expense to the CSV file, writing a header when needed."""
    needs_header = (
        not os.path.exists(EXPENSES_FILE) or os.path.getsize(EXPENSES_FILE) == 0
    )

    with open(EXPENSES_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        if needs_header:
            writer.writeheader()
        writer.writerow(
            {
                "date": expense["date"],
                "item": expense["item"],
                "category": expense["category"],
                "amount": f"{expense['amount']:.2f}",
            }
        )


def prompt_non_empty(label: str) -> str:
    """Ask for a text value until the user enters something non-empty."""
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print("  This field cannot be empty. Please try again.")


def prompt_amount() -> float:
    """Ask for an amount until it is a valid positive number.

    A ValueError is raised by float() when the text is not numeric. The error is
    caught here so the program can explain the problem and ask again.
    """
    while True:
        raw_value = input("Amount: ").strip()
        try:
            amount = float(raw_value)
        except ValueError:
            print("  Invalid amount. Enter a number, for example 25.50.")
            continue

        if not math.isfinite(amount) or amount <= 0:
            print("  Amount must be a positive number.")
            continue

        return amount


def add_expense(expenses: list[dict]) -> None:
    """Collect one expense, save it, and keep it in the in-memory list."""
    print("\n--- Add New Expense ---")
    date = prompt_non_empty("Date (YYYY-MM-DD)")
    item = prompt_non_empty("Item name")
    category = prompt_non_empty("Category (for example, Stationery)")
    amount = prompt_amount()

    expense = {
        "date": date,
        "item": item,
        "category": category,
        "amount": amount,
    }

    try:
        save_expense(expense)
    except OSError as exc:
        print(f"  Could not save the expense: {exc}")
        return

    expenses.append(expense)
    print(f"  Saved: {item} | {category} | {amount:.2f}")


def show_expenses(expenses: list[dict]) -> None:
    """Print every expense and the set of unique categories."""
    if not expenses:
        print("\nNo expenses have been recorded yet.")
        return

    print(f"\n{'Date':<12} {'Item':<24} {'Category':<18} {'Amount':>10}")
    print("-" * 68)
    for expense in expenses:
        print(
            f"{expense['date']:<12} {expense['item']:<24} "
            f"{expense['category']:<18} {expense['amount']:>10.2f}"
        )

    categories = {expense["category"] for expense in expenses}
    print(f"\nUnique categories ({len(categories)}): {', '.join(sorted(categories))}")


def total_by_category(expenses: list[dict]) -> None:
    """Calculate and print the total amount spent in each category."""
    if not expenses:
        print("\nNo expenses have been recorded yet.")
        return

    totals: dict[str, float] = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0.0) + expense["amount"]

    print("\nTotal Expenses by Category")
    print("-" * 40)
    for category in sorted(totals):
        print(f"{category:<20} {totals[category]:>10.2f}")
    print("-" * 40)
    print(f"{'GRAND TOTAL':<20} {sum(totals.values()):>10.2f}")

    categories = {expense["category"] for expense in expenses}
    print(f"\nUnique categories ({len(categories)}): {', '.join(sorted(categories))}")


def display_menu() -> None:
    """Show the main menu."""
    print("\n===== Institute Expense Tracker =====")
    print("1. Add New Expense")
    print("2. Show All Expenses")
    print("3. Calculate Total Expenses by Category")
    print("4. Exit")


def main() -> None:
    """Run the expense tracker menu loop."""
    print("Institute Expense Tracker")
    expenses = load_expenses()
    print(f"Loaded {len(expenses)} saved expense record(s).")

    while True:
        display_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            total_by_category(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()