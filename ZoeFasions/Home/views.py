from django.shortcuts import render
from .forms import ProductForm
from . models import product
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(req):
    #using session for view page
    count = int (req.session.get('visits',0))
    t_count = count + 1
    req.session['visits'] = t_count


    # count using cookie
    visits = int (req.COOKIES.get('num_of_visits' , 0))
    total_visit = visits + 1
    response = render(req,'Home.html',{'Total_visit' : total_visit ,'count' : count}) 
    response.set_cookie('num_of_visits', total_visit)
    print("app : HOME")
    return response

@login_required(login_url='login')
def creation(req):
    frm = ProductForm()
    msg = ''
    #session create for counting visits
    count = req.session.get('visits',0)
    total_count = int(count)
    visit = total_count + 1
    req.session['visits'] = visit

    if req.method == 'POST':
        frm = ProductForm(req.POST , req.FILES)
        if frm.is_valid:
            frm.save()
            msg = "One item added to the list :) "
    response = render(req,'Create.html',{'form' : frm , 'message' : msg , 'count' : visit})
            
    return response

def list(req):
    #session displaying
    recent_visit = req.session.get('visited',[])
    # to avoid TypeError: 'int' object is not iterable "making it a list"
    # recent_visit = [recent_visit]
    recent_visited_data = product.objects.filter(pk__in = recent_visit )

    #coockies creation for count
    count = int(req.COOKIES.get('visits',0))
    visit = count + 1

    items = product.objects.all()
    response = render(req,'View.html',{'items' : items , 'Recently' :recent_visited_data, 'total' : visit})
    #set cookie value to response
    response.set_cookie('visits', visit)
    return response

@login_required(login_url='login')
def delete(req,pk):
    item = product.objects.get(id=pk)
    item.delete()
    items = product.objects.all()
    return render(req,'View.html',{'items' : items})

@login_required(login_url='login')
def edit(req,pk):
    data = product.objects.get(id=pk)
    frm = ProductForm(instance=data)
    msg =''
    #session creation
    recent_visits = req.session.get('visited',[])
    recent_visits.insert(0,pk)
    req.session['visited'] = recent_visits

    if req.method == 'POST':
        frm = ProductForm(req.POST,req.FILES,instance=data)
        if frm.is_valid:
            frm.save()
            msg = 'Edited successfully'
    #seting cookie value
    else:
        response = render(req,'create.html',{'form' : frm , 'message' : msg })
    
    return response


