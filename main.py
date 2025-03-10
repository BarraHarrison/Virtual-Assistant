# Simple Virtual Assistant in Python
from neuralintents import GenericAssistant
import pandas_datareader as web
import sys

stock_tickers = [
    "TSLA",
    "FB",
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "NFLX",
    "NVDA",
    "BABA",
    "JPM"
]

todos = [
    "Study Korean",
    "Clean House",
    "Food Shopping",
    "Exercise for 30 minutes",
    "Prepare dinner"
]

def stock_function():
    for ticker in stock_tickers:
        data = web.DataReader(ticker, 'yahoo')
        print(f"The last price of {ticker} was {data['Close'].iloc[-1]}")

def show_todos():
    print("Your To-Do List: ")
    for todo in todos:
        print(todo)

def add_todo():
    todo = input("What To-Do do you want to add: ")
    todos.append(todo)

def remove_todo():
    todo_index = int(input("What To-Do do you want to remove (number): ")) - 1
    if todo_index < len(todos):
        print(f"Removing {todos[todo_index]}")
        todos.pop(todo_index)
    else:
        print("There is no To-Do at this position/number")

def goodbye_function():
    print("Goodbye!")
    sys.exit()


mappings = {"stocks": stock_function,
            "todos": show_todos,
            "farewell": goodbye_function}

assistant = GenericAssistant("short_intents.json", mappings)


try:
    assistant.load_model()
    print("Model loaded successfully.")
except Exception:
    print("Training new model...")
    assistant.train_model()
    assistant.save_model()
    print("Model trained and saved successfully.")

# Main loop for user interaction
while True:
    message = input("Message: ")
    try:
        assistant.request(message)
    except Exception as e:
        print(f"Sorry, I didn't understand that. Error: {e}")