from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('companyprofile/',views.company_profile,name='profile'),
    path('products/',views.products,name='products'),
    path('qualitystandards/',views.quality,name='quality'),
    path('designstudio/',views.design,name='design'),
    path('contactus/',views.contact,name='contact'),
]