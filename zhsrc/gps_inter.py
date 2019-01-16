#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
#   @File   : gps_inter.py
#   @Author : wmy
#   @Date   : 2018/2/2
#
#   format:
#   $GPGGA,031351.000,3355.3471,N,11741.7128,W,1,07,1.4,112.2,M,-33.7,M,,0000*6C 用这个
# ------------------------------------------------------------
class Gps:
    gps_dict = {
        'form': 0,
        'utc_time': 1,
        'lat': 2,
        'lat_hemi': 3,
        'long': 4,
        'long_hemi': 5,
        'pos_active': 6,
        'sate_num': 7,
        'sa': 8,
        'hoafsl': 9,
        'geohei': 10,
        'rtcm': 11,
        'label': 12
    }
    gps_init_data = ""

    def __init__(self):
        pass

    def __init__(self, gps_data= None):
        pass
        self.gps_init_data = gps_data

    def getPos(self):
        gpsDataList = self.gps_init_data.split(',')
        print(gpsDataList)
        if gpsDataList[0] == "$GPGGA":
            pass
            self.gps_dict = dict(zip(self.gps_dict.keys(), gpsDataList))
        else:
            print("the GPS data is invalid")
        return gpsDataList

    def disInfo(self):
        print("----------GPS original information--------")
        print(gps_test_data)
        print("----------invalid GPS data as follows-------------")
        for i in self.gps_dict:
            print("-> %s: %s" % (i, self.gps_dict[i]))
# --------------------------------------------------------------------
#
# test gps data
gps_test_data = "$GPGGA,031351.000,3355.3471,N,11741.7128,W,1,07,1.4,112.2,M,-33.7,M,,0000*6C "
gps = Gps(gps_test_data)
gps.getPos()
gps.disInfo()
