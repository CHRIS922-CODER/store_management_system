from django.shortcuts import render,redirect
from .models import Product,Category,Department,Issuance
from .forms import *
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.utils import timezone
import csv





from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


# Create your views here.
@login_required(login_url='login')
def home(request):
    issuances = Issuance.objects.order_by('-id')[:5]
    context = {'issuances':issuances}
    return render(request, 'commodity_app/mytemplate.html',context=context)

# PRODUCT VIEWS
@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']  # Convert the name to lowercase
            product, created = Product.objects.get_or_create(name=name, defaults=form.cleaned_data)
            if not created:
                # Update the quantity if the product already exists
                product.quantity += form.cleaned_data['quantity']
                product.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "product/product_add.html", {'form': form})


@login_required(login_url='login')
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        context = {'products':products}
        return render(request,"product/product_list.html",context)

@login_required(login_url='login')
def product_edit(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else :
        form = ProductForm(instance=product)
        return render(request,'product/product_edit.html',{'product':product,'form':form})
@login_required(login_url='login')   
def product_delete(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect("product_list")
    return render(request,'product/delete_product.html')
       
@staff_member_required
def product_reorder_level_list(request):
    productsList = Product.objects.all()
    products = [product for product in productsList if product.quantity <= product.reorder_level]
    context = {
        'products':products
    }
    return render(request,'product/product_reorder_level_list.html',context)

def export_productList_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Issuance.csv"'
    writer = csv.writer(response)
    writer.writerow(['Issuance id','Product','Quantity','Date','Staff','Department'])
    issuances = Issuance.objects.all()

    for issuance in issuances:
        writer.writerow([issuance.id, issuance.product, issuance.quantity_issued,issuance.date_issued,issuance.user, issuance.department]) 
    return response

# PRODUCT NAME VIEWS
@login_required(login_url='login')
def product_name(request):
    if request.method == 'POST':
        form = ProductNameForm(request.POST)
        if  form.is_valid():
            try:
                name = form.cleaned_data['name']
                product =ProductName.objects.filter(name=name)
                if product:
                    messages.warning(request, name + ' already exist', extra_tags='warning')
                    return redirect('product_name')
                else:
                    form.save()
                    messages.success(request, name+' added successfully', extra_tags='success')
                    return redirect('product_name')
            except:
                pass
    else:
        form = ProductNameForm()
        return render(request,"product/product_name.html",{'form':form})
    
@login_required(login_url='login')
def product_name_list(request):
    if request.method == "GET":
        products = ProductName.objects.all()
        context = {'products':products}
        return render(request,"product/product_name_list.html",context)
    
@login_required(login_url='login')
def product_name_edit(request,id):
    product = ProductName.objects.get(id=id)
    if request.method == 'POST':
        form = ProductNameForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_name_list")
    else :
        form = ProductNameForm(instance=product)
        return render(request,'product/product_name_edit.html',{'product':product,'form':form})
    
@login_required(login_url='login')   
def product_name_delete(request,id):
    product = ProductName.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect("product_name_list")
    return render(request,'product/product_name_delete.html')


# PRODUCT CATEGORY VIEWS
@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if  form.is_valid():
            try:
                name = form.cleaned_data['name']
                category =Category.objects.filter(name=name)
                if category:
                    messages.warning(request, category  + ' already exist', extra_tags='warning')
                    return redirect('product_name')
                else:
                    form.save()
                    messages.success(request, name+' added successfully', extra_tags='success')
                    return redirect('product_name')
            except:
                pass
    else:
        form = CategoryForm()
        return render(request,"category/category_add.html",{'form':form})
    
@login_required(login_url='login')   
def category_list(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'category/category_list.html',context)

@login_required(login_url='login')
def category_edit(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)
        return render(request,"category/category_edit.html",{'form':form, 'category':category})
    
@login_required(login_url='login')   
def category_delete(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.delete()
        return redirect("category_list")
    return render(request,'category/category_delete.html')

def export_categoryList_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Issuance.csv"'
    writer = csv.writer(response)
    writer.writerow(['Issuance id','Product','Quantity','Date','Staff','Department'])
    issuances = Issuance.objects.all()

    for issuance in issuances:
        writer.writerow([issuance.id, issuance.product, issuance.quantity_issued,issuance.date_issued,issuance.user, issuance.department]) 
    return response



# DEPARTMENT VIEWS
@login_required(login_url='login')
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data['name']
                department =Department.objects.filter(name=name)
                if department:
                    messages.warning(request, name + ' already exist', extra_tags='warning')
                    return redirect('add_department')
                else:
                    form.save()
                    messages.success(request, name+' added successfully', extra_tags='success')
                    return redirect('department_list')
            except:
                pass
    else:
        form = DepartmentForm()
        return render(request,"department/department_add.html",{'form':form})
    
@login_required(login_url='login')
def department_list(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request,"department/department_list.html",context)

@login_required(login_url='login')
def department_edit(request,id):
    department = Department.objects.get(id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form = DepartmentForm(instance=department)
        return render(request,"department/department_edit.html",{'form':form,'department':department})

@login_required(login_url='login')   
def department_delete(request,id):
    department = Department.objects.get(id=id)
    if request.method == 'POST':
        department.delete()
        return redirect("category_list")
    return render(request,'department/department_delete.html')

def export_departmentList_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Issuance.csv"'
    writer = csv.writer(response)
    writer.writerow(['Issuance id','Product','Quantity','Date','Staff','Department'])
    issuances = Issuance.objects.all()

    for issuance in issuances:
        writer.writerow([issuance.id, issuance.product, issuance.quantity_issued,issuance.date_issued,issuance.user, issuance.department]) 
    return response

# ISSUANCE VIEWS
@login_required(login_url='login')
def add_issuance(request,product_id):
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

            return redirect("issuance_list")
    else:
        initial_data = {
            'product': product.id if product else None,
            'user': request.user.pk if request.user.is_authenticated else None,
            'date_issued': timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        form = IssuanceForm(initial=initial_data)

    issued_products = Issuance.objects.filter(user=request.user)
    context = {'form': form, 'product': product, 'issued_products': issued_products}
    
    return render(request, 'issuance/issuance_add.html', context)

@login_required(login_url='login')    
def issuance_list(request):
    issuances = Issuance.objects.all()
    context = {'issuances':issuances}
    return render(request,'issuance/issuance_list.html',context)

@login_required(login_url='login')
def issuance_edit(request, id):
    issuance = Issuance.objects.get(id=id)

    if request.method == 'POST':
        form = IssuanceForm(request.POST, instance=issuance)
        if form.is_valid():
            quantity_issued = form.cleaned_data['quantity_issued']
            required_quantity = issuance.product.quantity

            if quantity_issued <= required_quantity:
                form.save()
                return redirect("issuance_list")
            else:
                messages.warning(request, ' Quantity cannot exceed the required quantity. ', extra_tags='warning')
                return redirect("issuance_list")
    else:
        form = IssuanceForm(instance=issuance)

    context = {'form': form, 'issuance': issuance}
    return render(request, 'issuance/issuance_edit.html', context)

    
@login_required(login_url='login')   
def issuance_delete(request,id):
    issuance = Issuance.objects.get(id=id)
    if request.method == 'POST':
        issuance.delete()
        return redirect("issuance_list")
    return render(request,'issuance/issuance_delete.html')

@login_required(login_url='login')
def issuance_records(request):
    issuances =  Issuance.objects.all()
    context = {
        'issuances' : issuances
    }
    return render(request,'issuance/issuance_records.html',context)

def export_issuanceList_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Issuance.csv"'
    writer = csv.writer(response)
    writer.writerow(['Issuance id','Product','Quantity','Date','Staff','Department'])
    issuances = Issuance.objects.all()

    for issuance in issuances:
        writer.writerow([issuance.id, issuance.product, issuance.quantity_issued,issuance.date_issued,issuance.user, issuance.department]) 
    return response
def export_issuanceRecords_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Issuance.csv"'
    writer = csv.writer(response)
    writer.writerow(['Issuance id','Product','Quantity','Date','Staff','Department'])
    issuances = Issuance.objects.all()

    for issuance in issuances:
        writer.writerow([issuance.id, issuance.product, issuance.quantity_issued,issuance.date_issued,issuance.user, issuance.department]) 
    return response


def modify_product_quantity(request):
    quantity = request.POST['quantity']
    product = Product.objects.get(product=request.POST['product'])
    product.quantity -= quantity

@login_required(login_url='login')
def reorder_level(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ReorderForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ReorderForm(instance=product)
        return render(request, 'product/reorder_item.html', {'product': product, 'form': form})


def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Issuance.csv"'
    writer = csv.writer(response)
    writer.writerow(['Issuance id','Product','Quantity','Date','Staff','Department'])
    issuances = Issuance.objects.all()

    for issuance in issuances:
        writer.writerow([issuance.id, issuance.product, issuance.quantity_issued,issuance.date_issued,issuance.user, issuance.department]) 
    return response

def settings(request):
    return render(request, 'product/settings.html')


def export_to_pdf_issuance(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Issuance.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Create the PDF content
    elements = []

    # Add logo and header information
    logo_path = '/home/chrispers/Public/store_management_system/static/images/hospital-logo.jpg'
  # Replace with the actual path to your logo image
    logo = Image(logo_path, width=1.5 * inch, height=1.5 * inch)
    elements.append(logo)

    styles = getSampleStyleSheet()
    header_text = '<h1>Issuance Report</h1>'
    header = Paragraph(header_text, styles['Heading1'])
    elements.append(header)

    additional_info = '<strong>Date:</strong> {}<br/><strong>Generated By:</strong> {}' \
                      .format(timezone.now().strftime('%Y-%m-%d'), request.user)
    additional_info_paragraph = Paragraph(additional_info, styles['Normal'])
    elements.append(additional_info_paragraph)

    elements.append(Spacer(1, 0.5 * inch))

    # Create the table
    data = [['Issuance id', 'Product', 'Quantity', 'Date', 'Staff', 'Department']]

    issuances = Issuance.objects.all()
    for issuance in issuances:
        issuance_data = [
            issuance.id,
            str(issuance.product),
            issuance.quantity_issued,
            issuance.date_issued.strftime('%Y-%m-%d'),
            str(issuance.user),
            str(issuance.department)
        ]
        data.append(issuance_data)

    table = Table(data)
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()

    # Set the PDF content in the response
    response.write(pdf)

    return response




def export_to_pdf_product(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Product.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Create the PDF content
    elements = []

    # Add logo and header information
    logo_path = '/home/chrispers/Public/store_management_system/static/images/hospital-logo.jpg'
  # Replace with the actual path to your logo image
    logo = Image(logo_path, width=1.5 * inch, height=1.5 * inch)
    elements.append(logo)

    styles = getSampleStyleSheet()
    header_text = '<h1>Product Report</h1>'
    header = Paragraph(header_text, styles['Heading1'])
    elements.append(header)

    additional_info = '<strong>Date:</strong> {}<br/><strong>Generated By:</strong> {}' \
                      .format(timezone.now().strftime('%Y-%m-%d'), request.user)
    additional_info_paragraph = Paragraph(additional_info, styles['Normal'])
    elements.append(additional_info_paragraph)

    elements.append(Spacer(1, 0.5 * inch))

    # Create the table
    data = [['Product','serial_no', 'quantity', 'Category','release_date']]

    products = Product.objects.all()
    for product in products:
        product_data = [
            str(product.name),
            product.serial_no,
            product.quantity,
            str(product.category),
            product.release_date.strftime('%Y-%m-%d')
        ]
        data.append(product_data)

    table = Table(data)
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()

    # Set the PDF content in the response
    response.write(pdf)

    return response

def export_to_pdf_product_out_of_stock(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Product Out Of Stock.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Create the PDF content
    elements = []

    # Add logo and header information
    logo_path = '/home/chrispers/Public/store_management_system/static/images/hospital-logo.jpg'
  # Replace with the actual path to your logo image
    logo = Image(logo_path, width=1.5 * inch, height=1.5 * inch)
    elements.append(logo)

    styles = getSampleStyleSheet()
    header_text = '<h1>Product Out Of Stock Report</h1>'
    header = Paragraph(header_text, styles['Heading1'])
    elements.append(header)

    additional_info = '<strong>Date:</strong> {}<br/><strong>Generated By:</strong> {}' \
                      .format(timezone.now().strftime('%Y-%m-%d'), request.user)
    additional_info_paragraph = Paragraph(additional_info, styles['Normal'])
    elements.append(additional_info_paragraph)

    elements.append(Spacer(1, 0.5 * inch))

    # Create the table
    data = [['Product','serial_no', 'quantity', 'Category','release_date']]

    productsList = Product.objects.all()
    products = [product for product in productsList if product.quantity <= product.reorder_level]
    for product in products:
        product_data = [
            str(product.name),
            product.serial_no,
            product.quantity,
            str(product.category),
            product.release_date.strftime('%Y-%m-%d')
        ]
        data.append(product_data)

    table = Table(data)
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()

    # Set the PDF content in the response
    response.write(pdf)

    return response


