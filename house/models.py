from django.db import models

class Estate(models.Model):
    address= models.CharField(max_length=20)
    city= models.CharField(max_length=15)
    state= models.CharField(max_length=20)
    slug = models.SlugField(max_length=100)
    description= models.CharField(max_length=200)
    bedrooms =models.IntegerField()
    bathroom =models.IntegerField()
    square_feet =models.IntegerField()
    year_built= models.IntegerField()
    price = models.IntegerField()
    features=models.CharField(max_length=200) 
    main_photo=models.ImageField(upload_to="image")
    additional_photos=models.ImageField(upload_to="images")


    def __str__(self):
        return self.city
    
 
class Booking(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    date_arrived = models.DateField(auto_now_add= True)
    time_arrived = models.TimeField(auto_now_add= True) 

    def __str__(self):
        return self.name

