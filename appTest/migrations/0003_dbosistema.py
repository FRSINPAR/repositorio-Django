# Generated by Django 5.0.1 on 2024-10-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTest', '0002_producto_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='DboSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punSistema', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('archivoExe', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dbo.Sistema',
                'managed': False,
            },
        ),
    ]
