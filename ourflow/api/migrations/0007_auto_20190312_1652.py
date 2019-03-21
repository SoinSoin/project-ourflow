# Generated by Django 2.1.5 on 2019-03-12 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190306_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagepara',
            name='page',
        ),
        migrations.RemoveField(
            model_name='pagepara',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='paraitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='paraitem',
            name='paragraph',
        ),
        migrations.RenameField(
            model_name='paragraph',
            old_name='title_section',
            new_name='title_para',
        ),
        migrations.AddField(
            model_name='page',
            name='paragraph',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Paragraph'),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Item'),
        ),
        migrations.DeleteModel(
            name='PagePara',
        ),
        migrations.DeleteModel(
            name='ParaItem',
        ),
    ]
