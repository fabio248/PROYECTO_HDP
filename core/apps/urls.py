from django.urls import path
from core.apps.views.subsidios.views import *
from core.homepage.views.usuarios.views import UsuarioCreateView
from core.apps.views.dashboard.views import DashBoardView

app_name = 'apps'

urlpatterns = [
    #Inicio
    path('dashboard/', DashBoardView.as_view(),name='dashboard'),
    #LIstados
    #gas licuado
    path('subsidio/gas/listado/', SubsidioGasListView.as_view(),name='subsidio_gas_lista'),
    path('subsidio/gas/formulario/', SubsidioGasCreateView.as_view(),name='subsidio_gas_create'),
    path('subsidio/gas/editar/<int:pk>/', SubsidioGasUpdateView.as_view(),name='subsidio_gas_edit'),
    path('subsidio/gas/eliminar/<int:pk>/', SubsidioGasDeleteView.as_view(),name='subsidio_gas_delete'),
    #energia electrica
    path('subsidio/luz/listado/', SubsidioLuzListView.as_view(),name='subsidio_luz_lista'),
    path('subsidio/luz/formulario/', SubsidioLuzCreateView.as_view(),name='subsidio_luz_create'),
    path('subsidio/luz/editar/<int:pk>/', SubsidioLuzUpdateView.as_view(),name='subsidio_luz_edit'),
    path('subsidio/luz/eliminar/<int:pk>/', SubsidioLuzDeleteView.as_view(),name='subsidio_luz_delete'),
    #servicio agua
    path('subsidio/agua/listado/', SubsidioAguaListView.as_view(),name='subsidio_agua_lista'),
    path('subsidio/agua/formulario/', SubsidioAguaCreateView.as_view(),name='subsidio_agua_create'),
    path('subsidio/agua/editar/<int:pk>/', SubsidioAguaUpdateView.as_view(),name='subsidio_agua_edit'),
    path('subsidio/agua/eliminar/<int:pk>/', SubsidioAguaDeleteView.as_view(),name='subsidio_agua_delete'),
    #transporte publico
    path('subsidio/transporte/listado/', SubsidioTrasnporteListView.as_view(),name='subsidio_transporte_lista'),
    path('subsidio/transporte/formulario/', SubsidioTransporteCreateView.as_view(),name='subsidio_transporte_create'),
    path('subsidio/transporte/editar/<int:pk>/', SubsidioTransporteUpdateView.as_view(),name='subsidio_transporte_edit'),
    path('subsidio/transporte/eliminar/<int:pk>/', SubsidioTransporteDeleteView.as_view(),name='subsidio_transporte_delete'),
    #Administrador
    #path('administrador/formulario/', AdministradorCreateView.as_view(),name='adminitrador_create'),
]