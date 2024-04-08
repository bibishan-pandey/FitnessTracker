# Generated by Django 5.0.3 on 2024-04-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_rename_cid_comment_uid_rename_cid_community_uid_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notification",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterUniqueTogether(
            name="notification",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("new_like", "New like"),
                    ("new_comment", "New comment"),
                    ("new_comment_reply", "New comment reply"),
                    ("new_friend_request", "New friend request"),
                    ("friend_request_accepted", "Friend request accepted"),
                ],
                max_length=30,
            ),
        ),
    ]