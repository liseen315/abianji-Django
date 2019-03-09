from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'page/<int:page>/', views.IndexView.as_view(), name='index_page'),
    path(r'article/<int:year>-<int:month>-<int:day>/<int:article_id>.html',
         views.ArticleDetailView.as_view(),
         name='detailbyid')
]
