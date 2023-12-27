# Generated by Django 4.2.2 on 2023-12-27 15:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('parcel_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('origin', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru')], max_length=100)),
                ('destination', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru')], max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('is_shipped', models.BooleanField(default=False)),
                ('is_recieved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('id_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru')], max_length=100)),
                ('storage_number', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sending.parcel')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=100)),
                ('is_delivered', models.BooleanField(default=False)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sending.parcel')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=250, max_digits=10)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sending.parcel')),
            ],
        ),
        migrations.AddField(
            model_name='parcel',
            name='reciever',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to='sending.person'),
        ),
        migrations.AddField(
            model_name='parcel',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sending.person'),
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_collected', models.DateTimeField(auto_now_add=True)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sending.parcel')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sending.person')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sending.storage')),
            ],
        ),
    ]
