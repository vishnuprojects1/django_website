from django.urls import path
from . import views

urlpatterns = [
    path("",views.landing),
    path("addtocart", views.addcart),
    path("mycart", views.viewcart),
    path("search", views.searchitem),
    path("contain/<str:keyword>", views.getdata),
    path("delete-item", views.delete_item),
    path("contactus", views.contactus),
    path("detadded", views.addet)
]