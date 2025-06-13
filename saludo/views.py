from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm

def hola(request):
    mensajes = Mensaje.objects.all().order_by('-fecha')[:5]  # últimos 5 mensajes
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hola')
    else:
        form = MensajeForm()

    contexto = {
        'nombre': 'Invitado',
        'mensaje': 'Deja tu mensaje aquí:',
        'form': form,
        'mensajes': mensajes
    }
    return render(request, 'saludo.html', contexto)

def acerca(request):
    return render(request, 'acerca.html')