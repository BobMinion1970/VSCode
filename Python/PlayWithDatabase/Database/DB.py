import sqlite3
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError("Singletons must be accessed through instance().")


@Singleton
class DBSingleton:
    _con: sqlite3.Connection = None
    _cursor: sqlite3.Cursor = None

    # Singleton part
    _instances = (
        {}
    )  # a private attribute is defined of type dictionary. It will hold only one instance!

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(
                *args, **kwargs
            )  # store the one and only!

        return cls._instance  # if the instance is in _instances dictionary return it

    # def __init__(self) -> None:
    def initDB(self):
        try:
            self._con = sqlite3.connect(
                Path(
                    "D:/Develop/Projects/TAT/VSCode/Python/PlayWithDatabase/PlayWithDatabase.db"
                )
            )
            self._cursor = self._con.cursor()
        except sqlite3.error as e:
            logger.debug(e)

    def execute(self, sqlstring: str):
        retval: sqlite3.Row = None
        try:
            self._cursor.execute(sqlstring)
            retval = self._cursor.fetchall()
        except sqlite3.Error as e:
            logger.Debug(e)
        
        return retval

    def commit(self):
        self._cursor.commit()
