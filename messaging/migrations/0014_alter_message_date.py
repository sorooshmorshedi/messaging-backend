# Generated by Django 4.0.3 on 2022-03-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0013_message_seened'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
