# Webhallen Product Search Automation

This Python script automates the process of searching for laptops on the Webhallen website using Selenium. It navigates through the website, handles cookie acceptance, performs a search query, and extracts the names of the products listed.

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3.6 or higher
- Selenium package
- ChromeDriver (compatible with your version of Google Chrome)

## Installation

1. **Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Selenium**: Install Selenium using pip:

pip install selenium

3. **ChromeDriver**: Download ChromeDriver from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads). Ensure it’s in your PATH or the same directory as your script.

## Usage

To run the script, navigate to the directory containing the script and execute:

python search_webhallen.py


The script performs the following actions:
1. Opens the Webhallen website.
2. Accepts the cookies policy.
3. Enters "laptop" into the search field and submits the query.
4. Collects and prints the names of all products listed as a result of the search query.
5. Prints the total number of products found.
6. Closes the browser.

## Output

The script outputs the names of the laptops found and the total count of products listed on the console.

## Note

This script is intended for educational purposes and personal use. Please respect Webhallen's terms of service regarding automation and web scraping.

## License

This project is licensed under the MIT License - see the LICENSE file for details.



