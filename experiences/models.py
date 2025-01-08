from django.db import models
from common.models import CommonModel

class Experience(CommonModel):

    # Experience Model Definition
    country = models.CharField(max_length=50, default="USA")
    city = models.CharField(max_length=80, default="New York")
    name = models.CharField(max_length=250, default="")
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey("categories.Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
    def rating(experience):
        count = experience.review_set.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in experience.review_set.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)
        
    def reviews(experience):
        reviews = experience.review_set.all().values()
        return reviews
    
    def wishlists(experience):
        wishlists = experience.wishlist_set.all().values()
        return wishlists


class Perk(CommonModel):

    # What is included on an Experience
    name = models.CharField(max_length=100,)
    details = models.CharField(max_length=250, blank=True, default="")
    explanation = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name