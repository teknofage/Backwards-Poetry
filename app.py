import random

# #split the string words_str using the newline delimiter and store in a list variable called words
# words = words_str.split()
# print (words)
# #print out each item in the list variable called words
# for index in words:
#     print(index)
# #print out each item in the list variable called words in reverse

#helper function
def read_from_file(poem_file):
    with open(poem_file) as f:
        content = f.readlines()
        return content
    
#print backwards function
def lines_printed_backwards(poem_file):
    content = read_from_file(poem_file)
    for i in reversed(content):
        print (i)
    
#print lines in random order function
def lines_printed_random(poem_file):
    content = read_from_file(poem_file)
    random.shuffle(content)
    for i in content:
        print (i)
        
        
#helper function
def read_words_from_file(poem_file):
    with open(poem_file) as f:
        content = f.read()
        content = content.split()
        return content
        
def words_printed_random(poem_file):
    content = read_words_from_file(poem_file)
    random.shuffle(content)
    for i in content:
        print (i)

def main():
    poem_file = "poems/Sonnet_41.txt"
    print_option = input("How would you like your poem printed? backwards, line-random, or word-random? ")
    if print_option == "backwards":
        lines_printed_backwards(poem_file)
    elif print_option == "line-random":
        lines_printed_random(poem_file)
    elif print_option == "word-random":
        words_printed_random(poem_file)

if __name__ == '__main__':
    main()
    

# words_printed_random("poems/Sonnet_41.txt")