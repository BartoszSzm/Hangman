#Hangman game
#User should type words that may be in random generated word from defined list
#User have as much chances till until hangman will die

#Pseudocode
#Introduction
#Create words database
#Import random, generate random word from database
#While True:
#Show how much letters is in the word and letters that player guessed (i.e PYTH--)
#Ask for letter(Inform that if player type more than one letter, only first is taking into consideration)
#If word[0] is in the game word:
    #Inform that word is correct
    #Print same hangman picture
    #Show letters that player guessed alredy
    #Show letters that player typed already    
#If word[0] is not in the game word:
    #Inform that word is not correct
    #Print next hangman picture
    #Show letters that player guessed alredy
    #Show letters that player typed already
#If player loose:
    #Print "game over"
    #Print last hangman picture
    #Print correct word
    #Ending
#If player win:
    #Print gratulations
    #Print correct word
    #Ending
#Create while loop which asking about run game again
#Ending

def main():
    #Introduction
    print("Zagrajmy w wisielca. Zgadnij jakie to słowo podając litery, które się na nie składają zanim ludzik zawiśnie.")
    print("Pamiętaj, że jeżeli wprowadzisz więcej niż jedną literę, to jedynie pierwsza z nich będzie brana pod uwagę.")
    #Create words database
    WORDS = ("TABLETKA",
            "GITARA",
            "PACZKA",
            "GRZEJNIK",
            "RĘCZNIK",
            "BALKON",
            "MARKET",
            "RYNEK",
            "SZAFA",
            "DRUT",
            "OKNO",
            "KOMPUTER",
            "KRZESŁO",
            "NIEBO",
            "CHMURA",
            "SŁOŃCE",
            "BIURKO",
            "DROGA",
            "ULICA",
            "STACJA",)
    #Import random, generate random word from database
    #Define hangman tuple
    import random
    game_word = random.choice(WORDS)
    wrong = 0
    wrong = int(wrong)
    letters_wrong =[]
    current = []
    HANGMAN = ("""
    ---------
    |	|
    |       O
    |     --*--
    |       
    |		
    |      
    |      
    |
    |______________""","""
    ---------
    |	|
    |       O
    |    /--*--
    |       
    |			
    |      
    |      
    |
    |______________ ""","""
    ---------
    |	|
    |       O
    |    /--*--/
    |       		
    |	
    |      
    |      
    |
    |______________ ""","""
    ---------
    |	|
    |       O
    |    /--*--/
    |       |	    
    |	
    |      
    |      
    |
    |______________ ""","""
    ---------
    |	|
    |       O
    |    /--*--/
    |       |
    |	|
    |      
    |      			
    |
    |______________ ""","""
    ---------
    |	|
    |       O
    |    /--*--/
    |       |
    |	|
    |      | |
    |      
    |		
    |______________ ""","""
    ---------
    |	|
    |       O
    |    /--*--/
    |       |
    |	|
    |      | |
    |      | |	    
    |
    |______________ """)

    #While True:
    #Show how much letters is in the word and letters that player guessed (i.e PYTH--)
    #Ask for letter
    #Show first hangman

    word_length = len(game_word)
    print(HANGMAN[0],"\n")
    current = ["-"]*word_length
    while wrong < 6:
        letter_ans = input("Jaką literę typujesz ?\n")
        if not letter_ans:
            print("Wpisz dowolną literę...\n")
            continue
        letter_ans = letter_ans.upper()
        if (letter_ans in letters_wrong) or (letter_ans in current):
            print("Już wpisywałeś tą literę!\n")
            continue    
    #If word[0] is in the game word:
        if letter_ans[0] in game_word:
            print("Zgadza się!",letter_ans,"znajduje się w zagadkowym słowie!")
            print(HANGMAN[wrong],"\n")
            print("Błędnie wytypowane litery:",letters_wrong,"\n")
            for i in range(len(game_word)):
                if letter_ans == game_word[i]:
                    current[i] = letter_ans
            print("Obecnie zagadkowe słowo wygląda tak:",current)
            #If player win:
            if "-" not in current:
                print("Gratulacje! :)")
                break
    #If word[0] is not in the game word:
        elif letter_ans[0] not in game_word:
            print("Nie zgadza się...\n")
            wrong += 1
            print(HANGMAN[wrong],"\n")
            letters_wrong.append(letter_ans[0])
            print("Błędnie wytypowane litery:",letters_wrong,"\n")
            print("Obecnie zagadkowe słowo wygląda tak:",current)
    #If player loose:
    if wrong == 6:
        print(HANGMAN[wrong],"\n")
        print("Przegrałeś... spróbuj jeszcze raz.")
        print("Słowo, o które chodziło to:",game_word,"\n")            
        
#Run game / Play again ?
main()
again = input("Czy chcesz zagrać jeszcze raz ? (t/n)")
while again not in "n":
    if again == "t":
        main()
    again = input("Czy chcesz zagrać jeszcze raz ? (t/n)")
         
#Ending
input("Wciśnij ENTER, żeby zakończyć...")
    
         
        
        

