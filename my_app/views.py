from django.shortcuts import render,HttpResponse
import random
import re


# Create your views here.

def home(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        specialchar = request.POST['specialchar']
        numbers = request.POST['numbers']
        length =request.POST['value']

        all = firstname+lastname+specialchar+numbers

        try:
            while True:
                password = "".join(random.sample(all, int(length)))
                spechar = re.search('\W', password)
                num = re.search('\d', password)
                if spechar != None and num !=None:
                    password = password.capitalize()
                    print(password)
                    break
                else:
                    continue
            return render(request,'l.html',{'pass':password})
        except:
            return HttpResponse("<script>alert('Please select the length of the password....')</script>")


    return render(request,'index.html')