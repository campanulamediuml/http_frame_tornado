from pymongo import DESCENDING
from config import config
from pymongo import MongoClient
import json
import time
from datetime import datetime


class dbapi(object):
    mongodb = MongoClient(config.mongo_address,connect=False)
    mongodb_wst = MongoClient(config.mongo_address,connect=False)

    @staticmethod
    def mongo_dict_filter(d):
        if "_id" in d:
            d.pop("_id")
        for k in d:
            if isinstance(d[k], datetime):
                d[k] = int(d[k].timestamp())
        return d

    @staticmethod
    def get_cws_device_status(imei):
        # 查询机器
        return dbapi.mongodb.cws.device_status.find_one({'imei': imei})

    @staticmethod
    def get_cws_device_status_numbers(imeis, online):
        # online 0离线 1在线 4关机
        query = {'imei': {'$in': imeis}, 'online': online}
        return dbapi.mongodb.cws.device_status.find(query).count()

    @staticmethod
    def insert_datagram(data):
        data['time'] = datetime.now()
        dbapi.mongodb.mafu.datagram.insert_one(data)
        print('插入通讯记录')

    @staticmethod
    def fetch_datagram(dbtype, imei, page=1, psize=10, **kwargs):
        query = {'imei': imei}
        if 'start' in kwargs and 'end' in kwargs:
            query['time'] = {"$gte": kwargs['start'], "$lte": kwargs['end']}
        if 'datagram_type' in kwargs:
            query['datagram_type'] = kwargs['datagram_type']

        if dbtype == 1:
            mdb = dbapi.mongodb
        elif dbtype == 2:
            mdb = dbapi.mongodb_wst
        else:
            print('unkown db type: %d' % dbtype)
            return 0, []

        page = int(page)
        psize = int(psize)
        count = mdb.mafu.datagram.find(query).count()
        datagrams = mdb.mafu.datagram.find(query).skip(psize*(page-1)).limit(psize).sort("time", DESCENDING)
        datagrams = list(map(mongo_dict_filter, list(datagrams)))

        return count, datagrams







