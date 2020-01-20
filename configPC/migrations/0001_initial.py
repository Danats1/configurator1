# Generated by Django 3.0.2 on 2020-01-20 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название процессора')),
                ('tdp', models.IntegerField(verbose_name='потребляемое количество ват')),
                ('cost', models.IntegerField(verbose_name='цена')),
                ('APU', models.BooleanField(verbose_name='встроенность видеокарты')),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название видеокарты')),
                ('tdp', models.IntegerField(verbose_name='потребляемое количество ват')),
                ('cost', models.IntegerField(verbose_name='цена')),
                ('APU', models.BooleanField(verbose_name='серия видеокарты')),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название материнской платы')),
                ('soket', models.CharField(max_length=50, verbose_name='название разъема материнской платы')),
                ('cost', models.IntegerField(verbose_name='цена материнской платы')),
                ('ramslot', models.IntegerField(verbose_name='количество слотов под оперативную память')),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название блока питания')),
                ('tdp', models.IntegerField(verbose_name='количество ват')),
                ('cost', models.IntegerField(verbose_name='цена блока питания')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название оперативной памяти')),
                ('sumgb', models.IntegerField(verbose_name='объем оперативной памяти')),
                ('cost', models.IntegerField(verbose_name='цена оперативной памяти')),
            ],
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название ПК')),
                ('cost', models.IntegerField(verbose_name='цена компьютера')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configPC.CPU')),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configPC.GPU')),
                ('otherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configPC.Motherboard')),
                ('power', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configPC.Power')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configPC.RAM')),
            ],
        ),
    ]
