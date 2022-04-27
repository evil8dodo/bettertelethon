"""File generated by TLObjects' generator. All changes will be ERASED"""
from .._misc.tlobject import TLObject, TLRequest
from . import fn
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
import dataclasses
from datetime import datetime
if TYPE_CHECKING:
    from . import TypeChannelAdminLogEvent, TypeChannelParticipant, TypeChat, TypePeer, TypeUser



@dataclasses.dataclass(init=False, frozen=True)
class AdminLogResults(TLObject):
    """
    Constructor for channels.AdminLogResults: Instance of AdminLogResults.
    """
    __slots__ = ('events', 'chats', 'users',)
    CONSTRUCTOR_ID = 0xed8af74d
    SUBCLASS_OF_ID = 0x51f076bc

    events: List['TypeChannelAdminLogEvent']
    chats: List['TypeChat']
    users: List['TypeUser']
    def __init__(self, events: List['TypeChannelAdminLogEvent'], chats: List['TypeChat'], users: List['TypeUser']):
        object.__setattr__(self, 'events', events)
        object.__setattr__(self, 'chats', chats)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'M\xf7\x8a\xed',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.events)),b''.join(x._bytes() for x in self.events),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def _from_reader(cls, reader):
        reader.read_int()
        _events = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _events.append(_x)

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

        return cls(events=_events, chats=_chats, users=_users)


@dataclasses.dataclass(init=False, frozen=True)
class ChannelParticipant(TLObject):
    """
    Constructor for channels.ChannelParticipant: Instance of ChannelParticipant.
    """
    __slots__ = ('participant', 'chats', 'users',)
    CONSTRUCTOR_ID = 0xdfb80317
    SUBCLASS_OF_ID = 0x6658151a

    participant: 'TypeChannelParticipant'
    chats: List['TypeChat']
    users: List['TypeUser']
    def __init__(self, participant: 'TypeChannelParticipant', chats: List['TypeChat'], users: List['TypeUser']):
        object.__setattr__(self, 'participant', participant)
        object.__setattr__(self, 'chats', chats)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'\x17\x03\xb8\xdf',
            self.participant._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _participant = reader.tgread_object()
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

        return cls(participant=_participant, chats=_chats, users=_users)


@dataclasses.dataclass(init=False, frozen=True)
class ChannelParticipants(TLObject):
    """
    Constructor for channels.ChannelParticipants: Instance of either ChannelParticipants, ChannelParticipantsNotModified.
    """
    __slots__ = ('count', 'participants', 'chats', 'users',)
    CONSTRUCTOR_ID = 0x9ab0feaf
    SUBCLASS_OF_ID = 0xe60a6e64

    count: int
    participants: List['TypeChannelParticipant']
    chats: List['TypeChat']
    users: List['TypeUser']
    def __init__(self, count: int, participants: List['TypeChannelParticipant'], chats: List['TypeChat'], users: List['TypeUser']):
        object.__setattr__(self, 'count', count)
        object.__setattr__(self, 'participants', participants)
        object.__setattr__(self, 'chats', chats)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'\xaf\xfe\xb0\x9a',
            struct.pack('<i', self.count),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.participants)),b''.join(x._bytes() for x in self.participants),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _count = reader.read_int()
        reader.read_int()
        _participants = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _participants.append(_x)

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

        return cls(count=_count, participants=_participants, chats=_chats, users=_users)


@dataclasses.dataclass(init=False, frozen=True)
class ChannelParticipantsNotModified(TLObject):
    """
    Constructor for channels.ChannelParticipants: Instance of either ChannelParticipants, ChannelParticipantsNotModified.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0xf0173fe9
    SUBCLASS_OF_ID = 0xe60a6e64

    def _bytes(self):
        return b''.join((
            b'\xe9?\x17\xf0',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class SendAsPeers(TLObject):
    """
    Constructor for channels.SendAsPeers: Instance of SendAsPeers.
    """
    __slots__ = ('peers', 'chats', 'users',)
    CONSTRUCTOR_ID = 0x8356cda9
    SUBCLASS_OF_ID = 0x38cb8d21

    peers: List['TypePeer']
    chats: List['TypeChat']
    users: List['TypeUser']
    def __init__(self, peers: List['TypePeer'], chats: List['TypeChat'], users: List['TypeUser']):
        object.__setattr__(self, 'peers', peers)
        object.__setattr__(self, 'chats', chats)
        object.__setattr__(self, 'users', users)

    def _bytes(self):
        return b''.join((
            b'\xa9\xcdV\x83',
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

