from django.shortcuts import render,redirect
import models
import forms
from django.core.urlresolvers import resolve
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from permissions import check_permission

# Create your views here.
def dashboard(request):
    return render(request,'crm/dashboard.html')

@check_permission
def customers(request):
    cus_list = models.Customer.objects.all()
    paginator = Paginator(cus_list,2,2)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'crm/customers.html',{"cus_list":customer})


@check_permission
def customerInfo(request,customer_id):
    customer_obj = models.Customer.objects.get(pk=customer_id)
    if request.method == 'POST':
        form = forms.customerForm(request.POST, instance=customer_obj)
        if form.is_valid():
            form.save()
            baseUrl = "/".join(request.path.split("/")[:-2])
            print baseUrl
            return redirect(baseUrl)
        else:
            print form.errors
    else:
        form = forms.customerForm(instance=customer_obj)
    return render(request, 'crm/customers_detail.html', {'cust_info':form})

