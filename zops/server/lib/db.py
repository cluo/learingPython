#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'linzhonghong'
import pymysql
from util import mysql_opts
from mylog import init_sql_logger

sqllog = init_sql_logger('execsql', './logs/')

class DB(object):

    def __init__(self, cursorclass=pymysql.cursors.Cursor, conn=None):
        self.opts = mysql_opts()
        self.cursorclass = cursorclass
        self.res = None
        self.queries = [""]
        self.save_queries = True
        self.error_msg = None
        if conn is None:
            try:
                self.conn = pymysql.connect(cursorclass=cursorclass, **self.opts)
            except:
                self.conn = None
        else:
            self.conn = conn

    def connect(self):
        self.res = None
        self.queries = [""]
        self.save_queries = True
        self.error_msg = None
        try:
            self.conn = pymysql.connect(cursorclass=self.cursorclass, **self.opts)
        except:
            self.conn = None
        return self

    def close(self):
        self.queries = [""]
        self.conn.close()

    def select_db(self, db=None):
        if db is not None:
            self.conn.select_db(db)

    def close_conn(self):
        self.queries = [""]
        self.conn.close()

    def get_fields(self, table=None):
        if table is None:
            return False
        cur = self.conn.cursor()
        try:
            cur.execute('SHOW FIELDS FROM %s' % table)
        except Exception, e:
            self.error_msg = e
            return False
        return cur.fetchall()

    def execute(self, sqlstr, autolog=True):
        return self.conn.cursor().execute(sqlstr)

    def exec_sql(self, sqlstr, autolog=True):
        self.error_msg = None
        if not self.conn:
            return False
        error = False
        count = 0
        sqltype =sqlstr[0:6].lower()
        cur = self.conn.cursor()
        try:
            if self.save_queries:
                # self.queries.append(sqlstr)
                self.queries[0] = sqlstr
            if autolog is True:
                sqllog.info(sqlstr)
            count = cur.execute(sqlstr)
        except Exception, e:
            error = True
            self.error_msg = e
        if sqltype == 'select':
            if count == 0 or error:
                cur.close()
                self.res = False
                return False
            else:
                ret_list = cur.fetchall()
                cur.close()
                self.res = ret_list
                return ret_list
        elif sqltype == 'update' or sqltype == 'insert' or sqltype == 'delete':
            cur.close()
            if count == 0 or error:
                self.res = False
                return False
            else:
                self.res = True
                return True

    def last_query(self):
        return self.queries[-1]

    def result(self):
        return self.res

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()


class MysqlHandler(object):
    def __init__(self):
        self.opts = mysql_opts()
        self.res = None

    def conn_db(self):
        try:
            conn = pymysql.connect(**self.opts)
        except:
            return None
        return conn

    def close_conn(self, conn):
        conn.close()

    def exec_sql(self, sqlstr, conn):
        error = False
        count = 0
        sqltype =sqlstr[0:6].lower()
        cur = conn.cursor()
        try:
            count = cur.execute(sqlstr)
        except:
            error = True
        if sqltype == 'select':
            if count == 0 or error:
                cur.close()
                self.res = False
                return False
            else:
                ret_list = cur.fetchall()
                cur.close()
                self.res = ret_list
                return ret_list
        elif sqltype == 'update' or sqltype == 'insert' or sqltype == 'delete':
            cur.close()
            if error:
                self.res = False
                return False
            else:
                self.res = True
                return True

    def result(self):
        return self.res