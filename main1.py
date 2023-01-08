from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
import json

with open('restaurant.json', 'r') as json_file:
	json_load = json.load(json_file)
 
restaurant1 = json_load['restaurant1']
restaurant2 = json_load['restaurant2']
restaurant3 = json_load['restaurant3']
restaurant4 = json_load['restaurant4']



@app.route('/empDetails')
def method_name():
	return jsonify(restaurant1)

@app.route('/')
def none():
    return "Hello World"

@app.route('/res1')
def res1():
    return render_template('restaurant.html',restaurant=restaurant1)

@app.route('/res2')
def res2():
    return render_template('restaurant.html',restaurant=restaurant2)

@app.route('/res3')
def res3():
    return render_template('restaurant.html',restaurant=restaurant3)

@app.route('/res4')
def res4():
    return render_template('restaurant.html',restaurant=restaurant4)

if __name__ == '__main__':
    app.run(debug=True)
