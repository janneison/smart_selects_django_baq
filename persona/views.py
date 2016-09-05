from django.shortcuts import render
from .forms import PersonaForm, Persona

# Create your views here.

def home(request):
	form = PersonaForm(
		request.POST or None
	)
	if request.POST:
		if form.is_valid():
			form.save()
	context = {
		'form': form,
		'personas': Persona.objects.all()
	}		
	return render(request, 'home.html', context)