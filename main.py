import random

words = ['tooth', 'mood', 'wife', 'heart', 'role', 'hall', 'town', 'bird', 'king', 'mud', 'tea', 'thanks', 'year',
         'food', 'child', 'dirt', 'dad', 'two', 'love', 'hair', 'skill', 'blood', 'shirt', 'cell', 'speech', 'wealth',
         'thought', 'soup', 'clothes', 'sir', 'mode', 'son', 'pie', 'throat', 'steak', 'depth', 'girl', 'loss',
         'tale', 'news', 'youth', 'law', 'thing', 'height', 'week', 'ear', 'church', 'lab', 'bath']

word = random.choice(words)
print("Guess the characters")
print("The Word contains", len(word), "Characters, and starts with Letter " + word[0])
guesses = ''
turns = 12
angle = 0
while turns > len(word):
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
            angle += 1
        else:
            print("-")
            failed += 1

    if failed == 0:
        print()
        print("You Won")
        print("The word is: ", word)
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print()
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Lost")
