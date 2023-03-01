from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Elemento(_message.Message):
    __slots__ = ["descripcion", "id"]
    DESCRIPCION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    descripcion: str
    id: int
    def __init__(self, id: _Optional[int] = ..., descripcion: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListadoElementos(_message.Message):
    __slots__ = ["objetos"]
    OBJETOS_FIELD_NUMBER: _ClassVar[int]
    objetos: _containers.RepeatedCompositeFieldContainer[Elemento]
    def __init__(self, objetos: _Optional[_Iterable[_Union[Elemento, _Mapping]]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
