from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the resume page
@app.route('/resume')
def resume():
    return render_template('resume.html')

# Route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Handle the form submission (e.g., save to database, send email)
        return redirect(url_for('home'))
    return render_template('contact.html')

# Route to handle form submission
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Handle the form submission (e.g., save to database, send email)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

