"""Flask app for adopt app."""

from flask import Flask, render_template, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route("/")
def show_homepage():
    """ Displays pets on homepage """

    pets = Pet.query.all()

    return render_template("index.html", pets=pets)

@app.route("/add", methods=['GET','POST'])
def add_pet():
    """ Displays Add Pet form and proccesses form submission """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data

        pet = Pet(form.data)

        pet = Pet(name=name,
                species=species,
                age=age,
                photo_url=photo_url,
                notes=notes)

        db.session.add(pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("add_pet.html", form=form)



@app.route("/<pet_id>", methods=["GET", "POST"])
def show_and_edit_pet_detail(pet_id):
    """ Displays individual pet details and form to edit info
        processes edit information
        """

    pet = Pet.query.get(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect(f"/{pet_id}")

    else:
        return render_template("pet_detail.html", pet=pet, form=form)