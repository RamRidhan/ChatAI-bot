# ChatAI-bot
ChatAI plays a significant role in performing multi-tasking and helps us to utilize wide range of features available in today's world.
This contextual chatbot is implemented by using Pytorch.<br>
•	The implementation is easy to follow for beginners and provide a basic understanding of chatbots.<br>
•	The implementation is straightforward with a Feed Forward Neural net with 2 hidden layers.<br>
•	Customization for your own use case is super easy. Just modify intents.json with possible patterns and responses and re-run the training.<br>
It is inspired from article : https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077.<br>
# Install Pytorch and dependencies
```
pip install nltk
nltk.download('punkt') --> "In case the above code generates error"
```
<b>NOTE: Make sure to install pytorch in your IDE or other environment and execute program source codes using pytorch</b>
# Usage
```
python train.py
```
This will dump processor.pth file. And then run

```
python chat.py
```
# Applications
•	Customer Support.<br>
•	Virtual Assistants (advanced features - voice recognition, text analysis, voice navigation).<br>
•	Task Automation.<br>
•	Entertainment.<br>
