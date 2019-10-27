from dialog_bot_sdk.bot import DialogBot
from config.config import bot
import db.db as core_db


def add_event(peer: str, command: str):
    print("!", command)
    core_db.add_event(int(peer.id), command)
    send_message(
        peer,
        'added event'
    )


def add_review(peer: str, command: str):
    str1, str2 = command.split(" ", 1)
    core_db.add_review(int(peer.id), str1, str2)
    send_message(
        peer,
        'added review'
    )


def show_review(peer: str, command: str):
    res = core_db.show_review(int(peer.id), command)

    send_message(
        peer,
        "Reviews about " + command + ':' + '\n' + res + "\n-------------------------\nEnd of reviews"
    )


command_list = {
    'add_event': add_event,
    'show_review': show_review,
    'add_reviews': add_review
}


def send_message(peer, msg: str) -> None:
    bot.messaging.send_message(
        peer,
        msg
    )


def get(string: str):
    return string.split(" ", 1)


def check(peer, command: str) -> bool:
    command, params = get(command)
    if command not in command_list:
        send_message(
            peer,
            'Invalid command'
        )

        return False
    command_list[command](peer, params)
    return True
