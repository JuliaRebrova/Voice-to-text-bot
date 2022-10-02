# Voice-to-text-bot
Telegram bot for auto transcription of voice messages

# How to run in demone on service
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
