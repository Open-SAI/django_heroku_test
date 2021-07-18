from django.conf.urls import url
from concepto import views

urlpatterns = [
    url(r'^api/concepto$', views.concepto_list),
    url(r'^api/concepto/(?P<pk>[0-9]+)$', views.concepto_detail),
    url(r'^api/concepto/published$', views.concepto_list_published)
]

