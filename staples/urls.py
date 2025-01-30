from . import views
from django.urls import path

urlpatterns = [
    path('staples/', views.render_staples_list, name='staples'),
    path('staples/edit/<int:staple_id>/', views.edit_staple, name='edit_staple'),
    path('delete_staple/<int:staple_id>/', views.delete_staple, name='delete_staple')
]
