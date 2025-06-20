from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Perro, UsuarioAdoptante, PostulacionAdopcion
from .logica import GestorAdopciones  

def bienvenida(request):
    return HttpResponse("🐾 Bienvenido al Sistema de Adopción de Perros 🐶")

def lista_perros(request):
    perros = Perro.objects.all()
    data = [{"nombre": p.nombre, "raza": p.raza, "edad": p.edad, "estado": p.estado} for p in perros]
    return JsonResponse(data, safe=False)

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

            PostulacionAdopcion.objects.create(
                nombre=nombre,
                email=email,
                mensaje="Solicitud enviada desde formulario",
                perro=perro,
                fecha_postulacion=timezone.now()
            )

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

def historial_adopciones(request, dni):
    usuario = get_object_or_404(UsuarioAdoptante, dni=dni)
    data = [f"{p.nombre} ({p.raza}) - {p.estado}" for p in usuario.historial_adopciones.all()]
    return JsonResponse({"usuario": usuario.nombre, "adopciones": data})

def probar_gestor(request):
    perro1 = Perro.objects.create(nombre="Goku", estado="disponible", raza="Labrador", edad=3, peso=45)
    perro2 = Perro.objects.create(nombre="Terrabusi", estado="disponible", raza="Beagle", edad=2, peso=65)
    usuario = UsuarioAdoptante.objects.create(nombre="Pichichu", dni="12345678", email="test@mail.com")
    usuario.preferencias = "Beagle"
    usuario.save()
    usuario.historial_adopciones.add(perro2)
    perro2.estado = "adoptado"
    perro2.save()
    historial = [p.nombre for p in usuario.historial_adopciones.all()]
    return HttpResponse(f"Historial real en BD: {historial}")
