from iconservice import *
TAG = 'TryEventlog'
class TryEventlog(IconScoreBase):
    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._owner_name = VarDB("owner_name", db, str)
    def on_install(self) -> None:
        super().on_install()
        self._owner_name.set("Bumkyu")
    def on_update(self) -> None:
        super().on_update()
    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "Hello"
    @external(readonly=True)
    def getOwnerName(self) -> str:
        return self._owner_name.get()
    @external
    def setOwnerName(self, owner_name: str):
        self._owner_name.set(owner_name)
        self.OwnerNameChanged(owner_name)
    @eventlog
    def OwnerNameChanged(self, owner_name: str):
        pass    