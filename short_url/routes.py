from flask import Blueprint, render_template, redirect, url_for, request, current_app
from short_url.forms import UrlForm
import random
import string


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(5))  
    return short_url


@pages.route("/", methods=["GET", "POST"])
def index():
    form = UrlForm()
    
    if form.validate_on_submit():
        url = request.form.get("url")
        base_url = request.url_root
        short_url = generate_short_url()
        
        current_app.db.url.insert_one({"original_url": url, "short_url": short_url})
        return render_template("shortend_url.html", base_url=base_url, short_url=short_url, long_url=url)
        
    
    return render_template("index.html", form=form)

@pages.route("/<string:short_url>")
def short_url(short_url: str):
    current_url = current_app.db.url.find_one({"short_url": short_url})
    if current_url:
        original_url = current_url["original_url"]
        return redirect(original_url)
    else:
        return "URL not found"
    

    
    