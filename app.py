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
    
    
# def lines_printed_random():
        
        
        
# def words_printed_random():

lines_printed_backwards("poems/Sonnet_41.txt")