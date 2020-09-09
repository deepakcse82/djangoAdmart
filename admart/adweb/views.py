from django.shortcuts import render
from adweb.forms import RegisterForm
# from adadmin.models import AddCategory as adminCategory
# from adadmin.models import SubCategory as adminSubCategory
# from adadmin.models import AddBrand as adminBrand
# from adadmin.models import Product as adminProduct


def web_home(request):
    # product_category = adminProduct.objects.all()
    # print(product_category)
    return render(request, 'web_index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    register_form = RegisterForm()
    content = {'forms': register_form}
    return render(request, 'register.html', content)