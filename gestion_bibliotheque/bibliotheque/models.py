from django.db import models
from django.contrib.auth.models import User

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    date_publication = models.DateField()
    ajout_par = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

