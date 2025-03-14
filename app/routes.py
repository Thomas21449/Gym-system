from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Member
from gym_manager import GymManager

gm = GymManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        plan = request.form['plan']
        access_frequency = request.form['access_frequency']

        member_id = gm.add_member(name, email, plan, access_frequency)
        flash(f'Aluno cadastrado com ID: {member_id}', 'success')
        return redirect(url_for('index'))

    return render_template('cadastrar.html')

@app.route('/listar')
def listar():
    members = gm.list_members(filter_type="todos")
    return render_template('listar.html', members=members)