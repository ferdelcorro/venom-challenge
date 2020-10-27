"""Out Pet's views."""
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from pets.models import Pet


class DogView(APIView):
    """Dogs's API."""

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request: Request) -> Response:
        """Get a random dog.

        Args:
            request (Request):  API's request.

        Returns:
            Response:           A dog's object representation.
        """
        dog = Pet.get_dog()
        return Response(
            {"pet": dog.dihydrate},
            template_name="pets/pet.html",
            status=status.HTTP_200_OK,
        )


class CatView(APIView):
    """Cats's API."""

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request: Request) -> Response:
        """Get a random cat.

        Args:
            request (Request):  API's request.

        Returns:
            Response:           A cat's object representation.
        """
        cat = Pet.get_cat()
        return Response(
            {"pet": cat.dihydrate},
            template_name="pets/pet.html",
            status=status.HTTP_200_OK,
        )
