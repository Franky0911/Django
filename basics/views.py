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
    
def bsalary(request):
        if request.method=="POST":
            fname=request.POST.get("txtname")
            lname=request.POST.get("txtname1")
            gender=request.POST.get("txtgender")
            martial=request.POST.get("txtmartial")
            department=request.POST.get("dpt")
            basicsalary=int(request.POST.get("txtbasic"))
            if gender=="MALE":
                result="Mr "+fname+" "+lname
            
            else:
                if martial == "Married":
                    result="Mrs "+fname+" "+lname
                else:
                    result="Miss "+fname+" "+lname    
            
            if gender=="MALE":
                gen="Male"
            else:
                gen="Female"

            if martial=="Single":
                mar="Single"
            else:
                mar="Married"

            if department=="cs":
                dep="Computer Science"
            elif department=="it":
                dep="Information Technology"
            else:
                dep="Medical"
        
            if basicsalary>=10000:
                TA=basicsalary*(40/100)
                DA=basicsalary*(35/100)
                HRA=basicsalary*(30/100)
                LIC=basicsalary*(25/100)
                PF=basicsalary*(20/100)
            elif basicsalary>=5000:
                TA=basicsalary*(35/100)
                DA=basicsalary*(30/100)
                HRA=basicsalary*(25/100)
                LIC=basicsalary*(20/100)
                PF=basicsalary*(15/100)
            else:
                TA=basicsalary*(30/100)
                DA=basicsalary*(25/100)
                HRA=basicsalary*(20/100)
                LIC=basicsalary*(15/100)
                PF=basicsalary*(10/100)
            Dedu=LIC+PF
            Net=basicsalary+TA+DA+HRA-(LIC+PF)                           
            return render(request,"basics/bsalary.html",{"Name":result,"Gender":gen,"Martial":mar,"Dep":dep,"Basic":basicsalary,"Ta":TA,"Da":DA,"Hra":HRA,"Lic":LIC,"Pf":PF,
                                                        "Deduction":Dedu,"NET":Net})
            
        else:
            return render(request,"basics/bsalary.html")
