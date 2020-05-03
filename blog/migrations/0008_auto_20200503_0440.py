# Generated by Django 3.0.5 on 2020-05-03 04:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('blog', '0007_auto_20200501_1929'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewHomePage',
            new_name='ExpertPageCreator',
        ),
    ]
