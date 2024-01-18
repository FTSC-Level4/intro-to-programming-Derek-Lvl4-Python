


# Create a glossary (dictionary) of programming words and their meanings
#I used the items(), the for loop iterates over the dictionary, 
# 
programming_glossary = {
    'variable': 'A named storage location in memory used to store data.',
    'function': 'A block of reusable code designed to perform a specific task.',
    'loop': 'A control flow statement for specifying iteration, which allows code to be repeatedly executed.',
    'list': 'An ordered collection of items, where each item can be of a different data type.',
    'dictionary': 'An unordered collection of key-value pairs for efficient data retrieval.'
}

# Print each word and its meaning
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")