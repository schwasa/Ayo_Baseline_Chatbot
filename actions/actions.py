# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

#
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from nrclex import NRCLex
#
# class ActionEmotion(Action):
#
#     def name(self) -> Text:
#         return "action_emotion"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         text = str(tracker.latest_message["text"])
#
#         emotion = NRCLex(text)
#
#         dispatcher.utter_message(text="The Words lists are {}".format(emotion.words))
#         dispatcher.utter_message(text="The Affect dictionary of the emotions detected are {}".format(emotion.affect_dict))
#         dispatcher.utter_message(text="The raw emotion scores detected are {}".format(emotion.raw_emotion_scores))
#         dispatcher.utter_message(text="The top emotions detected are {}".format(emotion.top_emotions))
#         dispatcher.utter_message(text="The affect frequencies detected are {}".format(emotion.affect_frequencies))
#
#         return []
#
#
