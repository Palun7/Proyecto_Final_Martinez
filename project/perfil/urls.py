from django.urls import path

from .views import (
    index,
    MascotaCreate,
    MascotaDelete,
    MascotaDetail,
    MascotaUpdate,
    MascotaList,
)
app_name = 'perfil'

urlpatterns = [
    path('perfil/index', index, name='index'),
]

urlpatterns += [
    path('perfil/mascota/list', MascotaList.as_view(), name='mascota_list'),
    path('perfil/mascota/create', MascotaCreate.as_view(), name='mascota_create'),
    path('perfil/mascota/update/<int:pk>', MascotaUpdate.as_view(), name='mascota_update'),
    path('perfil/mascota/detail/<int:pk>', MascotaDetail.as_view(), name='mascota_detail'),
    path('perfil/mascota/delete/<int:pk>', MascotaDelete.as_view(), name='mascota_delete'),
]
