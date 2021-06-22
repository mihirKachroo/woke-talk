'''
Student: Mihir
Teacher: Mr. Ghorvei
Date: June 22, 2021
Program: MovieWatcher
'''

# Import packages from Flask, a web application framework
from flask import flash, Blueprint, render_template, request, jsonify, url_for, redirect

from __init__ import create_app, db # import create app and db functions from init
import smtplib # Defines an SMTP client session object that can be used to send emails

# main blueprint that organizes flask application flask application into smaller and re-usable application
main = Blueprint('main', __name__)

# Dictionary that maps movie's name to its respective show image
movieImagesFromName = {
  "Venom 2": "venom2.jpg",
  "FAST AND FURIOUS 9": "fast9.jpg",
  "Luca": "luca.jpg",
  "A Quiet Place 2": "quietplace2.jpg",
  "Free Guy": "freeguy.jpg"
}

# creates a blueprint template for the default home page
@main.route('/', methods = ['GET', 'POST']) # Allows us to send either GET (to recieve infomration) or POST (to give and recieve information) requests to this route
def index():
    # Executes block of code if a post request is sent
    if request.method == 'POST':
        gottenMovieName = request.form.get('movieName') # Gets value of a specific id from form through which the post request was made
        return redirect(url_for('main.movie_page', movieName=gottenMovieName)) # Redirects use to main movie page with the name of the movie as a passed parameter
    # Renders index.html if a get request is sent instead of a post request
    return render_template('index.html')

# creates a blueprint template for the ordering page
@main.route('/order', methods = ['GET', 'POST']) # Allows us to send either GET (to recieve infomration) or POST (to give and recieve information) requests to this route
def order():
    # Executes block of code if a post request is sent
    if request.method == 'POST':
        gottenMovieName = request.form.get('movieName') # Gets value of a specific id from form through which the post request was made
        gottenUserEmail = request.form.get('email') # Gets value of a specific id from form through which the post request was made
        gottenNumOfTickets = request.form.get('numOfTickets') # Gets value of a specific id from form through which the post request was made
        # ======= This block of code sends an email to the user with a proof of reciept ======= #
        HOST = 'smtp.gmail.com' # Host through which the email will be send
        PORT = 587 # Port the server that sends the email will run on
        SENDER = 'taforthelols@gmail.com' # Email of the sender
        PASSWORD = 'mko09ijn' # Password of the sender's email
        server = smtplib.SMTP(host=HOST, port=PORT) # Creates STMP server
        server.connect(host=HOST, port=PORT)  # create an SMTP server object
        server.ehlo() # sent by an email server to identify itself when connecting to another email server to start the process of sending an email
        server.starttls() # turns  an existing insecure connection into a secure one
        server.ehlo() # again identifies user to stmp server
        server.login(user=SENDER, password=PASSWORD) # logs into the user's email account
        RECIPIENT = gottenUserEmail # Sets who will recieve the email (in our case, it is the movie orderer)
        # Message that will be sent to user
        MESSAGE = '''
        Hi,

        Here is your proof of purchase receipt from your movie theater purchase for {0}:

        You have bought {1} tickets for Saturday July 30 at MovieWatcher Center, 5100 Erin Mills Pkwy, Mississauga, ON L5M 4Z5

        Hope to see you soon.
        '''.format(gottenMovieName, str(gottenNumOfTickets)) # Formats number into a string that can be added to the message variable
        # Executes send email function
        server.sendmail(SENDER,RECIPIENT,MESSAGE)
        return redirect(url_for('main.thankyou', movieName=gottenMovieName)) # Redirects use to thank you page with the name of the movie as a passed parameter
    
    # Gets movieName and movieTime parameter from the arguments that were passed to it
    movieName = request.args.get('movieName', None)
    movieTime = request.args.get('movieTime', None)
    # Renders order.html with parameters if a get request is sent instead of a post request
    return render_template('order.html', movieName=movieName, movieTime=movieTime)

# creates a blueprint template for the thank you page
@main.route('/thankyou')
def thankyou():
    movieName = request.args.get('movieName', None) # Gets movieName parameter from the arguments that were passed to it
    return render_template('thankyou.html', movieName=movieName)

# creates a blueprint template for the movie information page
@main.route('/movie_page', methods = ['GET', 'POST']) # Allows us to send either GET (to recieve infomration) or POST (to give and recieve information) requests to this route
def movie_page():
    # Executes block of code if a post request is sent
    if request.method == 'POST':
        gottenMovieName = request.form.get('movieName') # Gets value of a specific id from form through which the post request was made
        gottenMovieTime = request.form.get('movieTime') # Gets value of a specific id from form through which the post request was made
        return redirect(url_for('main.order', movieName=gottenMovieName, movieTime=gottenMovieTime)) # Redirects use to ordering page with the name of the movie as a passed parameter
    # Gets movieName parameter from the arguments that were passed to it
    movieName = request.args.get('movieName', None)

    # Sets information about the movie for movie_page depending on what the passed movieName parameter is
    if movieName == "Venom 2": # Sets information about Venom 2
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "9:00 a.m. – 11:00 a.m. EDT", "Watch new Marvel Venom: Let There Be Carnage", "Sequel to the 2018 film 'Venom'", "Andy Serkis", "Kelly Marcel (screenplay by), Kelly Marcel (story by)", "Tom Hardy, Michelle Williams, Stephen Graham"
    elif movieName == "FAST AND FURIOUS 9": # Sets information about Fast 9
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "11:00 a.m. – 1:00 p.m. EDT", "Watch new Fast and Furious 9 starring Vin Diesel and John Cena", "Cypher enlists the help of Jakob, Dom's younger brother to take revenge on Dom and his team.", "Justin Lin", "Vin Diesel, Michelle Rodriguez, Jordana Brewster", "Daniel Casey (screenplay by), Justin Lin (screenplay by)"
    elif movieName == "Luca": # Sets information about Luca
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "1:00 p.m. – 3:00 p.m. EDT", "Watch new Pixar Luca", "On the Italian Riviera, an unlikely but strong friendship grows between a human being and a sea monster disguised as a human.", "Enrico Casarosa", "Jacob Tremblay, Jack Dylan Grazer, Maya Rudolph", "Jesse Andrews (screenplay by), Mike Jones (screenplay by)"
    elif movieName == "A Quiet Place 2": # Sets information about A Quiet Place 2
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "3:00 p.m. – 5:00 p.m. EDT", "Watch new A Quiet Place Part II horror movie", "Following the events at home, the Abbott family now face the terrors of the outside world. Forced to venture into the unknown, they realize the creatures that hunt by sound are not the only threats lurking beyond the sand path.", "John Krasinski", "John Krasinski, Scott Beck", "Emily Blunt, Millicent Simmonds, Cillian Murphy"    
    elif movieName == "Free Guy": # Sets information about Free Guy
        movieDate, movieTime, movieSubtitle, movieAbout, movieDirectors, movieWriters, movieStars = "Fri., Jul. 30", "5:00 p.m. – 7:00 p.m. EDT", "Watch new Free Guy comedy and action movie", "A bank teller discovers that he's actually an NPC inside a brutal, open world video game.", "Shawn Levy", "Matt Lieberman (screenplay by), Matt Lieberman (story by)", "Ryan Reynolds, Jodie Comer, Taika Waititi"
    
    # Renders movie_page.html if a get request is sent instead of a post request
    return render_template('movie_page.html', movieName=movieName, movieImage=movieImagesFromName[movieName], movieDate=movieDate, movieTime=movieTime, movieSubtitle=movieSubtitle, movieAbout=movieAbout, movieDirectors=movieDirectors, movieWriters=movieWriters, movieStars=movieStars)


app = create_app() # initializes flask app using the __init__.py function

if __name__ == '__main__': # ensures that the run() method is called only when main.py is run as the main program
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode