word = input("Enter a word: ")
vowels = ("a", "e", "i", "o", "u")
vowel_counter = 0

for letters in word:
    print(letters)
    if letters in vowels:
        vowel_counter += 1

print(f"There are {vowel_counter} in {word}")