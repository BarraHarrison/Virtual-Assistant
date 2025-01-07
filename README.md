# Virtual Assistant Python Program
The assistant can perform various tasks and respond to the user's queries.
The python project is powered by the neuralintents library which uses NLP
(Natural Language Processing) to understand the user input and link it up with predefined actions.

# Purpose of the short_intents.json
This acts as the knowledge base for the virtual assistant.

It contains predefined intents each representing a category of user input:
- Tags: the topic the user is talking about
- Patterns: Sample phrases and keywords that the assistant matches to the user's input
- Responses: Predefined replies that the virtual assistant provides.

The JSON file ensures the assistant has a structured and customizable framework for handling
the user's interactions.

The logic (main.py) and the data (short_intents.json) are separated so that the virtual assistant
program is easy to maintain and improve.
  
