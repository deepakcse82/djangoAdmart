from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *


class BackendRegister(UserCreationForm):
    username = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter User name'
    })))
    email = forms.EmailField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@mail.com',
        'type': 'email'
    })))
    password1 = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'placeholder': '*********'
    })))
    password2 = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'placeholder': '********'
    })))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BackendLogin(AuthenticationForm):
    username = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Enter Username'
    })))
    password = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'placeholder': '******'
    })))

    class Meta:
        model = User
        field = ['username', 'password']


# =========================== product form =============================#
class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Enter Category Name'
    })))
    # cat_img = forms.CharField(widget=(forms.TextInput(attrs={
    #     'type': 'file',
    #     'class': 'form-control',
    #     'placeholder': 'choose file',
    #     'name': 'cat_img'
    # })))

    class Meta:
        model = AddCategory
        fields = ['cat_name', 'cat_img']


class SubCategoryForm(forms.ModelForm):
    # sub_cat_type = forms.ModelChoiceField(
    #     queryset=AddCategory.objects.all(),
    #     empty_label='Choose One',
    #     widget=forms.Select(
    #         attrs={'class': 'form-control'}
    #     ))
    # brand_name = forms.ModelChoiceField(
    #     queryset=AddBrand.objects.all(),
    #     empty_label='Choose One',
    #     widget=forms.Select(
    #         attrs={'class': 'form-control'}
    #     ))

    sub_cat_names = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Enter Sub category name'
    })))

    # sub_cat_img = forms.CharField(widget=(forms.TextInput(attrs={
    #     'type': 'file',
    #     'class': 'form-control',
    #     'placeholder': 'choose file',
    #     'name': 'cat_img'
    # })))

    class Meta:
        model = SubCategory
        fields = ['sub_cat_names', 'sub_cat_img']


class BrandForm(forms.ModelForm):

    brand_name = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Enter Sub category name'
    })))

    # brand_img = forms.CharField(widget=(forms.TextInput(attrs={
    #     'type': 'file',
    #     'class': 'form-control',
    #     'placeholder': 'choose file',
    #     'name': 'cat_img'
    # })))

    class Meta:
        model = AddBrand
        fields = ['brand_name', 'brand_img']


class FormProduct(forms.ModelForm):
    pro_brand = forms.ModelChoiceField(
        queryset=AddBrand.objects.all(),
        empty_label='Choose One',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ))
    pro_category = forms.ModelChoiceField(
        queryset=AddCategory.objects.all(),
        empty_label='Choose One',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ))
    pro_sub_category = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        empty_label='Choose One',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ))
    pro_name = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Enter Product name'
    })))
    pro_des = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Enter Description'
    })))
    pro_price = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'number',
        'class': 'form-control',
        'placeholder': 'Enter Price'
    })))
    pro_discount = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'number',
        'class': 'form-control',
        'placeholder': 'Enter Discount'
    })))

    choice_size =(
        ('', 'Choose Product Size'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', "L"),
        ('xl', 'XL'),
        ('2xl', '2XL')
    )
    pro_size = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=choice_size,
        required="False",

    )

    pro_Qty = forms.CharField(widget=(forms.TextInput(attrs={
        'type': 'number',
        'class': 'form-control',
        'placeholder': 'Enter Quantity'
    })))

    # pro_img = forms.CharField(widget=(forms.TextInput(attrs={
    #     'type': 'file',
    #     'class': 'form-control',
    #     'placeholder': 'choose file',
    #     # 'name': 'pro_img'
    # })))

    class Meta:
        model = Product
        fields = ['pro_brand',
                  'pro_category',
                  'pro_sub_category',
                  'pro_name',
                  'pro_des',
                  'pro_img',
                  'pro_price',
                  'pro_discount',
                  'pro_size',
                  'pro_Qty'
        ]
