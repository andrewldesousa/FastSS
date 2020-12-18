from flask import Flask
from ask_sdk_core.skill_builder import SkillBuilder
from flask_ask_sdk.skill_adapter import SkillAdapter, VERIFY_SIGNATURE_APP_CONFIG, VERIFY_TIMESTAMP_APP_CONFIG 
from alexa.fast_synonym.lambda_function import LaunchRequestHandler, sb as fast_synonym_sb

sb = SkillBuilder()
# Register all handlers, interceptors etc.
# For eg : sb.add_request_handler(LaunchRequestHandler())

sb.add_request_handler(LaunchRequestHandler())

app = Flask(__name__)
app.config.setdefault(VERIFY_SIGNATURE_APP_CONFIG, False) 
app.config.setdefault(VERIFY_TIMESTAMP_APP_CONFIG, False) 

skill_response = SkillAdapter(skill=fast_synonym_sb.create(), skill_id=None, app=app)
skill_response.register(app=app, route="/")

if __name__ == '__main__':
    app.run()
