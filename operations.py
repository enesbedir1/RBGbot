import telegram.ext
import random
from character import character, character_dict
from utils import write_characters, setattr_qualified

class operation():
    def run(self, update, context: telegram.ext.callbackcontext.CallbackContext):
        pass
    def help(self):
        pass
    def name(self):
        pass

class start(operation):
    def run(self, update, context: telegram.ext.callbackcontext.CallbackContext):
        update.message.reply_text("Hello! Welcome to RPG Telegram bot")
    
    def help(self):
        return ("usage {} : run to start".format(self.name()))
    
    def name(self):
        return "start"

class dice(operation):
    def run(self, update, context: telegram.ext.callbackcontext.CallbackContext):
        if len(context.args) > 2: 
            update.message.reply_text("1 or 2 number should be given for dicing!")
        elif len(context.args) == 1:
            if context.args[0].isdigit():
                update.message.reply_text("diced between 0 and {}: {}".format(context.args[0], random.randint(0, int(context.args[0]))))
            else:
                update.message.reply_text("First two arguments should be integer!")
                
        elif len(context.args) == 2:
            if context.args[0].isdigit() and context.args[1].isdigit():
                update.message.reply_text("diced between {} and {}: {}".format(context.args[0], context.args[1], random.randint(int(context.args[0]), int(context.args[1]))))
            else:
                update.message.reply_text("First two arguments should be integer!")

    def name(self):
        return "dice"

    def help(self):
        return ("usage {} : number1 number2".format(self.name()))

class create_ch(operation):
    def run(self, update, context: telegram.ext.callbackcontext.CallbackContext):
        if len(context.args) != 1: 
            update.message.reply_text("Please enter character name that you want to create")
        else: 
            if context.args[0] in character_dict:
                update.message.reply_text("There is already a character has name " + context.args[0])
                return
            character_dict[context.args[0]] = character(context.args[0])
            write_characters("/home/aenesbedir/RPGFather/character.yaml", character_dict)

    def name(self):
        return "create_ch"

    def help(self):
        return "/create_ch usage: enter character name"

class set_ch(operation):
    def run(self, update, context: telegram.ext.callbackcontext.CallbackContext):
        if len(context.args) != 3: 
            update.message.reply_text("3 arguman should be given!")
        else: 
            if context.args[0] not in character_dict:
                update.message.reply_text(context.args[0] + "is not a char!")
                return
            if context.args[1] not in character_dict[context.args[0]].to_dict():
                update.message.reply_text(context.args[1] + "is not a variable of a char")
                return
            setattr_qualified(character_dict[context.args[0]], context.args[1], context.args[2])
            write_characters("/home/aenesbedir/RPGFather/character.yaml", character_dict)
            update.message.reply_text(f"{context.args[0]}.{context.args[1]} is updated to {context.args[2]}.")
            
    def name(self):
        return "set_ch"

    def help(self):
        return "/set_ch usage: <name of char> <var of char> <value of var>"


class ls_ch(operation):
    def run(self, update, context: telegram.ext.callbackcontext.CallbackContext):
        result = "CHARACTERS: \n"
        for k, v in character_dict.items():
            result += "---------------- \n"
            result += "--" + k + "--" + " : \n" + v.to_string_defined()
        update.message.reply_text(result)

    def name(self):
        return "ls_ch"

    def help(self):
        return "/ls_ch usage: no argument is needed"

class ls_ch_all(operation):
    def run(self, update, context: telegram.ext.callbackcontext.CallbackContext):
        result = "CHARACTERS: \n"
        for k, v in character_dict.items():
            result += "---------------- \n"
            result += "--" + k + "--" + " : \n" + v.to_string_all()
        update.message.reply_text(result)

    def name(self):
        return "ls_ch_all"

    def help(self):
        return "/ls_ch_all usage: no argument is needed"
