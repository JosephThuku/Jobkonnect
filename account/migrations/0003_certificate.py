# Generated by Django 4.2.1 on 2023-05-17 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_employee_employer_user_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_of_issuance', models.DateField()),
                ('certificate_file', models.FileField(upload_to='certificates/')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.employee')),
            ],
            options={
                'verbose_name_plural': 'Certificates',
                'db_table': 'Certificate',
                'managed': True,
            },
        ),
    ]