# Generated by Django 3.0.2 on 2020-04-02 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0002_auto_20200401_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuser',
            name='image',
            field=models.ImageField(default='tutor_profile/default.png', upload_to='tutor_profile'),
        ),
    ]
