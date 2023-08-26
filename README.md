# LEGO Set Discord Bot
The LEGO Set Discord Bot is a Python-based project designed to enhance your Discord server with the ability to retrieve information and images of LEGO sets using the Rebrickable API. This bot can be easily installed in any Discord server, allowing users to quickly fetch information about specific LEGO sets by interacting with simple commands.

## Purpose
The purpose of this project is to provide LEGO enthusiasts in Discord communities with a convenient way to access information and images of LEGO sets using a user-friendly interface. By integrating with the Rebrickable API, the bot can seamlessly retrieve data about LEGO sets and present it directly in the Discord chat. This project serves as an example of how to create a functional Discord bot and integrate it with an external API.

## Functionality
The LEGO Set Discord Bot offers the following functionality:
- **Hello Command:** The bot responds to the `!hello` command with a friendly greeting message. This demonstrates the bot's responsiveness and interaction with users.
- **Set Image Command:** Using the `!setimage` command followed by a LEGO set number, users can request an image of a specific LEGO set. The bot contacts the Rebrickable API using the provided set number to fetch the image URL and then sends it back to the user. This allows users to quickly visualize the appearance of the requested LEGO set.

## Integration with Rebrickable API
The bot integrates with the Rebrickable API to retrieve LEGO set information, including images. It uses the set number provided by the user to make an API request to Rebrickable. If the request is successful (status code 200), the bot extracts the image URL from the response and sends it back to the user. If the request fails, an appropriate error message is sent.

## Installation
To install and run the LEGO Set Discord Bot, follow these steps:
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
    ```

## Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS and Linux: source venv/bin/activate
Install required packages:
```bash
pip install -r requirements.txt
```

## Set up environment variables:
Create a .env file in the project directory and add your Discord bot token and Rebrickable API key in the following format:
```
DISCORD_TOKEN=your_discord_bot_token
REBRICKABLE_API_KEY=your_rebrickable_api_key
```

## Run the bot:
```
python main.py
```

## Usage
Invite the bot to your Discord server.
Use the command !hello to receive a greeting from the bot.
Use the command !setimage set_number (replace set_number with an actual LEGO set number) to receive an image URL of the specified LEGO set.
Feel free to modify and extend this project to add more features and customize it according to your preferences.
