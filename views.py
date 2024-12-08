from flask import render_template, request, redirect, url_for, flash
from models import db, Vehicle # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def index():
        vehicles = Vehicle.query.all()
        return render_template('index.html', vehicles=vehicles)



    @app.route('/add', methods=['POST'])
     # This route should handle adding a new item to the database.
    def create_item():
        newvehicle = Vehicle(
            image = request.form.get("Image"),
            name = request.form.get("Name"),
            quote = request.form.get("Quote"),
            description = request.form.get("Description"),
            owner = request.form.get("Owner"),
            type = request.form.get("Type"),
            make = request.form.get("Make"),
            model = request.form.get("Model"),
            year = request.form.get("Year"),
            features = request.form.get("Features"),
            currentissues = request.form.get("CurrentIssues"),
            previousissues = request.form.get("PreviousIssues")
            )
        
        db.session.add(newvehicle)
        db.session.commit()
       
        return redirect(url_for('index'))

    @app.route('/view_vehicle', methods=['GET'])
    def view_vehicle():
        id = request.args.get('id')
        vehicle = Vehicle.query.get(id)
        return render_template('view_vehicle.html', vehicle = vehicle)

    @app.route('/update', methods=['POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')