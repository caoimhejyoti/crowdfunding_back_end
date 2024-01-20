from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Festival(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_festivals')
    tickets_available = models.BooleanField() 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Ticket(models.Model):
    ticket_name = models.CharField(max_length=200)
    cost=models.IntegerField()
    features=models.TextField()
    festival = models.ForeignKey(
        'Festival',
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    ticket_owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_tickets')

class Pledge(models.Model):
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    ticket_option = models.ForeignKey(
        'Ticket',
        on_delete=models.CASCADE,
        related_name="pledges"
    )
    festival = models.ForeignKey(
        'Festival',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supported_pledges'
    )