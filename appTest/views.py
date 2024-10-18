from django.shortcuts import render
from appTest.models import ApptestProducto
from appTest.models import Sistema
from django.db import connection
import random

from appTest.models import Afipcodigo, Afiptipocomprobante

def create_products(request):
    
    productos_nombres = [
            "Tablón de pino", "Tablón de roble", "Madera contrachapada",
            "Triplay de abedul", "Madera MDF", "Tablón de cedro", "Madera laminada",
            "Viga laminada", "Chapa de nogal", "Triplay de haya"
        ]
    calidades = [1, 2, 3, 4, 5]
    productos = []

    for i in range(10):
        producto = ApptestProducto(
            nombre=productos_nombres[i],
            calidad=random.choice(calidades),
            precio=random.uniform(3000, 10000)
        )
        productos.append(producto)
    ApptestProducto.objects.bulk_create(productos)
    return render(request, 'create_products.html', {
        'productos': ApptestProducto.objects.all()[:10]
    })
#----------------------------------------------------------------------------------#

def list_products(request):
    productos = ApptestProducto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'list_products.html', {'productos': productos})

#----------------------------------------------------------------------------------#

def mostrar_datos(request):
    datos = Sistema.objects.all()
    for dato in datos:
        print(dato.archivoExe)
    return render(request, 'lista_prueba.html', {'datos': datos})
#-------

def mostrar_datosSQL(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM dbo.Sistema")
        rows = cursor.fetchall()
        print(rows)  # Verificar los datos en la consola
    return render(request, 'lista_prueba.html', {'datos': rows})

#----------
def list_afipcodigos(request):
    afipcodigos = Afipcodigo.objects.all()  # Obtiene todos los registros de Afipcodigo
    return render(request, 'list_afipcodigos.html', {'afipcodigos': afipcodigos})

#----------
def list_afiptipocomprobante(request):
    afiptipocomprobantes = Afiptipocomprobante.objects.all()  # Obtiene todos los registros de Afipcodigo
    obtenerArticulos = obtener_articulos(20, "INTO")
    for articulo in obtenerArticulos:
        print(articulo[1])

    return render(request, 'afip_tipocomprobante.html', {'afiptipocomprobantes': afiptipocomprobantes})

#----------
def obtener_articulos(pun_articulo, rubro):
    with connection.cursor() as cursor:
        # Llama al procedimiento almacenado
        cursor.execute("EXEC dbo.retArticulosFranco @PunArticulo = %s, @Rubro = %s",[pun_articulo, rubro])
        #comentario:::------------->
        
        # Obtiene todos los resultados
        resultados = cursor.fetchall()
    return resultados   
