# Generated by Django 2.1.3 on 2019-05-01 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rtlrmodel_rtlrpcolony'),
    ]

    operations = [
        migrations.CreateModel(
            name='all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acompanyname', models.CharField(max_length=15)),
                ('aname', models.CharField(max_length=30, null=True)),
                ('ascity', models.CharField(max_length=30, null=True)),
                ('aprice', models.CharField(max_length=30, null=True)),
                ('amob', models.CharField(max_length=30, null=True)),
                ('aaddress', models.CharField(max_length=30, null=True)),
                ('auid', models.CharField(max_length=30, null=True)),
                ('asstate', models.CharField(max_length=30, null=True)),
                ('asdistrict', models.CharField(max_length=30, null=True)),
                ('aspinno', models.CharField(max_length=30, null=True)),
                ('ascolony', models.CharField(max_length=30, null=True)),
                ('asshopname', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]