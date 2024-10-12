import re
from word2number import w2n  

def extract_invoice_amount(value_content):
    value_content = value_content.lower().strip()

    if "amount:" in value_content or "total amount:" in value_content or "amount due:" in value_content:
        try:
            amount_str = value_content.split(":")[1].strip()
        except IndexError:
            return "N/A"  

        try:
            amount_in_words = w2n.word_to_num(amount_str)
            return f"{amount_in_words:.2f}"  
        except ValueError:
            pass  

        amount_match = re.search(r"[\d,.]+", amount_str)
        if amount_match:
            return amount_match.group().replace(",", "").strip()

    return "N/A"  

def run_test_cases():
    test_cases = [
        "Amount: 500",                 
        "Total Amount: $500.00",        
        "Amount Due: 500.00",           
        "Amount: Five Hundred",         
        "Amount:",                      
        "Total Amount: N/A",            
        "Amount Due: 1,234.56",         
        "Amount: four thousand five hundred",  
    ]

    for i, case in enumerate(test_cases):
        print(f"Test Case {i+1}: {case}")
        result = extract_invoice_amount(case)
        print(f"Extracted Amount: {result}\n")

run_test_cases()