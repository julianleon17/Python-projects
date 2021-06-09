import random


def generate_password( amount_characters ):
  
  # En esta parte se ponen los caracteres para generar la contraseña
  letters = "abcdefghijklmnñopqrstuvwxyz" 
  uppercase_letters = letters.upper()
  symbols = "/()!¡?!$%![]=-:;_*^{}<>\|"
  numbers = "123456789"

  characters = letters + numbers + uppercase_letters + symbols

  random_characters = []
  
  # Genera cada uno de los caracteres de manera aleatoria
  for i in range( amount_characters ):
    random_character = random.choice( characters )
    random_characters.append( random_character )

  # trasforma el array de caracteres es un solo string que será la contraseña
  password = ''.join( random_characters )

  return password

'''
Una forma de transformar el array en string
  
  password = ""

  for i in random_characters:
    password += i
    
    
Otra forma de transformar el array en string
  password = ''.join( password )
'''

def main():
  
  toContinue = True
  
  while( toContinue ):
    
    # Se controla el caso de que no sea ingresado un número para la cantidad de caracteres
    while True:
      try:
        amount_characters = int( input( "\nIngresa cuantos caracteres quieres que tenga tu contraseña : " ) )
        break
      except:
        print( "¡Ingresa solo Números!" )

    new_password = generate_password( amount_characters )

    print( f'\nLa contraseña generada es :  {new_password} \n' )

    # Se pregunta si se desea continuar generando contraseñas o no
    go_ahead = input( "Deseas volver a generar otra contraseña? [y/n] : " )
    
    if( go_ahead != "y" ):
      toContinue = False
  
  print( "\n\nEspero haber sido útil ¡Nos vemos! :D" )

if( __name__ == "__main__" ):
  main()