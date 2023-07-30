# Voice-to-text-bot
Telegram bot for auto transcription of voice messages.  
[Try it in Telegram](https://t.me/voice2textRuBot)

## Project structure
```
.
├── app
│   ├── .env                       # secret token
│   ├── main_telega.py             # runs telegram bot
│   └── speech.py                  # texts audio function
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```
## Before runing
To install the dependencies run:
```
$ pip install -r requirements.txt
```


## How to run in demone
1. Create demone file
`$ sudo nano /etc/systemd/system/bot.service`

Input in the file next script
```
[Unit]
Description=My bot
After=multi-user.target
 
[Service]
Type=idle
ExecStart=/usr/bin/python /usr/src/bot.py
Restart=always
 
[Install]
WantedBy=multi-user.target
```
2. Run the next commands
```
$ sudo systemctl daemon-reload
$ sudo systemctl enable bot.service
$ sudo systemctl start bot.service
```

3. Helpful commands
Stop bot  
`$ sudo systemctl stop bot.service`  
Delete from autorun   
`$ sudo systemctl disable bot.service`  
Check demone working  
`$ sudo systemctl status bot.service`

## How to run with Docker
1. Build Docker image:  
`docker build -t name:image -f Dockerfile .`
2. Run Docker in interactive mode:  
`docker run -it name:image`
3. Run in demone:  
`docker run -d name:image`

## Example
<img width="689" alt="Снимок экрана 2023-07-30 в 15 05 02" src="https://github.com/JuliaRebrova/Voice-to-text-bot/assets/90173032/528776fa-6e90-4f71-b708-a4a8e35511bf">

