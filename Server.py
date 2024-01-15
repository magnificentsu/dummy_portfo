from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/index.html')
# def my_home2():
#     return render_template('index.html')

@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return "Something must have went wrong. Try again!!"


    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)

# @app.route('/works.html')
# def works_page():
#     return render_template('works.html')
#
# @app.route('/about.html')
# def about_me():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def contact_page():
#     return render_template('contact.html')
#
# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'This is my blog about my dog'
#
