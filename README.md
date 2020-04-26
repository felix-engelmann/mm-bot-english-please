This Mattermost bot was created to maintain the discipline of writing in English instead of your mother tongue throughout channels with participants not understanding the language.

To remain unobtrusive, the bot will react to posts with a small union jack.


## Installation

clone the repository

    git clone https://github.com/felix-engelmann/mm-bot-english-please.git
    cd mm-bot-english-please

create virtual environment (recommended)

    python3 -m venv env
    source ./env/bin/activate

install the dependencies

    pip3 install -r requirements.txt
    
run

    python3 run.py  
   
### Systemd Service (optional)

to run the bot as a system service, it is useful to create a systemd service.
Adapt the `english-please.service` file with the correct path and user/group names and copy it into your services:

    cp english-please.service /etc/systemd/system/english-please.service

Reload the services

    sudo systemctl daemon-reload 

and then start and enable (starts automatically) it:

    sudo systemctl start english-please
    sudo systemctl enable english-please
   
## Configuration

To connect the bot to you Mattermost instance,
create a bot account on your instance:

    Integrations 
    -> Bot Accounts 
    -> Add New 
       - Role: Member, no additional permissions
       - note the Access Token.

Edit `mmpy_bot_settings.py`

    BOT_URL = 'https://your-mm-instance/api/v4'
    BOT_LOGIN = 'english-please' # or whatever name you gave the bot accout
    BOT_TOKEN = '0ß9uokjhaodasd' # the token retrieved in the account creation

restart the bot/systemd service.

## Adaptation

As the bot is responding to all messages and necessarily is a member of the town square, it actively ignores this channel.

Currently the bot only reacts to sentences with more than 3 words and only complains if the text is German. I noticed that the language detection library used (langdetect) has a hard time with short fragments. Therefore, it is useful to detect the presence of the prevalent unwanted language instead of the wanted one. Feel free to adapt the logic in `plugins/language.py`.

## Debugging

If you want to know the detected languages for a sentence, you can @mention or direct message the bot to get insight into it's "brain". Be aware that the language detection is not deterministic.
 
