from django.db import models
from time import time


# Create your models here.

'''Each Category '''
class Category(models.Model):
	 category_text=models.CharField(max_length=200)
	 def __str__(self):
	 	return self.category_text

'''From each subcategory each ListOfPlaces (one to many)  '''
'''
	 1 Creating Title
	 2 Creating Body
	 3 Creating list_ratings
	 4 Many reviews for each ListOfPlaces
	 5 Many btopianreviews for each ListOfPlaces
	 6 ListImages?

class RestaurantList(models.Model):
	 change the view to display the images and list_body and reviews, along with bstopian reviews
	 category=models.ForeignKey(Category,on_delete=models.CASCADE)
	 restaurant_name=models.CharField(max_length=200, null=True)	
	 restaurant_ratings=models.IntegerField(null=True)
	 restaurant_rankings=models.IntegerField(null=True)
	 restaurant_total=models.IntegerField(null=True)
	 #overview
	 #restaurant_imageList=models.FileField(upload_to='documents/%Y/%m/%d',null=True)
	 #add reviews form
	 #photos
	 
	 def __str__(self):
	 	return self.restaurant_name

class Restaurant(models.Model):
	 change the view to display the images and list_body and reviews, along with bstopian reviews
	 category=models.ForeignKey(RestaurantList,on_delete=models.CASCADE)
	 restaurant_imageList=models.FileField(upload_to='documents/%Y/%m/%d',null=True)
	 #add reviews form
	 #photos
	 def __str__(self):
	 	return self.restaurant_name

class UserReviews(models.Model):
	 reviewU=models.ForeignKey(RestaurantList,on_delete=models.CASCADE,null=True)
	 reviews_text=models.CharField(max_length=200,null=True)
	 
	 def __str__(self):
	 	return self.reviews_text
     
class BstopianReviews(models.Model):
	 reviewB=models.ForeignKey(RestaurantList,on_delete=models.CASCADE,null=True)
	 bstopianreview_text=models.CharField(max_length=200,null=True)
	 def __str__(self):
	 	return self.bstopianreview_text
     


class ListImages(object):
	 		ocstring for ClassName
	 		

	 		def __init__(self, arg):
	 			super(ClassName, self).__init__()
	 			self.arg = arg
'''	 				 	


'''From each subcategory each ListOfPlaces (one to many)  '''
'''
	 1 Creating Title
	 2 Creating Body
	 3 Creating list_ratings
	 4 Many reviews for each ListOfPlaces
	 5 Many btopianreviews for each ListOfPlaces
	 6 ListImages?
'''
class CategoryList(models.Model):
	 '''change the view to display the images and list_body and reviews, along with bstopian reviews'''
	 category=models.ForeignKey(Category,on_delete=models.CASCADE)
	 list_name=models.CharField(max_length=200, null=True)	
	 list_ratings=models.IntegerField(null=True)
	 list_rankings=models.IntegerField(null=True)
	 list_total=models.IntegerField(null=True)
	 #overview
	 #restaurant_imageList=models.FileField(upload_to='documents/%Y/%m/%d',null=True)
	 #add reviews form
	 #photos
	 
	 def __str__(self):
	 	return self.list_name

class CategoryDetail(models.Model):
	 '''change the view to display the images and list_body and reviews, along with bstopian reviews'''
	 category=models.ForeignKey(CategoryList,on_delete=models.CASCADE)
	 detail_imageList=models.FileField(upload_to='documents/%Y/%m/%d',null=True)
	 #add reviews form
	 #photos
	 def __str__(self):
	 	return self.category_name

class UserReviews(models.Model):
	 reviewU=models.ForeignKey(CategoryList,on_delete=models.CASCADE,null=True)
	 reviews_text=models.CharField(max_length=200,null=True)
	 def __str__(self):
	 	return self.reviews_text
     
class BstopianReviews(models.Model):
	 reviewB=models.ForeignKey(CategoryList,on_delete=models.CASCADE,null=True)
	 bstopianreview_text=models.CharField(max_length=200,null=True)
	 def __str__(self):
	 	return self.bstopianreview_text
  
class  ShareYourMemory(models.Model):
		sharedM=models.ForeignKey(CategoryList,on_delete=models.CASCADE,null=True)		
		memory_title=models.CharField(max_length=200,null=True)
		memory_desription=models.CharField(max_length=200,null=True)
		memory_images=models.FileField(upload_to='documents/%Y/%m/%d',null=True)
		def __str__(self):
			return self.memory_title
