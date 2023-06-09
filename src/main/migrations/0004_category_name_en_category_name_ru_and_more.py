# Generated by Django 4.2.1 on 2023-05-21 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_supplier', to='main.supplier'),
        ),
    ]
