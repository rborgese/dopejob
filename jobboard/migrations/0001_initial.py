# Generated by Django 2.0.2 on 2018-08-18 21:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20180818_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Enterprise')),
            ],
        ),
    ]
