from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('homepage/', views.homepage),
                  path('login/', views.login),
                  path('logout/', views.logout),
                  path('', views.register),
                  path('profile/', views.profile),
                  path('search/', views.search),
                  path('addblog/', views.add_blog),
                  path('edit/<int:cat_id>/', views.edit_blog),
                  path('delete/<int:cat_id>/', views.delete_blog),
                  path('read/<int:cat_id>/', views.current),  # 1
                  path('currentbook/', views.current_display),  # 1
                  path('remove_current/<int:cur_id>/', views.remove_current),  # 1
                  path('toread/<int:cat_id>/', views.tbr),  # 2
                  path('tbrdisplay/', views.tbr_display),  # 2
                  path('remove_tbr/<int:tbr_id>/', views.remove_tbr),
                  path('favourite/<int:cat_id>/', views.favourite),  # 3
                  path('fav_display/', views.fav_display),  # 3
                  path('remove_fav/<int:fav_id>/', views.remove_fav),
                  path('month/<int:cat_id>/', views.month),  # 4
                  path('monthdisplay/', views.month_display),  # 4
                  path('remove_month/<int:mon_id>/', views.remove_month),
                  path('recommend/<int:cat_id>/', views.recom),  # 5
                  path('recom_display/', views.recom_display),  # 5
                  path('remove_rec/<int:rec_id>/', views.remove_rec),
                  path('book/<int:cat_id>/', views.review),  # 6
                  path('bookreview/', views.review_display),  # 6
                  path('book_display/<int:cat_id>/', views.book_detail),  # 6
                  path('remove_post/<int:rev_id>/', views.remove_review),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
