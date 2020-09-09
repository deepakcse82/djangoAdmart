from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BackendRegister, BackendLogin, CategoryForm, SubCategoryForm, BrandForm, FormProduct
from .models import AddCategory, SubCategory, AddBrand, Product


def admin_register(request):
    register_form = BackendRegister()
    if request.method == 'POST':
        register_form = BackendRegister(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = register_form.cleaned_data.get('username')
            messages.success(request, 'Hii ' + user + ' Your Account has Created !!!!')
            # =================== login authentication at registration start===============================#
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('admin_home')
            # =================== login authentication at registration end===============================#

    content = {'form': register_form}
    return render(request, 'register.html', content)


def admin_login(request):
    login_form = BackendLogin()
    if request.method == 'POST':
        login_field = BackendLogin(request, data=request.POST)
        if login_field.is_valid():
            username = login_field.cleaned_data.get('username')
            password = login_field.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome ' + username )
                return redirect('admin_home')

    content = {'login_form': login_form}
    return render(request, 'login.html', content)


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


@login_required(login_url='admin_login')
def admin_home(request):
    return render(request, 'admin_index.html')


# ==================== product views start ========================= #
@login_required(login_url='admin_login')
def add_cat(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST, request.FILES)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('add_cat')
    cat_form = CategoryForm()
    main_category = AddCategory.objects.all()
    cat_content = {'cat_form': cat_form, 'main_category': main_category}
    return render(request, 'add_cat.html', cat_content)


@login_required(login_url='admin_login')
def edit_cat(request, pk):
    edit_cat = AddCategory.objects.get(id=pk)
    edit_cat_form = CategoryForm(instance=edit_cat)
    if request.method == 'POST':
        edit_cat_form = CategoryForm(request.POST, files=request.FILES,  instance=edit_cat)
        if edit_cat_form.is_valid():
            edit_cat_form.save()
            return redirect('add_cat')
    edit_content = {'edit_cat_form': edit_cat_form}
    return render(request, 'edit_cat.html', edit_content)


@login_required(login_url='admin_login')
def del_cat(request, id):
    del_cat = AddCategory.objects.get(id=id)
    del_cat.delete()
    return redirect('add_cat')


@login_required(login_url='admin_login')
def add_brand(request):
    if request.method == 'POST':
        brand_form = BrandForm(request.POST, request.FILES)
        if brand_form.is_valid():
            brand_form.save()
            return redirect('brands')
    brand_form = BrandForm()
    all_brands = AddBrand.objects.all()
    brand_content = {'brand_form': brand_form, 'all_brands': all_brands}
    return render(request, 'add_brand.html', brand_content)


@login_required(login_url='admin_login')
def edit_brand(request, pk):
    edit_brand = AddBrand.objects.get(id=pk)
    edit_brand_form = BrandForm(instance=edit_brand)
    if request.method == 'POST':
        edit_brand_form = BrandForm(request.POST, files=request.FILES, instance=edit_brand)
        if edit_brand_form.is_valid():
            edit_brand_form.save()
            return redirect('brands')
    edit_brand_content = {'edit_brand_form': edit_brand_form}
    return render(request, 'edit_brand.html', edit_brand_content)


@login_required(login_url='admin_login')
def del_brand(request, id):
    del_brand = AddBrand.objects.get(id=id)
    del_brand.delete()
    return redirect('brands')


@login_required(login_url='admin_login')
def subcategory(request):
    if request.method == 'POST':
        sub_cat_form = SubCategoryForm(request.POST, request.FILES)
        if sub_cat_form.is_valid():
            sub_cat_form.save()
            return redirect('subcategory')
    sub_cat_form = SubCategoryForm()
    all_sub_category = SubCategory.objects.all()
    sub_cat_content = {'sub_cat_form': sub_cat_form, 'all_sub_category': all_sub_category}
    return render(request, 'subcategory.html', sub_cat_content)


@login_required(login_url='admin_login')
def edit_sub_cat(request, pk):
    edit_sub_cat = SubCategory.objects.get(id=pk)
    edit_sub_cat_form = SubCategoryForm(instance=edit_sub_cat)
    if request.method == 'POST':
        edit_sub_cat_form = SubCategoryForm(request.POST, files=request.FILES,  instance=edit_sub_cat)
        # print(edit_sub_cat_form)
        if edit_sub_cat_form.is_valid():
            edit_sub_cat_form.save()
            return redirect('subcategory')
    edit_sub_cat_content = {'edit_sub_cat_form': edit_sub_cat_form}
    return render(request, 'edit_sub_cat.html', edit_sub_cat_content)


@login_required(login_url='admin_login')
def del_sub_cat(request, id):
    del_sub_cat = SubCategory.objects.get(id=id)
    del_sub_cat.delete()
    return redirect('subcategory')


@login_required(login_url='admin_login')
def product(request):
    if request.method == 'POST':
        form_product = FormProduct(request.POST, request.FILES)
        if form_product.is_valid():
            form_product.save()
            return redirect('product')
    product_form = FormProduct()
    all_product = Product.objects.all()
    product_content = {'product_form': product_form, 'all_product': all_product}
    return render(request, 'product.html', product_content)


@login_required(login_url='admin_login')
def del_product(request, id):
    del_product = Product.objects.get(id=id)
    print(del_product)
    del_product.delete()
    return redirect('product')


@login_required(login_url='admin_login')
def edit_product(request, pk):
    edit_product = Product.objects.get(id=pk)
    edit_product_form = FormProduct(instance=edit_product)
    if request.method == 'POST':
        edit_product_form = FormProduct(request.POST, files=request.FILES, instance=edit_product)
        if edit_product_form.is_valid():
            edit_product_form.save()
            return redirect('product')
    edit_product_content = {'edit_product_form': edit_product_form}
    return render(request, 'edit_product.html', edit_product_content)

