import scrapy


class QuotesSpider(scrapy.Spider):
    name = "matches"
    start_urls = [
        'http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id='+'2015'+';type=year',
    ]

    for i in range(2016, 2019):
        start_urls.append('http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id='+str(i)+';type=year')

    def parse(self, response):
        for match in response.css('tr.data1'):
            if match.css('td.left::text')[0].extract()!='no result':
                yield{
                    'Team1': match.css('td.left a.data-link::text')[0].extract(),
                    'Team2': match.css('td.left a.data-link::text')[1].extract(),
                    'Winner': match.css('td.left a.data-link::text')[2].extract(),
                    'Margin': match.css('td.left::text')[0].extract(),
                    'Ground': match.css('td.left a.data-link::text')[3].extract(),
                    'Match Date': match.css('td::text')[1].extract(),
                    'Scorecard Link' : match.css('a::attr(href)')[4].extract(),
                }
            else:
                yield {
                    'Team1': match.css('td.left a.data-link::text')[0].extract(),
                    'Team2': match.css('td.left a.data-link::text')[1].extract(),
                    'Winner': match.css('td.left::text')[0].extract(),
                    'Margin': '',
                    'Ground': match.css('td.left a.data-link::text')[2].extract(),
                    'Match Date': match.css('td::text')[1].extract(),
                    'Scorecard Link' : match.css('a::attr(href)')[3].extract(),
                }

