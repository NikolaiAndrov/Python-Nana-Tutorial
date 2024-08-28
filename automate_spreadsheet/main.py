import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv_file["Sheet1"]

products_per_supplier = {}
total_products_price_per_supplier = {}

for row in range(2, product_list.max_row + 1):
    supplier_name = product_list.cell(row, 4).value

    # calculating products count per supplier
    if supplier_name not in products_per_supplier:
        products_per_supplier[supplier_name] = 0
    products_per_supplier[supplier_name] += 1

    # calculating total products price per supplier
    if supplier_name not in total_products_price_per_supplier:
        total_products_price_per_supplier[supplier_name] = 0
    inventory = product_list.cell(row, 2).value
    price = product_list.cell(row, 3).value
    total_products_price_per_supplier[supplier_name] += inventory * price

print(products_per_supplier)
print(total_products_price_per_supplier)

