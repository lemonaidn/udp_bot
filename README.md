# udp_bot
Pulls information about UDP's Form 24/48's on a daily basis and pushes new filings out via a bot

3/17/24

I attempted to build a scraper using beautifulsoup that ultimately didn't work. After feeling like I was going crazy, I eventually figured out (with chatGPT's advice) that the FEC's content is loaded dynamically, meaning that scraping with bs4 just straight up isn't going to work.

Scraping no longer seems like the best path forward. I coooould build one out with Selenium, but at that point it makes more sense to just learn how to use the openFEC API.

Another problem: I want to be able to extract several pieces of information from the actual document that isn't present in the FEC's table on its webpages. Hopefully the info is included by default when pulling info about disclosures from the API, but I'm going to assume I'll run into the same problem I was going to have to deal with if scraping had worked. The key addtl info I want to extract is:

* Amount
* Name of Federal Candidate
* Support or Oppose
* District
* State
* Purpose of Expenditure
* Calendar Year-To-Date Per Election for Office Sought
* Primary of General

The first step of this process would have been to find a programmatic way to go through the urls hosting the csvs or pdfs of the disclosures, which would require a predictable url pattern. That ALMOST exists... but not quite, or at least not that I've been able to figure out yet.

https://docquery.fec.gov/pdf/877/202403169622431877/202403169622431877.pdf

The last two numbers exist in the FEC's table as the "beginning image number" so that's easy enough and could just be replaced filing-to-filing, similar to what we did for the MD Docs project. But the "877" number is a mystery, and that number changes with each filing.

So... if using the API doesn't get me closer to extracting that information, then I might need to try using Selenium anyway?? Or fastFEC? Let's really hope not.

I don't have much to show yet but hopefully that'll be different after playing around with the API
