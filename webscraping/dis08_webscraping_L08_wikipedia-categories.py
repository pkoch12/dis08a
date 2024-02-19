import requests
from bs4 import BeautifulSoup

response = requests.get('https://de.wikipedia.org/wiki/Blauwal')
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting the headline
headline = soup.find('h1', {'class': 'firstHeading'}).text.strip()

# Find the element with the link to "Ordnung (Biologie)"
ordnung_element = soup.find('a', {'title': 'Ordnung (Biologie)'})

# If the element is found, extract the class name
if ordnung_element:
    class_name = ordnung_element.find_next('td').text.strip()
else:
    class_name = 'Not found'

# Extracting binomial name
binomial_name_element = soup.find('td', {'class': 'taxo-name'})
binomial_name = binomial_name_element.text.strip() if binomial_name_element else 'Not found'

# Extracting the element with the link to "Familie (Biologie)"
familie_element = soup.find('a', {'title': 'Familie (Biologie)'})

# If the element is found, extract the family name
if familie_element:
    family_name = familie_element.find_next('td').text.strip()
else:
    family_name = 'Not found'

# Print the extracted information
animal_info = {
    'headline': headline,
    'binomial_name': binomial_name,
    'class': class_name,
    'family': family_name,
}

print(f"Information for {animal_info['headline']}:")
print(f"Binomial Name: {animal_info['binomial_name']}")
print(f"Class: {animal_info['class']}")
print(f"Family: {animal_info['family']}")
