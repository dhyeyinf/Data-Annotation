from main_code_part5 import process_pdf,extract_table_data,extract_field
def test_multi_page_extraction():

    multi_page_content = (
        "Page 1 Content: Invoice No: 12345\n"  
        "Page 2 Content: \nTransaction Details:\nItem A 2 $200.00\nItem B 3 $300.00"  
    )

    extracted_data = extract_field(multi_page_content, "Invoice Number", r"(Invoice\s*(No\.?|#|Number))\s*:\s*(\d+)")
    assert extracted_data == "12345", "Failed multi-page extraction"

    print("Multi-page extraction test passed.")

def test_multi_line_table():

    multi_line_table_content = (
        "Item A 2 $200.00\n"  
        "Item with a very long description\n"  
        "that continues on the next line 3 $300.00"
    )

    extracted_table = extract_table_data(multi_line_table_content)

    assert extracted_table[0]['Description'] == "Item A", "Failed multi-line table test (first item)"
    assert extracted_table[1]['Description'] == "Item with a very long description that continues on the next line", \
        "Failed multi-line table test (multi-line description)"

    print("Multi-line table test passed.")