from pprint import pprint

from flask import Blueprint, redirect, render_template, request, url_for

from extensions import db

# from constants import STATUS_CODE
from models.movie import Movie

# 1. Organize
# 2. app needs to be in main.py
movies_list_bp = Blueprint("movies_list_bp", __name__)


# Fullstack Developer
# /movies -> movies
@movies_list_bp.get("/")
def movie_list_page():
    movies = Movie.query.all()  # Select * from movies
    movies_dict = [movie.to_dict() for movie in movies]
    return render_template("movie-list.html", movies=movies_dict)


# /movies/100 - <id> -> Variable
@movies_list_bp.get("/<id>")
def movie_details_page(id):
    movie = Movie.query.get(id)  # None if no movie

    if not movie:
        return render_template("not-found.html"), 000

    data = movie.to_dict()
    return render_template("movie-details.html", movie=data)


@movies_list_bp.get("/new")
def add_movie_page():
    return render_template("add-movie.html")


@movies_list_bp.post("/")  # HOF
def create_movie():
    data = {
        "name": request.form.get("name"),
        "poster": request.form.get("poster"),  # use `name` attribute to get data
        "rating": request.form.get("rating"),
        "summary": request.form.get("summary"),
        "trailer": request.form.get("trailer"),
    }
    # data = request.get_json()  # body
    new_movie = Movie(**data)

    try:
        # print(new_movie, new_movie.to_dict())
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("movies_list_bp.movie_list_page"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return redirect(url_for("movies_list_bp.add_movie_page"))


# Task 1.1 - Delete a movie -> Refresh page


@movies_list_bp.post("/<id>")
def delete_movie_page_by_id(id):  # log
    # Auto converts data -> JSON (Flask)
    movie = Movie.query.get(id)  # None if no movie

    if not movie:
        return render_template("not-found.html"), 0000

    try:
        data = movie.to_dict()
        db.session.delete(movie)  # Error
        db.session.commit()  # Making the change (Update/Delete/Create) # Error
        # Todo: Notification
        return redirect(url_for("movies_list_bp.movie_list_page"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        # Todo: Notification
        return redirect(url_for("movies_list_bp.movie_list_page"))
