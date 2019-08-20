# Generated by Django 2.2.4 on 2019-08-20 09:05

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('language', models.CharField(default='th', help_text='th|en|ko|cn|ja', max_length=2)),
                ('description', models.TextField(verbose_name='Category description')),
            ],
            options={
                'verbose_name': 'i18n Category',
                'verbose_name_plural': 'i18n Categories',
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='language',
        ),
    ]
