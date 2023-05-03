from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import covid19_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_views),
    path('contact/', views.contact_views),
    path('about/', views.about_views),
    path('home/', views.home_views),
    path('about-me/', views.about_views),
    path('covid19/', views.covid19_views, name='covid19'),
    path('covid19/<str:country_code>/', covid19_views, name='covid19_country'),
    path('blog/', views.blog_views, name='blog'),
    path('blog/<post_id>', views.blog_detail_views, name='blog_detail'),
    path('category/<category_name>', views.blog_views, name='category_name'),
    path('author/<int:author_name>', views.author_views, name='author_name'),
]
