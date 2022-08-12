"""The main app"""

from flask import Flask, redirect, request, url_for

from forms import NameForm
from utils.form_handler import FormWithFileHandler
from utils.form_handler.exceptions import FormError

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 1 * 1000 * 1000


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # try:
        #     file = request.files.get("file")
        #     file = ImageFileSaver(file=file)
        #     filepath = file.save_using_uuid()
        #     print(filepath)
        # except ValidationError as e:
        #     print(e)
        return redirect(url_for("upload_file"))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """


@app.route("/with_form", methods=["GET", "POST"])
def upload_file_with_form():
    if request.method == "POST":
        try:
            form_data = FormWithFileHandler(
                request=request, FormModel=NameForm
            ).valid_form
            print(form_data)
        except FormError as e:
            print(e.errors)
            return redirect(url_for("upload_file_with_form"))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=text name=name>
      <input type=text name=age>
      <input type=submit value=Upload>
    </form>
    """
