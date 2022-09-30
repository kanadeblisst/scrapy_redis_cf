# -*- coding: utf-8 -*-
BOT_NAME = 'tests'

SPIDER_MODULES = ['tests.spiders']
NEWSPIDER_MODULE = 'tests.spiders'

ROBOTSTXT_OBEY = False

SCHEDULER = "scrapy_redis_cf.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis_cf.dupefilter.RFPDupeFilter"

REDIS_URL = "redis://127.0.0.1:6379"

