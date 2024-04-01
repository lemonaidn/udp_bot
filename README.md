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

## March 30

Used openFEC to download json for each filing instead. The json didn't include most of the key information I'm looking for, but it did include urls to the csvs of thefilings which did have that additional info.

The values in the csv required some mapping to connect them to the info from the pdf disclosures. The csvs were also formatted horribly -- they contained three lines/tables of data each. Wrote code to download the csvs (needed to build in some steps so the remote server wouldn't close the connection due to issues like rate limiting or incorrect headers), isolate only the third line/table of data, and extract only the information I'm interested in: campaign, disbursment_date_amount, amount_ytd, expense_type, oppose_or_support, candidate_last_name, candidate_first_name, house_or_senate, district, state.

ChatGPT was invaluable in helping me accomplish these steps.

My remaining steps:

* combine the scripts I used for each of these steps into one cohesive script
* add column headers to the data
* add pdf urls to the data so users can look at the original forms every time the bot sends out a new update
* add code to the script that isolates new filings since the prior day's data extraction
* clean values so they're more straightforward (for example, map any P2024 values to read "Primary 2023" instead)
* set up the bot
* set up github actions to run the script on a daily basis
