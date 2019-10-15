from django.test import TestCase
from .models import Images,Category, Location
import datetime as dt

# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location= Location(location = 'Kigali',) 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category= Category(category = 'food',) 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class ImagesTestClass(TestCase):

    def setUp(self):
        
       # Creating image and saving it
        self.new_picture= Images(image = 'images.jpg', name = 'picture', description ='testing for description', location ='kigali', category ='food')
        self.new_picture.save()


       # Creating location and saving it
        self.new_picture.location.add(location)
        self.new_location.save_location()


       # Creating category and saving it
        self.new_picture.category.add(self.new_category)
        self.new_category.save_category()

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Images.objects.all().delete()



