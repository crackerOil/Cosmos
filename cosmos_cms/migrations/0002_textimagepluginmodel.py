# Generated by Django 3.0.9 on 2020-08-19 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("cosmos_cms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TextImagePluginModel",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="cosmos_cms_textimagepluginmodel",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("text", models.CharField(max_length=400)),
                ("ButtonLink", models.URLField()),
                ("ButtonText", models.CharField(max_length=20)),
                ("image", models.ImageField(default="cardImg/default.jpg", upload_to="cardImg")),
                ("orientation", models.BooleanField(default=0)),
            ],
            options={"abstract": False},
            bases=("cms.cmsplugin",),
        ),
    ]
