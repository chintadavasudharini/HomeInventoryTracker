from flask import Flask, request, redirect, url_for, render_template, flash, session

app = Flask(__name__)
app.secret_key = "your_secret_key"

# In-memory storage (temporary)
users = {}
inventory = {}

# -------------------- HOME --------------------
@app.route('/')
def home():
    return render_template('home.html')


# -------------------- REGISTER --------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        if not username or not password or not email:
            flash("All fields are required!", "danger")
            return redirect(url_for('register'))

        if username in users:
            flash("User already exists!", "danger")
            return redirect(url_for('register'))

        users[username] = {'password': password, 'email': email}
        inventory[username] = []

        flash("Registration successful! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')


# -------------------- LOGIN --------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username not in users:
            flash("User does not exist!", "danger")
            return redirect(url_for('login'))

        if users[username]['password'] != password:
            flash("Invalid password!", "danger")
            return redirect(url_for('login'))

        # ✅ Store session
        session['username'] = username

        flash("Login successful!", "success")
        return redirect(url_for('dashboard'))

    return render_template('login.html')


# -------------------- DASHBOARD --------------------
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash("Please login first!", "danger")
        return redirect(url_for('login'))

    username = session['username']
    user_items = inventory.get(username, [])

    search_query = request.args.get('search', '').lower().strip()

    if search_query:
        filtered_items = []
        for item in user_items:
            if (
                search_query in item['name'].lower()
                or search_query in str(item['purchase_date']).lower()
                or search_query in item['location'].lower()
                or item['condition'].lower() == search_query
            ):
                filtered_items.append(item)
    else:
        filtered_items = user_items

    return render_template(
        'dashboard.html',
        username=username,
        inventory=filtered_items,
        search_query=search_query
    )


# -------------------- ADD ITEM --------------------
@app.route('/add_item', methods=['POST'])
def add_item():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']

    item_name = request.form.get('item_name')
    purchase_date = request.form.get('purchase_date')
    condition = request.form.get('condition')
    location = request.form.get('location')

    if not item_name:
        flash("Item name is required!", "danger")
        return redirect(url_for('dashboard'))

    new_item = {
        'name': item_name,
        'purchase_date': purchase_date,
        'condition': condition,
        'location': location
    }

    inventory[username].append(new_item)

    flash("Item Added Successfully!", "success")
    return redirect(url_for('dashboard'))


# -------------------- DELETE ITEM --------------------
@app.route('/delete_item/<int:item_index>')
def delete_item(item_index):
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']

    if 0 <= item_index < len(inventory[username]):
        del inventory[username][item_index]
        flash("Item Deleted Successfully!", "danger")

    return redirect(url_for('dashboard'))


# -------------------- EDIT ITEM --------------------
@app.route('/edit_item/<int:item_index>', methods=['POST'])
def edit_item(item_index):
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']

    if not (0 <= item_index < len(inventory[username])):
        return redirect(url_for('dashboard'))

    item_name = request.form.get('item_name')
    purchase_date = request.form.get('purchase_date')
    condition = request.form.get('condition')
    location = request.form.get('location')

    if not item_name:
        flash("Item name required!", "danger")
        return redirect(url_for('dashboard'))

    inventory[username][item_index] = {
        'name': item_name,
        'purchase_date': purchase_date,
        'condition': condition,
        'location': location
    }

    flash("Item Updated Successfully!", "success")
    return redirect(url_for('dashboard'))


# -------------------- LOGOUT --------------------
@app.route('/logout')
def logout():
    session.clear()  # ✅ Important
    flash("Logged out successfully!", "info")
    return redirect(url_for('home'))


# -------------------- RUN --------------------
if __name__ == '__main__':
    app.run(debug=True)