from django.shortcuts import render

from .models import PC,CPU,GPU,RAM,Power,Motherboard

def index(request):
	cpu_text = CPU.objects.all()
	gpu_text = GPU.objects.all()
	ram_text = RAM.objects.all()
	power_text = Power.objects.all()
	motherboard_text = Motherboard.objects.all()
	return render(request, 'configPC/index.html', context = {
		'cpu_texts': cpu_text, 
		'gpu_texts': gpu_text,
		'ram_texts': ram_text,
		'power_texts': power_text,
		'motherboard_texts': motherboard_text
		})