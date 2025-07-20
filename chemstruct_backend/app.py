from flask import Flask
from routes.predict import predict_bp

app = Flask(__name__)
app.register_blueprint(predict_bp, url_prefix='/api')

@app.route('/')
def home():
    return {'message': 'ChemStruct AI Backend is running!'}

if __name__ == '__main__':
    app.run(debug=True)
