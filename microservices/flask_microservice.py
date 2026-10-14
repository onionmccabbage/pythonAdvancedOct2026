# pythpn -m pip install flask
from flask import Flask # may neem to pip install flask
from flask import render_template # this lets us build HTML content
from yield_example import makeDateTimeStamp
from my_api import getJSON
# flask is a microservice for serving content over http

def main():
    '''a typical flask development server'''
    ts = makeDateTimeStamp()
    # NB there is no built in security in a Flask server
    app = Flask('my_server') # this gives us a fully-fledged http server
    # To use our server, we declare routes
    @app.route('/') # this is root of our server
    def root():
        return 'welcome to this Flask server'
    @app.route('/greet')
    def greet():
        now = ts.__next__()
        return f'Welcome user, the time is {now}'
    # we may provide routes for alternative access
    @app.route('/aluminium')
    @app.route('/aluminum') # we may have multiple routes that end up with the same content
    def al():
        return 'it is spelled `aluminium`'
    @app.route('/data')
    def data():
        # here we could retreive from file, db, api ....
        r = getJSON()
        part = r['title']
        response = f'<h3>Data goes here</h3>{part}'
        return response
    # we may need to make use of URL parameters
    @app.route('/person') # with no arguments
    @app.route('/person/<person>')
    def person(person='Ethel'):
        '''retrieve any URL parameter and use it in the returned data'''
        # return f'Parameter is {person}'
        # we need to pass in any arguments to the page
        return render_template('person+page.html', person=person)


    app.run() # our server begins listening

if __name__ == '__main__':
    main()