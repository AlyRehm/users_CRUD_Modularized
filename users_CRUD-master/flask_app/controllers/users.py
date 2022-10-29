from flask import render_template, redirect, request

from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', users=User.get_all_users())

@app.route('/create_user')
def create():
    return render_template('create.html')

@app.route('/user/create', methods=['POST'])
def add():
    User.new_user(request.form)
    return redirect('/users')


# route for editing user
@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))


#ROUTE TO RETURN TO TO EDIT USERS 
@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


#ROUTE FOR DELETING USER   
# note to self - be aware that 'delete' can be a reserved word in some languages 
@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={ 
        "id":id
    }
    User.destroy(data)
    return redirect('/users')


#ROUTE TO RETURN TO TO SHOW USERS 
# similiar to the edit, but this time we just want to view 
@app.route('/user/view/<int:id>')
def view(id):
    data ={ 
        "id":id
    }
    return render_template("view_user.html",user=User.get_one(data))
