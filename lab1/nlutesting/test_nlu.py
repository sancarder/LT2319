from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
#message = "let's see some italian restaurants"
#message = "is there a good japanese place nearby?"
#message = "hello there"
#message = "what would be a good lunch around here?"
#message = "thanks a lot"
#message = "i want to book a flight from paris to london"
#message = "i need help to reboot my computer"
#message = "what's up"
#message = "merci"
#message = "hello, what can you recommend for lunch"
#message = "howdy"
#message = "what's good this evening"
#message = "I'm hungry"
#message = "sushi"
message = "bye good"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))
