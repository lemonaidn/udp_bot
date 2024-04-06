import os
import pandas as pd
from slack import WebClient
from slack.errors import SlackApiError

# Slack token
slack_token = os.environ.get('SLACK_API_TOKEN')
client = WebClient(token=slack_token)

# Read new records
new_records_df = pd.read_csv('new_records.csv')

# Check if there are new records
if not new_records_df.empty:
    # Format message
    messages = []
    for index, row in new_records_df.iterrows():
        messages.append(f"- {row['Filename']}: ${row['Amount']} for {row['Candidate Name']} ({row['Support/Oppose']}) in {row['State']}-{row['District']} for {row['Purpose']}. YTD: ${row['YTD Amount']}, Election: {row['Election']}")
    msg = "New FEC Filings:\n" + "\n".join(messages)
    
    # Send message
    client = WebClient(token=slack_token)
    try:
        response = client.chat_postMessage(
            channel="slack-bots",
            text=msg,
            unfurl_links=True, 
            unfurl_media=True
        )
        print("success!")
    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"]
        print(f"Got an error: {e.response['error']}")