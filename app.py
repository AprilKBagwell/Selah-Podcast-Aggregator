from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Enable dictionary-style row access
def get_db_connection():
    conn = sqlite3.connect('selah.db')
    conn.row_factory = sqlite3.Row
    return conn

# Context processor to access datetime in templates
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow}

@app.route('/')
def home():
    conn = get_db_connection()
    search_query = request.args.get('q', '')

    if search_query:
        podcasts = conn.execute("SELECT * FROM podcasts WHERE name LIKE ? ORDER BY name ASC", 
                                ('%' + search_query + '%',)).fetchall()
    else:
        podcasts = conn.execute('SELECT * FROM podcasts ORDER BY name ASC').fetchall()

    conn.close()
    return render_template('home.html', podcasts=podcasts)

@app.route('/podcast/<int:podcast_id>')
def podcast_details(podcast_id):
    conn = get_db_connection()
    podcast = conn.execute('SELECT * FROM podcasts WHERE id = ?', (podcast_id,)).fetchone()
    episodes = conn.execute('SELECT * FROM episodes WHERE podcast_id = ? ORDER BY pub_date DESC', 
                            (podcast_id,)).fetchall()
    conn.close()
    return render_template('podcast-details.html', podcast=podcast, episodes=episodes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
