# PDF Data Extraction Project

## Overview

This project focuses on extracting structured data from PDF documents, specifically invoices. The main goals include:
- Extracting key fields like "Invoice Number", "Invoice Date", "Total Amount", and more.
- Handling varying formats across different invoices.
- Implementing efficient extraction techniques such as **memoization**.
- Addressing complex scenarios including **multi-page PDFs** and **multi-line table rows**.

---

## Steps Taken

### 1. Understanding the Task: Data Extraction from PDFs

At the outset, I needed to extract structured data from PDF invoices by identifying key fields, such as:
- **Invoice Number**
- **Invoice Date**
- **Total Amount**
- **Vendor Name**
- **Customer Name**

---

### 2. Template Creation for Data Extraction (Part 2)

I began by designing a JSON template to define the fields I wanted to extract. This template was used to map field names (like "Invoice Number", "Date", etc.) to extraction rules. I wrote a Python script that:

- **Defined rules** for header extraction (e.g., finding "Invoice No", "Date", etc.).
- **Created a JSON template** for extracting both headers and table data.
- I used **Python dictionaries** to represent the mappings, and each key-value pair defined a field name and the rule to extract it.

#### Code Example from Part 2:
```python
header_template = {
    "Invoice Number": {
        "rule": "Find 'Invoice No' and extract the following numeric value"
    },
    "Invoice Date": {
        "rule": "Find 'Date' and extract the following date"
    }
}
```
#### Purpose:
This step established the foundation by mapping fields in the PDF to structured data and enabled us to use those mappings to extract relevant information.

___

### 3. Debugging and Improving the Extraction Logic (Part 3)
I encountered the problem of inconsistent formats in invoice fields. For example, the "Invoice Amount" could be labeled differently (e.g., "Total Amount", "Amount Due"). I was tasked with debugging and improving the logic.

Here’s what I did:

- I **generalized the extraction rules** to handle different formats of fields using **regular expressions** (regex).
- I handled cases like **amounts in words** and scenarios where data might be missing.
- I also created test cases to ensure that the code worked for at least 5 variations of field formats.

#### Code Example from Part-3:
```python
def extract_invoice_amount(value_content):
    if "Amount:" in value_content:
        return value_content.split(":")[1].strip()  # Original logic
    # Enhanced to handle different formats and missing values
```
#### Purpose:
I ensured that the code was robust enough to extract data across different formats and handled missing or inconsistent data gracefully.

___

### 4. Template Optimization and Efficiency (Part 4)
The challenge was to handle **slightly varying formats** across different invoices without creating separate templates for each one. Additionally, I focused on **efficiency enhancements** to avoid redundant lookups and slow parsing.

**Optimizations Implemented:**
1. Generalized the Template:
   - I modified the template to be more flexible using **regular expressions** to match variations in field names (e.g., "Invoice No" vs. "Invoice #").

2. Memoization for Field Extraction:
   - I added a **memoization technique** to avoid extracting the same field multiple times by caching the results of previous lookups.

3. Streamlining Table Parsing:
   - I used regex to dynamically detect table rows and columns, making the extraction more efficient.

#### Code Example from Part 4:
```python
cache = {}

def extract_field(content, field_name, rule):
    if field_name in cache:
        return cache[field_name]
    match = re.search(rule, content)
    if match:
        result = match.group(2) if len(match.groups()) > 1 else match.group(1)
        cache[field_name] = result  # Store in cache
        return result
    return "N/A"
```
#### Purpose:
The goal was to handle field variations and make the extraction process more efficient by reducing redundant work and speeding up the parsing.

## What is Memoization?
[Memoization](https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/) is a technique used to **speed up programs** by storing the results of expensive function calls and returning the cached result when the same inputs occur again. It avoids doing the same work multiple times.

## How Memoization Helped in Our Scenario
In our PDF extraction case, I needed to **extract specific fields** (like "Invoice Number", "Invoice Date", etc.) from the document. Without memoization, the program would try to extract these fields every time it encounters them. If a field (e.g., "Invoice Number") appears more than once or if multiple sections of the PDF need the same data, the program would repeatedly run the extraction logic for that field.

Memoization helped by **caching the results** of field extractions. If the program already extracted "Invoice Number" earlier, it simply retrieves the cached result instead of performing the extraction again. This reduces redundant work, making the **program faster** and **more efficient**, especially for large PDFs or multiple documents.

___

### Example Without Memoization (Inefficient)
Let’s say you have a document where "Invoice Number" appears multiple times on different pages, and the program has to extract this number:

- **Page 1**: The program finds "Invoice Number: 12345" and extracts "12345".
- **Page 3**: The program again finds "Invoice Number: 12345" and **runs the same extraction logic** again, even though it’s already found it earlier.

Without memoization, this repeated extraction is unnecessary and slows down the program, especially for large documents.

___

### Example With Memoization (Efficient)
Using memoization, I **store the result** the first time the program extracts "Invoice Number":

- **Page 1**: The program finds "Invoice Number: 12345" and extracts "12345". It stores this result in a cache.
- **Page 3**: The program finds "Invoice Number: 12345" again but doesn’t run the extraction logic. Instead, it retrieves the value from the cache.

This way, the program only does the work once, avoiding redundant computations and speeding up the process.


## How I Used Memoization in Our Code
Here’s how memoization worked in our scenario:
 1. **Cache Setup**: I created a cache (a Python dictionary) to store results.
 2. **Check Cache**: Before running the extraction logic for any field (like "Invoice Number"), the program first checked if the value was already in the cache.
 3. **Store in Cache**: If the field was extracted for the first time, the program stored the result in the cache for future reference.
 4. **Retrieve from Cache**: If the same field needed to be extracted again, the program fetched the value from the cache instead of running the extraction logic again.

 #### Code Example:
 ```python
cache = {}

def extract_field(content, field_name, rule):
    if field_name in cache:
        return cache[field_name]  # Fetch from cache if already extracted
    
    match = re.search(rule, content)
    if match:
        result = match.group(1)
        cache[field_name] = result  # Store in cache after extraction
        return result
    return "N/A"  # Return "N/A" if the field is not found
 ```
### Benefits of Memoization in Our Scenario:
 1. **Speeds up Extraction**: By avoiding repeated extraction of the same fields, memoization helps the program run faster.
 2. **Reduces Redundant Work**: If the same field appears multiple times (e.g., on different pages), memoization prevents the program from doing the same work again.
 3. **Optimizes Performance for Large Documents**: When working with multi-page PDFs or processing multiple documents, memoization greatly reduces the number of expensive extraction operations, improving the overall efficiency.

In short, **memoization made the program faster** by ensuring it didn’t repeat the same work for extracting fields that Ire already found earlier.

___

### 5. Handling Complex Scenarios (Part 5)
I addressed more complex scenarios, including:

- **Multi-page PDFs**: Extracting data when headers are on one page and tables on another.
- **Multi-line rows**: Handling rows that span multiple lines due to long descriptions.
- **Advanced Error Handling**: Ensuring the program does not crash when encountering missing or inconsistent data.

#### Multi-Page Extraction:
I used a library like [pdfplumber](https://github.com/jsvine/pdfplumber) to handle multi-page PDFs by extracting text from each page and concatenating it for processing.

#### Multi-Line Rows:
For tables, I handled rows that spanned multiple lines by checking whether a line was part of the previous row or a new row based on its structure (e.g., presence of numeric values).

#### Advanced Error Handling:
**try-except blocks** were added to catch errors if fields or tables were missing or not formatted correctly. These errors were logged in a file (data_extraction_errors.log) for debugging.

#### Code Example from Part 5:
```python
def process_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        content = ""
        for page in pdf.pages:
            content += page.extract_text() + "\n"
        
    extracted_data = {}
    for field, details in header_template.items():
        rule = details['rule']
        extracted_data[field] = extract_field(content, field, rule)
    
    return extracted_data
```
#### Purpose:
The goal of this step was to handle **real-world complexities**, such as multi-page documents, multi-line rows, and unexpected data formats, while ensuring the program remained robust and provided meaningful error handling.

___

### 6. Handling Errors in Field Extraction
While running the script, I encountered **errors in field extraction**, specifically when fields like "Invoice Number" or "Invoice Date" could not be found in the content. The error log showed messages like:

```javascript
Error extracting Invoice Number: Field 'Invoice Number' not found in content.
```
To fix this:

- I **printed the extracted content** to check whether the actual text from the PDF matched our regex rules.
- I adjusted the **table parsing logic** to ensure it didn’t break when rows were incomplete or formatted inconsistently.

___

### What I've Learned and Achieved:

- **Understanding and extracting structured data** from PDFs is not always straightforward due to variations in formats.
- By creating a **generalized template** with regex, I can extract key fields, even when their labels differ slightly across documents.
- **Efficiency** matters when parsing large datasets or multi-page documents, and techniques like **memoization** help avoid redundant work.
- **Error handling** is crucial in real-world scenarios, where data might be missing or incorrectly formatted.

___
___
