from bs4 import BeautifulSoup

# Load the original and modified HTML files
with open('classcentral.html', 'r', encoding='utf-8') as f:
    original_html = f.read()

with open("updated_html.html", "r", encoding='utf-8') as f:
    modified_html = f.read()

# Replace links in modified HTML with links from original HTML
modified_soup = BeautifulSoup(modified_html, 'html.parser')
original_soup = BeautifulSoup(original_html, 'html.parser')

modified_links = modified_soup.find_all('a')
print(len(modified_links))
original_links = original_soup.find_all('a')
print(len(original_links))

for i, link in enumerate(modified_links):
    modified_link = link.get('href')
    original_link = original_links[i].get('href')

    if modified_link == original_link:
        print(f"Replacing link {modified_link} with {original_link}")
        modified_html = modified_html.replace(modified_link, original_link)

# Write the updated HTML back to the modified HTML file
with open("updated_html.html", "w", encoding='utf-8') as f:
    f.write(modified_html)