from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
"""from web.form import ContactFormForm"""
from .models import Flan, ContactForm, Location
from .form import ContactFormForm
from django.contrib.auth.decorators import login_required
import folium

# Create your views here.
def indice(request):
    public_flans = Flan.objects.filter(is_private=False)

    return render(request, 'index.html',{'public_flans': public_flans})

def acerca(request):
    #Recupero todas las sucursales
    locations = Location.objects.all()

    # Defino el mapa
    initialMap = folium.Map(location=[-35.439597,-71.664694], zoom_start=14)

    for location in locations:
        coordinates = (location.lat, location.lng)
        folium.Marker(coordinates, popup='Sucursal '+ location.name).add_to(initialMap)

    context = {'map':initialMap._repr_html_(), 'locations':locations}
    return render(request, 'about.html', context)

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)

    return render(request, 'welcome.html',{'private_flans': private_flans})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormForm()

    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})

