from django.db import models


class AddCategory(models.Model):
    cat_name = models.CharField(max_length=30, null=True)
    cat_img = models.ImageField(upload_to='product/', default='')

    def __str__(self):
        return self.cat_name


class AddBrand(models.Model):
    brand_name = models.CharField(max_length=30, null=True)
    brand_img = models.ImageField(upload_to='brand/', default='')

    def __str__(self):
        return self.brand_name


class SubCategory(models.Model):
    # sub_cat_type = models.ForeignKey(AddCategory, on_delete=models.CASCADE, null=True)
    # brand_name = models.ForeignKey(AddBrand, on_delete=models.CASCADE, null=True)
    sub_cat_names = models.CharField(max_length=30, null=True)
    sub_cat_img = models.ImageField(upload_to='sub_category/', default='')

    def __str__(self):
        return self.sub_cat_names


class Product(models.Model):

    pro_brand = models.ForeignKey(AddBrand, on_delete=models.CASCADE, null=True)
    pro_category = models.ForeignKey(AddCategory, on_delete=models.CASCADE, null=True)
    pro_sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    pro_name = models.CharField(max_length=30, null=True)
    pro_des = models.CharField(max_length=100, null=True)
    pro_img = models.ImageField(upload_to='products/', default='')
    pro_price = models.IntegerField(null=True)
    pro_discount = models.IntegerField(null=True)
    pro_size = models.CharField(max_length=5, null=True, blank=True)
    pro_Qty = models.IntegerField(null=True)

    def __str__(self):
        return self.pro_name
