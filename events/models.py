from django.db import models
from PIL import Image


class Venue(models.Model):
    id = models.IntegerField(primary_key=True)
    event_meetup_id = models.IntegerField(default=0)
    country = models.CharField(max_length=32, blank=False, null=False)
    city = models.CharField(max_length=32, blank=False, null=False)
    address = models.CharField(max_length=80, blank=False, null=False)
    name = models.CharField(max_length=80, blank=False, null=False)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    repinned = models.BooleanField(default=False)


class Fee(models.Model):
    amount = models.FloatField()
    currency = models.CharField(max_length=10, default='EU')
    label = models.CharField(max_length=30, default='price')
    required = models.BooleanField(default=True)


class Event(models.Model):
    """Equivalent to meet up's api Event model"""
    id = models.IntegerField(primary_key=True)
    event_venue = models.ForeignKey(to=Venue, on_delete=models.CASCADE)
    reservation_limit = models.IntegerField(default=100)
    headcount = models.IntegerField(default=0)
    visibility = models.CharField(max_length=10)
    waitlistcount = models.IntegerField(default=0)
    event_fee = models.ForeignKey(to=Fee, on_delete=models.CASCADE)
    description = models.TextField()
    event_url = models.CharField(max_length=250)
    yes_reservation_count = models.IntegerField(default=0)
    duration = models.IntegerField()
    name = models.CharField(max_length=80, blank=False, null=False)
    photo = models.ImageField(default='default.png', upload_to='event_pics')
    time = models.IntegerField()
    updated = models.IntegerField()
    status = models.CharField(max_length=50, default='upcoming')

    def save(self, *kwargs):
        """ Overrides default behaviour to crop the image """
        super.save()

        img  = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
