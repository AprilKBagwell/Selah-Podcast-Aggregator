from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = 'selah.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def home():
    search_query = request.args.get('q', '')
    conn = get_db_connection()
    if search_query:
        podcasts = conn.execute("SELECT * FROM podcasts WHERE name LIKE ?", ('%' + search_query + '%',)).fetchall()
    else:
        podcasts = conn.execute("SELECT * FROM podcasts").fetchall()
    conn.close()
    return render_template('home.html', podcasts=podcasts, search_query=search_query)

@app.route('/podcast/<int:podcast_id>')
def podcast_details(podcast_id):
    conn = get_db_connection()
    podcast = conn.execute("SELECT * FROM podcasts WHERE id = ?", (podcast_id,)).fetchone()
    episodes = conn.execute("SELECT * FROM episodes WHERE podcast_id = ? ORDER BY pub_date DESC", (podcast_id,)).fetchall()
    conn.close()
    return render_template('podcast-details.html', podcast=podcast, episodes=episodes)

@app.route('/admin/delete/<int:podcast_id>', methods=['POST'])
def delete_podcast(podcast_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM episodes WHERE podcast_id = ?", (podcast_id,))
    conn.execute("DELETE FROM podcasts WHERE id = ?", (podcast_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/admin/search', methods=['GET'])
def admin_search():
    query = request.args.get('q', '')
    conn = get_db_connection()
    podcasts = conn.execute("SELECT * FROM podcasts WHERE name LIKE ?", ('%' + query + '%',)).fetchall()
    conn.close()
    return render_template('home.html', podcasts=podcasts, search_query=query)

if __name__ == '__main__':
    app.run(debug=True)
