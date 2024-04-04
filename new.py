import httpx
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from openai import OpenAI
import fitz # PyMuPDF
import time
import telebot
import logging
from openai import OpenAI
import os
# import dotenv

# dotenv.load_dotenv()
client = OpenAI(api_key='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',http_client=httpx.Client(proxies='http://141.147.88.9:8888'))

conversation = [{"role": "system", "content": "You are an assistant."}]

print("How can I help you?")
inputquestion = input("Question: ")

conversation.append({"role": "user","content": inputquestion})

response = client.chat.completions.create(
model="gpt-3.5-turbo",
messages=conversation
)

assistant_response = response.choices[0].message.content

print(f"Assistant: {assistant_response}")
# Set your OpenAI API key
# OPENAI_API_KEY = "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"
# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=OPENAI_API_KEY, http_client=httpx.Client(proxies='http://141.147.88.9:8888'), timeout=60
# )
#
# # Initialize Telegram bot
# TOKEN = "7111032891:AAGMCu2PyHW29E_he03F5yBaPOhqmxwXRsc"
# bot = telegram.Bot(token=TOKEN)
# # logger = telebot.logger
# # telebot.logger.setLevel(logging.INFO)
# # bot = telebot.TeleBot(token=TOKEN, threaded=False)
#
# def typing(chat_id):
#     while True:
#         bot.send_chat_action(chat_id, 'typing')
#         time.sleep(5)
#
# # Define the prompt
# PROMPT = "Ask me anything about the topic you're interested in."
#
# # Function to extract text and images from PDF files
# def extract_text_and_images(file_path):
#     text = ""
#     images = []
#
#     # Open the PDF file
#     pdf_document = fitz.open(file_path)
#
#     # Extract text and images from each page
#     for page_number in range(pdf_document.page_count):
#         page = pdf_document.load_page(page_number)
#
#         # Extract text from the page
#         text += page.get_text()
#
#         # Extract images from the page
#         images += page.get_images(full=True)
#
#     pdf_document.close()
#     return text, images
#
#
# # Load knowledge base
# knowledge_base = ""
# knowledge_files_directory = "knowledge_files"
#
# # Read knowledge base from text and PDF files
# for filename in os.listdir(knowledge_files_directory):
#     file_path = os.path.join(knowledge_files_directory, filename)
#     if filename.endswith(".txt"):
#         with open(file_path, "r") as file:
#             knowledge_base += file.read() + "\n"
#     elif filename.endswith(".pdf"):
#         text, images = extract_text_and_images(file_path)
#         knowledge_base += text + "\n"
#     # Extract text and images from PDF files
#
# # Function to handle incoming messages
# def message_handler(update, context):
#     # Get user input
#     user_input = update.message.text
#
#     # Print user message to console
#     print("User:", user_input)
#
#     # Preprocess user input
#     user_input = preprocess_input(user_input)
#
#     # Generate response using OpenAI GPT
#     response = generate_response(user_input)
#
#     print('openai', response)
#
#     # Send response back to user along with prompt instructions
#     full_response = response
#     update.message.reply_text(full_response)
#
# # Function to preprocess user input
# def preprocess_input(input_text):
# # Implement your preprocessing logic here
# # For example, you can perform text normalization, filtering, etc.
#     return input_text
#
# # Function to generate response using OpenAI GPT
# def generate_response(input_text):
#     # Combine user input with prompt and knowledge base
#     # print(knowledge_base)
#     # input_text = input_text #+ "\n" + knowledge_base
#
#     # Generate response using OpenAI GPT
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # or any other engine
#             messages=[{"role": "system", "content": f'{PROMPT}'},
#             {"role": "user", "content": f'{input_text}'}]
#         )
#     except Exception as e:
#         print(e)
#     generated_text: str = response.choices[0].message.content.strip()
#     # generated_texts.append(generated_text)
#     return generated_text #response['choices'][0]['message']['content']
#
# # Set up Telegram bot handlers
# updater = Updater(TOKEN, use_context=True)
# dispatcher = updater.dispatcher
# dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
#
# # Start polling for incoming messages
# updater.start_polling()
# updater.idle()
