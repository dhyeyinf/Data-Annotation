from main_code_part4 import extract_field,cache
def test_memoization():

    content = "Invoice No: 12345\nDate: 01/01/2024"
    cache.clear()  

    result = extract_field(content, "Invoice Number", r"(Invoice\s*(No\.?|#|Number))\s*:\s*(\d+)")
    assert result == "12345", "Failed first extraction"

    result_from_cache = extract_field(content, "Invoice Number", r"(Invoice\s*(No\.?|#|Number))\s*:\s*(\d+)")
    assert result_from_cache == "12345", "Failed memoization test (cache retrieval)"

    print("Memoization test passed.")

def test_field_variation():

    content_variations = [
        {"content": "Invoice No: 12345", "expected": "12345"},
        {"content": "Invoice #: 54321", "expected": "54321"},
        {"content": "Invoice Number: 67890", "expected": "67890"}
    ]

    for variation in content_variations:
        result = extract_field(variation['content'], "Invoice Number", r"(Invoice\s*(No\.?|#|Number))\s*:\s*(\d+)")
        assert result == variation['expected'], f"Failed for content variation {variation['content']}"

    print("Field variation test passed.")