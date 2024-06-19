
from django.shortcuts import render

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
   
    return render(
        request,
        'index.html',
        context={},
    )