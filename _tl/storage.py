"""File generated by TLObjects' generator. All changes will be ERASED"""
from .._misc.tlobject import TLObject, TLRequest
from . import fn
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
import dataclasses
from datetime import datetime


@dataclasses.dataclass(init=False, frozen=True)
class FileGif(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0xcae1aadf
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'\xdf\xaa\xe1\xca',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class FileJpeg(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x7efe0e
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'\x0e\xfe~\x00',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class FileMov(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x4b09ebbc
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'\xbc\xeb\tK',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class FileMp3(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x528a0677
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'w\x06\x8aR',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class FileMp4(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0xb3cea0e4
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'\xe4\xa0\xce\xb3',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class FilePartial(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x40bc6f52
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'Ro\xbc@',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class FilePdf(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0xae1e508d
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'\x8dP\x1e\xae',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class FilePng(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0xa4f63c0
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'\xc0cO\n',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class FileUnknown(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0xaa963b05
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'\x05;\x96\xaa',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class FileWebp(TLObject):
    """
    Constructor for storage.FileType: Instance of either FileUnknown, FilePartial, FileJpeg, FileGif, FilePng, FilePdf, FileMp3, FileMov, FileMp4, FileWebp.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x1081464c
    SUBCLASS_OF_ID = 0xf3a1e6f3

    def _bytes(self):
        return b''.join((
            b'LF\x81\x10',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()

