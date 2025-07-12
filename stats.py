#function to read contents of the file
def get_book_text(path):
    with open(path) as file:
        file_contents = file.read();
    return file_contents;

# function to wordcount the file
# counts the number of words in a file
def get_num_words(path):
    contents = get_book_text(path);
    content_array = contents.split()
    book_len = len(content_array)
    #print(str(book_len) + " words found in the document")
    return book_len

# creates the dictionary of characters and returns the dictionary
def count_words(file_path):
    content = get_book_text(file_path);
    
    #creating dictionary
    char_count = {}

    #itterating words
    for char in content:
        #print(char);
        char_lower = char.lower()
        char_count[char_lower] = char_count.get(char_lower,0) + 1;
    return char_count;

# function that takes the dictionary of characters and their
# counts and returns a sorted list of dictionaries.

# sorted list of dictionaries in array
def dict_arr(input_dict):
    return_array = [];
    
    for key, value in input_dict.items():
       #print(key)
       #print(value)
       #creating dict
       temp_dict = {};
       temp_dict["char"] = key;
       temp_dict["num"] = value;
      # print(temp_dict);
       return_array.append(temp_dict)
   # print(return_array)
    return return_array;
# Snippet to print the final report

#extracting helper fxn
def sort_on(items):
    return items["num"]

def print_report(file_path):
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + file_path)
    print("----------- Word Count ----------")
    word_count = get_num_words(file_path)
    print("Found " + str(word_count) + " total words")
    print("--------- Character Count -------")
   #create dictionary of words
    dict_of_words = count_words(file_path);
    #create array of words in specific structure
    final_arr = dict_arr(dict_of_words);
    final_arr.sort(reverse = True, key = sort_on);
   # print(final_arr);
    
    #printing final array
    for item_dict in final_arr:
        character = item_dict['char']
        char_count = item_dict['num']
        if character.isalpha():
            print(f"{character}: {char_count}");
    print("============= END ===============")



