from flask import render_template,url_for,flash,redirect,request
from movieapp import app,db
from movieapp.forms import AddMovieForm
from movieapp.models import Movie

@app.route('/')
def home():
    movies=Movie.query.all()
    return render_template('home.html',movies=movies,title="Movie List")

@app.route('/add-movie',methods=['GET','POST'])
def addMovie():
    form=AddMovieForm()
    if form.validate_on_submit():
        movie=Movie(name=form.name.data,location=form.location.data,datetime=form.datetime.data)
        db.session.add(movie)
        db.session.commit()
        flash("New Movie Added Successfully",'success')
        return redirect(url_for('home'))
    return render_template('post_movie.html',title='Post Movie',form=form,legent="Add New Movie")

@app.route('/movie/<int:movie_id>',methods=['GET','POST'])
def update_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    form=AddMovieForm()
    if form.validate_on_submit():
        movie.name=form.name.data
        movie.location=form.location.data
        movie.datetime = form.datetime.data
        db.session.commit()
        flash("Your movie has been updated",'success')
        return redirect(url_for('home'))
    elif(request.method=='GET'):
        form.name.data=movie.name
        form.location.data=movie.location
        form.datetime.data=movie.datetime
    return render_template('post_movie.html', title='Update Post',form=form,legent="Update Movie")


@app.route('/delete_movie/<int:movie_id>',methods=['GET'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    db.session.delete(movie)
    db.session.commit()
    flash("Your movie has been deleted", 'success')
    return redirect(url_for('home'))