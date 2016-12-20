import random
#setting variables that we need later on
correct_letters = []        #correctly guessed letters
spent_letters = []          #all guessed letters
word_list = []              #wordlist from text file
my_word = ""                #word to be used for the game
my_num = 0                  #variable to get my_word from word_list

with open('sowpods.txt','r') as open_file:                      #opening dictionary text file
    line = open_file.readline().strip()
    while line:
        word_list.append(line.strip())                          #cleaning dictionary
        line = open_file.readline().strip().lower()

my_num = random.randint(0,len(word_list))                      #picking a number at random from the word list
my_word = word_list[my_num]
#my_word = 'ted'
correct_word = my_word
view_word = []
body_parts = 0
noose = ['head','left_arm','right_arm','body','left_leg','right_leg']


# ____
 #|   |
 #|  _O_
 #|   |
 #|  / \
#_|_

for i in range(len(my_word)):
    view_word.append('_')

while body_parts < 6:                                   #start game loop
    #print(body_parts)
    if body_parts == 6:
        print('You lose!')
        break

    if len(my_word) == 0:                                        #win condition
        print('You win!')
        print('The word was ' + correct_word)
        break

    guess_char = raw_input("please guess a letter: ")           #getting input
    print('You guessed: ' + guess_char)


    if guess_char in spent_letters:
        print("Guess something else!")
        print("Your used letters are: " + str(spent_letters))

    elif guess_char in my_word:                                 #checking if guessed letter is in selected word
        correct_letters.append(guess_char)
        for i in range(len(correct_word)):
             if correct_word[i] == guess_char:
                 view_word[i] = guess_char

        print('You guessed correctly!')
        print('the current words are: ')
        print(view_word)

        my_word = my_word.replace(guess_char,'')                #removing correctly guessed letter from word
        spent_letters.append(guess_char)


    else:
        print(noose[body_parts])
        spent_letters.append(guess_char)
        print('Try again!')
        print("Your used letters are: " + str(spent_letters))
        body_parts = body_parts + 1

                                                                #adding guessed letter to total letter count

print('Game over!')

















#end
