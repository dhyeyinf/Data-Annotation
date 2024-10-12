# Import functions from the main code files
from main_code_part3 import extract_invoice_amount
from main_code_part4 import extract_field, cache
from main_code_part5 import process_pdf, extract_table_data

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

def test_memoization():
    content = "Invoice No: 12345\nDate: 01/01/2024"
    cache.clear()  # Clear cache before testing
    result = extract_field(content, "Invoice Number", r"(Invoice\s*(No\.?|#|Number))\s*:\s*(\d+)")
    assert result == "12345", "Failed first extraction"
    result_from_cache = extract_field(content, "Invoice Number", r"(Invoice\s*(No\.?|#|Number))\s*:\s*(\d+)")
    assert result_from_cache == "12345", "Failed memoization test (cache retrieval)"
    print("Memoization test passed.")

def test_multi_page_extraction():
    multi_page_content = (
        "Page 1 Content: Invoice No: 12345\n"
        "Page 2 Content: \nTransaction Details:\nItem A 2 $200.00\nItem B 3 $300.00"
    )
    extracted_data = extract_field(multi_page_content, "Invoice Number", r"(Invoice\s*(No\.?|#|Number))\s*:\s*(\d+)")
    assert extracted_data == "12345", "Failed multi-page extraction"
    print("Multi-page extraction test passed.")

def run_all_tests():
    test_extract_invoice_amount()
    test_memoization()
    test_multi_page_extraction()

# Run all test cases
if __name__ == "__main__":
    run_all_tests()
