from django.shortcuts import render

from .models import PC,CPU,GPU,RAM,Power,Motherboard

def index(request):
	pc_text = PC.objects.all()
	cpu_text = CPU.objects.all()
	gpu_text = GPU.objects.all()
	ram_text = RAM.objects.all()
	power_text = Power.objects.all()
	motherboard_text = Motherboard.objects.all()
	return render(request, 'configPC/index.html', context = {
	    'pc_text': pc_text,
		'cpu_text': cpu_text,
		'gpu_text': gpu_text,
		'ram_text': ram_text,
		'power_text': power_text,
		'motherboard_text': motherboard_text
		})

def detail(request, pc_id):
		cpu_text = CPU.objects.all()
		gpu_text = GPU.objects.all()
		ram_text = RAM.objects.all()
		power_text = Power.objects.all()
		motherboard_text = Motherboard.objects.all()
		return render(request, 'configPC/detail.html', context = {
			'cpu_text': cpu_text,
			'gpu_text': gpu_text,
			'ram_text': ram_text,
			'power_text': power_text,
			'motherboard_text': motherboard_text
			})

def leave_pc(request, pc_id):
	pass
	# pc_set.create(name = request.post['name'])
