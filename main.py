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
        print(f"Removing {todos.index(todo_index)}")
        todos.pop(todo_index)
    else:
        print("There is no To-Do at this position/number")

def goodbye_function():
    print("Goodbye!")
    sys.exit()

assistant = GenericAssistant(intents)