from django.db import models

class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

class Images(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length =80)
    description = models.TextField()
    location = models.ForeignKey(Location,db_column='location',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,db_column="category",on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name
    def save_images(self):
        return self.save()


    @classmethod
    def search_by_category(cls,search_term):
        photo = cls.objects.filter(category__category__contains=search_term)
        return photo

    @classmethod
    def filter_by_location(cls, location):
        pictures = cls.objects.filter(location=location)
        return pictures