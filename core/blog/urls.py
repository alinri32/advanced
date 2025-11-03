
from django.urls import path
from blog.views import indexViews
from django.views.generic import TemplateView

APP_NAME = 'blog'

urlpatterns = [
    path('fbv', indexViews , name='fbv'),
    path('cbv', TemplateView.as_view(template_name = 'base.html',extra_context={'name':'ali'}) , name='cbv'),
    # path('cbv', indexViews , name='cbv'),

]