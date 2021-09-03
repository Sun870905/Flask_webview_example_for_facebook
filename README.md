readme for repo for simple example of using Rasa with Facebook Messenger webview (described in https://medium.com/@markryan_69718/using-facebook-messenger-webview-with-a-rasa-chatbot-67b43af3324a )

*actions.py*: custom actions file for Rasa

*custom_action_config.yml*: config file read by actions.py containing data shown in Facebook Messenger webview

*flash_test.py*: simple Flask server that serves page shown in Facebook Messenger webview

*domain.yml, endpoints.yml, config.yml*: standard Rasa files

*templates/home.html*: page served in FM webview

*data/nlu.md*: utterance level training for Rasa model

*data/stories.md*: multi-utterance level training for Rasa model