import json, os
from datetime import date

FILE = "expenses.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    try:
        desc = input("  Description: ").strip()
        amount = float(input("  Amount ($): ").strip())
        category = input("  Category (food/transport/bills/other): ").strip() or "other"
        d = input(f"  Date (YYYY-MM-DD, default today): ").strip() or str(date.today())
        expenses.append({"desc": desc, "amount": amount, "category": category, "date": d})
        save(expenses)
        print(f"  ✅ Added: ${amount:.2f} for {desc}")
    except ValueError:
        print("  Invalid amount.")

def view_summary(expenses):
    if not expenses:
        print("  No expenses yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    total = sum(totals.values())
    print(f"
  {'Category':<15} {'Total':>10}")
    print("  " + "-" * 27)
    for cat, amt in sorted(totals.items()):
        print(f"  {cat:<15} ${amt:>9.2f}")
    print("  " + "-" * 27)
    print(f"  {'TOTAL':<15} ${total:>9.2f}
")

def list_expenses(expenses):
    if not expenses:
        print("  No expenses yet.")
        return
    print(f"
  {'#':<4} {'Date':<12} {'Category':<12} {'Amount':>8}  Description")
    print("  " + "-" * 60)
    for i, e in enumerate(expenses, 1):
        print(f"  {i:<4} {e['date']:<12} {e['category']:<12} ${e['amount']:>7.2f}  {e['desc']}")
    print()

def main():
    expenses = load()
    print("=== Expense Tracker ===")
    print("Commands: add | list | summary | quit
")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "quit":
            print("Goodbye!")
            break
        elif cmd == "add":
            add_expense(expenses)
        elif cmd == "list":
            list_expenses(expenses)
        elif cmd == "summary":
            view_summary(expenses)
        else:
            print("  Unknown command.")

if __name__ == "__main__":
    main()
