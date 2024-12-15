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
            odometer = request.form.get("Odometer"),
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
    
    @app.route('/edit', methods=['GET', 'POST'])
    def edit_vehicle():
        id = request.args.get('id')
        vehicle = Vehicle.query.get(id)

        if request.method == 'GET':
            return render_template('edit.html', vehicle = vehicle)
    
        if request.method == 'POST':
            
            id = request.form["id"]
            vehicle = Vehicle.query.get(id)
            vehicle.image = request.form.get("Image")
            vehicle.name = request.form.get("Name")
            vehicle.quote = request.form.get("Quote")
            vehicle.description = request.form.get("Description")
            vehicle.odometer = request.form.get("Odometer")
            vehicle.owner = request.form.get("Owner")
            vehicle.type = request.form.get("Type")
            vehicle.make = request.form.get("Make")
            vehicle.model = request.form.get("Model")
            vehicle.year = request.form.get("Year")
            vehicle.features = request.form.get("Features")
            vehicle.currentissues = request.form.get("CurrentIssues")
            vehicle.previousissues = request.form.get("PreviousIssues")
                
            db.session.commit()
            return redirect(url_for('index'))


    @app.route('/delete', methods=['GET'])
    def delete_vehicle():
        id = request.args.get('id')
        vehicle = Vehicle.query.get(id)
        db.session.delete(vehicle)
        db.session.commit()

        # This route should handle deleting an existing item identified by the given ID.
        return redirect(url_for('index'))