# Un conversor de monedas, por ahora solo convierte de dolares a pocos países latinoamericanos

def main():
  valores = { "colombia" : 3804, "argentina" : 93, "chile" : 702, "méxico" : 20, "perú" : 3, } 
  paises = [ "colombia", "argentina", "chile", "méxico", "perú", "UUSS"] 
  
  peso = int( input(''' 
  Cual es la moneda que deseas cambiar a dolares? 
    [0]  Peso Colombiano
    [1]  Peso Argentino
    [2]  Peso Chileno
    [3]  Peso mexicano
    [4]  Sol Peruano \n
  Elegir : ''') ) 
  
  valor_dolar = valores[ paises[peso] ]  #Decidiendo el valor del dolar dependiendo del país
  
  dinero = float( input ( "Cual es la cantidad de dinero que deseas cambiar? : " ) ) 
  
  print( "\nLa cantidad de dolares que tienes es de $" + str( round( ( dinero / valor_dolar ), 2 ) ) ) 

if __name__ == "__main__":
  main()