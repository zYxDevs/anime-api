from dataclasses import dataclass
from datetime import datetime

import typing

from dateutil import parser

from anime_api.apis.nekos_api.types import NsfwLevel, ImageOrientation
from anime_api.utils import to_snake


@dataclass
class Artist:
    """
    Object representation of an artist
    """

    id: str
    name: str
    url: typing.Optional[str]
    images: typing.Optional[int] = None


@dataclass
class _Source:
    name: str
    url: str


@dataclass
class Category:
    """
    Object representation of a category
    """

    id: str
    name: str
    description: str
    nsfw: bool
    type: str
    created_at: datetime
    images: typing.Optional[int] = None


@dataclass
class Character:
    """
    Object representation of a character
    """

    id: str
    name: str
    description: str
    source: str
    created_at: datetime
    gender: typing.Optional[str]
    ages: typing.Optional[typing.List[int]]
    birth_date: typing.Optional[str]
    nationality: typing.Optional[str]
    occupations: typing.Optional[typing.List[str]]
    images: typing.Optional[int] = None


@dataclass
class _Dimens:
    height: int
    width: int
    aspect_ratio: str
    orientation: ImageOrientation

@dataclass
class Image:
    """
    Object representation of an image
    """

    id: str
    url: str
    artist: typing.Optional[Artist]
    source: typing.Optional[_Source]
    original: typing.Optional[bool]
    nsfw: NsfwLevel
    categories: typing.List[Category]
    characters: typing.List[Character]
    created_at: datetime
    etag: str
    size: int
    mimetype: str
    color: str
    expires: datetime
    dimens: _Dimens

    def from_json(self) -> 'Image':
        return Image(
            id=self["id"],
            url=self["url"],
            artist=Artist(**self["artist"]) if self["artist"] else None,
            source=_Source(**self["source"]) if self["source"] else None,
            original=self["original"],
            nsfw=NsfwLevel(self["nsfw"]),
            categories=[Category(**to_snake(c)) for c in data["categories"]],
            characters=[Character(**to_snake(c)) for c in data["characters"]],
            created_at=parser.parse(self["createdAt"]),
            etag=self["meta"]["eTag"],
            size=self["meta"]["size"],
            mimetype=self["meta"]["mimetype"],
            color=self["meta"]["color"],
            expires=parser.parse(self["meta"]["expires"]),
            dimens=_Dimens(
                height=self["meta"]["dimens"]["height"],
                width=self["meta"]["dimens"]["width"],
                aspect_ratio=self["meta"]["dimens"]["height"],
                orientation=ImageOrientation(
                    self["meta"]["dimens"]["orientation"]
                ),
            ),
        )
