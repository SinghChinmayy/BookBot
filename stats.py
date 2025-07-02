#function to read contents of the file
def get_book_text(path):
    with open(path) as file:
        file_contents = file.read();
    return file_contents;

#function to wordcount the file
def get_num_words(path):
    contents = get_book_text(path);
    content_array = contents.split()
    book_len = len(content_array)
    print(str(book_len) + " words found in the document")