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
    for index, row in new_records_df.iterrows():
        # Determine format based on presence of cents
        amount = float(row['Amount'])
        ytd_amount = float(row['YTD Amount'])
        amount_formatted = f"${amount:,.0f}" if amount.is_integer() else f"${amount:,.2f}"
        ytd_amount_formatted = f"${ytd_amount:,.0f}" if ytd_amount.is_integer() else f"${ytd_amount:,.2f}"
        
        # Format message for the current record, with formatted dollar amounts
        support_oppose_text = "supporting" if row['Support/Oppose'] == "Support" else "opposing"
        msg = (f"AIPAC's super PAC, the United Democracy Project, has submitted a new FEC filing for an independent expenditure, "
               f"- {amount_formatted} on {row['Purpose']} {support_oppose_text} {row['Candidate Name']} in {row['State']}-{row['District']}'s {row['Election']}. "
               f"Year to date, they've spent a total of {ytd_amount_formatted} on this race.")
        
        # Send a separate message for each record
        try:
            response = client.chat_postMessage(
                channel="slack-bots",
                text=msg,
                unfurl_links=True, 
                unfurl_media=True
            )
            print("Message sent successfully!")
        except SlackApiError as e:
            assert e.response["ok"] is False
            assert e.response["error"]
            print(f"Got an error: {e.response['error']}")
