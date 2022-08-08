
def hangman_game(wort):
  falsche_versuche = 0
  phasen = [" ","_____  ","|   |   ", "|   0" ,"|  /|\ ","|  / \ ","| "]
  buchstaben = list(wort)
  score_board = ['__']*len(wort)
  win = False
  print("ZEIT FÜR HANGMAN DU OPFER?")
   
  while falsche_versuche < len(phasen) - 1:
    print('\n')
    rate = input("ERRATE DIE BUCHSTABEN BITCH!")
    if rate in buchstaben:
      charakter_index = buchstaben.index(rate)
      score_board[charakter_index] = rate 
      buchstaben[charakter_index] = "$"
    else:
      falsche_versuche += 1 
    print("".join(score_board))
    print('\n'.join(phasen[0: falsche_versuche + 1]))
    if '__' not in score_board:
      print("\n")
      print("EZ WIN ! ")
      #print(''.join(score_board))
      win = True
      break  
  if not win:
    print('\n'.join(phasen[0: falsche_versuche]))
    print('Verkackt! Das Wort war {}'.format(wort))

hangman_game("kacken")






