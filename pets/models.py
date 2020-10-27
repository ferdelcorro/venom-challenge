"""Pet's objects."""
import logging
import os
from typing import Dict

import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

CATS_URL = os.environ["CATS_URL"]
DOGS_URL = os.environ["DOGS_URL"]


class ImageObject:
    """Pet image's representation."""

    src: str
    alt: str

    def __init__(self, src: str) -> None:
        """Init Imageobject.

        Args:
            src (str): Image source.
        """
        self.src = src
        self.alt = src.split("/")[-1].split(".")[0]

    @property
    def dihydrate(self) -> Dict:
        """Convert our image's representation to a dict.

        Returns:
            Dict: Our dihydrate image.
        """
        return {"src": self.src, "alt": self.alt}


class PetObject:
    """Pet's object."""

    image: ImageObject

    def __init__(self, **kwargs) -> None:
        """Init Petobject."""
        self.image = ImageObject(kwargs["url"])

    @property
    def dihydrate(self) -> Dict:
        """Convert our pet's representation to a dict.

        Returns:
            Dict: Our dihydrate pet.
        """
        return {
            "image": self.image.dihydrate,
        }


class Pet:
    """Pet wrapper."""

    def __get_pet(self, url: str) -> PetObject:
        """Get a random pet.

        Args:
            url (str): Url where we need to look for a pet.

        Returns:
            PetObject: Our Pet definition.
        """
        response = requests.get(url)
        if response.ok:
            return PetObject(**response.json()[0])
        else:
            raise Exception("An error ocurred when try to request a pet")

    @classmethod
    def get_cat(cls) -> PetObject:
        """Get a random cat from <CATS_URL>.

        Returns:
            PetObject: Our random cat object.
        """
        logger.info("Pets | get_cat")

        return cls().__get_pet(CATS_URL)

    @classmethod
    def get_dog(cls) -> PetObject:
        """Get a random dog from <DOGS_URL>.

        Returns:
            PetObject: Our random dog object.
        """
        logger.info("Pets | get_dog")

        return cls().__get_pet(DOGS_URL)
