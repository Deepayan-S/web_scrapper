import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = []
    for article in soup.find_all('h2'):
        link = article.find('a')
        if link:
            titles.append(link.get_text(strip=True))
        else:
            titles.append(article.get_text(strip=True))
    return titles

def save_to_file(data, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for item in data:
            file.write(item + "\n")

def main():
    url = input("Enter the url of the website to scrape it's code:")
    html_content = fetch_html(url)
    if html_content:
        print(html_content[:500])  # Debug: Print first 500 characters of HTML
        titles = parse_html(html_content)
        if titles:
            save_to_file(titles)
            print(f"Extracted {len(titles)} titles. Saved to output.txt.")
        else:
            print("No articles found. Check HTML structure.")
    else:
        print("Failed to retrieve data.")

if __name__ == "__main__":
    main()
