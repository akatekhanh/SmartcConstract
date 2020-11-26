from iconservice import *
TAG = 'LifeCycle'
class HelloWord(IconScoreBase):
    _NAME = "name"
    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._name = VarDB(self._NAME, self.db, str)
    def on_install(self) -> None:
        super().on_install()
        self._name.set("akatekhanh")
    def on_update(self) -> None:
        super().on_update()
        self._name.set("Updated to akateKhanh")
    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return f"Hello {self._name.get()}"