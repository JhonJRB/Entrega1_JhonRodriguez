from django.urls import path
from app_tutaxi import views

urlpatterns = [
    path('',views.inicio, name='inicio' ),
    path('cargarcliente/',views.cargar_cliente, name='cargar_cliente' ),
    path('cargarmovil/',views.cargar_movil, name='cargar_movil' ),
    path('cargarchofer/',views.cargar_chofer, name='cargar_chofer' ),
    path('buscarchofer/',views.buscar_chofer, name='buscar_chofer' ),
    path('verchofer/',views.ver_chofer, name='ver_chofer' ),
    path('vercliente/',views.ver_cliente, name='ver_cliente' ),
    path('vermovil/',views.ver_movil, name='ver_movil' ),
    path('traerchofer/',views.traer_chofer, name='traer_chofer' )
]
