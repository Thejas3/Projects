
letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def calculate_word_value(word):
    total_value = 0
    for letter in word:
        total_value += letter_values.get(letter, 0)
    return total_value


stop_words = {'quit', 'q'}

while True:
    word = input("Enter a word: ").lower()
    
    if word in stop_words:
        break
    else:
        word_value = calculate_word_value(word)
        print(f"The base total value of '{word}' is {word_value}")


