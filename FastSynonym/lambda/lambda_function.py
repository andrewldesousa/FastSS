# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import time
import re
import datetime
from pytz import timezone
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



SERVER_URL = "PUT YOUR SERVER LINK HERE"



class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to Fast Squared, you can get a summary of latest posts from subreddits or get the synonyms for a word. Which would you like to try?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What would you like to do with Fast Squared?")
                .response
        )

class SummarizeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SummarizeIntent")(handler_input)

    def handle(self, handler_input):
        global SERVER_URL
        # type: (HandlerInput) -> Response
        slots= handler_input.request_envelope.request.intent.slots
        num_posts = int(slots["num_posts"].value) if slots["num_posts"].value else 1
        subreddit = slots["subreddit"].value
        subreddit=subreddit.lower()
        subreddit = re.sub(r' ','',subreddit)
        #num_posts = num_posts if num_posts else 1
        
        try:
            headers = {
                'accept': 'application/json',
            }
            
            params = (
                ('subreddit', subreddit),
                ('num_posts', num_posts),
            )
            
            
            response = requests.get(SERVER_URL+'summarize', headers=headers, params=params)
            speak_output = ''
            summaries = list(response.json()['summaries'])
            dates = list(response.json()['dates'])
            try:
                for i in range(len(summaries)):
                    summary =summaries[i]
                    date=dates[i]
                    date = datetime.datetime.fromtimestamp(float(date))
                    speak_output += 'Summary of post made on {} is as follows: {}.'.format(date.strftime("%m/%d/%Y, %H:%M:%S"),summary) +' '
                   
            except Exception as e:
                speak_output = "There was an error processing your request."
            
        except Exception as e:
            speak_output="Could not find posts for your subreddit. Please check your subreddit"
            
           
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What would you like to do with Fast Squared?")
                .response
        )

class SynonymIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SynonymIntent")(handler_input)

    def handle(self, handler_input):
        global SERVER_URL
        # type: (HandlerInput) -> Response
        
        slots=handler_input.request_envelope.request.intent.slots
        word=slots["word"].value
        
        
        headers = {
            'accept': 'application/json',
        }
        
        params = (
            ('word', word),
        )
        
        response = requests.get(SERVER_URL+'synonyms', headers=headers, params=params)
        
        speak_output = 'Some synonyms for {} are '.format(word)
        for s in response.json()['synonyms']:
            speak_output += s + ', '
        
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What would you like to do with Fast Squared?")
                .response
        )



class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(SummarizeIntentHandler())
sb.add_request_handler(SynonymIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
