from django.urls import path
from adadmin import views as adview
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', adview.admin_login, name='admin_login'),
    path('register_mart/', adview.admin_register, name='admin_register'),
    path('admin_home/', adview.admin_home, name='admin_home'),
    path('admin_logout/', adview.admin_logout, name='admin_logout'),
    # =================== products module urls ============================== #
    path('add_cat/', adview.add_cat, name='add_cat'),
    path('edit_cat/<str:pk>/', adview.edit_cat, name='edit_cat'),
    path('del_cat/<int:id>/', adview.del_cat, name='del_cat'),
    path('add_brand/', adview.add_brand, name='brands'),
    path('edit_brand/<str:pk>/', adview.edit_brand, name='edit_brand'),
    path('del_brand/<int:id>/', adview.del_brand, name='del_brand'),
    path('subcategory/', adview.subcategory, name='subcategory'),
    path('edit_sub_cat/<str:pk>/', adview.edit_sub_cat, name='edit_sub_cat'),
    path('del_sub_cat/<int:id>/', adview.del_sub_cat, name='del_sub_cat'),
    path('product/', adview.product, name='product'),
    path('del_product/<int:id>/', adview.del_product, name='del_product'),
    path('edit_product/<str:pk>/', adview.edit_product, name='edit_product'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)