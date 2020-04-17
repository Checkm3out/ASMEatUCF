# Generated by Django 2.2 on 2020-04-14 04:22

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import phone_field.models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0001_squashed_0021'),
        ('printrequest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, default='', max_length=30)),
                ('body', models.TextField(blank=True, default='', max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.RichTextField()),
                ('date', models.DateField(verbose_name='Post date')),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('price', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OfficerTitleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asme_title', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='printerfile',
            name='subject',
        ),
        migrations.AddField(
            model_name='printerfile',
            name='creator',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='printerfile',
            name='dimensions',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='printerfile',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='printerfile',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='printerfile',
            name='member',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='printerfile',
            name='model_name',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='printerfile',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, default='', max_length=31),
        ),
        migrations.AddField(
            model_name='printerfile',
            name='special_requests',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='printerfile',
            name='message',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.CreateModel(
            name='OfficerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('description', models.TextField(blank=True, default='', max_length=3000)),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='printrequest.OfficerTitleModel')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPageRelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_links', to='printrequest.BlogPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='printerfile',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='printrequest.Colors'),
        ),
    ]