"""File generated by TLObjects' generator. All changes will be ERASED"""
from ..._misc.tlobject import TLObject, TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
import dataclasses
from datetime import datetime
if TYPE_CHECKING:
    from .. import TypeInputFolderPeer



@dataclasses.dataclass(init=False, frozen=True)
class DeleteFolder(TLRequest):
    """
    :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
    """
    __slots__ = ('folder_id',)
    CONSTRUCTOR_ID = 0x1c295881
    SUBCLASS_OF_ID = 0x8af52aac

    folder_id: int
    def __init__(self, folder_id: int):
        object.__setattr__(self, 'folder_id', folder_id)

    def _bytes(self):
        return b''.join((
            b'\x81X)\x1c',
            struct.pack('<i', self.folder_id),
        ))

    @classmethod
    def _from_reader(cls, reader):
        _folder_id = reader.read_int()
        return cls(folder_id=_folder_id)


@dataclasses.dataclass(init=False, frozen=True)
class EditPeerFolders(TLRequest):
    """
    :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
    """
    __slots__ = ('folder_peers',)
    CONSTRUCTOR_ID = 0x6847d0ab
    SUBCLASS_OF_ID = 0x8af52aac

    folder_peers: List['TypeInputFolderPeer']
    def __init__(self, folder_peers: List['TypeInputFolderPeer']):
        object.__setattr__(self, 'folder_peers', folder_peers)

    def _bytes(self):
        return b''.join((
            b'\xab\xd0Gh',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.folder_peers)),b''.join(x._bytes() for x in self.folder_peers),
        ))

    @classmethod
    def _from_reader(cls, reader):
        reader.read_int()
        _folder_peers = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _folder_peers.append(_x)

        return cls(folder_peers=_folder_peers)

