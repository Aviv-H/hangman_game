import os
import time
import random
os.system("color 7")

MAX_TRIES = 7


# __________________________Function__________________________#


def check_win(secret_word, old_letters_guessed):
    """
    Chack if all the letters that in the secret word show in in the list "old letters guessed".

    :param secret_word:         The secret word that the user need to guessed
    :param old_letters_guessed: The list of all the letters that the user guessed
    :type secret_word:          str 
    :type old_letters_guessed:  list 
    :return:                    The answer if user guessed all the letter from the secret word 
    :rtype:                     bool 
    """ 
    for letter in secret_word:
       if not (letter in old_letters_guessed):
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """
    Return the secret word without letters that don't show in the list "old letters guessed". 

   :param secret_word:          The secret word that the user need to guessed
   :param old_letters_guessed:  The list of all the letters that the user guessed
   :type secret_word:           str 
   :type old_letters_guessed:   list
   :return:                     The secret word without letters that the user didn't guessed
   :rtype:                      str 
   """ 
    hidden_word = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter
        else:
            hidden_word += '_'
        hidden_word += ' '
    return hidden_word

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Chack if the letter is legal and chack that he doesn't show in the list "old letters guessed"
    and show to the user message accordingly.

    :param letter_guessed:      The letter that the user guessed
    :param old_letters_guessed: The list of all the letters that the user guessed
    :type letter_guessed:       str 
    :type old_letters_guessed:  list 
    :return:                    The answer if it possible to append to the list "old letters guessed"
    :rtype:                     bool 
    """
    if len(letter_guessed) < 2:
        if letter_guessed.isalpha():
            return True
        else:
            print(ColorText("""
                        \  /
                         \/
                         /\      
                        /  \  ""","red"))
            print("this is not letter!!")
            return False
    else:
        if letter_guessed.isalpha():
            print(ColorText("""
                        \  /
                         \/
                         /\      
                        /  \  ""","red"))
            print(ColorText("Write just one letter!","mark"))
            return False
        else:
            print(ColorText("""
                        \  /
                         \/
                         /\      
                        /  \  ""","red"))
            print(ColorText("Write just one letter in English!","mark"))
            return False
    return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Chack if the letter is legal and chack that it doesn't show in the list "old letters guessed"
    and than it is append to the list "old letters guessed".

    :param letter_guessed:      The letter that the user guessed
    :param old_letters_guessed: The list of all the letters that the user guessed
    :type letter_guessed:       str 
    :type old_letters_guessed:  list
    :return:                    The answer if it possible to append to the list "old letters guessed"
    :rtype:                     bool 
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        if str(letter_guessed.lower()) in old_letters_guessed: 
            print("You guessed this letter!")
            print(ColorText("""
                        \  /
                         \/
                         /\      
                        /  \  ""","red"))
            letter_old_sort = sorted(old_letters_guessed)
            print("-> ".join(letter_old_sort))
            return False
        else: 
            old_letters_guessed.append(letter_guessed.lower())
            return True
    return False

def choose_word(file_path, index):
    """
    The function gets location of file that contain sentence and index.
    The function retern the secret word in location of the index in the file.

    :param file_path:       String of the location of the file
    :type file_path:        str 
    :param index:           the location of the secret word in the file 
    :type index:            int 
    :return:                the secret word
    :rtype:                 str 
    """
    file_words = open(file_path, "r")
    file_words_data = file_words.read()
    list_of_words = file_words_data.split(" ")
    list_to_search = file_words_data.split(" ")
    i = 0
    num_of_words = 0
    size_list = len(list_of_words)
    while size_list:
        amount_words = list_of_words.count(list_of_words[i])
        if amount_words > 1:
            word_to_del =  list_of_words[0]
            for j in range(amount_words):
                list_of_words.remove(word_to_del)

        else:
            list_of_words.remove(list_of_words[0])
        
        num_of_words += 1
        size_list = len(list_of_words)

    word_index = (index - 1) % len(list_to_search)
  
    file_words.close()
    
    return list_to_search[word_index] 

def welcome_screen():
    """The function print to the screen the logo of
       the game, HANGMAN, in green and the number of the max tries.
       The function not gets params and return None."""

    HANGMAN_ASCII_ART="""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
    print(ColorText(HANGMAN_ASCII_ART,"green"), MAX_TRIES - 1)
    return None

def print_hangman(num_of_tries):
    """
    the function gets the num_of_tries that the player try 
    and return str that express the advance in the game.

    :param num_of_tries:        the num of tries that the player try
    :type num_of_tries:         int 
    :return:                    str of picture
    :rtype:                     srt 
    """
    HANGMAN_PHOTOS = dict()
    HANGMAN_PHOTOS[0] = ("    x-------x")
    HANGMAN_PHOTOS[1] = ("""    x-------x
    |
    |
    |
    |
    |""")
    HANGMAN_PHOTOS[2] = ("""    x-------x
    |       |
    |       0
    |
    |
    |
""")
    HANGMAN_PHOTOS[3] = ("""    x-------x
    |       |
    |       0
    |       |
    |
    |""")
    HANGMAN_PHOTOS[4] = ("""    x-------x
    |       |
    |       0
    |      /|\      
    |
    |""")
    HANGMAN_PHOTOS[5] = ("""    x-------x
    |       |
    |       0
    |      /|\      
    |      /
    |""")
    HANGMAN_PHOTOS[6] = ("""    x-------x
    |       |
    |       0
    |      /|\       
    |      / \        
    |""")
    return HANGMAN_PHOTOS[num_of_tries - 1]


# ______________________Extra function_______________________#


def ColorText(text, color):
    """
    Return the text with the color. 

   :param text:     The text that you want to color
   :param color:    The color
   :type text:      str 
   :type color:     str
   :return:         The text with the color
   :rtype:          str 
   """ 
    CEND      = '\033[0m'
    CBOLD     = '\033[1m'
    CRED    = '\033[91m'
    CMARK = '\033[100m'
    CGREEN  = '\033[32m'
    CYELLOW = '\033[33m'
    CBLUE   = '\033[34m'
    CVIOLET = '\033[35m'
    CBEIGE  = '\033[36m'
    if color == 'red':
        return CRED + CBOLD + text + CEND
    elif color == 'green':
        return CGREEN + CBOLD + text + CEND
    elif color == 'yellow':
        return CYELLOW + CBOLD + text + CEND
    elif color == 'blue':
        return CBLUE + CBOLD + text + CEND
    elif color == 'voilet':
        return CVIOLET + CBOLD + text + CEND
    elif color == 'beige':
        return CBEIGE + CBOLD + text + CEND
    elif color == 'mark':
        return CMARK + CBOLD + text + CEND
    return

def clean_screen():
    """ The function clean the screen.
        The function not gets params and return None."""
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    return None

def currect_ans():
    """
    the function return str of cheers call.
    :return:                    str of cheers call
    :rtype:                     srt 
    """
    random_num = random.randint(0,9)
    CURRECT_ANSWERS = dict()

    CURRECT_ANSWERS[0] = "Good!"
    CURRECT_ANSWERS[1] = "You are lucky!"
    CURRECT_ANSWERS[2] = "Correct!"
    CURRECT_ANSWERS[3] = "You are right!"
    CURRECT_ANSWERS[4] = "You in the right direction!"
    CURRECT_ANSWERS[5] = "Perfect!"
    CURRECT_ANSWERS[6] = "Wonderful!"
    CURRECT_ANSWERS[7] = "Excellent!"
    CURRECT_ANSWERS[8] = "WOW!"
    CURRECT_ANSWERS[9] = "Hooray!"


    return CURRECT_ANSWERS[random_num]

def worng_ans():
    """
    the function return str of failure reads.
    :return:                    str of failure reads
    :rtype:                     srt 
    """
    random_num = random.randint(0,9)
    WORNG_ANSWERS = dict()

    WORNG_ANSWERS[0] = "Try again"
    WORNG_ANSWERS[1] = "Try other letter"
    WORNG_ANSWERS[2] = "Wrong"
    WORNG_ANSWERS[3] = "Mistake"
    WORNG_ANSWERS[4] = "Incorrect"
    WORNG_ANSWERS[5] = "Not even close"
    WORNG_ANSWERS[6] = "Bad luck"
    WORNG_ANSWERS[7] = "Wasted try"
    WORNG_ANSWERS[8] = "what a shame"
    WORNG_ANSWERS[9] = "you're way of target!"


    return WORNG_ANSWERS[random_num]

def print_star(size_star):
    """
    the function gets the size_star 
    and return str that of picture of star.

    :param num_of_tries:        the num of the size of the star
    :type num_of_tries:         int 
    :return:                    str of picture of star
    :rtype:                     srt 
    """
    STAR_PHOTOS = dict()
    
    STAR_PHOTOS[0] = (""" 
                                       ss              
                                   `-:/h+/h/:-          
                                    /d/    /d/          
                                     `N`.. N`           
                                     -mo++om-""")
    STAR_PHOTOS[1] = ("""  
                                       ``                   
                                      .mm.                  
                                   `.:m//m:.`               
                                 +Nmo+-  -+omN+             
                                  .yh.    .hy.              
                                    N/ -- :N                
                                   -MhhoohhM-               
                                   .-      -.               
                                 """)
    STAR_PHOTOS[2] = ("""                                        
                                       ::                        
                                      +MM+                       
                                     oM//Mo                      
                               :yhdddh:  :hdddhy:                
                                :md:        -dm:                 
                                  /Ny      yN/                   
                                   Ny `::` yN                    
                                  -MddmssmddM-                   
                                  /s:`    `:s/                   
                                                  
                                        
""")
    STAR_PHOTOS[3] = ("""
                                       yy                             
                                     `hMMh`                           
                                    `dM//Md`                          
                             .:+oshdNN:  :NNdhso+:.                   
                             `oNMy:-`      `-:yMNo`                   
                               `sMd-        -hMs`                     
                                 .NM.      .Mm.                       
                                 `MN  .//.  NM`                       
                                 :MmymNhhNmymM:                       
                                 omy+.    .+ymo                       
                                 `            `                       
                                                            
                                                  """)
    STAR_PHOTOS[4] = (""" 
                                       ..                                  
                                      .mm.                                 
                                     -NMMN-                                
                                    :NM//MN:                               
                             `-:/osyMN:  -NMyso/:-`                        
                           .yMMMdyso/.    ./osydMMMy.                      
                             -dMd:            :dMd-                        
                               :dMh-        -hMd:                          
                                 mMo        +Mm                            
                                `MM-  -++-  -MM`                           
                                :MMohNMddMNhoMM:                           
                                oMNho:`  `:ohNMo                           
                                :-            -:            """)
    STAR_PHOTOS[5] = ("""
                                       //                                       
                                      +MM+                                      
                                     oMMMMo                                     
                                    yMM/:NMy                                    
                              `.-/+hMN:  -NMh+/-.`                              
                         `sdmNMMMMmdy-    .ydmMMMMNmds`                         
                           +NMNo`              `+NMN+                           
                            `oNMd-            -hMNo`                            
                              `sMMh          yMMs`                              
                                dMd          dMd                                
                               `MMs  `:oo:`  oMM`                               
                               :MMssdMMNNMMdssMM:                               
                               sMMMms/.  ./smMMMs                               
                               ss:`          `:ss                               
                                                                              """)
    STAR_PHOTOS[6] = ("""                                                                 
                                       //                                       
                                      +MM+                                      
                                     oMMMMo                                     
                                    yMM/:NMy                                    
                              `.-/+hMN:  -NMh+/-.`                              
                         `sdmNMMMMmdy-    .ydmMMMMNmds`                         
                           +NMNo`              `+NMN+                           
                            `oNMd-    Win!!   -hMNo`                            
                              `sMMh          yMMs`                              
                                dMd          dMd                                
                               `MMs  `:oo:`  oMM`                               
                               :MMssdMMNNMMdssMM:                               
                               sMMMms/.  ./smMMMs                               
                               ss:`          `:ss                               
                                                                                
                                                                                    """)
    return STAR_PHOTOS[size_star]


# _________________The function of the game_________________#


def hangman_game():
    """ The hangman game.
        The function not gets params and return None."""
    clean_screen()
    welcome_screen()
    old_letters_guessed = []
    file_path = input("Enter file path: ")
    if_file_open = True
    while if_file_open:
        try:
            myfile = open(file_path, "r")
            if_file_open = False
        except IOError:
            print("Could not open file!")
            file_path = input("Enter file path: ")
    index = input("Enter index: ")
    if not(index.isdigit()):
        flag = 1
        while flag:
            print("Enter just integer!")
            index = input("Enter index: ")
            if index.isdigit():
                flag = 0
    secret_word = choose_word(file_path, int(index))
    clean_screen()
    print(ColorText("Let’s start!","green"))
    num_of_tries = 1
    while num_of_tries < MAX_TRIES:
        print(print_hangman(num_of_tries))
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("You have more ", MAX_TRIES - num_of_tries," tries!")
        letter_guessed = input("Guess a letter: ")
        clean_screen()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed.lower() in secret_word:
                print(ColorText(currect_ans(),"green"))
                if check_win(secret_word, old_letters_guessed):
                    clean_screen()
                    print(show_hidden_word(secret_word, old_letters_guessed))
                    for i in range(MAX_TRIES):
                        print(ColorText(print_star(i%7), 'yellow'))
                        time.sleep(0.5)
                        clean_screen()
                    print(ColorText(print_star(6), 'yellow'))
                    break
            else:
                print(ColorText(":(", 'red'))
                print(ColorText(worng_ans(), 'red'))
                num_of_tries += 1
        
        else:
            print("look on what you are writing!")
              
    if num_of_tries == MAX_TRIES:
        clean_screen()
        print(ColorText(print_hangman(num_of_tries),"red"))
        print("""
                                     Lose
                             good luck next time
                             """)
    thank_you = ("""
                                                  
                                  Thank you 
                                   so much 
                                 for playing   """) 

    print(ColorText(thank_you, 'green'))
    return None
  


def main():
    return_to_more_game = "yes"
    while return_to_more_game.lower() == "yes":
        hangman_game()
        return_to_more_game = input("You want to play again (yes/no)? ")



if __name__ == "__main__": 
    main()


    