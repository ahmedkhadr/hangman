def hangman():
    word='Khalid'
    wrong_guesses=0
    stages=[' ','_____ ','|   |  ','|   0  ','|  /|\ ','|   |  ','|  / \ ','|   ']
    letters_left=list(word)
    score_board=['#']*len(word)
    win=False
    print('welcome to hangman game!')
    while wrong_guesses<len(stages)-1:
        print()
        guess=input('Guess a letter: ')
        if guess in letters_left:
            char_index=letters_left.index(guess)
            score_board[char_index]=guess
            letters_left[char_index]='$'
            print(''.join(score_board))
        else:
            wrong_guesses+=1
            print(''.join(score_board))
            print('\n'.join(stages[0:wrong_guesses+1]))
        if '#' not in score_board:
            print('Yep! You Win!')
            print('The word was: ')
            print(''.join(score_board))
            win=True
            break
    if not win:
        print('Oh!You Lose!')
        print('the word was {}'.format(word))
hangman()
            
