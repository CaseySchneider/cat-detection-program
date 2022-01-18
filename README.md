# cat-detection-program
This program is used to detect cats (big cats, small cats, house cats, etc.) that have infiltrated your Slack channel. 


### API Keys, Tokens, and Environment Variables
Sendgrid API keys (SENDGRID_API_KEY) can be generated here https://app.sendgrid.com/settings/api_keys.

Slack Tokens (SLACK_BOT_TOKEN, SLACK_APP_TOKEN) can be generated here https://api.slack.com/apps/\<YOUR-APP-ID\> for SLACK_APP_TOKEN and here https://api.slack.com/apps/\<YOUR-APP-ID\>/oauth? for SLACK_BOT_TOKEN.
  
SENDGRID_API_KEY, SLACK_BOT_TOKEN and SLACK_APP_TOKEN should be set as environment variables in your local environment so that app.py will have access to them. 
