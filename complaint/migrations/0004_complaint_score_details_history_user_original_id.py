# Generated by Django 4.2.16 on 2025-01-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_remove_complaint_score_details_history_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint_score_details_history_user',
            name='original_id',
            field=models.IntegerField(default=0),
        ),
    ]
