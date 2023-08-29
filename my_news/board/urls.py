from django.urls import path,include
import board.views as views
urlpatterns = {
    path('',views.board),
    path('list/', views.list),
    path('blog/<int:id>',views.show),
    path('comment/<int:id>',views.comment),
    path('search/',views.search),
    path('classify/',views.classify)
}