from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
main_bp = Blueprint("main_bp", __name__)

name = "Jamie"
hobbies = [
    "Gaming",
    "Reading",
    "Soccer",
    "Ballet",
    "Gyming",
    "Yoga",
    "Cricket",
    "Chess",
]

users = [
    {
        "name": "Jeevan",
        "pic": "https://media.istockphoto.com/id/1682296067/photo/happy-studio-portrait-or-professional-man-real-estate-agent-or-asian-businessman-smile-for.jpg?s=612x612&w=0&k=20&c=9zbG2-9fl741fbTWw5fNgcEEe4ll-JegrGlQQ6m54rg=",
        "isVerified": False,
    },
    {
        "name": "Jamie",
        "pic": "https://media.istockphoto.com/id/1437816897/photo/business-woman-manager-or-human-resources-portrait-for-career-success-company-we-are-hiring.jpg?s=612x612&w=0&k=20&c=tyLvtzutRh22j9GqSGI33Z4HpIwv9vL_MZw_xOE19NQ=",
        "isVerified": True,
    },
    {
        "name": "Ethan",
        "pic": "https://t4.ftcdn.net/jpg/03/64/21/11/360_F_364211147_1qgLVxv1Tcq0Ohz3FawUfrtONzz8nq3e.jpg",
        "isVerified": False,
    },
]


#  API / Endpoint
@main_bp.get("/")
def hello_world():
    return render_template("home.html")


# Flask use Jinja2 -> Replace {{}} with python value
@main_bp.get("/about")
def about_page():
    return render_template("about.html", name=name, hobbies=hobbies)


# Task 2 - Create profile page
@main_bp.get("/profile")
def profile_page():
    return render_template("profile.html", users=users)
