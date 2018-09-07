from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
	services = Service.objects.all() #Service es el modelo
	return render(request,"services/services.html", {"services":services})
