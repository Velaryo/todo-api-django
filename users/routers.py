from rest_framework.routers import Route, DynamicRoute, SimpleRouter

#SimpleRouter es el padre de defaultRoter
# DefaulRouter tiene APIRoot (lsitado de apis)
#los maping tienen esos nombres de funcion xq 
	# estan usando genericViewSet en la API
#mapeo de rutas
#todo| No se suele usar a menos q se requiera
class CustomRouter(SimpleRouter):
    """ ARRAY de rutas """
    routes = [
        Route(
          url=r"^{prefix}$",
          mapping={'get': 'get'}, #funcion GT
          name="{basename}-list",
		  detail = False, #si no muestra info
          initkwargs={'suffix': 'List'}
        ),
        Route(
          url=r"^{prefix}/{lookup}$",
		  #funcion retrieve
          mapping={'get': 'retrieve'}, 
          name="{basename}-detail",
		  detail = True,
          initkwargs={'suffix': 'Detail'}
        )
    ]