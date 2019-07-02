"""
# Word Count
Given a phrase, count the occurrences of each word in that phrase.
For example for the input `"olly olly in come free"`
```plain
olly: 2
in: 1
come: 1
free: 1
"""
def word_count(phrase):
    words = []
    left_index = 0
    new_phrase = phrase[:]

    for right_index, char in enumerate(phrase):
    	if not char.isalnum(): 
            if phrase[left_index:right_index] != '':
                words.append(phrase[left_index:right_index].lower()) 
            left_index = right_index + 1
        elif right_index == len(phrase)-1:
            if phrase[left_index:right_index] != '':
                words.append(phrase[left_index:right_index+1].lower())
    
    printed = {}    
    for word in words:
        if word not in printed:
            printed[word] = words.count(word)
    return printed