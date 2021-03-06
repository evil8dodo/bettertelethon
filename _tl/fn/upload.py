"""File generated by TLObjects' generator. All changes will be ERASED"""
from ..._misc.tlobject import TLObject, TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
import dataclasses
from datetime import datetime
if TYPE_CHECKING:
    from .. import TypeInputFileLocation, TypeInputWebFileLocation



@dataclasses.dataclass(init=False, frozen=True)
class GetCdnFile(TLRequest):
    """
    :returns upload.CdnFile: Instance of either CdnFileReuploadNeeded, CdnFile.
    """
    __slots__ = ('file_token', 'offset', 'limit',)
    CONSTRUCTOR_ID = 0x2000bcc3
    SUBCLASS_OF_ID = 0xf5ccf928

    file_token: bytes
    offset: int
    limit: int
    def __init__(self, file_token: bytes, offset: int, limit: int):
        object.__setattr__(self, 'file_token', file_token)
        object.__setattr__(self, 'offset', offset)
        object.__setattr__(self, 'limit', limit)

    def _bytes(self):
        return b''.join((
            b'\xc3\xbc\x00 ',
            self._serialize_bytes(self.file_token),
            struct.pack('<i', self.offset),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _file_token = reader.tgread_bytes()
        _offset = reader.read_int()
        _limit = reader.read_int()
        return cls(file_token=_file_token, offset=_offset, limit=_limit)


@dataclasses.dataclass(init=False, frozen=True)
class GetCdnFileHashes(TLRequest):
    """
    :returns Vector<FileHash>: This type has no constructors.
    """
    __slots__ = ('file_token', 'offset',)
    CONSTRUCTOR_ID = 0x4da54231
    SUBCLASS_OF_ID = 0xa5940726

    file_token: bytes
    offset: int
    def __init__(self, file_token: bytes, offset: int):
        object.__setattr__(self, 'file_token', file_token)
        object.__setattr__(self, 'offset', offset)

    def _bytes(self):
        return b''.join((
            b'1B\xa5M',
            self._serialize_bytes(self.file_token),
            struct.pack('<i', self.offset),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _file_token = reader.tgread_bytes()
        _offset = reader.read_int()
        return cls(file_token=_file_token, offset=_offset)


@dataclasses.dataclass(init=False, frozen=True)
class GetFile(TLRequest):
    """
    :returns upload.File: Instance of either File, FileCdnRedirect.
    """
    __slots__ = ('location', 'offset', 'limit', 'precise', 'cdn_supported',)
    CONSTRUCTOR_ID = 0xb15a9afc
    SUBCLASS_OF_ID = 0x6c9bd728

    location: 'TypeInputFileLocation'
    offset: int
    limit: int
    precise: Optional[bool]
    cdn_supported: Optional[bool]
    def __init__(self, location: 'TypeInputFileLocation', offset: int, limit: int, precise: Optional[bool]=None, cdn_supported: Optional[bool]=None):
        object.__setattr__(self, 'location', location)
        object.__setattr__(self, 'offset', offset)
        object.__setattr__(self, 'limit', limit)
        object.__setattr__(self, 'precise', precise)
        object.__setattr__(self, 'cdn_supported', cdn_supported)

    def _bytes(self):
        return b''.join((
            b'\xfc\x9aZ\xb1',
            struct.pack('<I', (0 if self.precise is None or self.precise is False else 1) | (0 if self.cdn_supported is None or self.cdn_supported is False else 2)),
            self.location._bytes(),
            struct.pack('<i', self.offset),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def _from_reader(cls, reader):
        flags = reader.read_int()

        _precise = bool(flags & 1)
        _cdn_supported = bool(flags & 2)
        _location = reader.tgread_object()
        _offset = reader.read_int()
        _limit = reader.read_int()
        return cls(location=_location, offset=_offset, limit=_limit, precise=_precise, cdn_supported=_cdn_supported)


@dataclasses.dataclass(init=False, frozen=True)
class GetFileHashes(TLRequest):
    """
    :returns Vector<FileHash>: This type has no constructors.
    """
    __slots__ = ('location', 'offset',)
    CONSTRUCTOR_ID = 0xc7025931
    SUBCLASS_OF_ID = 0xa5940726

    location: 'TypeInputFileLocation'
    offset: int
    def __init__(self, location: 'TypeInputFileLocation', offset: int):
        object.__setattr__(self, 'location', location)
        object.__setattr__(self, 'offset', offset)

    def _bytes(self):
        return b''.join((
            b'1Y\x02\xc7',
            self.location._bytes(),
            struct.pack('<i', self.offset),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _location = reader.tgread_object()
        _offset = reader.read_int()
        return cls(location=_location, offset=_offset)


@dataclasses.dataclass(init=False, frozen=True)
class GetWebFile(TLRequest):
    """
    :returns upload.WebFile: Instance of WebFile.
    """
    __slots__ = ('location', 'offset', 'limit',)
    CONSTRUCTOR_ID = 0x24e6818d
    SUBCLASS_OF_ID = 0x68f17f51

    location: 'TypeInputWebFileLocation'
    offset: int
    limit: int
    def __init__(self, location: 'TypeInputWebFileLocation', offset: int, limit: int):
        object.__setattr__(self, 'location', location)
        object.__setattr__(self, 'offset', offset)
        object.__setattr__(self, 'limit', limit)

    def _bytes(self):
        return b''.join((
            b'\x8d\x81\xe6$',
            self.location._bytes(),
            struct.pack('<i', self.offset),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _location = reader.tgread_object()
        _offset = reader.read_int()
        _limit = reader.read_int()
        return cls(location=_location, offset=_offset, limit=_limit)


@dataclasses.dataclass(init=False, frozen=True)
class ReuploadCdnFile(TLRequest):
    """
    :returns Vector<FileHash>: This type has no constructors.
    """
    __slots__ = ('file_token', 'request_token',)
    CONSTRUCTOR_ID = 0x9b2754a8
    SUBCLASS_OF_ID = 0xa5940726

    file_token: bytes
    request_token: bytes
    def __init__(self, file_token: bytes, request_token: bytes):
        object.__setattr__(self, 'file_token', file_token)
        object.__setattr__(self, 'request_token', request_token)

    def _bytes(self):
        return b''.join((
            b"\xa8T'\x9b",
            self._serialize_bytes(self.file_token),
            self._serialize_bytes(self.request_token),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _file_token = reader.tgread_bytes()
        _request_token = reader.tgread_bytes()
        return cls(file_token=_file_token, request_token=_request_token)


@dataclasses.dataclass(init=False, frozen=True)
class SaveBigFilePart(TLRequest):
    """
    :returns Bool: This type has no constructors.
    """
    __slots__ = ('file_id', 'file_part', 'file_total_parts', 'bytes',)
    CONSTRUCTOR_ID = 0xde7b673d
    SUBCLASS_OF_ID = 0xf5b399ac

    file_id: int
    file_part: int
    file_total_parts: int
    bytes: bytes
    # noinspection PyShadowingBuiltins
    def __init__(self, file_id: int, file_part: int, file_total_parts: int, bytes: bytes):
        object.__setattr__(self, 'file_id', file_id)
        object.__setattr__(self, 'file_part', file_part)
        object.__setattr__(self, 'file_total_parts', file_total_parts)
        object.__setattr__(self, 'bytes', bytes)

    def _bytes(self):
        return b''.join((
            b'=g{\xde',
            struct.pack('<q', self.file_id),
            struct.pack('<i', self.file_part),
            struct.pack('<i', self.file_total_parts),
            self._serialize_bytes(self.bytes),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _file_id = reader.read_long()
        _file_part = reader.read_int()
        _file_total_parts = reader.read_int()
        _bytes = reader.tgread_bytes()
        return cls(file_id=_file_id, file_part=_file_part, file_total_parts=_file_total_parts, bytes=_bytes)


@dataclasses.dataclass(init=False, frozen=True)
class SaveFilePart(TLRequest):
    """
    :returns Bool: This type has no constructors.
    """
    __slots__ = ('file_id', 'file_part', 'bytes',)
    CONSTRUCTOR_ID = 0xb304a621
    SUBCLASS_OF_ID = 0xf5b399ac

    file_id: int
    file_part: int
    bytes: bytes
    # noinspection PyShadowingBuiltins
    def __init__(self, file_id: int, file_part: int, bytes: bytes):
        object.__setattr__(self, 'file_id', file_id)
        object.__setattr__(self, 'file_part', file_part)
        object.__setattr__(self, 'bytes', bytes)

    def _bytes(self):
        return b''.join((
            b'!\xa6\x04\xb3',
            struct.pack('<q', self.file_id),
            struct.pack('<i', self.file_part),
            self._serialize_bytes(self.bytes),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _file_id = reader.read_long()
        _file_part = reader.read_int()
        _bytes = reader.tgread_bytes()
        return cls(file_id=_file_id, file_part=_file_part, bytes=_bytes)

