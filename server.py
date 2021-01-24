import tornado.ioloop
import tornado.web
import os
import uuid
import json

class user():
    def __init__(self):
        self.email = email
        self.name = username
        self.id = UUID
        self.albums = []
        self.pictures = []

database = {}

database['users'] = []
database['users'].append({
    'id': '89154a32-526f-431c-991c-1e262498b8b6',
    'name': 'Noah',
    'files': [
        'c94ec089-ab7f-40da-a5a0-c13c5a293f10',
        '191b3cce-0ce5-40e9-ae3e-983385469bcb',
        '3f543cc6-ae15-48df-8334-eb5084d9acb9'
    ]
})
database['users'].append({
    'id': '89154a32-526f-431c-991c-1e262498b8b6',
    'name': 'Noah',
    'files': [
        'c94ec089-ab7f-40da-a5a0-c13c5a293f10',
        '191b3cce-0ce5-40e9-ae3e-983385469bcb',
        '3f543cc6-ae15-48df-8334-eb5084d9acb9'
    ]
})
database['users'].append({
    'id': '89154a32-526f-431c-991c-1e262498b8b6',
    'name': 'Noah',
    'files': [
        'c94ec089-ab7f-40da-a5a0-c13c5a293f10',
        '191b3cce-0ce5-40e9-ae3e-983385469bcb',
        '3f543cc6-ae15-48df-8334-eb5084d9acb9'
    ]
})

with open('database.txt', 'w') as json_file:
    json.dump(database, json_file)

__UPLOADS__ = "uploads/"


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class ViewHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument('id')
        if (id):
            with open(f'uploads/{id}.JPG', 'rb') as f:
                data = f.read()
                self.write(data)
        else:
            self.write("Id not given")

    pass


class ImageHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument('id')
        if (id):
            with open(f'uploads/{id}.JPG', 'rb') as f:
                data = f.read()
                self.write(data)
        else:
            self.write("Id not given")

    pass

# To upload files to the database
class FileHandler(tornado.web.RequestHandler):
    def post(self):
        filesList = self.request.files['filearg']
        for i in range(len(filesList)):
            fileinfo = filesList[i]
            fname = fileinfo['filename']
            extn = os.path.splitext(fname)[1]
            cname = str(uuid.uuid4()) + extn
            fh = open(__UPLOADS__ + cname, 'wb')
            fh.write(fileinfo['body'])
        self.finish(f'{len(filesList)} Files have been uploaded!!')

# To query the database for user data

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_body_argument("emailarg", default=None, strip=False)
        password = self.get_body_argument("passwordarg", default=None, strip=False)
        confirm_password = self.get_body_argument("confirm_passwordarg", default=None, strip=False)
        if password != confirm_password:
            self.render('login.html')
        else:
            self.write(f'logged in as {email}')

class SignUpHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('signup.html')

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user')
        print('trying')
        try:
            db = open(f'database.txt')
            db = json.load(db)
            print(db['users'][0])
            for index in db['users']:
                if index['id'] == user:
                    self.write(index)
        except:
            self.write('User not found')


class LoginPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/upload", FileHandler),
        (r"/view", ViewHandler),
        (r"/user", UserHandler),
        (r"/login", LoginHandler),
        (r"/signup", SignupHandler),
        (r"/login_page", LoginPageHandler)
    ])


if __name__ == "__main__":
    print('Server started on port: 8888')
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

#single session UUID
#After logging in
#That session is linked to the id
#stored in ram in a dict linked to your user file
#files are in files under users
#user files have UUID names
#UUID.txt for example
#User class
