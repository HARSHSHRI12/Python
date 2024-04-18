from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model import Response
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import SimpleCard
from ask_sdk_core.utils import is_request_type, is_intent_name

# Create a skill builder
sb = SkillBuilder()

# Launch request handler (when the skill is invoked without a specific intent)
@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input: HandlerInput) -> Response:
    speech_text = "Welcome to my Alexa skill!"
    handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Welcome", speech_text)).set_should_end_session(False)
    return handler_input.response_builder.response

# Intent handler (for the custom "HelloWorldIntent")
@sb.request_handler(can_handle_func=is_intent_name("HelloWorldIntent"))
def hello_world_handler(handler_input: HandlerInput) -> Response:
    speech_text = "Hello, world!"
    handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("HelloWorldIntent", speech_text)).set_should_end_session(True)
    return handler_input.response_builder.response

# Fallback intent handler
@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input: HandlerInput) -> Response:
    speech_text = "Sorry, I didn't understand that. Can you please try again?"
    handler_input.response_builder.speak(speech_text).set_should_end_session(False)
    return handler_input.response_builder.response

# Add other intent handlers here as needed

# Error handler
@sb.exception_handler()
def exception_handler(handler_input: HandlerInput, exception: Exception) -> Response:
    speech_text = "Sorry, I encountered an error."
    handler_input.response_builder.speak(speech_text).set_should_end_session(True)
    return handler_input.response_builder.response

# Define the skill entry point
lambda_handler = sb.lambda_handler()
