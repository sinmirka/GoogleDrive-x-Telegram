# Telegram → Google Drive Bot

A personal Telegram bot that automatically saves messages and files to Google Drive.

This bot is designed for personal use and helps store important content from Telegram directly into a chosen Google Drive folder.

## Features

### The bot supports saving the following types of messages:

Text messages (saved as .txt files)

Photos (JPG, PNG, GIF)

Documents (PDF, DOCX, XLSX, ZIP and others)

Audio files

Voice messages (.ogg)

Videos

Video notes (round videos)

Animations (GIF)

Unsupported message types are handled gracefully with a fallback response.

All files are uploaded to a specified Google Drive folder.

## Tech Stack

Python 3.10+

aiogram 3

Google Drive API (OAuth 2.0)

## Setup

### Clone the repository

git clone https://github.com/your-username/GoogleDrive-x-Telegram.git

cd GoogleDrive-x-Telegram

### Create and activate a virtual environment

python -m venv .venv

Linux / macOS: source .venv/bin/activate

Windows: .venv\Scripts\Activate.ps1

### Install dependencies

pip install -r requirements.txt

## Configuration

### Telegram Bot

Create a Telegram bot using @BotFather and put the bot token into a config file (config.py or .env):

BOT_TOKEN=your_bot_token_here

OWNER_ID=your_telegram_id

## Google Drive

Create a Google Cloud project

Enable Google Drive API

Create OAuth 2.0 credentials

Download credentials.json

Run the OAuth flow to generate token.json

### Important: credentials.json and token.json must NOT be committed to the repository and should be listed in .gitignore.

## Running the bot

Start the bot with:

python main.py

## Notes

This bot is intended for personal use only

Only the owner (defined by OWNER_ID) can interact with the bot

All sensitive credentials are excluded from the repository via .gitignore. Dont leak your tokens.

# Demonstration

![TGxGD_demo](https://github.com/user-attachments/assets/3f6a04d4-40e3-4a06-bba2-204e7f70a529)
