from django.db import models
from django.contrib.auth.models import User


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.item


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.CharField(max_length=100)
    seat = models.CharField(max_length=20)

    def __str__(self):
        return self.movie



class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username