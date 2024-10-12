import json
import re
import pdfplumber  
import logging

logging.basicConfig(filename='data_extraction_errors.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

cache = {}

def extract_field(content, field_name, rule):

    if field_name in cache:
        return cache[field_name]

    try:

        match = re.search(rule, content)
        if match:
            result = match.group(2) if len(match.groups()) > 1 else match.group(1)  
            cache[field_name] = result  
            return result
        else:
            raise ValueError(f"Field '{field_name}' not found in content.")
    except Exception as e:
        logging.error(f"Error extracting {field_name}: {e}")
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
    }
}

def extract_table_data(content):

    table_data = []
    rows = content.splitlines()
    current_row = {}

    for row in rows:

        if re.search(r'[\d,.]+', row):
            if current_row:  
                table_data.append(current_row)
            current_row = {"Description": "", "Quantity": "", "Price": ""}

            row_parts = row.split()
            if len(row_parts) >= 3:
                current_row["Price"] = row_parts[-1]  
                current_row["Quantity"] = row_parts[-2]  
                current_row["Description"] = " ".join(row_parts[:-2])  
            else:

                logging.error(f"Table row does not have enough parts: {row}")
                continue
        else:

            current_row["Description"] += " " + row.strip()

    if current_row:  
        table_data.append(current_row)

    return table_data

def process_pdf(pdf_path):
    try:
        extracted_data = {}
        with pdfplumber.open(pdf_path) as pdf:
            content = ""
            for page in pdf.pages:
                content += page.extract_text() + "\n"

        print("Extracted PDF Content:\n", content)

        for field, details in header_template.items():
            rule = details['rule']
            extracted_data[field] = extract_field(content, field, rule)

        extracted_data["Table Data"] = extract_table_data(content)

        return extracted_data

    except Exception as e:
        logging.error(f"Error processing PDF {pdf_path}: {e}")
        return {}

extracted_data = process_pdf('sample-invoice.pdf')
print("Extracted Data:", json.dumps(extracted_data, indent=4))