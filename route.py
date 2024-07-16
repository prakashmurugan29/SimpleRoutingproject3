from flask import Flask
app=Flask("__name__")
@app.route('/')
def name():
    return "<div><h1>Hello</h1></div>"
@app.route('/user name')
def name1():
    return "<div><h1>Prakash</h1></div>"
@app.route('/password')
def name2():
    return "<div><h1>Prakash@2004</h1></div>"    
if __name__=='__main__':
    app.run(debug=True)