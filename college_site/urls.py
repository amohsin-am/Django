from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django_demo.views import (
    home_page,
    contact_page,
    form_page,
    user_list,
    user_update,
    user_delete,
    product_list,
    user_login,
    user_logout,
    user_register,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_page, name="home_page_path"),
    path('contact/', contact_page, name="contact_page_path"),
    path('form/', form_page, name="form_page_path"),
    path('user_list/', user_list, name="user_list_path"),
    path('Update/<int:user_id>/', user_update, name="user_update_path"),
    path('Delete/<int:user_id>/', user_delete, name="user_delete_path"),
    path('product/', product_list, name="product_path"),

    
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('register/', user_register, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
