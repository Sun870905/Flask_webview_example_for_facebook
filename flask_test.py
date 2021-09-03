# tester app to exercised Flask

from flask import Flask, render_template, request
from string import Template
from OpenSSL import SSL
import pickle
from rasa.nlu.model import Interpreter
import requests
import json
#import string
#from actions import wv_payload
# import ssl
# context = SSL.Context(SSL.PROTOCOL_TLS)
# client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#





API_ENDPOINT = "http://localhost:5005/webhooks/rest/webhook"
messagePayload = ''
selected_item = ''
selected_category = ''


app = Flask(__name__)

HTML_TEMPLATE = Template("""
<h1>Hello ${file_name}!</h1>

<img src="https://image.tmdb.org/t/p/w342/${file_name}" alt="poster for ${file_name}">

""")

def package_list(key_name,list_in):
    i = 0
    list_out = []
    for element in list_in:
        key_value = list_in[i].strip()
        list_out.append({key_name:key_value})
        i = i+1
    return(list_out)

# @app.route('/animals', methods=['GET', 'POST'])
# @app.route('/')
@app.route('/')
def homepage():   
    graphic_example = "https://raw.githubusercontent.com/ryanmark1867/webview_rasa_example/master/media/Flag_of_Ontario.svg"
    image_URL = request.args.get('image')
    description_text = request.args.get('description')
    province = request.args.get('province')
    print("image_URL is "+str(image_URL))
    print("province is "+str(province))
    title_text = "Flag of "+province
    title = {'titlename':title_text}
    image = {'graphicname':image_URL}
    description = {'descriptionname':description_text}
    return render_template('home.html',title=title,image = image,description=description)
    #return """<h1>Test of web page Feb 9 night</h1>"""
    
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/<some_file>')
def some_place_page(some_file):
    return(HTML_TEMPLATE.substitute(file_name=some_file))
    
def test_call(test_text):
    print("from actions.py got "+test_text)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
