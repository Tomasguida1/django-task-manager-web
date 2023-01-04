from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo
from django.contrib.auth.views import LogoutView

urlpatterns = [path("login/", Logueo.as_view(),name = "Login"),
               path("logout/", LogoutView.as_view(next_page = "Login"),name = "Logout"),
               path("", ListaPendientes.as_view(), name = 'Tareas'),
               path("tarea/<int:pk>", DetalleTarea.as_view(), name = "tarea"),
               path("crear-tarea/" ,CrearTarea.as_view(), name = "crear-tarea"),
               path("editar-tarea/<int:pk>", EditarTarea.as_view(), name = "editar-tarea"),
               path("eliminar-tarea/<int:pk>", EliminarTarea.as_view(), name = "eliminar-tarea")]