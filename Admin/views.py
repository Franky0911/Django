from django.shortcuts import render

# Create your views here.
from Admin.models import *

# Create your views here.
def District(request):
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("txtdistrict"))
        return render(request,"Admin/district.html")    
    else:
        return render(request,"Admin/district.html")