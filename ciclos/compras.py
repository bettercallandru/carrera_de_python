#prints
nuestros_productos = """Estos son nuestros productos: 
 1. Zapatos (10000)
 2. Jeans (20000)
 3. Zapatillas (5000)
 4. Camiseta (8000)
-----------------------------
Que producto desea comprar: """

desea_continuar = """-----------------------------
Desea continuar [S / N]: ?
-----------------------------
-----------------------------
"""

#bases de datos
articulos = {
    'Zapatos': 10000,
    'Jeans': 20000,
    'Zapatillas': 5000,
    'Camiseta': 8000
}
canasta = []  

#funciones
def esContinuar (continuar):
    if continuar == 'S':
        return True
    else: 
        print('Disfrute su compra')
        return False

def imprimir_recibo():      
  productos = []
  total = 0
  
  for item in canasta:
    productos.append(item['producto'])
    total += item['precio']
  print(f"""-----------------------------
 Productos: {productos}
 Cantidad: {len(canasta)}
 Valor Tot: {total}""")  

def añadir_a_canasta(producto):
  canasta.append(producto)
  imprimir_recibo()

def convertir_a_producto(numero_producto):
  if numero_producto == '1':        
    añadir_a_canasta({'precio' : articulos['Zapatos'], 'producto' : 'Zapatos'})
  elif numero_producto == '2':        
    añadir_a_canasta({'precio' : articulos['Jeans'], 'producto' : 'Jeans'})
  elif numero_producto == '3':        
    añadir_a_canasta({'precio' : articulos['Zapatillas'], 'producto' : 'Zapatillas'})
  elif numero_producto == '4':        
    añadir_a_canasta({'precio' : articulos['Camiseta'], 'producto' : 'Camiseta'})
  else: 
    print('Producto inexistente, Porfavor vuelva a intentarlo')

def main ():    
    do_continue = True
    while do_continue == True:
        choose = input(nuestros_productos)

        convertir_a_producto(choose)     

        continuar = input(desea_continuar)
        do_continue = esContinuar(continuar)

if __name__ == '__main__':
    main()