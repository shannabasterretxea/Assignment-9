#This script is an extract of a code that extracts a word (asked by a user) and its POS from a text file if the word is in the text file
  
def query_pos(pos_dict):
  user_word= input("Enter a word:")
  if user_word in pos_dict:
    print ('POS of your word:' + pos_dict[user_word])
  else:
    print ("I am sorry. This word is not in the text.")