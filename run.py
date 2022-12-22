import telegram.ext
from asyncore import dispatcher
import random
import operations
from character import character_dict, cwd
from utils import read_characters, write_characters

token = "5902060357:AAHJ2Wxo48lBT76OWHq9lHIDUgPFkkbJ3vk"

updater = telegram.ext.Updater("5902060357:AAHJ2Wxo48lBT76OWHq9lHIDUgPFkkbJ3vk", use_context = True)
dispatcher = updater.dispatcher

ops = {"start": operations.start(),
        "dice": operations.dice(),
        "create_ch": operations.create_ch(),
        "ls_ch": operations.ls_ch(),
        "ls_ch_all": operations.ls_ch_all(),
        "set_ch": operations.set_ch(),
        }

def help(update, context: telegram.ext.callbackcontext.CallbackContext):
    help_msgs = ""
    for key, op in ops.items():
        help_msgs += op.help() + "\n"
    update.message.reply_text("All operations: \n" + help_msgs)
        

def add_to_all_operations():
    dispatcher.add_handler(telegram.ext.CommandHandler("help", help))

    for key, op in ops.items():
        dispatcher.add_handler(telegram.ext.CommandHandler(op.name(), op.run))


if __name__ == "__main__":
    add_to_all_operations()
    read_characters(cwd, character_dict)
    updater.start_polling()
    updater.idle()