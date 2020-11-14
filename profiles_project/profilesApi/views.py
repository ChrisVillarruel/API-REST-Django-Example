from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profilesApi import serializer


"""
    -> Serializador: Nos permite convertir objetos de python en informacion
    -> de JSON y viceversa

    -> status: Tiene varios codigos HTTP que podemos utilizar como respuesta
    -> usando nuestro API

"""


class HelloApiView(APIView):
    """ clase de un APIView de prueba """

    serializer_class = serializer.HelloSerializer

    def get(self, request, form=None):
        """ Retornar lista de caracteristicas del APIView """
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, path, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayo control sobre la logica de nuestra aplicación',
            'Esta mapeado manualmente a los urls'
        ]

        """ Retornamos siempre un objeto de response y response lo convertira en
            formato JSON
        """
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """

        # Froma estandar que se utiliza para obtener el serializador
        # cuando se esta trabajando en un view basado en clase con APIView
        serializer = self.serializer_class(data=request.data)

        # validamos si los datos que recivio serializer son validos
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name.upper()}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
