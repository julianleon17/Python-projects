#                             Números pares e impares

def main():
  cantidad_pares = 0
  cantidad_impares = 0
  
  continuar = input( "Deseas Ingresar Números?[y/n] : " )
    
  while( continuar == "y" ):
    
    num = int( input( "\nEscribe el número que quieras : " ) ) 
    
    if( num % 2 == 0 ):
      cantidad_pares += 1
    else:
      cantidad_impares += 1
    
    continuar = input( "\n Deseas Ingresar Números?[y/n] : " )
  
  
  print( "\n\nLa cantidad de números pares registrados fueron = ", cantidad_pares )
  print( "La cantidad de números impares registrados fueron = ", cantidad_impares )



if( __name__ == "__main__" ):
  main()