from flask import Flask, jsonify, request
import json
import mysql.connector 

app = Flask(__name__)

user=""
password=""
database="python"
host="localhost"
port="3306"
conn = mysql.connector.connect(host=host,user=user,password=password,port=port, database=database)
cursor = conn.cursor()

@app.route('/informations', methods = ['POST'])
def insert_informations(): 	
	data = json.loads(request.data)
	requete = """ INSERT INTO informations VALUES ("%s", "%s", "%s", %f, %i) ON DUPLICATE KEY UPDATE operatingSystem = "%s", user = "%s", percentRam = %f, usedRam = %i """
	requete = requete % (data["host"],data["os"],data["user"],data["percentRam"],data["usedRam"],data["os"],data["user"],data["percentRam"],data["usedRam"],)
	cursor.execute(requete)
	conn.commit()
	return requete


@app.route('/host/<hostname>')
def host(hostname):
	requete = """ SELECT hostname FROM informations WHERE hostname = '%s' """ % hostname
	cursor.execute(requete)
	for value in cursor:
		reponse = value
	return json.dumps(reponse)


@app.route('/os/<hostname>')
def os(hostname):
	requete = """ SELECT operatingSystem FROM informations WHERE hostname = '%s' """ % hostname
	cursor.execute(requete)
	for value in cursor:
		reponse = value
	return json.dumps(reponse)


@app.route('/user/<hostname>')
def user(hostname):
	requete = """ SELECT user FROM informations WHERE hostname = '%s' """ % hostname
	cursor.execute(requete)
	for value in cursor:
		reponse = value
	return json.dumps(reponse)


@app.route('/percentRam/<hostname>')
def percentRam(hostname):
	requete = """ SELECT percentRam FROM informations WHERE hostname = '%s' """ % hostname
	cursor.execute(requete)
	for value in cursor:
		reponse = value
	return json.dumps(reponse)


@app.route('/usedRam/<hostname>')
def usedRam(hostname):
	requete = """ SELECT usedRam FROM informations WHERE hostname = '%s' """ % hostname
	cursor.execute(requete)
	for value in cursor:
		reponse = value
	return json.dumps(reponse)