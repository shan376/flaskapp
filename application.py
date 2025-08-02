from flask import Flask
application = Flask(__name__)

@application.route('/')
def home():
    return "Hello from AWS Elastic Beanstalk!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 8080))
    application.run(host='0.0.0.0', port=port)
