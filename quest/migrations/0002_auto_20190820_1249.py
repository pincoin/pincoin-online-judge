# Generated by Django 2.2.4 on 2019-08-20 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together={('category', 'language')},
        ),
    ]