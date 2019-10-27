from dialog_bot_sdk.bot import DialogBot
import grpc

token = '6167474259d7f4616796b09e6c0a108b62b9f813'
endpoint = 'hackathon-mob.transmit.im'
bot = DialogBot.get_secure_bot(
    endpoint,
    grpc.ssl_channel_credentials(),
    token,
    verbose=True
)

DBHOST = 'localhost'
BDPORT = 27017
DBNAME = 'bot2'
