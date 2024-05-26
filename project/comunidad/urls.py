from django.urls import path
from .views import (
    index, 
    veterinariaslist, 
    VeterinariasCreate, 
    VeterinariasDelete, 
    VeterinariasDetail, 
    VeterinariasUpdate, 
    LocalidadCreate, 
    TipCuriosidadCreate,
    TipCuriosidadDelete,
    TipCuriosidadDetail,
    TipCuriosidadUpdate,
    TipoAnimalCreate,
    tipcuriosidadlist
    )

app_name = 'comunidad'

urlpatterns = [
    path('comunidad/', index, name='index'),
]

urlpatterns += [
    path('comunidad/veterinarias/list', veterinariaslist, name='veterinarias_list'),
    path('comunidad/veterinarias/create', VeterinariasCreate.as_view(), name='veterinarias_create'),
    path('comunidad/veterinarias/update/<int:pk>', VeterinariasUpdate.as_view(), name='veterinarias_update'),
    path('comunidad/veterinarias/detail/<int:pk>', VeterinariasDetail.as_view(), name='veterinarias_detail'),
    path('comunidad/veterinarias/delete/<int:pk>', VeterinariasDelete.as_view(), name='veterinarias_delete'),
]

urlpatterns += [
    path('comunidad/localidad_create', LocalidadCreate.as_view(), name='localidad_create')
]

urlpatterns += [
    path('comunidad/tipcuriosidad/list', tipcuriosidadlist, name='tipcuriosidad_list'),
    path('comunidad/tipcuriosidad/create', TipCuriosidadCreate.as_view(), name='tipcuriosidad_create'),
    path('comunidad/tipcuriosidad/update/<int:pk>', TipCuriosidadUpdate.as_view(), name='tipcuriosidad_update'),
    path('comunidad/tipcuriosidad/detail/<int:pk>', TipCuriosidadDetail.as_view(), name='tipcuriosidad_detail'),
    path('comunidad/tipcuriosidad/delete/<int:pk>', TipCuriosidadDelete.as_view(), name='tipcuriosidad_delete'),
]

urlpatterns += [
    path('comunidad/tipoanimal/create', TipoAnimalCreate.as_view(), name='tipoanimal_create')
]
