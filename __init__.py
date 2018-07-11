from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class ExordiumHelp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('help.exordium.intent')
    def handle_help_exordium(self, message):
        self.speak_dialog('help.exordium')


def create_skill():
    return ExordiumHelp()

