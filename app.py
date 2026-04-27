from flask import Flask, request, redirect, url_for, render_template, flash, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key"

users = {}
inventory = {}

# Decorator for route protection
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please log in first', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        if username in users:
            flash('User already exists', 'error')
            return redirect(url_for('login'))
        
        users[username] = {'password': password, 'email': email}
        inventory[username] = []
        flash(' Registration successful! Please login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username]['password'] == password:
            session['username'] = username
            flash(' Login successful!', 'success')
            return redirect(url_for('dashboard'))
        elif username not in users:
            flash('User does not exist, please register', 'error')
            return redirect(url_for('register'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    username = session['username']
    user_items = inventory.get(username, [])
    search_query = request.args.get('search', '').lower().strip()

    if search_query:
        filtered_items = []
        for item in user_items:
            name_match = search_query in item['name'].lower()
            date_match = search_query in str(item['date']).lower()
            location_match = search_query in item['location'].lower()
            condition_match = item['condition'].lower() == search_query

            if name_match or condition_match or date_match or location_match:
                filtered_items.append(item)
    else:
        filtered_items = user_items

    return render_template('dashboard.html', username=username, inventory=filtered_items, search_query=search_query)

@app.route('/item_condition', methods=['POST'])
@login_required
def item_condition():
    username = session['username']
    
    item_name = request.form.get('item_name')
    condition = request.form.get('condition')
    location = request.form.get('location')
    date = request.form.get('date')
    service_number = request.form.get('service_number')

    return redirect(url_for('dashboard'))

    


@app.route('/add_item', methods=['POST'])
@login_required
def add_item():
    username = session['username']
    
    item_name = request.form.get('item_name')
    date = request.form.get('date')
    condition = request.form.get('condition')
    location = request.form.get('location')

    if item_name:
        new_item = {
            'name': item_name,
            'date': date,
            'condition': condition,
            'location': location
        }
        inventory[username].append(new_item)
        flash(" Item Added Successfully ✅", "success")
    else:
        flash("Please enter an item name", "error")

    return redirect(url_for('dashboard'))

@app.route('/delete_item/<int:item_index>')
@login_required
def delete_item(item_index):
    username = session['username']
    
    if 0 <= item_index < len(inventory[username]):
        del inventory[username][item_index]
        flash(" Item Deleted Successfully ❌", "danger")
    else:
        flash("Item not found", "error")
    
    return redirect(url_for('dashboard'))

@app.route('/edit_item/<int:item_index>', methods=['POST'])
@login_required
def edit_item(item_index):
    username = session['username']
    
    if not (0 <= item_index < len(inventory[username])):
        flash("Item not found", "error")
        return redirect(url_for('dashboard'))

    item_name = request.form.get('item_name')
    date = request.form.get('date')
    condition = request.form.get('condition')
    location = request.form.get('location')

    if item_name:
        inventory[username][item_index] = {
            'name': item_name,
            'date': date,
            'condition': condition,
            'location': location
        }
        flash("Item Updated Successfully ✏️ ", "info")
    else:
        flash("Please enter an item name", "error")

    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'danger')
    return redirect(url_for('home'))

app.run(debug=True, use_reloader=True)