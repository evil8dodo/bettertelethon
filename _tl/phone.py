"""File generated by TLObjects' generator. All changes will be ERASED"""
from .._misc.tlobject import TLObject, TLRequest
from . import fn
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
import dataclasses
from datetime import datetime
if TYPE_CHECKING:
    from . import TypeChat, TypeGroupCall, TypeGroupCallParticipant, TypeGroupCallStreamChannel, TypePeer, TypePhoneCall, TypeUser



@dataclasses.dataclass(init=False, frozen=True)
class ExportedGroupCallInvite(TLObject):
    """
    Constructor for phone.ExportedGroupCallInvite: Instance of ExportedGroupCallInvite.
    """
    __slots__ = ('link',)
    CONSTRUCTOR_ID = 0x204bd158
    SUBCLASS_OF_ID = 0x3b3bfe8f

    link: str
    def __init__(self, link: str):
        object.__setattr__(self, 'link', link)

    def _bytes(self):
        return b''.join((
            b'X\xd1K ',
            self._serialize_bytes(self.link),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _link = reader.tgread_string()
        return cls(link=_link)


@dataclasses.dataclass(init=False, frozen=True)
class GroupCall(TLObject):
    """
    Constructor for phone.GroupCall: Instance of GroupCall.
    """
    __slots__ = ('call', 'participants', 'participants_next_offset', 'chats', 'users',)
    CONSTRUCTOR_ID = 0x9e727aad
    SUBCLASS_OF_ID = 0x304116be

    call: 'TypeGroupCall'
    participants: List['TypeGroupCallParticipant']
    participants_next_offset: str
    chats: List['TypeChat']
    users: List['TypeUser']
    def __init__(self, call: 'TypeGroupCall', participants: List['TypeGroupCallParticipant'], participants_next_offset: str, chats: List['TypeChat'], users: List['TypeUser']):
        object.__setattr__(self, 'call', call)
        object.__setattr__(self, 'participants', participants)
        object.__setattr__(self, 'participants_next_offset', participants_next_offset)
        object.__setattr__(self, 'chats', chats)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'\xadzr\x9e',
            self.call._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.participants)),b''.join(x._bytes() for x in self.participants),
            self._serialize_bytes(self.participants_next_offset),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _call = reader.tgread_object()
        reader.read_int()
        _participants = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _participants.append(_x)

        _participants_next_offset = reader.tgread_string()
        reader.read_int()
        _chats = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _chats.append(_x)

        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(call=_call, participants=_participants, participants_next_offset=_participants_next_offset, chats=_chats, users=_users)


@dataclasses.dataclass(init=False, frozen=True)
class GroupCallStreamChannels(TLObject):
    """
    Constructor for phone.GroupCallStreamChannels: Instance of GroupCallStreamChannels.
    """
    __slots__ = ('channels',)
    CONSTRUCTOR_ID = 0xd0e482b2
    SUBCLASS_OF_ID = 0x9157c5e4

    channels: List['TypeGroupCallStreamChannel']
    def __init__(self, channels: List['TypeGroupCallStreamChannel']):
        object.__setattr__(self, 'channels', channels)

    def _bytes(self):
        return b''.join((
            b'\xb2\x82\xe4\xd0',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.channels)),b''.join(x._bytes() for x in self.channels),
        ))

    @classmethod
    def _from_reader(cls, reader):
        reader.read_int()
        _channels = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _channels.append(_x)

        return cls(channels=_channels)


@dataclasses.dataclass(init=False, frozen=True)
class GroupCallStreamRtmpUrl(TLObject):
    """
    Constructor for phone.GroupCallStreamRtmpUrl: Instance of GroupCallStreamRtmpUrl.
    """
    __slots__ = ('url', 'key',)
    CONSTRUCTOR_ID = 0x2dbf3432
    SUBCLASS_OF_ID = 0xd1f515cb

    url: str
    key: str
    def __init__(self, url: str, key: str):
        object.__setattr__(self, 'url', url)
        object.__setattr__(self, 'key', key)

    def _bytes(self):
        return b''.join((
            b'24\xbf-',
            self._serialize_bytes(self.url),
            self._serialize_bytes(self.key),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _url = reader.tgread_string()
        _key = reader.tgread_string()
        return cls(url=_url, key=_key)


@dataclasses.dataclass(init=False, frozen=True)
class GroupParticipants(TLObject):
    """
    Constructor for phone.GroupParticipants: Instance of GroupParticipants.
    """
    __slots__ = ('count', 'participants', 'next_offset', 'chats', 'users', 'version',)
    CONSTRUCTOR_ID = 0xf47751b6
    SUBCLASS_OF_ID = 0x72d304f4

    count: int
    participants: List['TypeGroupCallParticipant']
    next_offset: str
    chats: List['TypeChat']
    users: List['TypeUser']
    version: int
    def __init__(self, count: int, participants: List['TypeGroupCallParticipant'], next_offset: str, chats: List['TypeChat'], users: List['TypeUser'], version: int):
        object.__setattr__(self, 'count', count)
        object.__setattr__(self, 'participants', participants)
        object.__setattr__(self, 'next_offset', next_offset)
        object.__setattr__(self, 'chats', chats)
        object.__setattr__(self, 'users', users)
        object.__setattr__(self, 'version', version)

    def _bytes(self):
        return b''.join((
            b'\xb6Qw\xf4',
            struct.pack('<i', self.count),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.participants)),b''.join(x._bytes() for x in self.participants),
            self._serialize_bytes(self.next_offset),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
            struct.pack('<i', self.version),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _count = reader.read_int()
        reader.read_int()
        _participants = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _participants.append(_x)

        _next_offset = reader.tgread_string()
        reader.read_int()
        _chats = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _chats.append(_x)

        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        _version = reader.read_int()
        return cls(count=_count, participants=_participants, next_offset=_next_offset, chats=_chats, users=_users, version=_version)


@dataclasses.dataclass(init=False, frozen=True)
class JoinAsPeers(TLObject):
    """
    Constructor for phone.JoinAsPeers: Instance of JoinAsPeers.
    """
    __slots__ = ('peers', 'chats', 'users',)
    CONSTRUCTOR_ID = 0xafe5623f
    SUBCLASS_OF_ID = 0xb4b770fb

    peers: List['TypePeer']
    chats: List['TypeChat']
    users: List['TypeUser']
    def __init__(self, peers: List['TypePeer'], chats: List['TypeChat'], users: List['TypeUser']):
        object.__setattr__(self, 'peers', peers)
        object.__setattr__(self, 'chats', chats)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'?b\xe5\xaf',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.peers)),b''.join(x._bytes() for x in self.peers),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def _from_reader(cls, reader):
        reader.read_int()
        _peers = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _peers.append(_x)

        reader.read_int()
        _chats = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _chats.append(_x)

        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(peers=_peers, chats=_chats, users=_users)


@dataclasses.dataclass(init=False, frozen=True)
class PhoneCall(TLObject):
    """
    Constructor for phone.PhoneCall: Instance of PhoneCall.
    """
    __slots__ = ('phone_call', 'users',)
    CONSTRUCTOR_ID = 0xec82e140
    SUBCLASS_OF_ID = 0xd48afe4f

    phone_call: 'TypePhoneCall'
    users: List['TypeUser']
    def __init__(self, phone_call: 'TypePhoneCall', users: List['TypeUser']):
        object.__setattr__(self, 'phone_call', phone_call)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'@\xe1\x82\xec',
            self.phone_call._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _phone_call = reader.tgread_object()
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return cls(phone_call=_phone_call, users=_users)
