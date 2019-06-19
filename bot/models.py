from django.db import models

WHITELIST_CONTRIBUTORS = (
    "njgheorghita",
    "kclowes",
    "pipermerriam",
    "carver",
    "cburgdorf",
    "lithp",
    "ralexstokes",
)

class CuteAnimalPicture(models.Model):
    img_url = models.CharField(max_length=500)
    pr_url = models.CharField(max_length=500)

class Contributor(models.Model):
    username = models.CharField(max_length=200)
    shame_count = models.IntegerField()
