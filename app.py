from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{"id": 1, "title": "Data Analyst", "location": "mumbai, india", "salary": "10LPA"},
        {"id": 2, "title": "Data Scientist", "location": "Pune, india", "salary": "12LPA"},
        {"id": 3, "title": "Data Engineer", "location": "Delhi, india"},
        {"id": 4, "title": "Python Developer", "location": "Mumbai, india", "salary": "15LPA"}]

@app.route('/')
def hello_jovian():
    return render_template("home3.html", jobs=JOBS, company_name="jovian")

#@app.route('/')
#def hello_world():
    #return 'Hello, gauree!'

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)
