import csv
from datetime import datetime, timedelta


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary.
    """
    dictionary = {}
    
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        
        
        next(reader)
        
       
        for row in reader:
            if len(row) > 0:
                key = row[key_column_index]
                dictionary[key] = row
                
    return dictionary

def main():
 
    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    
    
    REQUEST_PRODUCT_INDEX = 0
    REQUEST_QUANTITY_INDEX = 1
    
   
    SALES_TAX_RATE = 0.06

    try:
        
        products_dict = read_dictionary("products.csv", PRODUCT_INDEX)
        
       
        print(f"All products\n {products_dict}")

        
        subtotal = 0
        total_items = 0

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            for row in reader:
                if len(row) > 0:
                   
                    product_id = row[REQUEST_PRODUCT_INDEX]
                    quantity = int(row[REQUEST_QUANTITY_INDEX])

                   
                    product_info = products_dict[product_id]

                    # Extract name and price
                    product_name = product_info[NAME_INDEX]
                    product_price = float(product_info[PRICE_INDEX])

                  
                    print(f"{product_name}: {quantity} @ {product_price}")

                    total_items += quantity

             
                    subtotal += (product_price * quantity)

        # 5. Calculations
        sales_tax = subtotal * SALES_TAX_RATE
        total_due = subtotal + sales_tax

        # 6. Print Footer Details
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_due:.2f}")
        
        print("Thank you for shopping at the Inkom Emporium.")
        
       
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

        # --- Exceeding Requirements Feature ---
        # Calculate return date (30 days from now)
        return_date = current_date_and_time + timedelta(days=30)
        print(f"Return by: {return_date:%a %b %d %Y} by 9:00 PM")

    except FileNotFoundError as perm_err:
        print("Error: missing file")
        print(perm_err)
        
    except PermissionError as perm_err:
        print("Error: cannot read file. Please close the file if it is open.")
        print(perm_err)
        
    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file")
        print(key_err)

if __name__ == "__main__":
    main()