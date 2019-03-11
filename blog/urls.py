from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'page/<int:page>/', views.IndexView.as_view(), name='index_page'),
    path(r'article/<int:year>-<int:month>-<int:day>/<int:article_id>.html',
         views.ArticleDetailView.as_view(),
         name='detailbyid'),
    path(r'category/<slug:category_name>.html', views.CategoryDetailView.as_view(), name='category_detail'),
    path(r'category/<slug:category_name>/<int:page>.html', views.CategoryDetailView.as_view(),
         name='category_detail_page'),
    path(r'tag/<slug:tag_name>.html', views.TagDetailView.as_view(), name='tag_detail'),
    path(r'tag/<slug:tag_name>/<int:page>.html', views.TagDetailView.as_view(), name='tag_detail_page'),
]
