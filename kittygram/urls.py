from django.urls import path

# from cats.views import cat_list, cat_detail
from cats.views import APIcats, APICatsDetail

# urlpatterns = [
#    path('cats/', cat_list),
#    path('cats/<int:pk>/', cat_detail),
# ]
urlpatterns = [
   path('cats/', APIcats.as_view()),
   path('cats/<int:pk>/', APICatsDetail.as_view())
]


