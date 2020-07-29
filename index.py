import os
from flask import render_template, request, redirect, url_for
from werkzeug import secure_filename

# Create a directory in a known location to save files to.
uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exists_ok=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # save the single "profile" file
        profile = request.files['profile']
        profile.save(os.path.join(uploads_dir, secure_filename(profile.filename)))

        # save each "charts" file
        for file in request.files.getlist('charts'):
            file.save(os.path.join(uploads_dir, secure_filename(file.name)))

        return redirect(url_for('upload'))

    return render_template('upload.html')