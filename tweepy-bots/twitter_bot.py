import tweepy
import pandas as pd

# Authenticate to Twitter

auth = tweepy.OAuthHandler(os.environ.get('TWITTER_CONSUMER_API_KEY'), os.environ.get('TWITTER_CONSUMER_API_KEY_SECRET'))

auth.set_access_token(os.environ.get('TWITTER_AUTH_ACCESS_TOKEN'), os.environ.get('TWITTER_AUTH_ACCESS_TOKEN_SECRET'))

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

new_records_df = pd.read_csv('new_records.csv')

# Read new records similar to the Slack bot
new_records_df = pd.read_csv('new_records.csv')

# Check if there are new records and tweet each
if not new_records_df.empty:
    for index, row in new_records_df.iterrows():
        # Determine format based on presence of cents
        amount = float(row['Amount'])
        ytd_amount = float(row['YTD Amount'])
        amount_formatted = f"${amount:,.0f}" if amount.is_integer() else f"${amount:,.2f}"
        ytd_amount_formatted = f"${ytd_amount:,.0f}" if ytd_amount.is_integer() else f"${ytd_amount:,.2f}"
        
        # Format message for the current record, with formatted dollar amounts
        support_oppose_text = "supporting" if row['Support/Oppose'] == "Support" else "opposing"
        msg = (f"AIPAC's super PAC, the United Democracy Project, has submitted a new FEC filing for an independent expenditure: "
               f"{amount_formatted} on {row['Purpose']} {support_oppose_text} {row['Candidate Name']} in {row['State']}-{row['District']}'s {row['Election']}. "
               f"Year to date, they've spent a total of {ytd_amount_formatted} on this race.")
        try:
            api.update_status(message)
        except tweepy.TweepError as e:
            print(f"Failed to tweet: {e}")
    