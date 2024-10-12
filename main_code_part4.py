import json
import re

cache = {}

def extract_field(content, field_name, rule):

    if field_name in cache:
        return cache[field_name]

    match = re.search(rule, content)
    if match:
        result = match.group(2) if len(match.groups()) > 1 else match.group(1)  
        cache[field_name] = result  
        return result

    return "N/A"  

header_template = {
    "Invoice Number": {
        "rule": r"(Invoice\s*(No\.?|#|Number))\s*:\s*(\d+)",  
        "explanation": "Matches common variations of the 'Invoice Number' field"
    },
    "Invoice Date": {
        "rule": r"(Date)\s*:\s*([\d./]+)",  
        "explanation": "Matches common variations of the 'Invoice Date' field"
    },
    "Vendor Name": {
        "rule": r"(Vendor\s*Name|Supplier)\s*:\s*(.+)",  
        "explanation": "Matches common variations of the 'Vendor' field"
    },
    "Customer Name": {
        "rule": r"(Customer\s*Name|Client)\s*:\s*(.+)",  
        "explanation": "Matches common variations of the 'Customer' field"
    },
    "Total Amount without VAT": {
        "rule": r"(Total\s*Amount)\s*(without\s*VAT|before\s*tax)?\s*:\s*([\d.,]+)",
        "explanation": "Handles total amounts, both with and without VAT mentioned"
    },
    "Gross Amount incl. VAT": {
        "rule": r"(Gross\s*Amount)\s*(incl\.?|including)\s*(VAT)?\s*:\s*([\d.,]+)",
        "explanation": "Matches variations of the 'Gross Amount' field including VAT"
    }
}

table_template = {
    "Table Data": {
        "columns": ["Description", "Quantity", "Price"],
        "rules": [
            {
                "Description": "Extract descriptions from the table rows",
                "Quantity": "Extract quantities from the table rows",
                "Price": "Extract prices from the table rows"
            }
        ],
        "explanation": "Matches common table structures where column positions might vary"
    }
}

content = """
Invoice No: 12345
Date: 01/03/2024
Vendor Name: CPB Software
Customer Name: Musterkunde AG
Total Amount: 381.12
Gross Amount incl. VAT: 453.53
"""

def extract_invoice_data(content):
    invoice_data = {}
    for field, details in header_template.items():
        rule = details['rule']
        invoice_data[field] = extract_field(content, field, rule)  

    return invoice_data

full_template = {
    "Headers": header_template,
    "Table": table_template
}

template_json = json.dumps(full_template, indent=4)

with open('generalized_invoice_template_with_memoization.json', 'w') as json_file:
    json_file.write(template_json)

print(template_json)

extracted_data = extract_invoice_data(content)
print("Extracted Data:", extracted_data)