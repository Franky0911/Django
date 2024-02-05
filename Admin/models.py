from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name = models.CharField(max_length = 20)

class tbl_category(models.Model):
    category_name = models.CharField(max_length = 20)