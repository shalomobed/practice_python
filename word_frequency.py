def build_dictionary(words):
    dictionary = {}
    for x in words:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1

    sorted_dictionary = {i: y for i, y in sorted(dictionary.items())}
    for x in sorted_dictionary:
        print(x, "-", sorted_dictionary[x])


text = input(":> ").lower()
words = text.split()
print()
print("Word List: ")
print(words)
print()
print("Bag of Words: ")
build_dictionary(words)



