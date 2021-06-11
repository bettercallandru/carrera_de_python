# inventario de insumos
inventario = {
    'Tomate': 100,
    'Lechuga': 40,
    'Plátano': 25,
    'Cebolla': 15,
    'Pan': 100,
    'Carne': 30,
    'Pollo': 20,
    'Salchica': 15,
    'Pan perro':10,
    'Papa ripio':20
}

# menu de productos (cantidad de insumos necesarios)
productos = {
    'Hamburguesa mixta': {
        'Tomate': 1,
        'Lechuga': 0.5,
        'Cebolla':0.5,
        'Pan':2,
        'Carne':1,
        'Pollo':1
    },
    'Hamburguesa doble': {
        'Tomate': 1,
        'Lechuga': 0.5,
        'Cebolla':0.5,
        'Pan':2,
        'Carne':2
    },
    'Hamburguesa pollo': {
        'Tomate': 1,
        'Lechuga': 0.5,
        'Cebolla':0.5,
        'Pan':2,
        'Pollo':1
    },
    'Súper perro': {
        'Pan perro':1,
        'Salchica': 1,
        'Papa ripio': 1
    }
}

def actualizar_inventario (insumosUsados):    
    # recorrer la base de datos (nombreInsumo, cantidadUsada)
    for insumo, cantidad in insumosUsados.items():
        # restar a la base de datos la cantidad de insumos gastadas
        inventario[insumo] -= cantidad

def insumos_gastados (cantidad, nombreProducto):
    for i in range(cantidad):
        # actualizar el inventario restando los insumos usados
        actualizar_inventario (productos[nombreProducto])              
