# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/19 16:34
# @Author : waxberry
# @File : 实现类似JMeter_GUI操作性能测试一样的效果.py
# @Software : PyCharm


from unittest import TestCase,main
from pymeter.api.config import TestPlan, ThreadGroupWithRampUpAndHold
from pymeter.api.postprocessors import JsonExtractor
from pymeter.api.reporters import HtmlReporter
from pymeter.api.samplers import DummySampler, HttpSampler
from pymeter.api.timers import UniformRandomTimer


class TestTestPlanClass(TestCase):
    def test_1(self):
        json_extractor = JsonExtractor('variable', 'args.var')
        timer = UniformRandomTimer(1000, 2000)
        http_sampler = HttpSampler(
            "Echo",
            "https://postman-echo.com/get?var=${__Random(0,10)}",
            timer,
            json_extractor
        )
        dummy_sampler = DummySampler('dummy ${variable}', 'hi')
        tg = ThreadGroupWithRampUpAndHold(
            10, 1, 60, http_sampler, dummy_sampler, name='Some Name'
        )
        html_reporter = HtmlReporter()
        tp = TestPlan(tg, html_reporter)
        stats = tp.run()
        print(
            f"duration= {stats.duration_milliseconds}",
            f"mean= {stats.sample_time_mean_milliseconds}",
            f"min= {stats.sample_time_min_milliseconds}",
            f"median= {stats.sample_time_median_milliseconds}",
            f"90p= {stats.sample_time_90_percentile_milliseconds}",
            f"95p= {stats.sample_time_95_percentile_milliseconds}",
            f"99p= {stats.sample_time_99_percentile_milliseconds}",
            f"max= {stats.sample_time_max_milliseconds}",
            set='\t',
        )
        self.assertLess(stats.sample_time_99_percentile_milliseconds, 2000)

if __name__ == '__main__':
    main()