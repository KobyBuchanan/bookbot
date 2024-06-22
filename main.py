def book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)


def sort_on(dict):
    return dict["num"]


def character_dict(text:str):
    lowered_string = text.lower()
    freq_dict = {}
    for char in lowered_string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def dict_to_list(dict:dict) -> list[dict]:
    list_from_dict = list(dict.items())
    sort_list = []
    for i in range(len(list_from_dict)):
        if list_from_dict[i][0].isalpha() == True:
            new_data = {"name": list_from_dict[i][0], "num":list_from_dict[i][1] }
            sort_list.append(new_data)
        else:
            continue
    sort_list.sort(reverse=True,key=sort_on)
    return sort_list

def printer(data:list[dict]):
    for i in range(len(data)):
        name = data[i]['name']
        value = data[i]['num']
        print(f"The '{name}' character was found {value} times")
    return None




def main():
    #run functions
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = word_count(text)
    chars_count = character_dict(text)
    data = dict_to_list(chars_count)

    #Print to console
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    printer(data)

main()