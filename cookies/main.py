import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(id=1, email="mary@example.com", password="password", name="mary")
    posts = [
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Another Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Yet another Food Title", person_count=1, cooking_time=1
        )
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
def profile():
    user = model.User(id=2, email="john@example.com", password="password", name="JohnDoe")
    posts = [
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
    ]
    return render_template("main/profile.html", posts=posts)

@bp.route("/bookmark")
def bookmark():
    user = model.User(id=3, email="john@example.com", password="password", name="JohnDoe")
    posts = [
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
    ]
    return render_template("main/bookmark.html", posts=posts)

@bp.route("/recipe")
def recipe():
    user = model.User(id=4, email="test@example.com", password="password", name="testUser")
    posts = [
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
    ]
    return render_template("main/recipe.html", posts=posts)

@bp.route("/new_recipe")
def new_recipe():
    #missing code here to add all of the information from the form into the database
    return render_template("main/new_recipe.html")

#need a controller here to recieve form