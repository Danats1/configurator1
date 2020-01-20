from django.db import models

class CPU(models.Model):
	name = models.CharField('название процессора', max_length = 50)
	soket = models.CharField('сокет', max_length = 50)
	tdp = models.IntegerField('потребляемое количество ват')
	cost = models.IntegerField('цена')
	APU = models.BooleanField('встроенность видеокарты')

	def __str__(self):
		return self.name

class GPU(models.Model):
	name = models.CharField('название видеокарты', max_length = 50)
	tdp = models.IntegerField('потребляемое количество ват')
	cost = models.IntegerField('цена')

	def __str__(self):
		return self.name

class Power(models.Model):
	name = models.CharField('название блока питания', max_length = 50)
	tdp = models.IntegerField('количество ват')
	cost = models.IntegerField('цена блока питания')

	def __str__(self):
		return self.name

class RAM(models.Model):
	name = models.CharField('название оперативной памяти', max_length = 50)
	sumgb = models.IntegerField('объем оперативной памяти')
	cost = models.IntegerField('цена оперативной памяти')

	def __str__(self):
		return self.name

class Motherboard(models.Model):
	name = models.CharField('название материнской платы', max_length = 50)
	soket = models.CharField('название разъема материнской платы', max_length = 50)
	cost = models.IntegerField('цена материнской платы')
	ramslot = models.IntegerField('количество слотов под оперативную память')

	def __str__(self):
		return self.name

class PC(models.Model):
	cpu = models.ForeignKey(CPU, on_delete = models.CASCADE)
	gpu = models.ForeignKey(GPU, on_delete = models.CASCADE)
	power = models.ForeignKey(Power, on_delete = models.CASCADE)
	ram = models.ForeignKey(RAM, on_delete = models.CASCADE)
	otherboard = models.ForeignKey(Motherboard, on_delete = models.CASCADE)
	name = models.CharField('название ПК', max_length = 50)
	cost = models.IntegerField('цена компьютера')

	def __str__(self):
		return self.name
