"""Pets tests."""

import os
from unittest import mock

from django.test import TestCase
from django.urls import reverse

from pets.models import ImageObject, Pet, PetObject

IMG_DEFAULT_ALT = "img_alt"
IMG_DEFAULT_SRC = "default/img/{}.png".format(IMG_DEFAULT_ALT)
MOCKED_PET = [
    {
        "breeds": [],
        "id": "ata",
        "url": "https://cdn2.thecatapi.com/images/ata.jpg",
        "width": 432,
        "height": 640,
    }
]
SUCCESS_URL = os.environ["DOGS_URL"]
FAIL_URL = os.environ["CATS_URL"]


def mocked_pets_get_pet(*args, **kwargs):
    """Generate a method to make requests.get.

    Returns:
        [type]: A mocked response.
    """

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        @property
        def ok(self):
            return self.status_code == 200

    if args[0] == SUCCESS_URL:
        return MockResponse(MOCKED_PET, 200)
    elif args[0] == FAIL_URL:
        return MockResponse({"error": "Bad Request"}, 404)

    return MockResponse(None, 404)


def _create_img() -> ImageObject:
    """Create a reutilizable Imageobject.

    Returns:
        ImageObject: A generic Imageobject.
    """
    return ImageObject(IMG_DEFAULT_SRC)


class ImageObjectModelTests(TestCase):
    """Imageobject's tests."""

    def test_create_an_object(self):
        """Create an Imageobject."""

        img_object = _create_img()
        self.assertEqual(img_object.src, IMG_DEFAULT_SRC)
        self.assertEqual(img_object.alt, IMG_DEFAULT_ALT)

    def test_dehydrate(self):
        """Test dehydate."""

        img_object = ImageObject(IMG_DEFAULT_SRC)
        self.assertIs(type(img_object.dihydrate), dict)
        self.assertIs("src" in img_object.dihydrate, True)
        self.assertEqual(img_object.dihydrate["src"], IMG_DEFAULT_SRC)
        self.assertIs("alt" in img_object.dihydrate, True)
        self.assertIs(len(img_object.dihydrate.keys()), 2)


class PetObjectModelTests(TestCase):
    """Petobject's tests."""

    def test_create_an_object(self):
        """Create a Petobject."""

        pet_object = PetObject(url=IMG_DEFAULT_SRC)
        self.assertIs(pet_object.image.__class__, ImageObject)

    def test_dehydrate(self):
        """Test dehydate."""

        pet_object = PetObject(url=IMG_DEFAULT_SRC)
        self.assertIs("image" in pet_object.dihydrate, True)
        self.assertIs(len(pet_object.dihydrate.keys()), 1)
        self.assertEqual(pet_object.dihydrate["image"]["src"], IMG_DEFAULT_SRC)


class PetsModelTest(TestCase):
    """Pets's tests."""

    @mock.patch("requests.get", side_effect=mocked_pets_get_pet)
    def test_get_pet(self, mock_get):
        """Test Pet's __get_pet method return a valid PetObject.

        Args:
            mock_get ([type]): A mocked requests.get function.
        """

        pet_object = PetObject(**MOCKED_PET[0])
        pet = Pet.get_dog()
        self.assertEqual(pet.dihydrate, pet_object.dihydrate)


class DogViewTest(TestCase):
    """DogView's tests."""

    def test_success_dog_view_response(self):
        """Dogview return success."""

        response = self.client.get(reverse("dogs"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, "pets/pet.html")
