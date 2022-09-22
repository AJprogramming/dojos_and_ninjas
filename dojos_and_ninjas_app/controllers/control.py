from dojos_and_ninjas_app import app
from flask import render_template,redirect,request,session,flash
from dojos_and_ninjas_app.models.ninjas import Ninja
from dojos_and_ninjas_app.models.dojos import Dojo

# these are all the site's pages
@app.route('/')
@app.route('/dojos')
def dojos():
    return render_template('dojos.html', all_dojos = Dojo.get_all())

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', all_dojos = Dojo.get_all())

@app.route('/dojos/<int:id>')
def show(id):
    data={
        "id" : id
    }
    return render_template('show.html', one_dojo =  Dojo.get_one_dojo(data))

@app.route('/dojos/edit/<int:id>')
def edit(id):
    data = {
        'id' : id
    }
    ninja = Ninja.get_one(data)
    return render_template('edit.html', ninja=ninja)

# redirect
@app.route('/new_ninja', methods=["POST"])
def new_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/create_dojo', methods=["POST"])
def new_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/edit_ninja/<int:dojo_id>', methods=['POST'])
def edit_ninja(dojo_id):
    data ={
        'id' : request.form['id'],
        'f_name' : request.form['f_name'],
        'l_name' : request.form['l_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    Ninja.edit(data)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id" : id
    }
    Ninja.delete(data)
    return redirect('/dojos')
