from django.db import models

class SymptomCheck(models.Model):
    name = models.CharField(max_length=100)
    fever = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    breath = models.BooleanField(default=False)
    chest_pain = models.BooleanField(default=False)
    score = models.IntegerField()
    risk_level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    time = models.TimeField()
    repeat_daily = models.BooleanField(default=True)
    email_reminder = models.BooleanField(default=False)
    sms_reminder = models.BooleanField(default=False)
    voice_alert = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name