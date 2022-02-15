"""
JSON parser
"""
import json

def reader(file_path: str) -> list:
    """
    Reads json file
    """
    with open(file_path, 'r') as fle:
        return json.load(fle)

def main(file):
    """
    Main function for navigating through the content of file
    """
    data = reader(file)
    while True:

        if type(data) == dict:
            print("----------\nIt is dictionary. Keys:\n")
            for key in data.keys():
                print(key)
            next = input("----------\nWhich key is next? >>> ")
            if next not in data.keys():
                print("Input is incorrect, try again: ")
                continue
            data = data[next]

        elif type(data) == list:
            len_of_list = len(data)
            print("----------\nIt is a list. Number of elements: {}\n".format(len_of_list))
            if len_of_list == 0:
                break
            countr = 0
            for elem in data:
                print(str(countr) + " - " + str(elem)[:65] + "...  " + str(type(elem)))
                countr += 1
            next = int(input("\nIndex of element (0-{}) you want to see >>> ".format(len_of_list-1)))
            if next >= len_of_list:
                print("\nInput is incorrect, check the number! ")
                continue
            data = data[next]

        elif type(data) != list and type(data) != dict:
            print("----------\nInside:\n\n{}".format(data))
            break

    return ""

main('twitter1.json')
