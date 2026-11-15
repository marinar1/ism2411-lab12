# ISM2411 Lab 12 - Read a Sales CSV, Write a Cleaned Report
# Marina Rodriguez Teixeira
#
# Reflection 1:
# In Excel I would have to open the file, add a Total column, filter the rows,
# and copy them to a new sheet by hand every week. With Python I write the steps
# once and can run the same script on next week's file in less than a second,
# and the result is always the same. Excel is still easier for quickly looking
# at the data, making a fast chart, or doing a one-time change without code.
#
# Reflection 2:
# A store could keep a daily sales log where a script adds one line every night
# with the date and that day's total revenue. Append mode is the right tool
# because it adds the new line at the end and keeps all the old days, while
# "w" mode would erase the whole history every time the script runs.

import csv
from datetime import datetime

SALES_PATH = "data/sales.csv"
CLEANED_PATH = "data/cleaned.csv"
LOG_PATH = "data/run_log.txt"

# ---------- Exercise 1: Get the file ----------
print("Exercise 1: Get the file")
with open(SALES_PATH, "r") as f:
    reader = csv.reader(f)
    all_rows = list(reader)
print("Columns:", all_rows[0])
print("Data rows:", len(all_rows) - 1)

# ---------- Exercise 2: Read and print raw rows ----------
print("\nExercise 2: Read and print raw rows")
with open(SALES_PATH, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ---------- Exercise 3: Skip the header ----------
print("\nExercise 3: Skip the header")
with open(SALES_PATH, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# ---------- Exercise 4: Compute totals ----------
print("\nExercise 4: Compute totals")
orders = []
total_revenue = 0
with open(SALES_PATH, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        qty = int(qty_str)
        total = price * qty
        orders.append([product, price, qty, total])
        total_revenue += total
        print(f"{product}: {qty} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:,.2f}")

# ---------- Exercise 5: Filter and write ----------
print("\nExercise 5: Filter and write")
high_value = [order for order in orders if order[3] > 100]
with open(CLEANED_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for product, price, qty, total in high_value:
        writer.writerow([product, f"{price:.2f}", qty, f"{total:.2f}"])
print(f"Wrote {len(high_value)} of {len(orders)} rows to {CLEANED_PATH}")
