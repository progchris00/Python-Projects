from website import create_app

app = create_app()

# @app.route('/')
# @app.route('/home')
# def home_page() -> 'html':
#     return render_template('entry.html',
#                             the_title = "Note taking application")

if __name__ =='__main__':
    app.run(debug=True)