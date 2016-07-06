from django.conf.urls import url
from . import views
from django.conf.urls.static import static



urlpatterns = [
    # ex: /file1/
    url(r'^$', views.home, name='home'),
    # ex: /file1/education/
    url(r'^(?P<cat_text>\w+)/$', views.categorypage, name='subcategories'),
    # ex: /file1/education/enginnering/
    #url(r'^(?P<cat_text>\w+)/(?P<subcategory_text>\w+)/$', views.subcategorypage, name='subcategories'),
    # ex: /file1/education/enginnering/rv college/
    #url(r'^(?P<cat_text>\w+)/(?P<subcategory_text>\w+)/(?P<details_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<cat_text>\w+)/(?P<subcategory_id>[0-9]+)/$', views.subcategorypage, name='subcategories'),
    #url(r'^(?P<cat_text>\w+)/(?P<subcategory_id>[0-9]+)/memory$', views.subcategorypage, name='subcategories'),

]