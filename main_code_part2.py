header_template = {
    "Headers": {
        "Invoice Number": {
            "rule": "(Invoice\\s*(No\\.?|#|Number))\\s*:\\s*(\\d+)",
            "explanation": "Matches common variations of the 'Invoice Number' field"
        },
        "Invoice Date": {
            "rule": "(Date)\\s*:\\s*([\\d./]+)",
            "explanation": "Matches common variations of the 'Invoice Date' field"
        },
        "Vendor Name": {
            "rule": "(Vendor\\s*Name|Supplier)\\s*:\\s*(.+)",
            "explanation": "Matches common variations of the 'Vendor' field"
        },
        "Customer Name": {
            "rule": "(Customer\\s*Name|Client)\\s*:\\s*(.+)",
            "explanation": "Matches common variations of the 'Customer' field"
        },
        "Total Amount without VAT": {
            "rule": "(Total\\s*Amount)\\s*(without\\s*VAT|before\\s*tax)?\\s*:\\s*([\\d.,]+)",
            "explanation": "Handles total amounts, both with and without VAT mentioned"
        },
        "Gross Amount incl. VAT": {
            "rule": "(Gross\\s*Amount)\\s*(incl\\.?|including)\\s*(VAT)?\\s*:\\s*([\\d.,]+)",
            "explanation": "Matches variations of the 'Gross Amount' field including VAT"
        }
    },
    "Table": {
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
}

