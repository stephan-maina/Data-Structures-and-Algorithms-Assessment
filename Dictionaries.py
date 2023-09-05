def word_frequency(sentence):
    """
    Counts the frequency of each word in a sentence.

    Args:
        sentence (str): The sentence to count the word frequency of.

    Returns:
        dict: A dictionary with the word frequencies.
    """

    # Convert the sentence to lowercase and split it into words.
    words = sentence.lower().split()

    # Create a dictionary to store the word frequencies.
    word_frequency = {}

    # Iterate over the words and count their frequency.
    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    #


import string

def word_frequency(sentence):
    word_count = {}
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = sentence.lower().split()  # Convert to lowercase and split into words
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Sample input
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

def is_balanced(expression):
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}
    
    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0

# Sample input
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
