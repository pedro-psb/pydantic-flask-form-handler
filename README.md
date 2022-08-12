# Pydantic/Flask Form Handler

## Overview

Helper classes to cut boilerplate on pydantic/flask form and file handling.

The classes `FormHandler` and `FormWithFileHandler` get a flask request and a pydantic
Form Model as parameters. The return is either the validated form data or the errors,
which can have a custom format. By default they are shown per field (which differs form pydantic default).

In the case of files, it handles the file exceptions alongside pydantic validation errors.

```python
try:
    form_data = FormWithFileHandler(
        request=request, FormModel=NameForm
    ).valid_form
    print(form_data)
except FormError as e:
    print(e.errors)
    return redirect(url_for("upload_file_with_form"))
```

## Observations

When `request.form` or `request.files` is accessed, the app raises `werkzeug.exceptions.RequestEntityTooLarge`.
So, if the file is too big, the rest of the form won't be validated.

## TODO

* Write tests
* Feature: allow server-side data injection on the `request.form` data.
* Make it an installable package/plugin/blueprint
