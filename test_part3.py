from main_code_part3 import extract_invoice_amount 

def test_extract_invoice_amount():

    test_cases = [
        {"input": "Amount: 500", "expected": "500"},
        {"input": "Total Amount: $500.00", "expected": "500.00"},
        {"input": "Amount Due: 500.00", "expected": "500.00"},
        {"input": "Amount: Five Hundred", "expected": "500"},
        {"input": "Amount:", "expected": "N/A"},  
    ]

    for case in test_cases:
        result = extract_invoice_amount(case['input'])
        assert result == case['expected'], f"Failed for input {case['input']}"

    print("All test cases for Part 3 passed.")