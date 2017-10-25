from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)


@app.route('/')
def root():
  return render_template('home.html')

@app.route('/movies/')
def movies():
  return render_template('movies.html')

@app.route('/characters/')
def characters():
  return render_template('characters.html')

@app.route('/characters/Spiderman/')
def characters1():
  return render_template('Spiderman.html')

@app.route('/signin/',methods=["GET","POST"])
def signin():
  error=None
  if request.method == "POST":
      attempted_emailaddress = request.form['emailaddress']
      attempted_password = request.form['password']
      
      if attempted_emailaddress == "111@111" and attempted_password == "password":
          return redirect(url_for('root'))
      else:
          error = "Invalid credentials. Try Again."
         
  return render_template('signin.html',error=error)  

@app.route('/signin/signup/')
def signin1():
  return render_template('signup.html')

@app.errorhandler(404)
def page_not_found( error ):
  return("Sorry,Couldn't find your page,this web page is designing...:D")



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
