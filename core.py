from dialog_bot_sdk.bot import DialogBot
import config.config as core_config
import functions.functions as func_core


def on_msg(*params):
    peer = params[0].peer
    message = params[0].message.textMessage.text
    print(peer, str(message).strip())
    func_core.check(peer, message)


if __name__ == '__main__':
    core_config.bot.messaging.on_message(on_msg)
