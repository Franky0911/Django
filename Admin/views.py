from django.shortcuts import render

# Create your views here.
from Admin.models import *


def District(request):
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("txtdistrict"))
        return render(request,"Admin/district.html")    
    else:
        return render(request,"Admin/district.html")

def Category(request):
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get("txtcategory"))
        return render(request,"Admin/category.html")    
    else:
        return render(request,"Admin/category.html")