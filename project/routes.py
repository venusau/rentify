# backend/routes.py
from flask import request, jsonify , redirect, url_for, render_template
from app import app, db
from models import User, Property
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user, logout_user

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        data = request.json
        hashed_password = generate_password_hash(data['password'])
        new_user = User(
            first_name=data['first_name'], 
            last_name=data['last_name'], 
            email=data['email'], 
            phone=data['phone'], 
            password=hashed_password,
            is_seller=data['is_seller']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_get'))

@app.route('/properties', methods=['POST'])
def create_property():
    user_is_seller=current_user.is_seller
    if user_is_seller==None or user_is_seller==False:
        return jsonify({"message": "Unauthorized"}), 401
    data = request.json
    new_property = Property(
        title=data['title'],
        description=data['description'],
        place=data['place'],
        area=data['area'],
        bedrooms=data['bedrooms'],
        bathrooms=data['bathrooms'],
        hospitals_nearby=data['hospitals_nearby'],
        colleges_nearby=data['colleges_nearby'],
        seller_id=current_user.id
    )
    db.session.add(new_property)
    db.session.commit()
    return jsonify({"message": "Property created successfully"}), 201

@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    results = [
        {
            "id": prop.id,
            "title": prop.title,
            "description": prop.description,
            "place": prop.place,
            "area": prop.area,
            "bedrooms": prop.bedrooms,
            "bathrooms": prop.bathrooms,
            "hospitals_nearby": prop.hospitals_nearby,
            "colleges_nearby": prop.colleges_nearby,
            "likes": prop.likes,
            "seller_id": prop.seller_id
        } for prop in properties
    ]
    return jsonify(results), 200

@app.route('/properties/<int:id>', methods=['GET'])
@login_required
def get_property(id):
    prop = Property.query.get(id)
    if not prop:
        return jsonify({"message": "Property not found"}), 404
    return jsonify({
        "id": prop.id,
        "title": prop.title,
        "description": prop.description,
        "place": prop.place,
        "area": prop.area,
        "bedrooms": prop.bedrooms,
        "bathrooms": prop.bathrooms,
        "hospitals_nearby": prop.hospitals_nearby,
        "colleges_nearby": prop.colleges_nearby,
        "likes": prop.likes,
        "seller_id": prop.seller_id
    }), 200

@app.route('/properties/<int:id>', methods=['PUT'])
@login_required
def update_property(id):
    user_is_seller=current_user.is_seller
    if user_is_seller==None or user_is_seller==False:
        return jsonify({"message": "Unauthorized"}), 401
    prop = Property.query.get(id)
    if not prop or prop.seller_id != current_user.id:
        return jsonify({"message": "Property not found or unauthorized"}), 404
    data = request.json
    prop.title = data['title']
    prop.description = data['description']
    prop.place = data['place']
    prop.area = data['area']
    prop.bedrooms = data['bedrooms']
    prop.bathrooms = data['bathrooms']
    prop.hospitals_nearby = data['hospitals_nearby']
    prop.colleges_nearby = data['colleges_nearby']
    db.session.commit()
    return jsonify({"message": "Property updated successfully"}), 200

@app.route('/properties/<int:id>', methods=['DELETE'])
@login_required
def delete_property(id):
    user_is_seller= current_user.is_seller
    if user_is_seller == None or user_is_seller==False :
        return jsonify({"message": "Unauthorized"}), 401
    prop = Property.query.get(id)
    if not prop or prop.seller_id != current_user.id:
        return jsonify({"message": "Property not found or unauthorized"}), 404
    db.session.delete(prop)
    db.session.commit()
    return jsonify({"message": "Property deleted successfully"}), 200

@app.route('/properties/<int:id>/like', methods=['POST'])
def like_property(id):
    prop = Property.query.get(id)
    if not prop:
        return jsonify({"message": "Property not found"}), 404
    prop.likes += 1
    db.session.commit()
    return jsonify({"likes": prop.likes}), 200



@app.route('/properties/filter', methods=['GET'])
def filter_properties():
    place = request.args.get('place')
    bedrooms = request.args.get('bedrooms')
    bathrooms = request.args.get('bathrooms')

    # Your filtering logic goes here
    # Use the place, bedrooms, and bathrooms parameters to filter properties
    # You can use SQLAlchemy queries to filter properties based on these parameters

    # For example:
    filtered_properties = Property.query.filter_by(place=place, bedrooms=bedrooms, bathrooms=bathrooms).all()

    # Convert filtered properties to JSON and return
    results = [
        {
            "id": prop.id,
            "title": prop.title,
            "description": prop.description,
            "place": prop.place,
            "area": prop.area,
            "bedrooms": prop.bedrooms,
            "bathrooms": prop.bathrooms,
            "hospitals_nearby": prop.hospitals_nearby,
            "colleges_nearby": prop.colleges_nearby,
            "likes": prop.likes,
            "seller_id": prop.seller_id
        } for prop in filtered_properties
    ]
    
    return jsonify(results), 200



# TODO: Need to create routes for the rendering the templates index.html , login.html, buyer.html, property_dashboard.html, register.html and seller_dashboard.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/buyer')
@login_required
def buyer():
    user_is_seller=current_user.is_seller
    if user_is_seller==None:
        return render_template('login.html')
        
    else:
        if user_is_seller == False:
            return render_template('buyer_dashboard.html')
        else:
            return redirect(url_for('seller_dashboard'))

@app.route('/property_detail')
@login_required
def property_detail():
    return render_template('property_detail.html')


@app.route('/seller_dashboard' , methods=['GET'])
@login_required
def seller_dashboard():
    user_is_seller=current_user.is_seller
    if user_is_seller==None:
        return render_template('login.html')
        
    else:
        if user_is_seller == True:
            return render_template('seller_dashboard.html')
        else:
            return redirect(url_for('buyer'))
    

