import sqlite3


class DBUtils:
    def __init__(self, name_db):
        self.con = sqlite3.connect(name_db)

    def create_execute(self, execute):
        cur = self.con.cursor()
        if execute[:6] == 'SELECT':
            return cur.execute(execute).fetchall()
        cur.execute(execute).fetchall()
        self.con.commit()

    def get_data(self, table, *args, **kwargs):
        cur = self.con.cursor()
        condition = ""
        if not args:
            args = "*"
        else:
            args = ', '.join(args)
        if kwargs:
            condition = "WHERE"
            for key, value in kwargs.items():
                condition += ' '
                condition += f"{key}={value}"
        request = f"SELECT {args} FROM {table} {condition}"
        return cur.execute(request).fetchall()

    def delete_genre(self, idd):
        cur = self.con.cursor()
        cur.execute(f"DELETE from genre WHERE id={idd}").fetchall()
        self.con.commit()

    def delete_cinema(self, name):
        cur = self.con.cursor()
        cur.execute(f"DELETE from cinema WHERE name='{name}'").fetchall()
        self.con.commit()

    def add_genre(self, title):
        cur = self.con.cursor()
        cur.execute(f"INSERT INTO genre(title) VALUES('{title}')").fetchall()
        self.con.commit()

    def add_film(self, name, genre, year, description, pathPici, pathCinema):
        cur = self.con.cursor()
        data = [name, genre, year, description, pathPici, pathCinema]
        cur.execute("INSERT INTO cinema(name, genre, year, description, pathPici, pathCinema) VALUES(?,?,?,?,?,?)",
                    data).fetchall()
        self.con.commit()

    def update_genre(self, idd, title):
        cur = self.con.cursor()
        cur.execute(f"""UPDATE genre SET title = '{title}' WHERE id = {idd}""", ).fetchall()
        self.con.commit()

    def check_film_name(self, name):
        names = [i[0] for i in self.get_data('cinema', 'name')]
        return names.count(name)

    def close(self):
        self.con.close()


def kwargs_to_lists(**kwargs):
    names_list = []
    data_list = []
    for key, value in kwargs.items():
        names_list.append(key)
        data_list.append(str(value))
    return names_list, data_list


def get_file_ex(path):
    return path.split(".")[-1]
