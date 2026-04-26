from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

users = {}

inventory = {}

@app.route('/')
def welcome():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        if username not in users:
            users[username] = {'password': password, 'email': email}
            inventory[username] = [] 
            return redirect(url_for('login'))
        else:
            return 'User already exists'
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username]['password'] == password:
            return redirect(url_for('dashboard', username=username))
        elif username not in users:
            return 'User does not exist, please register'
        else:
            return 'Invalid username or password'    
    return render_template('login.html')

@app.route('/dashboard/<username>', methods=['GET', 'POST'])
def dashboard(username):
    if username not in users:
        return redirect(url_for('login'))

    user_items = inventory.get(username, [])
    search_query = request.args.get('search', '').lower().strip()

    if search_query:
        filtered_items = []
        for item in user_items:
            name_match = search_query in item['name'].lower()
            date_match = search_query in str(item['purchase_date']).lower()
            location_match = search_query in item['location'].lower()

            # Use an exact match for 'condition'
            condition_match = item['condition'].lower() == search_query  

            # If the query matches any field, include it
            if name_match or date_match or condition_match or location_match:
                filtered_items.append(item)
    else:
        filtered_items = user_items

    return render_template('dashboard.html', username=username, inventory=filtered_items, search_query=search_query)

@app.route('/item_condition/<username>', methods=['POST'])
def item_condition(username):
    if username not in users:
        return redirect(url_for('login'))

    item_name = request.form.get('item_name')
    condition = request.form.get('condition')
    location = request.form.get('location')
    service_number = request.form.get('service_number') 

    return redirect(url_for('dashboard', username=username))

    


@app.route('/add_item/<username>', methods=['POST'])
def add_item(username):
    if username not in users:
        return redirect(url_for('login'))

    item_name = request.form.get('item_name')
    purchase_date = request.form.get('purchase_date')
    condition = request.form.get('condition')
    location = request.form.get('location')

    if item_name:
        new_item = {
            'name': item_name,
            'purchase_date': purchase_date,
            'condition': condition,
            'location': location
        }
        inventory[username].append(new_item)

        flash("Item Added Successfully", "success")  # Success message

    return redirect(url_for('dashboard', username=username))

# @app.route('/item_condition/<username>', methods=['POST'])
# def item_condition(username):
#     if username not in users:
#         return redirect(url_for('login'))

#     item_name = request.form.get('item_name')
#     condition = request.form.get('condition')
#     location = request.form.get('location')
#     service_number = request.form.get('service_number') 

#     return redirect(url_for('dashboard', username=username))

@app.route('/delete_item/<username>/<int:item_index>')
def delete_item(username, item_index):
    if username in inventory and 0 <= item_index < len(inventory[username]):
        del inventory[username][item_index]
        flash("Item Deleted Successfully", "danger")  # Success message
    return redirect(url_for('dashboard', username=username))

@app.route('/edit_item/<username>/<int:item_index>', methods=['POST'])
def edit_item(username, item_index):
    if username not in users or not (0 <= item_index < len(inventory[username])):
        return redirect(url_for('login'))

    item_name = request.form.get('item_name')
    purchase_date = request.form.get('purchase_date')
    condition = request.form.get('condition')
    location = request.form.get('location')

    if item_name:
        inventory[username][item_index] = {
            'name': item_name,
            'purchase_date': purchase_date,
            'condition': condition,
            'location': location
        }

        flash("Item Updated Successfully", "success")  # Success message

    return redirect(url_for('dashboard', username=username))

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

app.run(debug=True, use_reloader=True)