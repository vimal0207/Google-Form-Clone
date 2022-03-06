# Generated by Django 3.2.5 on 2022-03-05 10:06

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userformdata',
            name='display_field',
            field=picklefield.fields.PickledObjectField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='userformdata',
            name='filter_field',
            field=picklefield.fields.PickledObjectField(blank=True, editable=False, null=True),
        ),
    ]