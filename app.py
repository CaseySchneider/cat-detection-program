import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
print("hello human")


# When the bot hears a specific message 
# (the message content is up to you), it
# should create a thread and respond in 
# that thread acknowledging the message
@app.message("meow")
def message_hello(message, say):

    threadTs = message["ts"];
    say(text=f"Hello <@{message['user']}>...\n I detected that you \
are a cat. The authorities are being alerted.\n /\_/\\\n( o.o )\n > ^ <",\
     thread_ts=threadTs)
        


    # The bot should send a payload with the Slack
    # user’s name, their email address, and the
    # Slack message to a SendGrid API endpoint

    user_id = message.get('user')
    user_info = {}
    try:
        user_info = app.client.users_info(
            user=user_id
        )
    except Exception as e:
        print("Unable to retrieve user info.")
        print("Error: ", e)

    user_email = user_info['user']['profile']['email']
    user_name = user_info['user']['profile']['real_name_normalized']
    payload = {'user_name':user_name, 'user_email':user_email, 'message_text':message.get('test')}



    # SendGrid should send an email to you and 
    # another email address with the API
    # payload as the email body.

    message = Mail(
        from_email='caseyschneider10@gmail.com',
        to_emails='caseyschneider10@gmail.com',
        subject='Red Alert: Cat Detected',
        plain_text_content=('A cat has just been detected in Slack. Info below: \n' \
             + json.dumps(payload)),
        html_content='<strong>A cat has been detected.</strong>',
    )
    try:
        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)



# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()