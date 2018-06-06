# ############################################################################# #
#  Automatically generated protobuf typings for python                          #
#   by protoc-gen-python-typings plugin for protoc                              #
# ############################################################################# #

from google.protobuf.message import Message
from google.protobuf.descriptor import FieldDescriptor
from typing import List, Union
from google.protobuf.internal.well_known_types import Timestamp

A: int = 0
B: int = 1
C: int = 3


class SimpleMessage(Message):
    class InnerMessage(Message):
        A: int = 0
        B: int = 1
        C: int = 3

        id: int = ...
        startFrom: Timestamp = ...
        enumField: int = ...

        def __init__(self,
                     id: int = None,
                     startFrom: Timestamp = None,
                     enumField: int = None):
            pass

        # region <<<Message Implementation>>>
        def __eq__(self, other_msg: 'SimpleMessage.InnerMessage') -> bool: ...
        def __str__(self) -> str: ...
        def __unicode__(self) -> str: ...
        def MergeFrom(self, other_msg: 'SimpleMessage.InnerMessage'): ...
        def Clear(self): ...
        def SetInParent(self): ...
        def IsInitialized(self) -> bool: ...
        def MergeFromString(self, serialized: str): ...
        def SerializeToString(self, **kwargs) -> str: ...
        def SerializePartialToString(self, **kwargs) -> str: ...
        def ListFields(self) -> List[FieldDescriptor]: ...
        def HasField(self, field_name: str) -> bool: ...
        def ClearField(self, field_name: str): ...
        def WhichOneof(self, oneof_group: str): ...
        def HasExtension(self, extension_handle: str) -> bool: ...
        def ClearExtension(self, extension_handle): ...
        def DiscardUnknownFields(self): ...
        def ByteSize(self) -> int: ...
        def _SetListener(self, message_listener): ...

        # endregion <<<Message Implementation>>>
        ...

    id: int = ...
    startFrom: Timestamp = ...
    until: Timestamp = ...
    enumField: List[int] = ...

    def __init__(self,
                 id: int = None,
                 startFrom: Timestamp = None,
                 until: Timestamp = None,
                 enumField: List[int] = None):
        pass

    # region <<<Message Implementation>>>
    def __eq__(self, other_msg: 'SimpleMessage') -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: 'SimpleMessage'): ...
    def Clear(self): ...
    def SetInParent(self): ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: str): ...
    def SerializeToString(self, **kwargs) -> str: ...
    def SerializePartialToString(self, **kwargs) -> str: ...
    def ListFields(self) -> List[FieldDescriptor]: ...
    def HasField(self, field_name: str) -> bool: ...
    def ClearField(self, field_name: str): ...
    def WhichOneof(self, oneof_group: str): ...
    def HasExtension(self, extension_handle: str) -> bool: ...
    def ClearExtension(self, extension_handle): ...
    def DiscardUnknownFields(self): ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener): ...

    # endregion <<<Message Implementation>>>
    ...
