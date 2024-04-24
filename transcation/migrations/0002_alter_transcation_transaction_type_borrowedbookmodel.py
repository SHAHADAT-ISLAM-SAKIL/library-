# Generated by Django 4.2.6 on 2023-12-31 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
        ('transcation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcation',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'Borrow_book')], null=True),
        ),
        migrations.CreateModel(
            name='BorrowedBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.postmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]