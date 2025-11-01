from flask import Flask
from flask import *

app =Flask(__name__)


@app.route('/home')
def home():
    return'Welcome'

@app.route('/home/<name>')
def homename(name):
    return'Welcome '+name

@app.route('/age/<int:age>')
def age(age):
    return'age %d'%age

@app.route('/age2/<age>')
def age2(age):
    return('Rathin '+ age)



#add url rule


def haii():
    return('hi ')
app.add_url_rule('/hiii','haiiii',haii)


@app.route('/ad')
def admin():
    return'Hai Admin'

@app.route('/st')
def stud():
    return'Hai Student'

@app.route('/th')
def teach():
    return'Hai Teacher'

@app.route('/user/<name>')
def user(name):

    if name =='ad':
        return redirect(url_for('admin'))
    if name =='st':
        return redirect(url_for('stud'))
    if name =='th':
        return redirect(url_for('teach'))

@app.route('/loadpost',methods= ['POST','GET'])
def post_data():
    if request.method=='POST':
        n = request.form['name']
        e = request.form['email']
        p = request.form['Place']
        return'Success'
    if request.method=='GET':
        return render_template('dataload.html')



@app.route('/loadget',methods= ['GET'])
def get_data():
    if request.method=='GET':
        n = request.args.get('name')
        e = request.args.get('email')
        p = request.args.get('Place')
        return'Success'


@app.route('/pass')
def data_pass():
    name='Ram'
    return render_template('dataload.html',n =name,age =22)

@app.route('/empre',methods=['GET','POST'])
def emreg():
    if request.method=='GET':
        return render_template('empreg.html')
    else:
        res=request.form
        return render_template('empview.html',data=res)
    

# cookies

@app.route('/setc')
def set_c ():
    res = make_response('<h1>Cookies set </h1>')
    res.set_cookie('name','Ram')
    return res
@app.route('/getc')
def get_c ():
    x= request.cookies.get('name')
    return x

# session

app.secret_key='1234'
@app.route('/sets')
def set_s ():
    session['email']='rathin@gmail.com'
    res= make_response('<h1>session set </h1>')
    return res

@app.route('/gets')
def get_s():
    if 'email' in session:
        x = session['email']
        return x
    else:
        return'Error'
    
@app.route('/dels')
def del_s ():
    del session['email']
    return 'Deleted!'
    

if __name__ == '__main__':
    app.run(debug=True)





