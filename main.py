from website import create_app

app = create_app()

# only if we run this file, are we going to execute this line.
if __name__ == '__main__':
    #this is going to run our flask app. Debug = True means that any time we make a change to our python code it's going to
    #automatically rerun our python server.
    # you are going to turn this off when you are running in production.
    app.run(debug=True)