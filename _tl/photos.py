"""File generated by TLObjects' generator. All changes will be ERASED"""
from .._misc.tlobject import TLObject, TLRequest
from . import fn
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
import dataclasses
from datetime import datetime
if TYPE_CHECKING:
    from . import TypePhoto, TypeUser



@dataclasses.dataclass(init=False, frozen=True)
class Photo(TLObject):
    """
    Constructor for photos.Photo: Instance of Photo.
    """
    __slots__ = ('photo', 'users',)
    CONSTRUCTOR_ID = 0x20212ca8
    SUBCLASS_OF_ID = 0xc292bd24

    photo: 'TypePhoto'
    users: List['TypeUser']
    def __init__(self, photo: 'TypePhoto', users: List['TypeUser']):
        object.__setattr__(self, 'photo', photo)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'\xa8,! ',
            self.photo._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _photo = reader.tgread_object()
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(photo=_photo, users=_users)


@dataclasses.dataclass(init=False, frozen=True)
class Photos(TLObject):
    """
    Constructor for photos.Photos: Instance of either Photos, PhotosSlice.
    """
    __slots__ = ('photos', 'users',)
    CONSTRUCTOR_ID = 0x8dca6aa5
    SUBCLASS_OF_ID = 0x27cfb967

    photos: List['TypePhoto']
    users: List['TypeUser']
    def __init__(self, photos: List['TypePhoto'], users: List['TypeUser']):
        object.__setattr__(self, 'photos', photos)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'\xa5j\xca\x8d',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.photos)),b''.join(x._bytes() for x in self.photos),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def _from_reader(cls, reader):
        reader.read_int()
        _photos = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _photos.append(_x)

        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(photos=_photos, users=_users)


@dataclasses.dataclass(init=False, frozen=True)
class PhotosSlice(TLObject):
    """
    Constructor for photos.Photos: Instance of either Photos, PhotosSlice.
    """
    __slots__ = ('count', 'photos', 'users',)
    CONSTRUCTOR_ID = 0x15051f54
    SUBCLASS_OF_ID = 0x27cfb967

    count: int
    photos: List['TypePhoto']
    users: List['TypeUser']
    def __init__(self, count: int, photos: List['TypePhoto'], users: List['TypeUser']):
        object.__setattr__(self, 'count', count)
        object.__setattr__(self, 'photos', photos)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'T\x1f\x05\x15',
            struct.pack('<i', self.count),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.photos)),b''.join(x._bytes() for x in self.photos),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _count = reader.read_int()
        reader.read_int()
        _photos = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _photos.append(_x)

        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(count=_count, photos=_photos, users=_users)
