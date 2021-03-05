import dateutil.parser

from flask import Flask, request, render_template
from flask_adminlte import AdminLTE
from show_cmd import show_cmd


class User(object):
    """
    Example User object.  Based loosely off of Flask-Login's User model.
    """
    full_name = "Alexandre Vasseur"
    avatar = "/static/img/photo.JPG"
    created_at = dateutil.parser.parse("November 12, 2012")


def create_app(configfile=None):
    app = Flask(__name__)
    AdminLTE(app)

    # This is a placeholder user object.  In the real-world, this would
    # probably get populated via ... something.
    current_user = User()

    @app.route('/')
    def index():
        return render_template('index.html', current_user=current_user)
		
    @app.route('/login')
    def login():
        return render_template('login.html', current_user=current_user)

    @app.route('/lockscreen')
    def lockscreen():
        return render_template('lockscreen.html', current_user=current_user)

    @app.route('/show', methods=['GET', 'POST'])
    def show():
        if request.method == 'POST':
            device_name = request.form['device_name']
            cmd = request.form['cmd']
            if request.form['device_name']:
                #device1 = request.form['device1']
                msg1 = str(show_cmd(device_name,cmd))
                #msg = msg1.splitlines()
                msg = msg1.replace('\r\n', '<br>')
                print msg
            else:
                msg = """It's time to enter a valid name!"""
            print device_name
            return render_template('show.html', current_user=current_user, msg=msg)
        elif request.method == 'GET':
            return render_template('show.html', current_user=current_user)

    @app.route('/vlan', methods=['GET', 'POST'])
    def vlan():
        if request.method == 'POST':
            return render_template('vlan.html', current_user=current_user)
        elif request.method == 'GET':

            value1 = []
            value1.append('test2')
            value1.append('test3')
            return render_template('vlan.html', current_user=current_user, value1=value1)
		
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
