# Generated by Django 2.2.5 on 2019-12-11 15:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SanitationHub', '0002_auto_20191211_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='codeID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='OrgID'),
        ),
    ]
