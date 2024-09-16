# Data Extraction Tool

This project is a Python-based data extraction tool that uses regular expressions to identify and extract various types of data from text.

## Features

The tool can extract the following types of data:
- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Time expressions
- HTML tags
- Hashtags
- Currency amounts

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/your-username/alu_regex-data-extraction-group17.git
   cd alu_regex-data-extraction-group17
   ```

2. Ensure you have a text file named `sample_text.txt` in the same directory as the script. This file should contain the text you want to analyze.

3. Run the script:
   ```
   python extractor.py
   ```

4. The script will read the content from `sample_text.txt`, extract the specified data types, and print the results.

## How it works

The script uses predefined regular expressions to match different data patterns in the text. It reads the content of `sample_text.txt`, applies these regular expressions, and collects all matching items for each data type.

## Customization

You can modify the `patterns` dictionary in `extractor.py` to add, remove, or modify the types of data to be extracted. Each key-value pair in this dictionary represents a data type and its corresponding regular expression.

## Sample Output

The output will list each data type found in the text, along with the specific instances of that data type. For example:

```
Email:
  - user@example.com
Url:
  - https://www.example.com
Phone:
  - (123) 456-7890
Credit_card:
  - 1234-5678-9012-3456
Time:
  - 14:30
  - 2:30 PM
Html_tag:
  - <div class="example">
Hashtag:
  - #ThisIsAHashtag
Currency:
  - $1,234.56
```

## Contributing

Contributions to improve the tool are welcome. Please feel free to submit a Pull Request.
