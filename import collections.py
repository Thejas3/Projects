import collections

word_list = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
def build_dictionary(words):
    word_count = {}
    for word in words: 
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word] = 1
    return word_count

def main():
    text = input(":> ")
    words = text.lower().split()
    word_count = build_dictionary(words)
    sorted_dict = (sorted(word_count.items(), key = lambda x: x[0]))

    print("Word Frequency Dictionary: ")
    for word, count in sorted_dict:
        print(f"{word}: {count}")
print(f"(the Word List is: {word_list}")
if __name__ == "__main__":
    main()
