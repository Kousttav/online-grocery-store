from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user import register_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        if form['password'] != form['confirm_password']:
            flash("Passwords do not match.", "danger")
            return render_template('register.html')

        success = register_user({
            "username": form['username'],
            "email": form['email'],
            "mobile": form['mobile'],
            "password": form['password']
        })
        if not success:
            flash("User already exists.", "warning")
            return render_template('register.html')

        flash("Registration successful!", "success")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mobile = request.form['mobile']
        password = request.form['password']
        user = authenticate_user(mobile, password)
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash("Logged in successfully!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials", "danger")
    return render_template('auth/login.html')
