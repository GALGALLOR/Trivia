from flask import Flask,request,render_template,redirect,flash,url_for,session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key='mimi'
marks=0
mydb = MySQL(app)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='GALGALLO10'
app.config['MYSQL_DB']='Trivia'


@app.route('/')
def base():
	return redirect(url_for('home'))

@app.route('/home',methods=['GET','POST'])
def home():
	if request.method =='POST':
		names=request.form['names']
		session['names']=names
		return redirect(url_for('question1'))
	else:
		session.pop('names',None)
		return render_template('trivia.html')

@app.route('/Question1',methods=['GET','POST'])
def question1():
	if 'names' in session:
		if request.method =='POST':
			try:
				president=request.form['president']
				if president == 'kenyatta':
					global marks
					marks=marks+1
					print(marks)
					return redirect(url_for('question2'))
				else:
				
					return redirect(url_for('question2'))
			except:
				return redirect(url_for('question2'))
		else:
			return render_template('question1.html')
	else:
		return redirect(url_for('home'))

@app.route('/Question2',methods=['GET','POST'])
def question2():
	if 'names' in session:
		if request.method =='POST':
			try:
				ww1=request.form['ww1']
				if ww1 == '1918':
					global marks
					marks=marks+1
					print(marks)
					return redirect(url_for('question3'))
				else:
					return redirect(url_for('question3'))
			except:
				return redirect(url_for('question3'))

		else:
			return render_template('question2.html')
	else:
		return redirect(url_for('home'))


@app.route('/Question3',methods=['GET','POST'])
def question3():
	if 'names' in session:
		if request.method =='POST':
			try:
				ageobama=request.form['ageobama']
				if ageobama == '59':
					global marks
					marks=marks+1
					print(marks)
					return redirect(url_for('question4'))
				else:
					return redirect(url_for('question4'))
			except:
				return redirect(url_for('question4'))

		else:
			return render_template('question3.html')
	else:
		return redirect(url_for('home'))

@app.route('/Question4',methods=['GET','POST'])
def question4():
	if 'names' in session:
		if request.method =='POST':
			try:
				nile=request.form['nile']
				if nile == '11':
					global marks
					marks=marks+1
					print(marks)
					
					return redirect(url_for('done'))
	
				else:
					
					return redirect(url_for('done'))
			except:
				
				return redirect(url_for('done'))

		else:
			return render_template('question4.html')
	else:
		return redirect(url_for('home'))

@app.route('/Done',methods=['POST','GET'])
def done():
	if request.method=='POST':
		global marks
		marks=0
		return redirect(url_for('home'))
	else:
		try:
			names=session['names']
			#insert data into database
			cursor = mydb.connection.cursor()
			cursor.execute("INSERT INTO UserData (names,score)VALUES(%s,%s)", (names, marks))
			mydb.connection.commit()
			#reveal the data into a leaderBoard
			cursor.execute('SELECT names,score FROM UserData ORDER BY score DESC ')
			names=cursor.fetchall()
			return render_template('Answersheet.html',names=names,marks=marks)
		except:
			return redirect(url_for('home'))


@app.route('/logout')
def logout():
	session.pop('names',None)
	flash('logged out successfully')
	return redirect(url_for('home'))

if __name__=='__main__':
	app.run(debug=True)
