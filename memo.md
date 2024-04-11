Creating this bot followed the following steps:

* Using openFEC to download json of the 20 most-recent 24/48 hour reports for AIPAC's super pac
* extracting the .fec file and pdf file urls from the json
* downloading the .fec files for each record and storing them in in a folder within the environment
* using the fecfile python library to extract key information from each file
* comparing the newly downloaded records to the prior download to extract only the new records since that last run
* writing a slack bot that populates a contextual message with the information in those new records, mad libs style. If there are multiple new records, each filing is sent as a separate message.

I wasn't able to add the pdf links to the message. i'm trying to use the index numbers of the .fec records that are identified as new, to pull the same indexes/rows from my csv of pdfs. But the closest I've gotten is a successful attempt on the first new record that fails on any subsequent records. You can see my efforts in scratchpad.py. I'm pretty sure I'm clsoe and just missing somethin or overcomplicating it.

I also didn't turn this into a Twitter bot yet. That's the goal but there wasn't time to learn how to use Twitter's API and write a new script that pushes these messages to Twitter instead of a slackbot.

I also want to incorporate an image of the disclosure in the slack message (and eventually the tweet too) so it's right there in the post.

Running this on an hourly basis seems like a happy medium between regular update (to avoid too many multi-messages/multi-tweets if there are a bunch of filings in the same day) and overkill.

I also want to start storing this data in a csv rather than overwriting it every time. Mygoal this summer is to combine all of the data in a news app that allows users to explore the entire impact of UDP on the nation's primaries, rather than just an alert to individual new filings.