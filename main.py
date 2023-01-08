from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

data = {
    "users": [
        {
            "id": 0,
            "fName": "Om",
            "lName": "Patel",
            "email": "ompatel@gail.com",
            "password": "123456"
        },
        {
            "id": 1,
            "fName": "Jagrat",
            "lName": "Patel",
            "email": "jagratpatel@gail.com",
            "password": "987654"
        },
        {
            "id": 2,
            "fName": "Jaivin",
            "lName": "Barot",
            "email": "jaivinbarot@gail.com",
            "password": "123456"
        },
    ],
    "restaurant": [
        {
            "id": 0,
            "name": "Abc",
            "location": 1,
            "dishes": [0, 1]
        },
        {
            "id": 1,
            "name": "Def",
            "location": 1,
            "dishes": [0, 1, 2]
        },
        {
            "id": 2,
            "name": "Hij",
            "location": 0,
            "dishes": [0]
        },
        {
            "id": 3,
            "name": "Klm",
            "location": 2,
            "dishes": [1, 2]
        },
    ],
    "dishes": [
        {
            "id": 0,
            "name": "dish 1",
            "ingredient": ["ing1", "ing2", "ing3", "ing4"]
        },
        {
            "id": 1,
            "name": "dish 2",
            "ingredient": ["ing5", "ing2", "ing3", "ing4"]
        },
        {
            "id": 2,
            "name": "dish 3",
            "ingredient": ["ing6", "ing2", "ing4"]
        }
    ],
    "locations": [
        {
            "id": 0,
            "name": "Ahmedabad"
        },
        {
            "id": 1,
            "name": "Ahmedanagar"
        },
        {
            "id": 2,
            "name": "Gandhinagar"
        },
        {
            "id": 3,
            "name": "Gandhidham"
        },
        {
            "id": 4,
            "name": "Surat"
        }
    ]
}


'''@app.route('/')
def hello_world():
    dishes = data["dishes"]
    return render_template("index.html", dishes=dishes)'''

@app.route('/restaurant', methods=['GET','POST'])
def restaurantPage():
    data = {
        "name" : "Pizza house",
        "items": ["Pizza"],
        "address": "Ahmedabad",
        "time": "12:00 PM to 12:00 AM",
        "about": "Station Bar is a one-stop destination for people who want to have a fun time with their families and friends. The eye-catching colorful decor just does not ends there. We have a spectacular outdoor seating for romantic evenings."
    }
    return render_template("restaurant.html", restaurant=data)

    
    
    
@app.route('/users', methods=['GET', 'POST'])
def userFetch():
    if(request.method == 'GET'):
        user_Id = request.args.get('userId')
        userArr = [user if user["id"] ==
                   int(user_Id) else 0 for user in data["users"]]
        user = {}
        for i in userArr:
            if i != 0:
                user = i
        return jsonify(user)


@app.route('/location', methods=['GET', 'POST'])
def locationFetch():
    if(request.method == 'GET'):
        loc_name = request.args.get('name')
        locArr = [loc if loc_name.lower() in loc["name"].lower()
                  else 0 for loc in data["locations"]]
        loc = {"data": []}
        for i in locArr:
            if i != 0:
                loc["data"].append(i)
        return jsonify(loc)
    

    
@app.route('/', methods=['GET', 'POST'])
def Home():
    return render_template("Home.html")

@app.route('/Offer', methods=['GET', 'POST'])
def Offer():
    return render_template("Offer.html")

@app.route('/Search', methods=['GET', 'POST'])
def Search():
    return render_template("Search.html")

@app.route('/Blog', methods=['GET', 'POST'])
def Blog():
    return render_template("Blog.html")
    


if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = 8000)

