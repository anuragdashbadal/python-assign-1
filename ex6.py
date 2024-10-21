# Exercise -6 Write a Python program that:
# 1. Asks for a sentence input from the user.
# 2. Asks for a word to search in the sentence.
# 3. Outputs whether the word exists in the sentence and, if it does, at which position (index).

def search_word_in_sentence(sentence,word):
    index = sentence.find(word)
    
    if index != -1:
        print(f"The Word '{word}' exists in the sentence at index {index}.")
    else:
        print(f"The Word '{word}' does not exist in the Sentence.")
        
        
sentence = input("Enter a Sentence: ")
word = input("Enter The Word TO Search For: ")

search_word_in_sentence(sentence,word)            