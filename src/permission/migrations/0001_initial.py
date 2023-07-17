# Generated by Django 4.1 on 2023-07-17 02:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("label", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "Role",
                "verbose_name_plural": "Roles",
            },
        ),
        migrations.CreateModel(
            name="UserPermission",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("permission_name", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.user",
                    ),
                ),
            ],
            options={
                "verbose_name": "User Permission",
                "verbose_name_plural": "User Permissions",
            },
        ),
        migrations.CreateModel(
            name="RolePermission",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("permission_name", models.TextField()),
                (
                    "role",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="permission.role",
                    ),
                ),
            ],
            options={
                "verbose_name": "Role Permission",
                "verbose_name_plural": "Role Permissions",
            },
        ),
    ]
