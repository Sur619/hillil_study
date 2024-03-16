from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("product/<slug:product_slug>/", views.index, name='product_index'),
    path('main_page/', views.main_page, name='main_page'),
    path('news/', views.news, name='news'),
    path('forum/', views.forum, name='forum'),
    path('login/', views.login_page, name='login'),
    path('products/', views.all_products, name='products'),
    path('views_t/', views.test_views, name='test_products'),
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
