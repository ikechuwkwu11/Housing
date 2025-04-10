from flask import Flask,jsonify,request
from models import User,Housing,db
from flask_login import LoginManager,login_user,logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iyke'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///housing.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/api/house')
def house():
    house_all = Housing.query.all()
    return jsonify({"house":house_all}),200

@app.route('/api/register',methods = ['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({"message":"Please fill in all data"}), 400

    new_user = User(username=username,email=email,password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"This user has been registered. Now login!!"}),201

@app.route('/api/login',methods = ['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({"message":"Please login well"}),400

    user = User.query.filter_by(username = username).first()

    if user and user.password == 'password':
        login_user(user)
        db.session.commit()
        return jsonify({"message":"you have logged in well"}),200
    return jsonify({"message":"invalid user"}),400

@app.route('/api/logout',methods=['GET'])
def logout():
    logout_user()
    return jsonify({"message":"You have been logged out"}), 200


@app.route('/api/house',methods = ['POST'])
def add_house():
    data = request.get_json()
    name = data.get('name')
    street = data.get('street')
    number = data.get('number')
    if not name or not street or not number:
        return jsonify({"message":"Please fill in all"}), 400

    new_user = Housing(name = name,street=street,number=number)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"You have successfully added"}),200



@app.route('/api/house/<int:house_id>',methods =['PUT'])
def edit_house(house_id):
    house = Housing.query.get_or_404(house_id)
    data = request.get_json()
    house.name = data.get('name', house.name)
    house.street = data.get('street', house.street)
    house.number = data.get('number',house.number)
    db.session.commit()
    return jsonify({"message":"house has been updated"}),200

@app.route('/api/house/<int:house_id>',methods = ['DELETE'])
def delete_house(house_id):
    house = Housing.query.get_or_404(house_id)
    db.session.delete(house)
    db.session.commit()
    return jsonify({"message":"House has been deleted"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)

