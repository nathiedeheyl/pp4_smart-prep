from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

MEASUREMENT_UNITS = [
    ('kg', 'Kilogram'),
    ('g', 'Gram'),
    ('l', 'Liter'),
    ('ml', 'Milliliter'),
    ('pcs', 'Pieces'),
    ('tbsp', 'Tablespoon'),
    ('tsp', 'Teaspoon'),
    ('pack', 'Pack'),
    ('bottle', 'Bottle'),
    ('can', 'Can'),
]

CATEGORIES = [
    ('bakery', 'Bread & Bakery'),
    ('baking', 'Baking'),
    ('baby', 'Baby Items'),
    ('beverages', 'Beverages'),
    ('canned', 'Canned Goods'),
    ('condiments', 'Condiments & Spices'),
    ('dairy', 'Dairy'),
    ('deli', 'Deli'),
    ('frozen', 'Frozen Foods'),
    ('fruits', 'Fruits'),
    ('health', 'Health Care'),
    ('household', 'Household & Cleaning Supplies'),
    ('meat', 'Meat'),
    ('pasta', 'Pasta, Rice & Cereal'),
    ('personal', 'Personal Care'),
    ('pet', 'Pet Care'),
    ('produce', 'Vegetables'),
    ('seafood', 'Fish & Seafood'),
    ('snacks', 'Snacks'),
]

# Create your models here.
class StapleItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(validators=[MinValueValidator(limit_value=0)])
    measurement_unit = models.CharField(
        max_length=50, 
        choices=MEASUREMENT_UNITS
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORIES
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="staple_items"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)