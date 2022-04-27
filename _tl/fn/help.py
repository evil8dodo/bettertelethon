"""File generated by TLObjects' generator. All changes will be ERASED"""
from ..._misc.tlobject import TLObject, TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
import dataclasses
from datetime import datetime
if TYPE_CHECKING:
    from .. import TypeDataJSON, TypeInputAppEvent, TypeInputPeer, TypeInputUser, TypeMessageEntity



@dataclasses.dataclass(init=False, frozen=True)
class AcceptTermsOfService(TLRequest):
    """
    :returns Bool: This type has no constructors.
    """
    __slots__ = ('id',)
    CONSTRUCTOR_ID = 0xee72f79a
    SUBCLASS_OF_ID = 0xf5b399ac

    id: 'TypeDataJSON'
    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeDataJSON'):
        object.__setattr__(self, 'id', id)

    def _bytes(self):
        return b''.join((
            b'\x9a\xf7r\xee',
            self.id._bytes(),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _id = reader.tgread_object()
        return cls(id=_id)


@dataclasses.dataclass(init=False, frozen=True)
class DismissSuggestion(TLRequest):
    """
    :returns Bool: This type has no constructors.
    """
    __slots__ = ('peer', 'suggestion',)
    CONSTRUCTOR_ID = 0xf50dbaa1
    SUBCLASS_OF_ID = 0xf5b399ac

    peer: 'TypeInputPeer'
    suggestion: str
    def __init__(self, peer: 'TypeInputPeer', suggestion: str):
        object.__setattr__(self, 'peer', peer)
        object.__setattr__(self, 'suggestion', suggestion)

    async def _resolve(self, client, utils):
        r = {}
        r['peer'] = utils.get_input_peer(await client._get_input_peer(self.peer))
        return dataclasses.replace(self, **r)

    def _bytes(self):
        return b''.join((
            b'\xa1\xba\r\xf5',
            self.peer._bytes(),
            self._serialize_bytes(self.suggestion),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _peer = reader.tgread_object()
        _suggestion = reader.tgread_string()
        return cls(peer=_peer, suggestion=_suggestion)


@dataclasses.dataclass(init=False, frozen=True)
class EditUserInfo(TLRequest):
    """
    :returns help.UserInfo: Instance of either UserInfoEmpty, UserInfo.
    """
    __slots__ = ('user_id', 'message', 'entities',)
    CONSTRUCTOR_ID = 0x66b91b70
    SUBCLASS_OF_ID = 0x5c53d7d8

    user_id: 'TypeInputUser'
    message: str
    entities: List['TypeMessageEntity']
    def __init__(self, user_id: 'TypeInputUser', message: str, entities: List['TypeMessageEntity']):
        object.__setattr__(self, 'user_id', user_id)
        object.__setattr__(self, 'message', message)
        object.__setattr__(self, 'entities', entities)

    async def _resolve(self, client, utils):
        r = {}
        r['user_id'] = utils.get_input_user(await client._get_input_peer(self.user_id))
        return dataclasses.replace(self, **r)

    def _bytes(self):
        return b''.join((
            b'p\x1b\xb9f',
            self.user_id._bytes(),
            self._serialize_bytes(self.message),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.entities)),b''.join(x._bytes() for x in self.entities),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _user_id = reader.tgread_object()
        _message = reader.tgread_string()
        reader.read_int()
        _entities = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _entities.append(_x)

        return cls(user_id=_user_id, message=_message, entities=_entities)


@dataclasses.dataclass(init=False, frozen=True)
class GetAppChangelog(TLRequest):
    """
    :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
    """
    __slots__ = ('prev_app_version',)
    CONSTRUCTOR_ID = 0x9010ef6f
    SUBCLASS_OF_ID = 0x8af52aac

    prev_app_version: str
    def __init__(self, prev_app_version: str):
        object.__setattr__(self, 'prev_app_version', prev_app_version)

    def _bytes(self):
        return b''.join((
            b'o\xef\x10\x90',
            self._serialize_bytes(self.prev_app_version),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _prev_app_version = reader.tgread_string()
        return cls(prev_app_version=_prev_app_version)


@dataclasses.dataclass(init=False, frozen=True)
class GetAppConfig(TLRequest):
    """
    :returns JSONValue: Instance of either JsonNull, JsonBool, JsonNumber, JsonString, JsonArray, JsonObject.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x98914110
    SUBCLASS_OF_ID = 0xeb9987b3

    def _bytes(self):
        return b''.join((
            b'\x10A\x91\x98',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class GetAppUpdate(TLRequest):
    """
    :returns help.AppUpdate: Instance of either AppUpdate, NoAppUpdate.
    """
    __slots__ = ('source',)
    CONSTRUCTOR_ID = 0x522d5a7d
    SUBCLASS_OF_ID = 0x5897069e

    source: str
    def __init__(self, source: str):
        object.__setattr__(self, 'source', source)

    def _bytes(self):
        return b''.join((
            b'}Z-R',
            self._serialize_bytes(self.source),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _source = reader.tgread_string()
        return cls(source=_source)


@dataclasses.dataclass(init=False, frozen=True)
class GetCdnConfig(TLRequest):
    """
    :returns CdnConfig: Instance of CdnConfig.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x52029342
    SUBCLASS_OF_ID = 0xecda397c

    def _bytes(self):
        return b''.join((
            b'B\x93\x02R',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class GetConfig(TLRequest):
    """
    :returns Config: Instance of Config.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0xc4f9186b
    SUBCLASS_OF_ID = 0xd3262a4a

    def _bytes(self):
        return b''.join((
            b'k\x18\xf9\xc4',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class GetCountriesList(TLRequest):
    """
    :returns help.CountriesList: Instance of either CountriesListNotModified, CountriesList.
    """
    __slots__ = ('lang_code', 'hash',)
    CONSTRUCTOR_ID = 0x735787a8
    SUBCLASS_OF_ID = 0xea31fe88

    lang_code: str
    hash: int
    # noinspection PyShadowingBuiltins
    def __init__(self, lang_code: str, hash: int):
        object.__setattr__(self, 'lang_code', lang_code)
        object.__setattr__(self, 'hash', hash)

    def _bytes(self):
        return b''.join((
            b'\xa8\x87Ws',
            self._serialize_bytes(self.lang_code),
            struct.pack('<i', self.hash),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _lang_code = reader.tgread_string()
        _hash = reader.read_int()
        return cls(lang_code=_lang_code, hash=_hash)


@dataclasses.dataclass(init=False, frozen=True)
class GetDeepLinkInfo(TLRequest):
    """
    :returns help.DeepLinkInfo: Instance of either DeepLinkInfoEmpty, DeepLinkInfo.
    """
    __slots__ = ('path',)
    CONSTRUCTOR_ID = 0x3fedc75f
    SUBCLASS_OF_ID = 0x984aac38

    path: str
    def __init__(self, path: str):
        object.__setattr__(self, 'path', path)

    def _bytes(self):
        return b''.join((
            b'_\xc7\xed?',
            self._serialize_bytes(self.path),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _path = reader.tgread_string()
        return cls(path=_path)


@dataclasses.dataclass(init=False, frozen=True)
class GetInviteText(TLRequest):
    """
    :returns help.InviteText: Instance of InviteText.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x4d392343
    SUBCLASS_OF_ID = 0xcf70aa35

    def _bytes(self):
        return b''.join((
            b'C#9M',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class GetNearestDc(TLRequest):
    """
    :returns NearestDc: Instance of NearestDc.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x1fb33026
    SUBCLASS_OF_ID = 0x3877045f

    def _bytes(self):
        return b''.join((
            b'&0\xb3\x1f',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class GetPassportConfig(TLRequest):
    """
    :returns help.PassportConfig: Instance of either PassportConfigNotModified, PassportConfig.
    """
    __slots__ = ('hash',)
    CONSTRUCTOR_ID = 0xc661ad08
    SUBCLASS_OF_ID = 0xc666c0ad

    hash: int
    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        object.__setattr__(self, 'hash', hash)

    def _bytes(self):
        return b''.join((
            b'\x08\xada\xc6',
            struct.pack('<i', self.hash),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _hash = reader.read_int()
        return cls(hash=_hash)


@dataclasses.dataclass(init=False, frozen=True)
class GetPromoData(TLRequest):
    """
    :returns help.PromoData: Instance of either PromoDataEmpty, PromoData.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0xc0977421
    SUBCLASS_OF_ID = 0x9d595542

    def _bytes(self):
        return b''.join((
            b'!t\x97\xc0',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class GetRecentMeUrls(TLRequest):
    """
    :returns help.RecentMeUrls: Instance of RecentMeUrls.
    """
    __slots__ = ('referer',)
    CONSTRUCTOR_ID = 0x3dc0f114
    SUBCLASS_OF_ID = 0xf269c477

    referer: str
    def __init__(self, referer: str):
        object.__setattr__(self, 'referer', referer)

    def _bytes(self):
        return b''.join((
            b'\x14\xf1\xc0=',
            self._serialize_bytes(self.referer),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _referer = reader.tgread_string()
        return cls(referer=_referer)


@dataclasses.dataclass(init=False, frozen=True)
class GetSupport(TLRequest):
    """
    :returns help.Support: Instance of Support.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x9cdf08cd
    SUBCLASS_OF_ID = 0x7159bceb

    def _bytes(self):
        return b''.join((
            b'\xcd\x08\xdf\x9c',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class GetSupportName(TLRequest):
    """
    :returns help.SupportName: Instance of SupportName.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0xd360e72c
    SUBCLASS_OF_ID = 0x7f50b7c2

    def _bytes(self):
        return b''.join((
            b',\xe7`\xd3',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class GetTermsOfServiceUpdate(TLRequest):
    """
    :returns help.TermsOfServiceUpdate: Instance of either TermsOfServiceUpdateEmpty, TermsOfServiceUpdate.
    """
    __slots__ = ()
    CONSTRUCTOR_ID = 0x2ca51fd1
    SUBCLASS_OF_ID = 0x293c2977

    def _bytes(self):
        return b''.join((
            b'\xd1\x1f\xa5,',
        ))

    @classmethod
    def _from_reader(cls, reader):
        return cls()


@dataclasses.dataclass(init=False, frozen=True)
class GetUserInfo(TLRequest):
    """
    :returns help.UserInfo: Instance of either UserInfoEmpty, UserInfo.
    """
    __slots__ = ('user_id',)
    CONSTRUCTOR_ID = 0x38a08d3
    SUBCLASS_OF_ID = 0x5c53d7d8

    user_id: 'TypeInputUser'
    def __init__(self, user_id: 'TypeInputUser'):
        object.__setattr__(self, 'user_id', user_id)

    async def _resolve(self, client, utils):
        r = {}
        r['user_id'] = utils.get_input_user(await client._get_input_peer(self.user_id))
        return dataclasses.replace(self, **r)

    def _bytes(self):
        return b''.join((
            b'\xd3\x08\x8a\x03',
            self.user_id._bytes(),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _user_id = reader.tgread_object()
        return cls(user_id=_user_id)


@dataclasses.dataclass(init=False, frozen=True)
class HidePromoData(TLRequest):
    """
    :returns Bool: This type has no constructors.
    """
    __slots__ = ('peer',)
    CONSTRUCTOR_ID = 0x1e251c95
    SUBCLASS_OF_ID = 0xf5b399ac

    peer: 'TypeInputPeer'
    def __init__(self, peer: 'TypeInputPeer'):
        object.__setattr__(self, 'peer', peer)

    async def _resolve(self, client, utils):
        r = {}
        r['peer'] = utils.get_input_peer(await client._get_input_peer(self.peer))
        return dataclasses.replace(self, **r)

    def _bytes(self):
        return b''.join((
            b'\x95\x1c%\x1e',
            self.peer._bytes(),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


@dataclasses.dataclass(init=False, frozen=True)
class SaveAppLog(TLRequest):
    """
    :returns Bool: This type has no constructors.
    """
    __slots__ = ('events',)
    CONSTRUCTOR_ID = 0x6f02f748
    SUBCLASS_OF_ID = 0xf5b399ac

    events: List['TypeInputAppEvent']
    def __init__(self, events: List['TypeInputAppEvent']):
        object.__setattr__(self, 'events', events)

    def _bytes(self):
        return b''.join((
            b'H\xf7\x02o',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.events)),b''.join(x._bytes() for x in self.events),
        ))

    @classmethod
    def _from_reader(cls, reader):
        reader.read_int()
        _events = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _events.append(_x)

        return cls(events=_events)


@dataclasses.dataclass(init=False, frozen=True)
class SetBotUpdatesStatus(TLRequest):
    """
    :returns Bool: This type has no constructors.
    """
    __slots__ = ('pending_updates_count', 'message',)
    CONSTRUCTOR_ID = 0xec22cfcd
    SUBCLASS_OF_ID = 0xf5b399ac

    pending_updates_count: int
    message: str
    def __init__(self, pending_updates_count: int, message: str):
        object.__setattr__(self, 'pending_updates_count', pending_updates_count)
        object.__setattr__(self, 'message', message)

    def _bytes(self):
        return b''.join((
            b'\xcd\xcf"\xec',
            struct.pack('<i', self.pending_updates_count),
            self._serialize_bytes(self.message),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _pending_updates_count = reader.read_int()
        _message = reader.tgread_string()
        return cls(pending_updates_count=_pending_updates_count, message=_message)
