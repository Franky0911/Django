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
    

def Calculate(request):
    if request.method == "POST":
        n1 = int(request.POST.get("txtn1"))
        n2 = int(request.POST.get("txtn2"))
        button = request.POST.get("btn")
        if button == "+":
            sum = n1 + n2
            return render(request,"basics/calculator.html",{"result": sum})
        elif button == "-":
            diff = n1 - n2
            return render(request,"basics/calculator.html",{"result": diff})
        elif button == "*":
            prod = n1 * n2
            return render(request,"basics/calculator.html",{"result": prod})
        elif button == "/":
            div = n1 / n2
            return render(request,"basics/calculator.html",{"result": div})
        else:
            return render(request,"basics/calculator.html")
    else:
        return render(request,"basics/calculator.html")


def large(request):
    if request.method == "POST":
        n1 = int(request.POST.get("txtn1"))
        n2 = int(request.POST.get("txtn2"))
        n3 = int(request.POST.get("txtn3"))
        if n1 > n2 and n1 > n3:
            l = n1
        elif n2 > n1 and n2 > n3:
            l = n2
        else:
            l = n3

        if n1 < n2 and n1 < n3 :
            s = n1
        elif n2 < n1 and n2 < n3:
            s = n2
        else:
            s = n3
        return render(request,"basics/ls.html",{"large": l,"small":s})                    
    else:
        return render(request,"basics/ls.html")
