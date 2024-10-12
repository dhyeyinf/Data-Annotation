import json

# Create header extraction rules
header_template = {
    "Invoice Number": {
        "rule": "Find 'Invoice No' and extract the following numeric value"
    },
    "Invoice Date": {
        "rule": "Find 'Date' and extract the following date"
    },
    "Vendor Name": {
        "rule": "Find 'Vendor' or 'CPB Software' and extract the name"
    },
    "Customer Name": {
        "rule": "Find 'Musterkunde AG' or 'Customer' and extract the name"
    },
    "Total Amount without VAT": {
        "rule": "Find 'Total' and extract the total amount before VAT"
    },
    "VAT": {
        "rule": "Find 'VAT' and extract the VAT amount"
    },
    "Gross Amount incl. VAT": {
        "rule": "Find 'Gross Amount' or 'Total incl. VAT' and extract the total"
    }
}

# Create table data extraction rules
table_template = {
    "Table Data": {
        "columns": ["Description", "Quantity", "Price"],
        "rules": [
            {
                "Description": "Extract item description from table rows",
                "Quantity": "Extract quantity from table rows",
                "Price": "Extract price from table rows"
            }
        ]
    }
}

# Combine both templates into one
full_template = {
    "Headers": header_template,
    "Table": table_template
}

# Output the JSON template to a file or print to console
template_json = json.dumps(full_template, indent=4)

# Optionally, save to a file
with open('invoice_template.json', 'w') as json_file:
    json_file.write(template_json)

# Print the JSON template to the console
print(template_json)
