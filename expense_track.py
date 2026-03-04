import csv
from datetime import datetime

# Define Index Constants
DATE_INDEX = 0
CATEGORY_INDEX = 1
DESC_INDEX = 2
AMOUNT_INDEX = 3

def main():
    filename = "expenses.csv"
    
    print("Welcome to the Personal Expense Tracker")
    
    try:
        while True:
            print("\nMenu:")
            print("1. Add a new expense")
            print("2. View total by category")
            print("3. View all expenses")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                cat = input("Enter category: ").capitalize()
                desc = input("Enter description: ")
                amt = float(input("Enter amount: "))
                
                # 1. Use get_current_date
                date = get_current_date()
                
                # 2. Use make_expense_record
                record = make_expense_record(date, cat, desc, amt)
                
                # Save to file (Helper logic)
                with open(filename, "at", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(record)
                print("Expense saved!")

            elif choice == "2":
                cat = input("Enter category to sum: ").capitalize()
                
                # 3. Use read_expenses
                all_data = read_expenses(filename)
                
                # 4. Use filter_by_category
                filtered_data = filter_by_category(all_data, cat)
                
                # 5. Use calculate_total
                total = calculate_total(filtered_data)
                
                print(f"Total spent on {cat}: ${total:.2f}")

            elif choice == "3":
                all_data = read_expenses(filename)
                print(f"\n{'Date':<12} {'Category':<15} {'Description':<20} {'Amount':>10}")
                print("-" * 60)
                for row in all_data:
                    print(f"{row[DATE_INDEX]:<12} {row[CATEGORY_INDEX]:<15} {row[DESC_INDEX]:<20} {float(row[AMOUNT_INDEX]):>9.2f}")

            elif choice == "4":
                print("Goodbye!")
                break
                
    except FileNotFoundError:
        print("Error: The file could not be found.")
    except PermissionError:
        print("Error: You do not have permission to access the file.")
    except ValueError:
        print("Error: Please enter a valid number for the amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_current_date():
    """Returns the current date as a string YYYY-MM-DD."""
    return datetime.now().strftime("%Y-%m-%d")

def make_expense_record(date, category, description, amount):
    """Creates a list representing an expense record."""
    return [date, category, description, float(amount)]

def read_expenses(filename):
    """Reads the CSV file and returns a list of lists."""
    data_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader) # Skip header
        for row in reader:
            if len(row) > 0:
                data_list.append(row)
    return data_list

def filter_by_category(expenses_list, category):
    """Returns a new list containing only expenses of the given category."""
    filtered_list = []
    for row in expenses_list:
        if row[CATEGORY_INDEX].lower() == category.lower():
            filtered_list.append(row)
    return filtered_list

def calculate_total(expenses_list):
    """Calculates the total amount from a list of expenses."""
    total = 0.0
    for row in expenses_list:
        total += float(row[AMOUNT_INDEX])
    return total

if __name__ == "__main__":
    main()