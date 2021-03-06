# Generated by Django 3.0.5 on 2020-04-19 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200419_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'OrderedMenu',
                'verbose_name_plural': 'OrderedMenues',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='is_new',
            field=models.NullBooleanField(verbose_name='Newly Added'),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Orders')),
                ('menu', models.ManyToManyField(to='core.OrderedMenu', verbose_name='Ordered Menu')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Table', verbose_name='Table')),
            ],
            options={
                'verbose_name': 'Orders',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='orderedmenu',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Menu', verbose_name='Menu'),
        ),
    ]
