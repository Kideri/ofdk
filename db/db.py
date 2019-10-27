from pymongo import MongoClient
import config.config as core_config

client = MongoClient(core_config.DBHOST, core_config.BDPORT)
db = client.bot2
collection = db.users


def add_event(user_id: int, event_name: str) -> None:
    if not check_user(user_id):
        collection.insert_one(
            {
                "user_id": str(user_id),
                "event_names": [
                    {
                        str(event_name): []
                    }
                ]
            }
        )
    else:
        collection.update_one(
            {
                'user_id': str(user_id)
            },
            {
                "$push": {
                    "event_names": {
                        str(event_name): []
                    }
                }
            }
        )


def show_review(user_id: int, event_name: str):
    events = list(collection.find_one({'user_id': str(user_id)})['event_names'])
    for event in events:
        k = event.get(event_name)
        str1 = '\n------------------------------------------\n'
        if k is not None:
            return str1.join(k)


def add_review(user_id: int, event_name: str, message: str):
    event = collection.find_one({'user_id': str(user_id)})['event_names']
    i = 0
    for ev in event:
        if event_name in ev:
            event = ev[event_name]
            break
        i += 1
    event.append(message)
    try:
        collection.update_one(
            {
                'user_id': str(user_id)
            },
            {
                "$set": {
                    'event_names.' + str(i) + '.' + event_name: event
                }
            }

        )
    except Exception as e:
        print(e)


def check_user(user_id: int) -> bool:
    if not collection.count_documents({"user_id": str(user_id)}):
        return False
    return True
