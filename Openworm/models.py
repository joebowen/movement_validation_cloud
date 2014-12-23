from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Strain(models.Model):
    #owner = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    strain_name = models.CharField(max_length=100, null=False, default='')
    gene = models.CharField(max_length=20, null=True)
    genotype = models.BinaryField(null=True)
    allele = models.CharField(max_length=20, null=True)
    chromosome = models.CharField(max_length=20, null=True)
    simulated = models.CharField(max_length=1, null=False)

class Worm(models.Model):
    #owner = models.ForeignKey(User)
    strain = models.ForeignKey(Strain)
    timestamp = models.DateTimeField(auto_now_add=True)
    sex = models.CharField(max_length=20, null=True)
    thawed_date = models.DateTimeField(null=True)
    generations_since_thawing = models.FloatField(null=True)
    habituation = models.CharField(max_length=20, null=True)