from website import create_app
from flask import Flask, send_from_directory

app=create_app()

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

#Run web server if you run this file directly
if __name__=='__main__':
    app.run(debug=True)
    
