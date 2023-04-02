from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def homePage(request):
    data= {
        'title' : 'HomePage',
        'name':'Ram',
        'city':'pune',
        'lit':['java','python','php'],
        'student_data':[
            {'name':'Pradip pande','city':'Pune'},
            {'name':'Ravi Kant', 'city':'Mumbai'}
        ],
        'linst2':[1,2,3,5,8,9,8]
    }
   
    
    return render(request, "index.html" ,data)

def demoPage(request):
    return render(request, 'about.html')

def usrForm(request):
    # finalSum = 0
    data= {}
    try:
        n1 = int(request.GET['val1'])
        n2 = int(request.GET['val2'])
        # print(n1 + n2)
        finalSum = n1+n2
        data = {
            'n1':n1 , 'n2':n2 , 'finalSum':finalSum
        }
       
    except:
        pass
    return render(request , 'userForm.html', data)

def UserFormData(request):
    aata = {}
    if request.method == 'POST':
        
        try:
            Name = request.POST['Name']
            Email = request.POST['Email']
            DOB = request.POST['DOB']
            Mobile = request.POST['Mobile']
            
            aata={
                'Name':Name, 'Email':Email, 'DOB':DOB , 'Mobile':Mobile
            }
            return HttpResponseRedirect('/admin/')
            
        except:
            pass
    return render(request, 'UserFormData.html', aata)
    
def submitformdata(request):
    try:
            Name = request.POST['Name']
            Email = request.POST['Email']
            DOB = request.POST['DOB']
            Mobile = request.POST['Mobile']
            
            aata={
                'Name':Name, 'Email':Email, 'DOB':DOB , 'Mobile':Mobile
            }
            # return HttpResponseRedirect('/admin/')
            
    except:
            pass
    return HttpResponse(Name)

def Course(request):
    return HttpResponse("WellCome to Course Page")
def courseDetailes(request,courseid):
    return HttpResponse(courseid)
