__author__ = 'baza'

import os
from autofootball.langtools import cached_property

import sqlite3


class FootballDb():
    DB_FILE = 'football.db'

    @cached_property
    def connection(self):
        return sqlite3.connect(self.DB_FILE)

    @cached_property
    def cursor(self):
        cursor = self.connection.cursor()
        if self.need_init:
            self.reinit(cursor)

        return cursor

    def reinit(self, cursor=None):
        if not cursor:
            cursor = self.cursor

        cursor.execute(
            '''CREATE TABLE lines
               (id int, field_id, latitude real, longitude real, x int, y int)'''
        )

        cursor.execute(
            '''CREATE TABLE fields
               (id int, name text, left_goals int, right_goals int, country_goals text)'''
        )

    def add_visit(self, field_name, latitude, longitude, x, y):
        pass

    def update_field(self, name, left_goals_inc=False, right_goals_inc=False, country_goals=None):
        pass

    def __init__(self):
        self.need_init = not os.path.exists(self.DB_FILE)