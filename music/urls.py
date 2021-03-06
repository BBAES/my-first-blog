from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/712/
    # /music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # # /music/<album_id>/favorite
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album_add'),

]