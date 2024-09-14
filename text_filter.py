def text_filter(message):
    banned_words = ['Turkey', 'Dog', 'Fox','Cat','Chicken']
    words = message.split()
    new_message = []

    for word in words:
        if word not in banned_words:
            new_message.append(word)
    return ' '.join(new_message)
def main():
    message = input(">:")
    new_message = text_filter(message)
    print(f"Input Message: {message}")
    print(f"Output Message: {new_message}")

if __name__=="__main__":
    main()
