from django.shortcuts import render

# Create your views here.

def sum(request):
    if request.method == "POST":
        n1 = int(request.POST.get("txtn1"))
        n2 = int(request.POST.get("txtn2"))
        add = n1+n2
        return render(request,"basics/demo.html",{"result":add})
    else:
        return render(request,"basics/demo.html")
    
  