from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This renders your HTML page
    path('extract_and_translate/', views.extract_and_translate, name='extract_and_translate'),  # API for OCR & Translation
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('api/extract_and_translate/', views.extract_and_translate, name='extract_and_translate'),
# ]

