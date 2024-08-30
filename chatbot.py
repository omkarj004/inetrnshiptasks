from chatterbot import ChatBot # type: ignore

chatbot = ChatBot("MyChatbot")
from chatterbot.trainers import ChatterBotCorpusTrainer # type: ignore

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
