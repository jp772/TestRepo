from flask import Flask, render_template, flash
from content_management import Content

...


@app.route('/dashboard/')
def dashboard():
    flash("flash test!!!!")
    flash("fladfasdfsaassh test!!!!")
    flash("asdfas asfsafs!!!!")
    return render_template("dashboard.html", TOPIC_DICT=TOPIC_DICT)


