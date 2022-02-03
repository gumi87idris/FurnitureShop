from django.db import models


class Product(models.Model):
    SOFA = 'sofa'
    ARMCHAIR = 'armchair'
    TABLE = 'table'
    CHAIR = 'chair'
    BED = 'bed'
    KIDS = 'kids'

    CHOICE_GROUP = {
        (SOFA, 'sofa'),
        (ARMCHAIR, 'armchair'),
        (TABLE, 'table'),
        (CHAIR, 'chair'),
        (BED, 'bed'),
        (KIDS, 'kids')
    }

    name = models.CharField(max_length=100)
    description = models.TextField(default='description')
    price = models.IntegerField()
    status = models.BooleanField()
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, )
    img = models.ImageField(default='static/default.png', upload_to='product_image')

    def __str__(self):
        return self.name
