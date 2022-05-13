from app import app

@app.route('/')
@app.route('/index') 
@app.route('/test')

def index():
    return "hello, worlddad?????"

def test():
    return "hi this is our test page"
