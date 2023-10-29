from flask import Flask, jsonify, render_template
import openai
import os
openai.api_key = os.environ.get('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')

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('a.html')
  
@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  response = openai.Image.create(prompt=prompt, n=5, size="256x256") 
  print(response)
  return jsonify(response)


app.run(debug=false,host='0.0.0.0')
