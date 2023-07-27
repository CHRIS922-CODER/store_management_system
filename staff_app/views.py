from django.shortcuts import render
from .filters import ProductFilter
from commodity_app.models import *
from commodity_app.forms import *
from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required
from datetime import  datetime
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@login_required(login_url='login')
def item_list(request):
    query_set = Product.objects.all()
    productFilter = ProductFilter(request.GET, query_set)
    return render(request, 'items/items_search.html', {'productFilter':productFilter})


@login_required(login_url='login')
def index(request):
    return redirect("item_list")



@login_required(login_url='login')
def issuance_request(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = IssuanceForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(form.cleaned_data)
            quantity = form.cleaned_data['quantity_issued']
            if product.quantity >= quantity:
                issuance = form.save(commit=False)
                issuance.product = product
                issuance.user = request.user
                issuance.save()
                product.quantity -= quantity
                product.save()

            return redirect("issuance_history")
    else:
        initial_data = {
            'product': product.id if product else None,
            'user': request.user.pk if request.user.is_authenticated else None,
            'date_issued': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        form = IssuanceForm(initial=initial_data)
        print(initial_data)

    issued_products = Issuance.objects.filter(user=request.user)
    context = {'form': form, 'product': product, 'issued_products': issued_products}
    return render(request, 'items/issuance_request.html', context)





@login_required(login_url='login')
def issuance_editing(request, id):
    issuance = Issuance.objects.get(id=id)
    if request.method == 'POST':
        form = IssuanceForm(request.POST, instance=issuance)
        if form.is_valid():
            form.save()
            return redirect("issuance_history")
    else:
        initial_data = {
            'issuance': issuance.id if issuance else None,
            'user': request.user.pk if request.user.is_authenticated else None,
            'date_issued': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        form = IssuanceForm(instance=issuance,initial=initial_data)
        context = {'form': form, 'issuance': issuance}
        return render(request, 'items/issuance_editing.html', context)

@login_required(login_url='login')
def issuance_history(request):
    username = request.user.pk
    issuances = Issuance.objects.filter(user=username)
    context = {'issuances':issuances}
    return render(request,'items/issuance_history.html',context)