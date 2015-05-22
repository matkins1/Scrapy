# -*- coding: utf-8 -*-

# Scrapy settings for realtor project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'realtor'

SPIDER_MODULES = ['realtor.spiders']
NEWSPIDER_MODULE = 'realtor.spiders'
DEFAULT_ITEM_CLASS = 'realtor.items.RealtorItem'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'realtor (+http://www.yourdomain.com)'
