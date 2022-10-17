# telegram-project

# Tutorials / Notebooks / Code

## Data collection from Telegram 

To collect all the messages from a public channel/group execute this Python [script](https://github.com/IshitaGopal/TelegramProject/blob/code_for_data_collection/code/collect_all_messages.py) in the terminal. You will need to provide a channel/group username as the input. The below example will collect all the messages from New York Time's telegram channel (viewable at t.me/nytimes) in json format. Each json file will contain a maximum of 10000 posts. 
     
```console
foo@bar:~$ ./collect_all_messages.py --channel_input nytimes
```

 The script creates a folder with the same name as the channel which is stored in the chat_data root directory. 
 
 ```
 Eg path chat_data/nytimes/nytimes_1.json
```

