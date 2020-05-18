from django.urls import path
from .views import sign_up, sign_in, sign_out, profile, ajax_reg


urlpatterns = [
    path('sign_up', sign_up),
    path('sign_in', sign_in),
    path('sign_out', sign_out),
    path('profile', profile),
    path('ajax_reg', ajax_reg)
]
