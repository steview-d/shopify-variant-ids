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
        return

    # Scrape data from product page
    soup = BeautifulSoup(r.text, 'html.parser')
    result = str(soup.find('script', text=re.compile('var meta = {"product":')))
    data = result.split('var meta = ')[1].split(',"page":')[0]
    json_data = json.loads(data + '}')

    # Display product name and variants
    name = json_data['product']['variants'][0]['name'].split(' - ')[0]
    print('-' * len(name))
    print(name)
    print('-' * len(name))
    for idx, i in enumerate(json_data['product']['variants']):
        print(f"[{idx + 1}] - {i['public_title']} - {i['id']}")
    print('-' * len(name))

    # Store variant name & IDs
    num_ids = len(json_data['product']['variants'])
    variant_nums = []
    for n in range(1, num_ids + 1):
         variant_nums.append(str(n))

    # User options
    print_to_screen(['Select variant ID line number to copy to list, or'])
    print_to_screen(['Select multiple variants like so... [1,2,3] or'])
    option = input("Go [b]ack. ")

    if option == 'b':
        user_options()
    elif ',' in option:
        try:
            choices = option.split(',')
        except:
            print_to_screen({'Input not recognised...'})
            return
        else:
            # Where user ends input with a ',' remove last list item
            if choices[len(choices)-1] == '':
                choices.pop()

            # where multiple IDs selected, add them all to the list
            for c in choices:
                try:
                    id_list.append(json_data['product']['variants'][int(c) - 1]['id'])
                except:
                    print_to_screen({'Input not recognised...'})
                    return

    # If only a single variant selected, add it to the list
    elif option in variant_nums:
       id_list.append(json_data['product']['variants'][int(option) - 1]['id'])
    else:
        pass


def list_ids():
    # List all stored variant IDs
    print("Variant IDs")
    print("-----------")
    for i in id_list:
        print(i)
    print("-----------")


def export_id_list():
    if not id_list:
        print_to_screen(['There are no IDs to export...'])
        return

    export_options = ['[1] - Print to screen as .csv', '[2] - Email as .csv [Not Yet Implemented]']

    #make csv list...
    ids_csv = ''
    for i in id_list:
        ids_csv += f"{i},"

    ids_csv = ids_csv[:-1]


    print_to_screen(export_options)
    option = input('Choose an Export option: ')
    if option == '1':
        print('----------------')
        print_to_screen([ids_csv])
        print('----------------')
    elif option == '2':
        print_to_screen(['----------------', 'Feature still to be added...', '----------------'])
        pass
    return


def print_to_screen(text_list):
    # Simple function for printing list items
    for text in text_list:
        print(text)


def user_options():
    # Initial options
    options_list = [' ', '1 - Get Variant ID', '2 - List All Stored IDs', '3 - Export ID List', '4 - Clear ID List', '5 - Exit']
    print_to_screen(options_list)
    print_to_screen(' ')

    option = input("Choose an option... ")
    if option == '1':
        get_variant_id()
    elif option == '2':
        list_ids()
    elif option == '3':
        export_id_list()
    elif option == '4':
        id_list.clear()
        print_to_screen(['ID list has been cleared.'])
    elif option == '5':
        list_ids()
        print_to_screen(['Exiting now...'])
        quit()
    else:
       return


print_to_screen([ '---------', 'DAVID -v1', '---------', 'Deadly Accurate Variant Id Detector' ])
while True:
    user_options()
