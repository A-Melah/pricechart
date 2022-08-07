# Generated by Django 4.0.6 on 2022-08-07 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, default='default-product.png', upload_to='')),
                ('url_jumia', models.URLField(db_index=True, max_length=9999)),
                ('url_konga', models.URLField(db_index=True, max_length=9999)),
                ('price_jumia', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('price_konga', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('star_reviews', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price_compare_app.brand')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_listed', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('phone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='price_compare_app.phone')),
                ('wish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='price_compare_app.wishlist')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=100000, null=True)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='price_compare_app.phone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
