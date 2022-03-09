# Generated by Django 4.0.3 on 2022-03-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_message_file_message_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='store_image/'),
        ),
        migrations.AddField(
            model_name='group',
            name='pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='store_image/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]