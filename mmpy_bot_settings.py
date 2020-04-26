SSL_VERIFY = True  # Whether to perform SSL cert verification
BOT_URL = 'https://mattermost-vs.informatik.uni-ulm.de/api/v4'  # with 'http://' and with '/api/v4' path. without trailing slash.
BOT_LOGIN = 'english-please'
#BOT_PASSWORD = '<bot-password>'

try:
    from secrets import BOT_TOKEN
except ImportError:
    pass

# or '<bot-personal-access-token>' if you have set bot personal access token.
BOT_TEAM = 'verteilte-systeme'  # possible in lowercase
#WEBHOOK_ID = '<bot-webhook-id>' # otherwise the bot will attempt to create one

PLUGINS = [
    'plugins',
]