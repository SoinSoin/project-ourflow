# Generated by Django 2.1.5 on 2019-02-27 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190227_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='name_para',
            new_name='name_type',
        ),
    ]
