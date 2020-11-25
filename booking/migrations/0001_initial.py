# Generated by Django 3.0 on 2020-10-27 08:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cni', models.CharField(max_length=100)),
                ('sexe', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('libelle', models.CharField(max_length=100)),
                ('montant', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('idpiece', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=100)),
                ('etage', models.IntegerField()),
                ('typep', models.CharField(max_length=100)),
                ('num_tel', models.CharField(max_length=100)),
                ('nbre_place', models.CharField(max_length=100)),
                ('equipement', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('nbre_lits', models.CharField(max_length=100)),
                ('montant', models.IntegerField()),
                ('libre', models.BooleanField()),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbre_personne', models.CharField(max_length=100)),
                ('debut_sejour', models.CharField(max_length=100)),
                ('fin_sejour', models.CharField(max_length=100)),
                ('date_reserve', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.Client')),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.Facture')),
                ('piece', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.Piece')),
            ],
        ),
    ]