from flask import Flask, render_template, request, redirect
import sqlite3 as sql

##BDD
import bdd

##Flask
app = Flask(__name__)
app.static_folder = 'static' # dossier où tout ce qui ne bouge pas est ('/static')

@app.route('/') # menu
def home():
	with sql.connect('static/bdd/bdd.db') as con:
		cur = con.cursor()

		races = cur.execute("SELECT nom FROM RACE").fetchall() # toute les races
		couleurs = cur.execute("SELECT DISTINCT(couleur) FROM ANIMAUX").fetchall() # toute les couleurs (unique)
		age_max = cur.execute("SELECT MAX(age) FROM animaux").fetchall()[0][0] # l'age max

	return render_template('/home.html', races=races, couleurs=couleurs, age_max=age_max)

@app.route('/recherche', methods=['GET']) # /recherche
def recherche():
	try:
		with sql.connect('static/bdd/bdd.db') as con:
			cur = con.cursor()
			
			race_get = request.args.get('race', "Tout") # selectionne la valeur du paramètre 'race', si inexistant, choisi 'Tout'
			couleur_get = request.args.get('couleur', "Tout") # pareil
			age_max = request.args.get('age-max', "age") # ...
			sexe_get = request.args.get('sexe', "Tout")
			non_reserve = request.args.get('non-reserve', "reserve")
			trier = request.args.get('trier', "nom")

			if race_get == 'Tout': race = "race" # si pas de choix de race, annuler
			else: race = "'" + race_get + "'" # sinon mettre la race entre guillemets

			if couleur_get == 'Tout': couleur = "couleur" # pareil
			else: couleur = "'" + couleur_get + "'"

			if sexe_get == 'Tout': sexe = "sexe" # ...
			else: sexe = "'" + sexe_get + "'"
			cur.execute("""
				SELECT * FROM ANIMAUX
				WHERE race={race} AND couleur={couleur} AND age<={age_max}
				AND sexe={sexe} AND reserve={non_reserve}
				ORDER BY {trier} ASC
				""".format(race=race, couleur=couleur, age_max=age_max, sexe=sexe, non_reserve=non_reserve, trier=trier)) # requete pour selectionner tout les animaux qui correspondent
			animaux = cur.fetchall()
			cur.close()
		return render_template('requete.html', animaux=animaux)
	except:
		return render_template('400.html') # problème dans la requête

@app.route('/race', methods=['GET'])
def race():
	race_get = request.args.get('type')

	#si la race n'est pas spécifiée
	if race_get is None:
		return redirect('/') #go back home

	try:
		with sql.connect('static/bdd/bdd.db') as con:
			cur = con.cursor()
			race = cur.execute("SELECT * FROM RACE WHERE nom='{race}'".format(race=race_get)).fetchall()[0] # selectionne la race qui correspond à son nom
			cur.close()
		return render_template('race.html', race=race)

	except:
		return render_template('400.html')

@app.route('/environement', methods=['GET'])
def environement():
	env_get = request.args.get('type')

	#si l'environement n'est pas spécifiée
	if env_get is None:
		return redirect('/') #go back home
	
	try:
		with sql.connect("static/bdd/bdd.db") as con:
			cur = con.cursor()
			env = cur.execute("SELECT *  FROM ENVIRONEMENT WHERE biome='{env}'".format(env=env_get)).fetchall()[0] # select l'environement par le nom
			animaux = cur.execute("SELECT * FROM RACE WHERE milieu='{env}'".format(env=env_get)).fetchall() # select les animaux qui vivent dans l'environement
			cur.close()
		return render_template('environement.html', env=env, animaux=animaux)
	
	except:
		return render_template('400.html') # pb dans la requête

@app.route('/soumettre', methods=['GET'])
def soumettre():
	with sql.connect('static/bdd/bdd.db') as con:
		cur = con.cursor()
		races = cur.execute("SELECT nom FROM RACE").fetchall()
		cur.close()
	return render_template("soumettre.html", races=races)

@app.route('/carnet', methods=['GET'])
def carnet():
	tatouage = request.args.get('tatouage')
	print(tatouage)
	if tatouage == None or len(tatouage) != 6 or not tatouage[0:3].isnumeric() or any(map(str.isnumeric, tatouage[3:6])): #mauvais tatouage
		return render_template("400.html") # pb dans la requête

	with sql.connect("static/bdd/bdd.db") as con:
		cur = con.cursor()
		sante = cur.execute("""SELECT CARNET_SANTE.tatouage, nom, race, taille, poids, sexe, vaccine, castre FROM CARNET_SANTE
		INNER JOIN ANIMAUX ON CARNET_SANTE.tatouage = ANIMAUX.tatouage
		WHERE CARNET_SANTE.tatouage='{tatouage}'""".format(tatouage=tatouage)).fetchall()[0] # select l'animal + son carnet à partir de son tatouage
		return render_template("carnet.html", sante=sante)

app.run(debug=True) # lance le site