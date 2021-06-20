########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import flash, Blueprint, render_template, request, jsonify, url_for, redirect

from flask_login import login_required, current_user
from __init__ import create_app, db

########################################################################################
# our main blueprint
main = Blueprint('main', __name__)

@main.route('/', methods = ['GET', 'POST']) # home page that return 'index'
def index():
    if request.method == 'POST':
        gottenMovieName = request.form.get('movieName')
        return redirect(url_for('main.movie_page', movieName=gottenMovieName))
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/movie_page')
def movie_page():
    movieName = request.args.get('movieName', None)
    if movieName == "Venom 2":
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "9:00 a.m. – 11:00 a.m. EDT", "Watch new Marvel Venom: Let There Be Carnage", "Sequel to the 2018 film 'Venom'", "Andy Serkis", "Kelly Marcel (screenplay by), Kelly Marcel (story by)", "Tom Hardy, Michelle Williams, Stephen Graham"
    elif movieName == "FAST AND FURIOUS 9":
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "11:00 a.m. – 1:00 p.m. EDT", "Watch new Fast and Furious 9 starring Vin Diesel and John Cena", "Cypher enlists the help of Jakob, Dom's younger brother to take revenge on Dom and his team.", "Justin Lin", "Vin Diesel, Michelle Rodriguez, Jordana Brewster", "Daniel Casey (screenplay by), Justin Lin (screenplay by)"
    elif movieName == "Luca":
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "1:00 p.m. – 3:00 p.m. EDT", "Watch new Pixar Luca", "On the Italian Riviera, an unlikely but strong friendship grows between a human being and a sea monster disguised as a human.", "Enrico Casarosa", "Jacob Tremblay, Jack Dylan Grazer, Maya Rudolph", "Jesse Andrews (screenplay by), Mike Jones (screenplay by)"
    elif movieName == "A Quiet Place 2":
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "3:00 p.m. – 5:00 p.m. EDT", "Watch new A Quiet Place Part II horror movie", "Following the events at home, the Abbott family now face the terrors of the outside world. Forced to venture into the unknown, they realize the creatures that hunt by sound are not the only threats lurking beyond the sand path.", "John Krasinski", "John Krasinski, Scott Beck", "Emily Blunt, Millicent Simmonds, Cillian Murphy"    
    elif movieName == "Free Guy":
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "5:00 p.m. – 7:00 p.m. EDT", "Watch new Free Guy comedy and action movie", "A bank teller discovers that he's actually an NPC inside a brutal, open world video game.", "Shawn Levy", "Matt Lieberman (screenplay by), Matt Lieberman (story by)", "Ryan Reynolds, Jodie Comer, Taika Waititi"
    return render_template('movie_page.html', movieName=movieName, movieDate=movieDate, movieTime=movieTime, movieSubtitle=movieSubtitle, movieAbout=movieAbout, movieDirectors=movieDirectors, movieWriters=movieWriters, movieStars=movieStars)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode