# -*- coding: utf-8 -*-
import datetime

__author__ = 'Feng_hui'
__time__ = '2018/1/30 19:14'
__introduction__ = '使用datetime库返回各种不同格式或类型的时间'


class CommonDateTime(object):
    """
    返回各种不同格式或类型的时间
    (get time of different format or different styles)
    """

    @staticmethod
    def time_now():
        """当前时间,类型为datetime.datetime()元组"""
        return datetime.datetime.now() or datetime.datetime.today()

    def now_year(self):
        """返回当前年份,类型为int"""
        return self.time_now().year

    def now_month(self):
        """返回当前月份,类型为int"""
        return self.time_now().month

    def now_day(self):
        """返回当前天数,类型为int"""
        return self.time_now().day

    def now_hour(self):
        """返回当前小时数,类型为int"""
        return self.time_now().hour

    def now_min(self):
        """返回当前分钟数,类型为int"""
        return self.time_now().minute

    def now_sec(self):
        """返回当前秒数,类型为int"""
        return self.time_now().second

    def now_micro(self):
        """返回当前微妙数,类型为int,不常用"""
        return self.time_now().microsecond

    def now_timestamp(self, dt=None):
        """获取任意datetime元组对应的时间戳,浮点数"""
        if not dt:
            return datetime.datetime.timestamp(self.time_now())
        else:
            assert isinstance(dt, datetime.datetime)
            return datetime.datetime.timestamp(dt)

    def datetime_to_time(self):
        """datetime元组转为time元组"""
        return datetime.datetime.timetuple(self.time_now())

    @staticmethod
    def str_to_dt(str_time):
        """字符串时间转化为datetime元组"""
        return datetime.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')

    def dt_to_str(self, dt=None):
        """datetime元组转化为字符串时间"""
        if not dt:
            return datetime.datetime.strftime(self.time_now(), '%Y-%m-%d %H:%M:%S')
        else:
            assert isinstance(dt, datetime.datetime)
            return datetime.datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')

    def str_to_timstamp(self):
        """时间字符串转化为时间戳"""
        pass

    def timestamp_to_str(self):
        """时间戳转化为时间字符串"""
        pass

    def yesterday(self):
        """获取昨天的时间"""
        return self.time_now() - datetime.timedelta(days=1)

    def tomorrow(self):
        """获取明天的时间"""
        return self.time_now() + datetime.timedelta(days=1)


if __name__ == "__main__":
    common_date_time = CommonDateTime()

    # 当前时间
    now_time = common_date_time.time_now()
    print('1、当前时间为：', now_time)

    # 当前时间对应的时间戳
    now_time_stamp = common_date_time.now_timestamp()
    print('2、当前时间对应的时间戳为：', now_time_stamp)

    # 任意datetime元组对应的时间戳为
    any_dt = datetime.datetime(2018, 2, 22)
    any_timestamp = common_date_time.now_timestamp(any_dt)
    print('3、任意datetime元组对应的时间戳为：', any_timestamp)

    # 任意字符串转化为datetime元组
    any_str_time = '2018-2-2 00:00:00'
    string_to_datetime = common_date_time.str_to_dt(any_str_time)
    print('4、字符串时间转为datetime元组：', string_to_datetime)

    # 任意时间字符串转化为时间戳
    any_timestamp = common_date_time.now_timestamp(string_to_datetime)
    print('5、字符串时间转化为时间戳：', any_timestamp)

    # datetime元组对应的字符串时间
    string_time = common_date_time.dt_to_str()
    string_time2 = common_date_time.dt_to_str(any_dt)
    print('6、datetime元组对应的字符串时间为(当前时间与任意时间)：', string_time, string_time2)

    # 获取昨天的时间
    yesterday = common_date_time.yesterday()
    print('7、获取昨天的时间：', yesterday)

    # 获取明天的时间
    tomorrow = common_date_time.tomorrow()
    print('8、获取明天的时间：', tomorrow)





