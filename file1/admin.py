
from django.contrib import admin

from .models import Category,CategoryDetail,CategoryList,UserReviews,BstopianReviews

admin.site.register(Category)
admin.site.register(CategoryDetail)
admin.site.register(CategoryList)
admin.site.register(UserReviews)
admin.site.register(BstopianReviews)