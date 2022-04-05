# Generated by Django 4.0 on 2022-04-01 14:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(help_text='category name', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(help_text='category name', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='simpleapp.category', verbose_name='This is the help text'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='simpleapp.category', verbose_name='This is the help text'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_en',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0, 'Price should be >= 0.0')]),
        ),
        migrations.AddField(
            model_name='product',
            name='price_ru',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0, 'Price should be >= 0.0')]),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_en',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, 'Quantity should be >= 0')]),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_ru',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, 'Quantity should be >= 0')]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='category name', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.category', verbose_name='This is the help text'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Price should be >= 0.0')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Quantity should be >= 0')]),
        ),
    ]
