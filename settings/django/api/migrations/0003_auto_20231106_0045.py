# Generated by Django 3.2.23 on 2023-11-06 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20231105_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='businessName',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='categoryId',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='communeId',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='description',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='recaptcha',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='sizeId',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='webUrl',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.CreateModel(
            name='ProviderUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=250)),
                ('legal_name', models.CharField(max_length=250)),
                ('region', models.CharField(max_length=250)),
                ('province', models.CharField(max_length=250)),
                ('commune', models.CharField(max_length=250)),
                ('category_id', models.CharField(max_length=250)),
                ('size_id', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('latitude', models.CharField(max_length=250)),
                ('longitude', models.CharField(max_length=250)),
                ('web_url', models.CharField(blank=True, max_length=250, null=True)),
                ('recaptcha', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
