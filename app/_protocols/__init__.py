import typing

T = typing.TypeVar('T')

class Observer(typing.Protocol):
    
    def update(self, payload:T) -> None:
        ...

class Observable(typing.Protocol):
    
    def register(self, obs: Observer):
        ...
        
    def deregister(self, obs: Observer):
        ...
        
    def update(self):
        ...
    