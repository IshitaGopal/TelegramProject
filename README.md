# TelegramProject

# Tutorials / Notebooks / Code

## Data collection from Telegram 

### Collect all the messages 
To collect all the messages from a public channel/group on Telegram, execute this Python [script](https://github.com/IshitaGopal/TelegramProject/blob/code_for_data_collection/code/collect_all_messages.py) in the terminal. You will need to provide a channel/group username as the input. The below example will collect all the messages from New York Time's telegram channel (viewable at t.me/nytimes) in json format. Each json file will contain a maximum of 10000 messages. There will be multiple json files if there are more than 10000 messages to collect.
     
```console
foo@bar:~$ ./collect_all_messages.py --channel_input nytimes
```
> **_NOTE:_** You will be prompted to input your phone number and autheticate by providing the code sent to you on you Telegram app. 

The script creates a folder with the same name as the channel in which all the json files are stored. The chanel directory is stored in the "chat_data" root directory (see config.py). The API Keys are stored as enviroment variables and are imported from the congig.py file. Eg json path:
 
 ```
chat_data/nytimes/nytimes_1.json
```

---
**NOTE**
 You will need your own API cridentials ([see here](https://docs.telethon.dev/en/stable/basic/signing-in.html))and add them to a .env file.  [This](https://www.youtube.com/watch?v=YdgIWTYQ69A) tutorial by Jonathan Soma shows how to do this. The format of the .env file should be as follows:

```
TELEGRAM_API_ID = ""
TELEGRAM_API_HASH = ""
PHONE_NUM = ""

```
---



 

