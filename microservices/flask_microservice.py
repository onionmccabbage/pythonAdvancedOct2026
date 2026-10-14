# pythpn -m pip install flask
from flask import Flask # may neem to pip install flask

# flask is a microservice for serving content over http

def main():
    '''a typical flask development server'''
    # NB there is no built in security in a Flask server
    app = Flask('my_server') # this gives us a fully-fledged http server
    # To use our server, we declare routes
    @app.route('/') # this is root of our server
    def root():
        return 'welcome to this Flask server'

    app.run() # our server begins listening

if __name__ == '__main__':
    main()