# Generated by Django 3.1 on 2022-02-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='description')),
                ('price', models.IntegerField()),
                ('status', models.BooleanField()),
                ('group', models.CharField(choices=[('table', 'table'), ('bed', 'bed'), ('sofa', 'sofa'), ('kids', 'kids'), ('chair', 'chair'), ('armchair', 'armchair')], max_length=20)),
                ('img', models.ImageField(default='default.png', upload_to='product_image')),
            ],
        ),
    ]
