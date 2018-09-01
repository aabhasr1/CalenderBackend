from django.db import models


class Event(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=255, null=False)
    date = models.DateField(null=False, blank=False)
    fav = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    startField = models.TimeField(null=False, blank=False)
    endField = models.TimeField(null=False, blank=False)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {}".format(self.id, self.title, self.date, self.fav, self.active,
                                                         self.startField, self.endField)
