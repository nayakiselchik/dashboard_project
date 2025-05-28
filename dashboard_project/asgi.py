# import os
# import django
#
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.core.asgi import get_asgi_application
#
# from dashboard_app.routing import websocket_urlpatterns
#
# # 1) Set the settings module before any Django import
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard_project.settings")
# django.setup()
#
# # 2) The ASGI application for HTTP (including static files via URLConf)
# django_http_app = get_asgi_application()
#
# # 3) Protocol router: HTTP → Django, WS → our consumers
# application = ProtocolTypeRouter({
#     "http": django_http_app,
#     "websocket": AuthMiddlewareStack(
#         URLRouter(websocket_urlpatterns)
#     ),
# })

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard_project.settings")
application = get_asgi_application()
