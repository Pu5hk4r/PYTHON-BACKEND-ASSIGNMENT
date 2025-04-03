from flask import Flask, request, jsonify
from models import db, App

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/assignment_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#  Home Route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Add App Route
@app.route('/add-app', methods=['POST'])
def add_app():
    try:
        data = request.json
        if not data or 'name' not in data or 'version' not in data or 'description' not in data:
            return jsonify({'message': 'Invalid request, missing fields'}), 400
        
        new_app = App(name=data['name'], version=data['version'], description=data['description'])
        db.session.add(new_app)
        db.session.commit()
        return jsonify({'message': 'App added successfully', 'id': new_app.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get App by ID Route
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app = App.query.get(id)
    if app:
        return jsonify({
            'id': app.id,
            'name': app.name,
            'version': app.version,
            'description': app.description
        })
    return jsonify({'message': 'App not found'}), 404

# Get All Apps Route
@app.route('/get-all-apps', methods=['GET'])
def get_all_apps():
    apps = App.query.all()
    return jsonify([{
        'id': app.id,
        'name': app.name,
        'version': app.version,
        'description': app.description
    } for app in apps])

# Delete App Route
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app = App.query.get(id)
    if app:
        db.session.delete(app)
        db.session.commit()
        return jsonify({'message': 'App deleted successfully'})
    return jsonify({'message': 'App not found'}), 404

# Receive Data from Emulator
@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json
    print("Received Data:", data)
    return jsonify({'message': 'Data received successfully'})

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("✅ Database connected and tables created.")
        except Exception as e:
            print("❌ Database connection error:", e)
    app.run(debug=True)
