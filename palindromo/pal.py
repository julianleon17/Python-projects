# La función palindromo evalua la palabra que se le pase por el parametro y devuelve valores booleanos (True, False)
def palindromo( string ):
  string = string.replace( " ", "" ).lower()

  if string == string[::-1]:
    return True
  else:
    return False


def main():
  
  print( """
  =====================================================================================
  Este programa te dirá si la palabra que ingreses es palindromo o no
  =====================================================================================\n\n""" )

  word = input( "Ingresa la palabra : " )

  # Acá se evalúa si es palindromo ya que devuelve booleanos (True, False)
  if( palindromo( word ) ):
    print( "\n> Es palindromo" )
  else: 
    print( "\n> NO es palindromo" )


if __name__ == "__main__":
  main()