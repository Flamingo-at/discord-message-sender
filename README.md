<h1 align="center">Discord Message Sender</h1>

<p align="center">A simple bot to send messages to discord indefinitely with a custom delay<br>
Support for only one account and a specific text message</p>
<p align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white">
</p>

## ⚡ Installation
+ Install [python](https://www.google.com/search?client=opera&q=how+install+python)
+ [Download](https://sites.northwestern.edu/researchcomputing/resources/downloading-from-github) and unzip repository
+ Install requirements:
```python
pip install -r requirements.txt
```

## 💻 Preparing
+ Rename the ```example.env``` file to ```.env```
+ Open ```.env``` with a text editor and paste your **discord token** from the account in the ```TOKEN```
+ Open ```config.yaml``` with a text editor:
  + In the ```DELAY``` enter the delay in seconds between sending messages
  + In the ```MESSAGE``` paste the text to be sent
  + In the ```CHANNEL_ID``` paste the ```id``` of the channel in which you want to send the message
    <details>
      <summary>How to find out the <code>id</code></summary>
      Copy the link to the channel and take the value after the last <code>/</code>
      <br>Example: <code>https://discord.com/channels/000000000000000000/123456789012345678</code>, id = <code>123456789012345678</code>
    </details>

## ✔️ Usage
+ Run the bot:
  ```python
  python discord_message_sender.py
  ```

## 📧 Contacts
+ Telegram - [@flamingoat](https://t.me/flamingoat)
