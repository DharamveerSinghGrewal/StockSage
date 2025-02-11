# 📈 FinanceBot

FinanceBot is a Telegram bot designed to provide real-time stock prices and explain financial concepts using OpenAI's GPT API. Hosted on a Google Compute Engine Virtual Machine, this bot serves as a handy financial assistant at your fingertips.
## 🔗 Live Demo

Try StockSage live on Telegram: [Stock Sage Bot](https://t.me/stock_sage_bot)

## 🚀 Features

- 📊 **Get Stock Prices**: Retrieve the latest stock price for any company using `/stock <symbol>`.
- 📖 **Explain Financial Terms**: Understand finance jargon with AI-powered explanations via `/explain <query>`.
- 🤖 **Seamless Telegram Integration**: Interact directly with the bot for quick financial insights.
- ⚡ **Fast & Reliable**: Hosted on Google Cloud for high availability and speed.

## 🛠️ Technologies Used

- **Python** 🐍
- **Telebot (Python Telegram Bot API)** 🤖
- **Yahoo Finance (yfinance)** 📈
- **OpenAI GPT API** 🧠
- **Google Compute Engine** ☁️

## 🔧 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/DharamveerSinghGrewal/StockSage.git
   cd StockSage
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Create a `.env` file and add your credentials:
   ```
   TELEGRAM_TOKEN=your_telegram_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## 📌 Commands

| Command      | Description |
|-------------|-------------|
| `/start`    | Welcome message with instructions |
| `/stock <symbol>` | Fetches the latest stock price of a company (e.g., `/stock AAPL`) |
| `/explain <query>` | Provides a simple AI-generated explanation of a financial concept (e.g., `/explain inflation`) |
| `/help`     | Displays the available commands |

## 🎯 Future Enhancements

- 🏦 **Crypto Price Support**: Fetch cryptocurrency prices.
- 📉 **Stock Performance Insights**: Analyze stock trends.
---

🚀 Built with passion for finance and technology! Stay ahead with StockSage! 💰

