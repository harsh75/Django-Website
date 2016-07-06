
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Category,CategoryList
from django.shortcuts import get_object_or_404, render
from file1.forms import UserReviewForm,ShareYourMemoryForm
#from django.core.context_processors import csrf


def home(request):
	q=Category.objects.all()
	return render(request, 'file1/home.html', {'categories':q})


'''def categorypage(request,cat_text):
    q=Category.objects.get(category_text=cat_text)
    context={'subcategories': q}
    return render(request, 'file1/categorypage.html',context)
'''	


def categorypage(request,cat_text):
    q=Category.objects.get(category_text=cat_text)
    s=CategoryList.objects.order_by('-list_ratings').filter(category=q.id)
    return render(request,'file1/categorypage.html', {'subcategories': q , 'ordering':s} )
    
def subcategorypage(request,cat_text,subcategory_id):
    if request.POST:
        if 'Create Comments' in request.POST:
            form=UserReviewForm(request.POST)
            #if form.is_valid():
            #   form.save()
            #  return HttpResponseRedirect('')
            if form.is_valid():
                q=Category.objects.get(category_text=cat_text)
                s=q.categorylist_set.get(id=subcategory_id)
                post = form.save(commit=False)
                post.reviewU = s
                post.save()
            

        #if form.is_valid():
        #   form.save()
        #  return HttpResponseRedirect('')
        elif 'Share Your Memories' in request.POST:
            form1=ShareYourMemoryForm(request.POST)
            if form1.is_valid():
                q=Category.objects.get(category_text=cat_text)
                s=q.categorylist_set.get(id=subcategory_id)
                post = form1.save(commit=False)
                post.sharedM = s
                post.save()
            



        return HttpResponseRedirect('/file1/'+cat_text+'/' + subcategory_id +'/')
    else:
        form=UserReviewForm()
        form1=ShareYourMemoryForm()
        #csrf for securety
        q=Category.objects.get(category_text=cat_text)
        s=q.categorylist_set.get(id=subcategory_id)
        return render(request,'file1/details.html', {'particular': s , 'form':form ,'form1': form1} )

