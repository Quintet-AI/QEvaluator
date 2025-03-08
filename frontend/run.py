from app import start_app
from flask import Flask, render_template

app = start_app()

if __name__ == "__main__":
    app.run(debug=True)
    

