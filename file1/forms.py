from django.forms import ModelForm
from file1.models import  CategoryList,CategoryDetail,UserReviews,BstopianReviews,ShareYourMemory
'''
class SubCategoryForm(object):
	"""docstring for SubCategoryForm"""
	class Meta:
		model= SubCategory
		fields=[
			"subcategory_text"
		]




class ListBstopianForm(object):
	"""docstring for ListBstopianForm"""
	class  Meta(object):
		"""docstring for  Meta"""
		model= Article
		fields=['bstopianreview_text']



class UserReviewForm(forms.ModelForm):
	"""docstring for SubCategoryForm"""
	class Meta:
		model= UserReviews
		fields=[
			"reviews_text"
		]


class BstopianReviewForm(object):
	"""docstring for SubCategoryForm"""
	class Meta:
		model= BstopianReviews
		fields=[
			"bstopianreview_text"
		]

'''
class UserReviewForm(ModelForm):
	"""docstring for SubCategoryForm"""
	class Meta:
		model= UserReviews
		fields=[
			"reviews_text"
		]

class ShareYourMemoryForm(ModelForm):
	class Meta:
		model=ShareYourMemory
		fields=[
			"memory_title",
			"memory_desription" ,
			"memory_images",
		]
