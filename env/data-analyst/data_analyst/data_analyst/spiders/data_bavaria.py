import time

import scrapy


class DataBavariaSpider(scrapy.Spider):
    name = 'data_bavaria'
    allowed_domains = ['de.indeed.com']
    start_urls = ['https://de.indeed.com/jobs?q=data%20analyst&l=Bavaria&from=searchOnHP&vjk=544649e0510faa94']

    def parse(self, response):
        time.sleep(5)
        links = response.xpath("//div[@class='job_seen_beacon']/table/tbody/tr/td/div/h2/a")
        for link in links:
            link = link.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_data)

        for page_number in range(0, 300, 10):
            pagination = f"https://de.indeed.com/jobs?q=data%20analyst&l=Bavaria&start={page_number}"
            yield scrapy.Request(url=pagination, callback=self.parse)


    def parse_data(self, response):
        company_name = response.xpath(
            "//h1[@ class='icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title']/text()").get()
        location = response.xpath("//div[@class='icl-u-xs-mt--xs icl-u-textColor--secondary "
                                  "jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle']/div["
                                  "2]/div/text()").get()

        try:
            salary = response.xpath("//div[@class='cmp-SalaryDistributionDisplayWidget-subinfo']/text()").get()
        except:
            salary = ''
        skills = []
        requirements = response.xpath("//div[@id='jobDescriptionText']/div/ul[2]/li")
        for requirement in requirements:
            skills.append(requirement.xpath(".//text()").get())

        yield {
            "company": company_name,
            "Location": location,
            "salary": salary,
            "requirement": [skills]
        }
