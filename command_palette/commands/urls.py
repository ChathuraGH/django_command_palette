from django.urls import path,re_path

from . import views

urlpatterns = [

   path('', views.cm, name='cm'),




   # path('search', views.ads_search, name='ads_search'),
   # path('post', views.ads_post, name='ads_post'),
   # path('redirect_through', views.redirect_through, name='redirect_through'),
   # path('ads_test_original_page', views.ads_test_original_page, name='ads_test_original_page'),
    
	# path('', views.index, name='index'),
	# path('', views.desktop_index, name='desktop_index'),
 #    path('desktop_logout', views.desktop_logout, name='desktop_logout'),
 #    path('desktop_lockout', views.desktop_lockout, name='desktop_lockout'),
 #    path('desktop_unlock', views.desktop_unlock, name='desktop_unlock'),
 #    re_path(r'.*', views.wrong_link, name='wrong_link'),
    
    
    # path('<str:room_name>/<int:groupid>/', views.room, name='room'),
    # path('<str:room_name>/<int:groupid>/group_does_not_found', views.group_does_not_found, name='group_does_not_found'),
    # re_path(r'.*', views.invalid_chat_url, name='invalid_chat_url'),
   # re_path(r'songs_playlist_.*',views.songs_playlist,name="songs_playlist"), 
]