import json, re, requests
from bs4 import BeautifulSoup


def get_variant_id():
    url = input("Please enter product full URL (or 'x' to go back): ")

    if url == 'x':
        return

    try:
        r = requests.get(url)
    except:
        print_to_screen(['Invalid URL'])
        get_variant_id()

    soup = BeautifulSoup(r.text, 'html.parser')
    result = str(soup.find('script', text=re.compile('var meta = {"product":')))
    data = result.split('var meta = ')[1].split(',"page":')[0]
    json_data = json.loads(data + '}')

    name = json_data['product']['variants'][0]['name'].split(' - ')[0]
    print('-' * len(name))
    print(name)
    print('-' * len(name))
    for i in json_data['product']['variants']:
        print(f"{i['public_title']} - {i['id']}")


def print_to_screen(text_list):
    for text in text_list:
        print(text)

def title():
    title_data = ['DAVID -v1', '---------', 'Deadly Accurate Variant Id Detector' ]
    print_to_screen(title_data)

def user_options():
    options_list = [' ', '1 - Get Variant ID', '2 - List All Stored IDs', '3 - Exit']
    print_to_screen(options_list)
    print_to_screen(' ')

    option = input("Choose an option... ")
    if option == '1':
        get_variant_id()
    elif option == '2':
        pass
    elif option == '3':
        print_to_screen(['Exiting now...'])
        quit()
    else:
        user_options()



title()

while True:
    user_options()
