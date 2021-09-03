# custom action file for Rasa with webview example

from rasa_sdk import Action, Tracker

from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_core_sdk.executor import CollectingDispatcher
import yaml
import pickle
import logging
import os
#

# set up logging
logging.getLogger().setLevel(logging.WARNING)
logging.warning("logging check")

# define config file
current_path = os.getcwd()
directory_symbol = "\\"

# load the config file
path_to_yaml = current_path+directory_symbol+"custom_action_config.yml"
logging.warning("path_to_yaml "+path_to_yaml)
try: 
    with open (path_to_yaml, 'r') as file:
       config = yaml.safe_load(file)
except Exception as e:
    print('Error reading the config file')

    
wv_URL = config['general']['wv_url']

class ActionProvinceBack(Action):
#
     def name(self) -> Text:
         return "action_province_back"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            province = tracker.get_slot('province')
            # build target_URL
            target_URL_suffix = "?image="+config['images'][province]+"&description="+config['descriptions'][province]+"&province="+province
            target_URL = wv_URL+target_URL_suffix
            logging.warning("target_URL is "+str(target_URL))
            # build JSON to be sent to Facebook Messenger based on province provided in Rasa chat
            
            
            message1 = {
               "attachment": {
                    "type": "template",
                    "payload": {
                      "template_type": "button",
                      "text": "click below to open webview",
                      "buttons": [
                        {
                           "type":"web_url",
                           "url":target_URL,
                           "title": province,
                           "messenger_extensions": "true",
                           "webview_height_ratio": "tall"
                        }
                     ]
                  }
               }
            }
            # send payload to Facebook Messenger and echo confirmation
            dispatcher.utter_custom_json(message1)
            return []
