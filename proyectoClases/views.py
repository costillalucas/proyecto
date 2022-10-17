from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context , Template 

def hola(request):
    return HttpResponse("<h1>Buenas</h1>")

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La fecha actal es {fecha_actual}')

def fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad 
    return HttpResponse(f'La fecha de nacimiento para tu {edad} es {fecha}')

def mi_template(request):

    cargar_archivo = open (r'F:\usuarios\alumno\Escritorio\Python\Django\proyecto-clases\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context() 
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)
