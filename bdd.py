#Importation du module (librairie) sqlite3
#NULL en SQL correspond à None en Python
import sqlite3

#Création d'une connexion avec la BDD Livres.db
#Les propriétés de la BDD sont stockées dans l'objet conn
conn = sqlite3.connect('static/bdd/bdd.db')
#Création de l'objet cur qui va permettre d'agir sur la BDD
cur = conn.cursor()

#Supprime les 4 tables

cur.execute("DROP TABLE ENVIRONEMENT;")
cur.execute("DROP TABLE CARNET_SANTE;")
cur.execute("DROP TABLE RACE;")
cur.execute("DROP TABLE ANIMAUX;")


#table CARNET_SANTE
cur.execute("""CREATE TABLE CARNET_SANTE
(
	tatouage TEXT,
	vaccine BOOL,
	taille INT,
	poids INT,
	castre BOOL,

	PRIMARY KEY(tatouage)
);""")

#table ENVIRONEMENT
cur.execute("""CREATE TABLE ENVIRONEMENT
(
	biome TEXT,
	milieu TEXT,
	temp_moyenne INT,
	precipitation_moyenne INT,

	PRIMARY KEY(biome)
);""")

#table RACE
cur.execute("""CREATE TABLE RACE
(
	nom TEXT,
	temperament TEXT,
	pelage TEXT,
	esperance_vie INT,
	milieu TEXT,

	PRIMARY KEY(nom),
	FOREIGN KEY(milieu) REFERENCES ENVIRONEMENT(biome)
);""")

#table ANIMAUX
cur.execute("""CREATE TABLE ANIMAUX
(
	tatouage TEXT,
	nom TEXT,
	race TEXT,
	couleur TEXT,
	age INT,
	sexe TEXT,
	reserve BOOL,

	PRIMARY KEY(tatouage),
	FOREIGN KEY(tatouage) REFERENCES CARNET_SANTE(tatouage),
	FOREIGN KEY(race) REFERENCES RACE(nom)
);""")

#valeurs de ENVIRONEMENT
cur.execute("""INSERT INTO ENVIRONEMENT(biome, milieu, temp_moyenne, precipitation_moyenne)
VALUES
	('plaine', 'terrestre', 22, 2240),
	('forêt', 'terrestre', 10, 100),
	('savane', 'terrestre', 25, 1237),
	('océan', 'marin', 12, 100),
	('rivière', 'marin', 8, 1284),
	('banquise', 'terrestre', -18, 853),
	('montagne', 'terrestre', 14, 1450),
	('désert', 'terrestre', 43, 125);""")

#valeurs de RACE
cur.execute("""INSERT INTO RACE(nom, temperament, pelage, esperance_vie, milieu)
VALUES
	('chat', 'affectueux', 'moyen', 15, 'plaine'),
	('chien', 'affectueux', 'moyen', 16, 'plaine'),
	('rat', 'énérgique', 'court', 4, 'plaine'),
	('chèvre', 'énérgique', 'long', 17, 'montagne'),
	('pingouin', 'calme', 'plumes', 20, 'banquise'),
	('lion', 'agressif', 'long', 15, 'savane'),
	('serpent', 'agressif', 'absent', 20, 'désert'),
	('étoile de mer', 'passif', 'absent', 5, 'océan'),
	('loup', 'agressif', 'long', 16, 'forêt');""")

#valeurs de CARNET_SANTE

#valeurs de ANIMAUX
cur.execute("""INSERT INTO ANIMAUX(tatouage, nom, race, couleur, age, sexe, reserve)
VALUES
	('123ABC', 'cookie', 'chat', 'noir', 9, 'masculin', true),
	('420AAA', 'ponyo', 'chat', 'gris', 8, 'feminin', false),
	('696EHE', 'patrick', 'étoile de mer', 'rose', 2, 'feminin', false),
	('028IHI', 'zorro', 'chèvre', 'blanc', 7,  'masculin', true),
	('294HDU', 'tanguy', 'chien', 'marron', 9, 'masculin', false),
	('49FHGU', 'malaria', 'chien', 'roux', 12, 'feminin', true),
	('234APE', 'eline', 'chien', 'tacheté', 10, 'feminin', true),
	('203ODO', 'anarchy', 'chien', 'noir', 11, 'feminin', true),
	('000OOO', 'igor', 'chat', 'roux', 4, 'masculin', false),
	('420ARA', 'chinai', 'chat', 'tacheté', 3, 'feminin', false),
	('475UET', 'quinai', 'chat', 'blanc', 2, 'feminin', false),
	('354YEH', 'sasuke', 'serpent', 'noir', 16, 'masculin', true),
	('283OIP', 'jungle', 'serpent', 'violet', 8, 'feminin', false),
	('789OOF', 'skipper', 'pingouin', 'blanc', 7, 'masculin', false),
	('253UDH', 'kowalski', 'pingouin', 'blanc', 9, 'masculin', false),
	('126EYD', 'soldat', 'pingouin', 'blanc', 8, 'masculin', false),
	('293IDO', 'rico', 'pingouin', 'blanc', 7, 'masculin', false),
	('364LOL', 'twitch', 'rat', 'gris', 2, 'masculin', true),
	('234UEY', 'totoro', 'chèvre', 'blanc', 36, 'feminin', true),
	('123ETU', 'zapata', 'chat', 'gris', 7, 'feminin', true),
	('374UET', 'toto', 'chien', 'gris', 7, 'masculin', false),
	('923EKD', 'ratatouille', 'rat', 'gris', 2, 'masculin', false),
	('235ATU', 'mallow', 'chat', 'blanc', 8, 'feminin', true),
	('690LYO', 'suke', 'chat', 'blanc', 8, 'feminin', true),
	('123PDP', 'dalaï', 'lama', 'roux', 69, 'masculin', false),
	('001OOF', 'roy', 'lion', 'roux', 32, 'masculin', true),
	('002OOF', 'marceline', 'chèvre', 'roux', 32, 'masculin', true),
	('003OOF', 'cody', 'pingouin', 'blanc', 16, 'masculin', false),
	('004OOF', 'simba', 'lion', 'roux', 12, 'masculin', true),
	('005OOF', 'rafiki', 'singe', 'marron', 17, 'feminin', true),
	('006OOF', 'gribouille', 'chat', 'vert', 4, 'masculin', false),
	('007OOF', 'milord', 'chien', 'blanc', 7, 'masculin', true),
	('008OOF', 'scott', 'chien', 'gris', 12, 'masculin', true),
	('009OOF', 'misty', 'chat', 'roux', 2, 'feminin', false),
	('000FDP', 'maïca', 'chien', 'blanc', 6, 'feminin', true),
	('000DPD', 'clifford', 'chien', 'marron', 8, 'masculin', false),
	('001DPD', 'kawano', 'rat', 'gris', 8, 'feminin', false),
	('002DPD', 'tomoe', 'rat', 'gris', 8, 'masculin', true),
	('003DPD', 'ahou', 'loup', 'blanc', 7, 'masculin', false),
	('004DPD', 'onyx', 'chien', 'noir', 8, 'masculin', false),
	('005DPD', 'weasley', 'chat', 'roux', 3, 'masculin', true),
	('006DPD', 'ryuji', 'chat', 'marron', 12, 'feminin', false),
	('420DPD', 'rodger', 'lapin', 'blanc', 4, 'masculin', true),
	('420OOF', 'toyota', 'rat', 'gris', 3, 'feminin', true),
	('283HDY', 'supra', 'rat', 'gris', 5, 'feminin', false),
	('273UEY', 'cassiopé', 'chat', 'roux', 6, 'feminin', true),
	('374EHU', 'gribouille', 'chat', 'gris', 8, 'masculin', false),
	('111III', 'mario', 'chat', 'blanc', 6, 'masculin', true),
	('234AZE', 'luigi', 'chat', 'noir', 7, 'masculin', true),
	('192UEG', 'boubou', 'étoile de mer', 'violet', 8, 'masculin', true);""")


cur.execute("""INSERT INTO CARNET_SANTE(tatouage, vaccine, taille, poids, castre)
VALUES
	('123ABC', true, 24, 4800, true),
	('420AAA', false, 23, 4250, true),
	('696EHE', false, 19, 1200, false),
	('028IHI', true, 45, 63700, false),
	('294HDU', false, 53, 32100, true),
	('49FHGU', true, 56, 30300, true),
	('234APE', false, 48, 28500, true),
	('203ODO', true, 51, 31300, false),
	('000OOO', true, 26, 5300, false),
	('420ARA', false, 21, 3800, true),
	('475UET', true, 24, 6400, true),
	('354YEH', true, 82, 1300, false),
	('283OIP', false, 103, 2300, false),
	('789OOF', true, 108, 35400, true),
	('253UDH', false, 112, 36600, false),
	('126EYD', false, 111, 35200, true),
	('293IDO', true, 102, 31500, false),
	('364LOL', true, 46, 390, true),
	('234UEY', true, 50, 46500, false),
	('123ETU', true, 30, 6500, true),
	('374UET', true, 56, 42700, false),
	('923EKD', false, 40, 420, false),
	('235ATU', true, 21, 3900, false),
	('690LYO', true, 25, 4600, true),
	('123PDP', false, 130,150000, true),
	('001OOF', true, 190, 165000, false),
	('002OOF', false, 52, 8000, true),
	('003OOF', false, 121, 660, false),
	('004OOF', false, 180, 150000, false),
	('005OOF', true, 62, 12600, true),
	('006OOF', false, 22, 4100, true),
	('007OOF', false, 68, 19400, true),
	('008OOF', true, 48, 8600, true),
	('009OOF', false, 26, 5200, true),
	('000FDP', true, 60, 29400, true),
	('000DPD', true, 76, 34500,false),
	('001DPD', true, 18, 120, true),
	('002DPD', true, 27, 340, true),
	('003DPD', false, 90, 61000, false),
	('004DPD', false, 76, 34700, true),
	('005DPD', true, 25, 4500, true),
	('006DPD', false, 22, 3800, true),
	('420DPD', true, 28, 990, false),
	('420OOF', true, 22, 850, true),
	('283HDY', true, 19, 675, true),
	('273UEY', false, 27, 6000, true),
	('374EHU', true, 24, 5100, true),
	('111III', false, 26, 5500, true),
	('234AZE', true, 22, 4700, false),
	('192UEG', false, 38, 24000,false);""")

#Validation et enregistrement des modifications dans la BDD
conn.commit()
#On ferme le curseur
cur.close()
#On ferme la connection avec la BDD
conn.close()