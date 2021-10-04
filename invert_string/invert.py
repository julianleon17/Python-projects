# Program in charge of converting from lowercase to uppercase and vice versa each letter of a string

def wayOne():
  while True:
    word = input( "Ingresa la palabra para invertir minusculas a mayusculas y viceversa: " )

    if ( (word.upper() == 'SP') or (word.upper() == 'STOP-PROGRAM') ):
      break
    else:
      new_word = word.swapcase()
      print( new_word )

# ====================================== Reversing the entire input word (Each letter changes to its opposite)

def wayTwo():
  temporal_word = ''
  letter = ''

  while True:
    word = input( "Ingresa la palabra para invertir minusculas a mayusculas y viceversa: " )
    size = len( word )            

    if ( (word.upper() == 'SP') or (word.upper() == 'STOP-PROGRAM') ):
      break
    else:
      temporal_word = ''

      for i in range( size ):
        current = word[i]
        letter = current.swapcase()
        temporal_word += letter

      new_word = temporal_word
      print( new_word  )

# ====================================== Using the "for" loop to trasnform each letter of the input word

def main():
  print( "\n\t\tEscribe 'sp' o 'stop-program' para dejar de digitar\n\n" )
  wayTwo()



# ============================
if ( __name__ == "__main__" ):
    main()
