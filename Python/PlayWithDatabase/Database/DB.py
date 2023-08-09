import sqlite3

class DB:
    def __init(self) -> None:
        self._connection = sqlite3.connect("E:\Develop\Projects\TAT\VSCode\Python\PlayWithDatabase\PlayWithDatabase")
        self._cursor = _connection.cursor