import scrapy
import csv
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from scrapy.exceptions import IgnoreRequest
from twisted.internet.error import ConnectionDone
from twisted.internet.error import ConnectionDone
#import tutorial.Links as Links


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    download_timeout = 20
    #Errori Successivi
    with open("entry.csv", "rt", encoding="utf-8") as f:
      lines = f.read().splitlines()
      def start_requests(self):
            for i in self.lines:
             yield scrapy.Request(i,
                                   callback=self.parse_httpbin,
                                   errback=self.errback_httpbin,
                                  dont_filter=True,
                                   meta={'dont_redirect': True})

    handle_httpstatus_list = [300,301,302,303,304,305,306,307,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,500,501,502,503,504,505,522]

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))
        if IgnoreRequest:
            yield{'URL': response.url}
        yield {
              'URL': response.url,
              'Status': response.status,
          }

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)
            yield {
                'HttpError': response.url,
                'RowNumber': self.lines.index(response.url),
                  }

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)
            yield {
                'DsnLookUpError': request.url,
                'RowNumber': self.lines.index(request.url),
            }
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
            yield {
                'TimeOuterror': request.url,
                'RowNumber' : self.lines.index(request.url),
            }
