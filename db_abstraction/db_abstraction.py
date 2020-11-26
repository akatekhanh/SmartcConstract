from iconservice import *
TAG = 'DBAbstraction'
class DBAbstraction(IconScoreBase):
    _NAME = "name"
    _ARRAY_DB_SAMPLE = "array_db_sample"
    _DICT_DB_SAMPLE = "dict_db_sample"
    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._name = VarDB(self._NAME, db, str)
        self._array_db = ArrayDB(self._ARRAY_DB_SAMPLE, db, str)
        self._dict_db = DictDB(self._DICT_DB_SAMPLE, db, str)
    def on_install(self) -> None:
        super().on_install()
        self._name.set("beomkyu")
        self._dict_db["BTC"] = "Bitcoin"
        self._array_db.put("BTC")
        self._dict_db["ETH"] = "Ethereum"
        self._array_db.put("ETH")
        self._dict_db["ICX"] = "ICON"
        self._array_db.put("ICX")
        self._dict_db["EOS"] = "EOS"
        self._array_db.put("EOS")
    def on_update(self) -> None:
        super().on_update()
    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        owner = self._name.get()
        elements = [(el, self._dict_db[el]) for el in self._array_db]
        return f"{owner}, {elements}"