from flask import Flask, json
from flask import request, jsonify
from flask import render_template, send_from_directory
from threading import Thread
import glob
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
import requests
import shutil
import PIL.Image
from flask import flash, redirect, url_for
from werkzeug.utils import secure_filename
import subprocess as sp

UPLOAD_FOLDER = '/storage'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'java', 'py', 'class', 'json'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
DIALOGFLOW_PROJECT_ID1 = os.getenv('PROJECT_ID1')
DIALOGFLOW_PROJECT_ID2 = os.getenv('PROJECT_ID2')
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'
app = Flask('')

@app.route('/fghudrtvyreybsr57y')
def ryuhvgryiuvrtybuvruinyduivc():
  return render_template('givdrsgbud.html')
  
@app.route('/assad')
def cvbxcbcvbvncvhfthdfthfdghfdgyhtrduyhtduh():
  return(r'''

''')
@app.route('/nexitybot')
def nexitybot():
  if 'text' in request.args:
    text = str(request.args['text'])
  else:
    return "Error: No text field provided. Please specify a text."
  try:
    f = open("private_key.json", "r")
    os.remove("private_key.json")
    mayb = requests.get(os.getenv('PRIVATE_KEY_LINK2'))
    with open('private_key.json', 'a') as f:
      f.write(mayb.text)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
  except IOError:
    mayb = requests.get(os.getenv('PRIVATE_KEY_LINK2'))
    with open('private_key.json', 'a') as f:
      f.write(mayb.text)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
  finally:
    f.close()
  text_to_be_analyzed = text

  session_client = dialogflow.SessionsClient()
  session = session_client.session_path(DIALOGFLOW_PROJECT_ID2, SESSION_ID)
  text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
  query_input = dialogflow.types.QueryInput(text=text_input)
  try:
      response = session_client.detect_intent(session=session, query_input=query_input)
      returnmessage = {
        "query_text": text,
        "intent": response.query_result.intent.display_name,
        "confidence": response.query_result.intent_detection_confidence,
        "response": response.query_result.fulfillment_text,
      }
      os.remove("private_key.json")
      return str(returnmessage)
  except InvalidArgument:
      raise

@app.route('/get')
def rdgvuybrtvybuvdrybutvurevyt():
  if 'link' in request.args:
    link = str(request.args['link'])
  else:
    return "Error: No link field provided. Please specify a link."
  r = requests.get(link)
  basedir = os.path.abspath(os.path.dirname(__file__))
  with open(basedir + '/templates/dfgybudfy7gdsg.html', 'w+') as f:
    f.write(r.text)
  return render_template('dfgybudfy7gdsg.html')
@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    f = request.files['file']
    filename = secure_filename(f.filename)
    basedir = os.path.abspath(os.path.dirname(__file__))
    f.save(os.path.join(basedir, "storage", filename))
    return "https://api.o7fire.ml" + str(url_for('upload_file', filename=filename))
  elif request.method == "GET":
    if 'filename' in request.args:
      filename = str(request.args['filename'])
      basedir = os.path.abspath(os.path.dirname(__file__))
      return send_from_directory(basedir + "/storage", filename, as_attachment=True)
      #with open(filename, "rb") as f:
      #  return render_template('uploader.html', content=f.read())
    else:
      return "Error: No filename field provided. Please specify a filename."
  
@app.route('/nsfwclassify', methods=['GET'])
def nsfwclassify():
  if 'text' in request.args:
    text = str(request.args['text'])
  else:
    return "Error: No text field provided. Please specify a text."
  try:
    f = open("private_key.json", "r")
    os.remove("private_key.json")
    mayb = requests.get(os.getenv('PRIVATE_KEY_LINK'))
    with open('private_key.json', 'a') as f:
      f.write(mayb.text)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
  except IOError:
    mayb = requests.get(os.getenv('PRIVATE_KEY_LINK'))
    with open('private_key.json', 'a') as f:
      f.write(mayb.text)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
  finally:
    f.close()
  text_to_be_analyzed = text

  session_client = dialogflow.SessionsClient()
  session = session_client.session_path(DIALOGFLOW_PROJECT_ID1, SESSION_ID)
  text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
  query_input = dialogflow.types.QueryInput(text=text_input)
  try:
      response = session_client.detect_intent(session=session, query_input=query_input)
      returnmessage = {
        "query_text": text,
        "intent": response.query_result.intent.display_name,
        "confidence": response.query_result.intent_detection_confidence,
      }
      os.remove("private_key.json")
      return str(returnmessage)
  except InvalidArgument:
      raise

@app.route('/convertimagetotext', methods=['GET'])
def convertimagetotext():
  if 'link' in request.args:
    link = str(request.args['link'])
  else:
    return('No link provided')
  try:
    r = requests.get(link, stream = True)
    with open("image1.png",'wb') as out_file:
      shutil.copyfileobj(r.raw, out_file)

    image = PIL.Image.open('image1.png')
    rgb_image = image.convert('RGB')
    rgb_image = rgb_image.transpose(PIL.Image.ROTATE_180)
    rgb_image = rgb_image.resize((100, 76))
    width, height = rgb_image.size
    with open('assad.txt', 'a+') as f:
      for w in range(width):
        for h in range(height):
          r, g, b = rgb_image.getpixel((w, h))
          f.write(f'{w+1} {h+1} {r} {g} {b}N')

    with open('assad.txt', 'r') as file:
      text = file.read()
      os.remove('assad.txt')
      os.remove('image1.png')
      return text
  except:
    return 'invalid image'

@app.route('/convertimagetotextblocks', methods=['GET'])
def convertimagetotextblocks():
  if 'link' in request.args:
    link = str(request.args['link'])
  else:
    return('No link provided')
  try:
    r = requests.get(link, stream = True)
    with open("image2.png",'wb') as out_file:
      shutil.copyfileobj(r.raw, out_file)

    image = PIL.Image.open('image2.png')
    rgb_image = image.convert('RGB')
    rgb_image = rgb_image.transpose(PIL.Image.ROTATE_180)
    rgb_image = rgb_image.resize((100, 76))
    width, height = rgb_image.size
    with open('assad2.txt', 'a+') as f:
      for w in range(width):
        for h in range(height):
          r, g, b = rgb_image.getpixel((w, h))
          f.write(f'{w+1} {h+1} {r} {g} {b}N')

    with open('assad2.txt', 'r') as file:
      text = file.read()
      os.remove('assad2.txt')
      os.remove('image2.png')
      return text
  except:
    return 'invalid image'

@app.route('/')
def main():
  with open('ping.txt', 'r') as f:
    text = f.read().split("\n")
    for string in text:
      if "https" in string:
        requests.get(string.split(' ')[1])
      else:
        a = 1

  return render_template('main.html')

@app.route('/ping')
def ping():
  sendstring = ""
  with open('ping.txt', 'r') as f:
    text = f.read().split("\n")
    for string in text:
      if "https" in string:
        requeststring = requests.get(string.split(' ')[1]).text
        if "alive 200" in requeststring:
          sendstring = sendstring + f"\n{string.split(' ')[0]} : active"
        else:
          sendstring = sendstring + f"\n{string.split(' ')[0]} : inactive"
      else:
        sendstring = sendstring + "\n" + string
  return render_template("ping.html", string=sendstring)


@app.route('/apidirfiles')
def apidirfiles():
  dirout = sp.getoutput('cd storage && ls -a | cat') 
  return (dirout)

  
def run():
  app.run(host="0.0.0.0", port=8444)  
run()
