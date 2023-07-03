import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ["my name is (.*)", ["Hi %1, how can I help you today?"]],
    ["(hi|hello|hey)", ["Hello, how can I assist you?"]],
    ["what is your name?", ["My name is Bot, nice to meet you!"]],
    ["how are you?", ["I'm doing well, thank you for asking."]],
    ["(.*) your age?", ["I am a computer program and do not have an age."]],
    ["(.*) (location|city) ?", ['I am a bot and do not have a physical location.']],
    ["(.*) help (.*)", ["Sure, I'd be happy to help you with %2."]],
    ["(.*) thank you (.*)", ["You're welcome!"]],
    ["bye", ["Goodbye, have a nice day!"]],
]# Create a chatbot
chatbot = Chat(pairs, reflections)
# Start the conversation
chatbot.converse()
