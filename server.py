from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/<page_name>")
def html_page(page_name):
  return render_template(page_name)

def write_to_file(data):
  with open("database.txt", mode="a") as database:
    email, subject, message = data['email'], data['subject'], data['message']
    file = database.write(f"\n{email},{subject},{message}")
    print(file)

# https://docs.python.org/3/library/csv.html#csv.writer
# https://stackoverflow.com/questions/3191528/csv-in-python-adding-an-extra-carriage-return-on-windows

def write_to_csv(data):
  with open("database.csv", mode="a", newline="\n") as database:
    email, subject, message = data['email'], data['subject'], data['message']
    csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])


# https://flask.palletsprojects.com/en/1.1.x/quickstart/?highlight=quickstart#the-request-object

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == "POST":
    try:
      data = request.form.to_dict()  # request.form['email']
      # print(data)
      # write_to_file(data)
      write_to_csv(data)
      return redirect("/thankyou.html")
    except: return 'did not save ⬇ to database 🛢'
  else: return 'Something went wrong ❌ Try again 🔙'
