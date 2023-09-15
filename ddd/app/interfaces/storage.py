from typing import Protocol


class StorageProtocol(Protocol):
    def session(self):
        pass
