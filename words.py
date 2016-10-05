import sys
import re


help = 'usage: words.py "<your phrase>"'

if len(sys.argv) < 2:
    print help
else:
    sentence = sys.argv[1]
    special_characters = ";!,?.:'1234567890"
    words = []

    def arghify(word):
        
        first_letter = word[0]
        last_letter = word[len(word)-1]
        append_index = len(word)-1
        respect_ending = False
        
        if word[len(word)-1] in special_characters:
            append_index = len(word)-2
            respect_ending = True
        
        new_word = word[1:append_index] + first_letter + "argh"
        
        if respect_ending == True:
            new_word = new_word + last_letter        
        return new_word


    for word in sentence.split():
        if not word.isdigit():
            words.append(arghify(word))

    print " ".join(words)
