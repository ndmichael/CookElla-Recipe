# Generated by Django 2.1.7 on 2020-05-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookella', '0013_auto_20200502_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtype',
            name='food_image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='food_photos'),
        ),
    ]
