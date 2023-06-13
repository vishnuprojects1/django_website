from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('get_item',views.getData),
    path('add_item',views.addItem),
    path('get_item/<int:id>',views.item_detail),
    path('get_contact',views.contactData),
    path('add_contact',views.addContact),
    path('get_contact/<int:id>',views.contact_detail)
]

urlpatterns=format_suffix_patterns(urlpatterns)