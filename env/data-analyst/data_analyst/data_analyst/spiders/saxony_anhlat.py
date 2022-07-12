import scrapy


class SaxonyAnhlatSpider(scrapy.Spider):
    name = 'saxony_anhlat'
    allowed_domains = ['de.indeed.com']
    start_urls = ['https://de.indeed.com/jobs?q=data%20analyst&l=Saxony-Anhalt&vjk=1ea919430e553022']

    def parse(self, response):
        links = response.xpath("//div[@class='job_seen_beacon']/table/tbody/tr/td/div/h2/a")
        for link in links:
            link = link.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_data)

        # for page_number in range(0, 350, 10):
        #     pagination = f"https://de.indeed.com/jobs?q=data%20analyst&l=Saxony&start={page_number}"
        #     yield scrapy.Request(url=pagination, callback=self.parse)

    def parse_data(self, response):
        try:
            salary = response.xpath("//div[@class='cmp-SalaryDistributionDisplayWidget-subinfo']/text()").get()
        except:
            salary = ''
        skills = []
        requirements = response.xpath("//div[@id='jobDescriptionText']/div/ul[2]/li")
        for requirement in requirements:
            skills.append(requirement.xpath(".//text()").get())

        yield {
            "salary": salary,
            "requirement": [skills]
        }



