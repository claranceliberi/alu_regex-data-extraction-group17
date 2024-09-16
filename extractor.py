import re

# Define regular expressions for each data type
patterns = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'url': r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)',
    'phone': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    'credit_card': r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
    'time': r'\b(?:(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)|(?:[01]?\d|2[0-3]):[0-5]\d)\b',
    'html_tag': r'<[^>]+>',
    'hashtag': r'#\w+',
    'currency': r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
}

def extract_data(text):
    results = {}
    for data_type, pattern in patterns.items():
        results[data_type] = re.findall(pattern, text, re.IGNORECASE)
    return results

# Read content from sample_text.txt
try:
    with open('sample_text.txt', 'r', encoding='utf-8') as file:
        sample_text = file.read()
except FileNotFoundError:
    print("Error: 'sample_text.txt' file not found in the current directory.")
    exit(1)
except IOError:
    print("Error: Unable to read 'sample_text.txt' file.")
    exit(1)

# Extract data from the file content
extracted_data = extract_data(sample_text)

# Print the extracted data
for data_type, items in extracted_data.items():
    print(f"{data_type.capitalize()}:")
    for item in items:
        print(f"  - {item}")
