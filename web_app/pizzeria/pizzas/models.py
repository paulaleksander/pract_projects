from django.db import models

class Pizza(models.Model):
    """A name of pizza."""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Return a string representation of the name."""
        return self.name

class Topping(models.Model):
    """Something specific about a topic."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    top_name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a string representation of the topping."""
        return self.top_name
