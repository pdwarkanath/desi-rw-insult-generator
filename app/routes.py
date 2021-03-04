from flask import render_template
from app import app
import numpy.random as r
from insults import *

@app.route('/')
@app.route('/index')
def index():
	rand_adj = adjective[r.randint(0, high=adj_len)]
	rand_anti = anti[r.randint(0, high=anti_len)]
	rand_adj1 = adjective1[r.randint(0, high=adj1_len)]
	rand_hero = hero[r.randint(0, high=hero_len)]

	txt = f'You {rand_adj}, {rand_anti} {rand_adj1} {rand_hero}'
	return render_template('index.html', txt = txt)

