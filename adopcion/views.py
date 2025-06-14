from django.http import HttpResponse
from .models import Perro, UsuarioAdoptante

def lista_perros(request):
    perros = Perro.objects.filter(estado='disponible')
    
    html = "<h1>Perros en Adopción</h1><ul>"
    for perro in perros:
        html += f"<li><strong>{perro.nombre}</strong> - {perro.raza} - {perro.edad} años</li>"
    if not perros:
        html += "<li>No hay perros disponibles en este momento.</li>"
    html += "</ul>"

    return HttpResponse(html)
def postular_adopcion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        dni = request.POST.get('dni')
        email = request.POST.get('email')
        perro_id = request.POST.get('perro_id')

        try:
            perro = Perro.objects.get(id=perro_id)
            usuario = UsuarioAdoptante.objects.create(nombre=nombre, dni=dni, email=email)
            usuario.historial_adopciones.add(perro)
            perro.estado = 'reservado'
            perro.save()

            return HttpResponse(f"<h1>Gracias, {nombre}. Has postulado para adoptar a {perro.nombre}.</h1>")
        except Exception as e:
            return HttpResponse(f"<h1>Error: {str(e)}</h1>")


    perros_disponibles = Perro.objects.filter(estado='disponible')
    html = """
        <h1>Formulario de Adopción</h1>
        <form method='POST'>
            Nombre: <input type='text' name='nombre'><br>
            DNI: <input type='text' name='dni'><br>
            Email: <input type='email' name='email'><br>
            Perro: <select name='perro_id'>
    """
    for perro in perros_disponibles:
        html += f"<option value='{perro.id}'>{perro.nombre} - {perro.raza}</option>"
    html += """
            </select><br><br>
            <input type='submit' value='Postular'>
        </form>
    """
    return HttpResponse(html)

from django.shortcuts import render, get_object_or_404
from .models import Perro

from django.http import JsonResponse
from .models import Perro

def lista_perros(request):
    perros = Perro.objects.all()
    data = [{"nombre": p.nombre, "raza": p.raza, "edad": p.edad, "estado": p.estado} for p in perros]
    return JsonResponse(data, safe=False)



def postular_adopcion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')


from django.shortcuts import get_object_or_404
from .models import UsuarioAdoptante

# Vista: Ver historial de adopciones por DNI
def historial_adopciones(request, dni):
    usuario = get_object_or_404(UsuarioAdoptante, dni=dni)
    data = [f"{p.nombre} ({p.raza}) - {p.estado}" for p in usuario.historial_adopciones.all()]
    return JsonResponse({"usuario": usuario.nombre, "adopciones": data})


def bienvenida(request):
    return HttpResponse("🐾 Bienvenido al Sistema de Adopción de Perros 🐶")
