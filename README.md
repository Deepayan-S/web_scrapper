# Web Scraper

A simple Python web scraper that extracts article titles from a given webpage using `requests` and `BeautifulSoup`.

## Features
- Fetches HTML content from a specified URL.
- Parses and extracts article titles.
- Saves extracted titles to a text file (`output.txt`).
- Prints a preview of the fetched HTML for debugging.

## Prerequisites
Ensure you have Python installed on your system. Then, install the required dependencies:

```sh
pip install requests beautifulsoup4
```

## Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/web_scrapper.git
   cd web-scraper
   ```
2. Run the script:
   ```sh
   python main.py
   ```
3. Extracted titles will be saved in `output.txt`.

## Troubleshooting
- If no articles are found, inspect the HTML structure by checking the printed output and modify the `parse_html` function accordingly.
- For JavaScript-rendered pages, consider using `selenium` instead of `requests`.

## License
This project is open-source under the MIT License.

## Contributing
Feel free to fork this repository and submit pull requests to improve functionality!

