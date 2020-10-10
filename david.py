import json, re, requests
from bs4 import BeautifulSoup

id_list = []


def get_variant_id():
    url = input("Please enter product full URL (or 'x' to go back): ")

    if url == 'x':
        user_options()

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
    for idx, i in enumerate(json_data['product']['variants']):
        print(f"[{idx + 1}] - {i['public_title']} - {i['id']}")

    num_ids = len(json_data['product']['variants'])
    variant_nums = []
    for n in range(1, num_ids + 1):
         variant_nums.append(str(n))


    option = input("Select variant ID line number to copy to list, or go [b]ack. ")

    if option == 'b':
        user_options()
    elif option in variant_nums:
       id_list.append(json_data['product']['variants'][int(option) - 1]['id'])
    else:
        pass


def list_ids():
    print("Variant IDs")
    print("-----------")
    for i in id_list:
        print(i)
    print("-----------")

def print_to_screen(text_list):
    for text in text_list:
        print(text)

def title():
    title_data = ['DAVID -v1', '---------', 'Deadly Accurate Variant Id Detector' ]
    print_to_screen(title_data)

def user_options():
    options_list = [' ', '1 - Get Variant ID', '2 - List All Stored IDs', '3 - Clear ID List', '4 - Exit']
    print_to_screen(options_list)
    print_to_screen(' ')

    option = input("Choose an option... ")
    if option == '1':
        get_variant_id()
    elif option == '2':
        list_ids()
    elif option == '3':
        id_list.clear()
        print_to_screen(['ID list has been cleared.'])
    elif option == '4':
        list_ids()
        print_to_screen(['Exiting now...'])
        quit()
    else:
        user_options()


title()
while True:
    user_options()
