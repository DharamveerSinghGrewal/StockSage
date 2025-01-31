import telebot
import requests
import openai
import yfinance as yf
import os
from dotenv import load_dotenv
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Command: Start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Welcome to the Finance Bot! 🤖\n\n"
        "Use the following commands:\n"
        "/stock <symbol> - Get stock price\n"
        "/explain <query> - Explain a financial term\n"
        "/help - Show help menu"
    )

# Command: Help
@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(
        message,
        "Here are the available commands:\n"
        "/stock <symbol> - Get stock price\n"
        "/explain <query> - Explain a financial term\n"
        "/help - Show help menu"
    )

# Command: Get Stock Price
@bot.message_handler(commands=["stock"])
def get_stock_price(message):
    try:
        symbol = message.text.split()[1]
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"].iloc[-1]
        bot.reply_to(message, f"**{symbol.upper()}**: ${price:.2f}")
    except IndexError:
        bot.reply_to(message, "Please provide a stock symbol. Usage: /stock <symbol>")
    except Exception:
        bot.reply_to(message, "Could not fetch stock price. Please check the symbol.")


# Command: Explain Financial Term
@bot.message_handler(commands=["explain"])
def explain_financial_term(message):
 
        query = " ".join(message.text.split()[1:])
        if not query:
            bot.reply_to(message, "Please provide a financial term. Usage: /explain <query>")
            return

        response = openai.Client().chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a financial expert explaining terms simply."},
        {"role": "user", "content": f"Explain the financial concept '{query}' in simple terms."}
        ],
        max_tokens=150
        )

        bot.reply_to(message, response.choices[0].message.content.strip())


# Start the bot
bot.polling()

