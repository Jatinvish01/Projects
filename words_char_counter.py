text =  input("Enter a sentence or paragraph: ")

char_count = len(text.replace(" ", ""))

word_count = len(text.split())

print(f"\nWord count: {word_count}")

print(f"Chacater count (excluding space): {char_count}")