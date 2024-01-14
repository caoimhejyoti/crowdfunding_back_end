from django.db import models

# Create your models here.

class Festival(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.CharField(max_length=200)
    # TODO: add the below to the model. Needed to allow users to pledge an additional amount beyond 
    # tickets = models.BooleanField() 
    # TODO: add the below to the model if possible. 
    # start_date = models.DateTimeField()
    # end_date = models.DateTimeField()


class Ticket(models.Model):
    cost=models.IntegerField()
    features=models.TextField()
    festival = models.ForeignKey(
        'Festival',
        on_delete=models.CASCADE,
        related_name='tickets'
    )


