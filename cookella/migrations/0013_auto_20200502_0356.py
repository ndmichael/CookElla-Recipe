# Generated by Django 2.1.7 on 2020-05-02 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookella', '0012_auto_20200502_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtype',
            name='food_image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='food_photos'),
        ),
    ]
