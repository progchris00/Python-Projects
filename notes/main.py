from website import create_app

app = create_app()

@app.route('/')
@app.route('/home')
def home_page() -> 'html':
    return render_template('entry.html',
                            the_title = "Note taking application")

@app.route('/login')
def login_page() -> 'html':
    return render_template('login.html',
                            the_title = "Login")

@app.route('/signup')
def signup_page() -> 'html':
    return render_template('signup.html',
                            the_title = "Sign Up")
    
if __name__ =='__main__':
    app.run(debug=True)