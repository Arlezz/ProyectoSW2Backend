# Generated by Django 3.2.23 on 2023-11-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='businessName',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='categoryId',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='communeId',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='latitude',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='longitude',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='recaptcha',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rut',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sizeId',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='webUrl',
            field=models.CharField(max_length=250),
        ),
    ]