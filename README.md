# Free-Mistral-Chat-Bot

A simple, interactive chat bot built with [Streamlit](https://streamlit.io/) and powered by [Mistral AI](https://docs.mistral.ai/), using LangChain.

This project is designed as a learning tool and collaboration space for developers interested in building AI chat apps. I'm new to GitHub and open-source projects, and this is my first step toward learning by doing — and hopefully, with your help, improving!

---

## Features

* Interactive chat interface built with Streamlit
* Context-aware responses using LangChain's conversation memory
* Uses `mistral-large-latest` model via LangChain's Mistral integration
* Reset/clear conversation with one click
* Simple and beginner-friendly codebase

---

## Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/free-mistral-chat-bot.git
cd free-mistral-chat-bot
```

2. **Install dependencies**
   Make sure you’re using Python 3.9+ and have a virtual environment active.

```bash
pip install -r requirements.txt
```

3. **Set up your API Key**
* Create a folder named .streamlit in the root of the project directory.
* Inside this folder, create a file named secrets.toml.
* Add your Mistral API key to the secrets.toml ( You can get your free mistral api key from here: https://console.mistral.ai/api-keys)


4. **Run the app**

```bash
streamlit run AI-Chat-Bot.py
```

---

## How It Works

* The app uses `ChatMistralAI` from `langchain_mistralai` to communicate with the Mistral model.
* LangChain's `ConversationChain` with `ConversationBufferMemory` allows the AI to remember the chat history and respond more naturally.
* Streamlit's session state is used to manage and persist chat history across messages.

---

## Contributing

I built this to learn and grow. If you’re experienced with:

* Streamlit
* LangChain
* Mistral AI
* Frontend improvements
* Adding features like file upload, persona etc

Feel free to:

* Fork this repo
* Open an issue or feature request
* Submit a pull request
* Leave suggestions or code reviews

All levels of contributions are welcome! 

---

## To-Do / Ideas

* Add custom persona/system prompts
* Save chat history to file
* Support file uploads (PDF/Q\&A)
* Dark mode toggle
* Add tests and error handling

---



