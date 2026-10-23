from  django.urls import path
from  .import consumers

#handls all the websocket URL patterns
websocket_urlpatterns = [
    #URL endpoint where the user connect vbia the websocket
    #converts chat consumer class into an ASGI application 
    # compatible so that Django channel can handel the asgnchronous websocket connection 
    path ("ws/chat/", consumers.ChartConsumer.as_asgi)
]