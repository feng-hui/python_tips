# -*- coding: utf-8 -*-
import time
__author__ = 'Feng_hui'
__time__ = '2018/1/27 9:59'
__introduction__ = '使用time库返回各种不同格式或类型的时间'


class CommonTime(object):
    """
    返回时间的各种格式,包括但不限于时间戳、年月日时分秒、格式化的字符串时间、
    字符串时间与时间戳等多种格式之间的转换等
    """

    @staticmethod
    def get_timestamp(is_integer=None):
        """
        :return 默认返回当前时间的时间戳,格式为浮点数(例如:1517019311.778607)
                 当is_integer的值合法的情况下,返回整数格式的时间戳(例如:1517019311(10位))
        """
        if not is_integer:
            return time.time()
        else:
            return int(time.time())

    def timestamp_of_anytime(self, str_time):
        """
        :return: 返回任意时间的时间戳,默认返回浮点数
        """
        assert isinstance(str_time, str)
        time_stamp = self.t_tuple(str_time)
        return time.mktime(time_stamp)

    @staticmethod
    def t_tuple(str_time):
        """
        :param str_time: 字符串形式的时间,返回时间元组格式的时间
        :return: 
        """
        if '00:00:00' not in str_time:
            str_time += ' 00:00:00'
        return time.strptime(str_time, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def t_tuple_now(seconds=None):
        """
        :param seconds: 时间戳
        :return: 默认返回当前时间的时间元组
        """
        return time.localtime(seconds)

    @staticmethod
    def tuple_to_str(t_tuple, date_format=1):
        if date_format == 1:
            return time.strftime('%Y-%m-%d %H:%M:%S', t_tuple)
        else:
            return time.strftime('%Y-%m-%d', t_tuple)

    def get_now_year(self):
        """:return: 返回当前时间的年份"""
        return self.t_tuple_now().tm_year

    def get_now_month(self):
        """:return: 返回当前时间的月份"""
        return self.t_tuple_now().tm_mon

    def get_now_day(self):
        """:return: 返回当前时间的天"""
        return self.t_tuple_now().tm_mday

    def get_now_hour(self):
        """:return: 返回当前时间的小时数"""
        return self.t_tuple_now().tm_hour

    def get_now_minute(self):
        """:return: 返回当前时间的分钟数"""
        return self.t_tuple_now().tm_min

    def get_now_seconds(self):
        """:return: 返回当前时间的秒数"""
        return self.t_tuple_now().tm_sec

    def is_dst(self):
        """获取当前所处时区是否为夏令时,0不是，1是，-1不确定"""
        return self.t_tuple_now().tm_isdst


if __name__ == "__main__":
    common_time = CommonTime()

    # 字符串转时间元组
    get_t_tuple = common_time.t_tuple('2018-01-29')

    # 当前时间的时间元组
    now_t_tuple = common_time.t_tuple_now()

    # 任意时间的时间元组
    any_t_tuple = common_time.t_tuple_now(28800)

    # 当前时间的时间戳(浮点数)
    now_time_stamp = common_time.get_timestamp()

    # 当前时间的时间戳(整数)
    now_time_stamp2 = common_time.get_timestamp(is_integer=1)

    # 返回当前时间的年月日时分秒以及是否为夏令时
    now_year = common_time.get_now_year()
    now_month = common_time.get_now_month()
    now_day = common_time.get_now_day()
    now_hour = common_time.get_now_hour()
    now_minute = common_time.get_now_minute()
    now_second = common_time.get_now_seconds()
    is_dst = common_time.is_dst()

    # 时间元组转化为字符串
    t_tuple_to_str = common_time.tuple_to_str(now_t_tuple)
    t_tuple_to_str2 = time.asctime(now_t_tuple)

    print('(1)[2018-01-29]对应的时间元组为:', get_t_tuple)
    print('(2)当前时间对应的时间元组为:', now_t_tuple)
    print('(3)任意时间戳[28800]对应的时间元组为:', any_t_tuple)
    print('(4)当前时间的时间戳为(浮点数):', now_time_stamp)
    print('(5)当前时间的时间戳为(整数):', now_time_stamp2)
    print('(6)当前日期与时间为：{}年{}月{}日 {}点:{}分:{}秒'.format(str(now_year), str(now_month), str(now_day),
                                                  str(now_hour), str(now_minute), str(now_second)))
    print('(7)当前时区是否为夏令时:{}'.format('是' if is_dst == 1 else '不是'))
    print('(8)当前时间的字符串时间格式的时间为:', t_tuple_to_str)
