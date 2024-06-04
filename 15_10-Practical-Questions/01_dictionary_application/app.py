import json 
from difflib import *

data = json.load(open("data.json"))

def load_data():
    try:
        with open("data.json", "r") as file: 
            return json.load(file)
    except FileNotFoundError:
        print("The data file was not found.")
        exit()
    except json.JSONDecodeError:
        print("Error decoding the JSON file.")
        exit()


def find_word(word,data):
    if len(data[word]) == 1:
        print(f"Meaning: {data[word][0]}")  
        exit()
    else: 
         if len(data[word]) > 0:
            for index , meaning in enumerate(data[word]):
                    print(f"\nMeaning {index+1} : {meaning}\n")
            exit()
    

def check_spelling_and_suggest_closest_word(word,data):
    matches = get_close_matches(word,data.keys(),cutoff=0.8)
    return matches if matches else False


def take_input():
    return input("Enter the word you want to search: ").strip().lower()
    

def main():
    data = load_data()
    user_word = take_input()

    if user_word in data:
        find_word(user_word,data)
    else: 
        closest_matches = check_spelling_and_suggest_closest_word(user_word,data)
        if closest_matches:
                print(f"Did you mean {closest_matches[0]} instead? Enter Y if yes, or N if no: ")
                user_response = input().strip().lower()
                
                if user_response == 'y':
                    find_word(closest_matches[0], data)
                else:
                    exit()
        else:
            print("The word does not exist. Please double-check it.")
            exit()

if __name__ == "__main__":
    main()