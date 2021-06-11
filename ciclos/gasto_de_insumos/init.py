from ventas import ventas
from insumos import inventario

# modulo
from insumos import insumos_gastados


def recorrer_ventas ():
    for i in ventas :
        for j in i:          
            #obtener los insumos gastados segun el producto  
            insumos_gastados(j['Cantidad'], j['Producto']) 
    print(inventario)           

if __name__ == '__main__':
    recorrer_ventas()