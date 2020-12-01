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
		session.pop('question1',None)
		session.pop('question2',None)
		session.pop('question3',None)
		session.pop('question4',None)
		session.pop('question5',None)
		session.pop('question6',None)
		session.pop('question7',None)
		session.pop('question8',None)
		session.pop('question9',None)
		session.pop('question10',None)

		return render_template('trivia.html')

@app.route('/Question1',methods=['GET','POST'])
def question1():
	if 'names' in session:
		if request.method =='POST':
			session['question1']='question1'
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
			if 'question1' in session:
				marks=marks-1
			return render_template('question1.html')
	else:
		return redirect(url_for('home'))

@app.route('/Question2',methods=['GET','POST'])
def question2():
	if 'names' in session:
		if request.method =='POST':
			session['question2']='question2'
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
			if 'question2' in session:
				marks=marks-1
			return render_template('question2.html')
	else:
		return redirect(url_for('home'))


@app.route('/Question3',methods=['GET','POST'])
def question3():
	if 'names' in session:
		if request.method =='POST':
			session['question3']='question3'
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
			if 'question3' in session:
				marks=marks-1
			return render_template('question3.html')
	else:
		return redirect(url_for('home'))

@app.route('/Question4',methods=['GET','POST'])
def question4():
	if 'names' in session:
		if request.method =='POST':
			session['question4']='question4'
			try:
				nile=request.form['nile']
				if nile == '11':
					global marks
					marks=marks+1
					print(marks)
					
					return redirect(url_for('question5'))
	
				else:
					
					return redirect(url_for('question5'))
			except:
				
				return redirect(url_for('question5'))

		else:
			if 'question4' in session:
				marks=marks-1	
			return render_template('question4.html')
	else:
		return redirect(url_for('home'))


@app.route('/Question5',methods=['GET','POST'])
def question5():
	if 'names' in session:
		if request.method =='POST':
			session['question5']='question5'
			try:
				apple=request.form['apple']
				if apple == 'ronald':
					global marks
					marks=marks+1
					print(marks)
					return redirect(url_for('question6'))
				else:
					return redirect(url_for('question6'))
			except:
				return redirect(url_for('question6'))

		else:
			if 'question5' in session:
				marks=marks-1
			return render_template('question5.html')
	else:
		return redirect(url_for('home'))

@app.route('/Question6',methods=['GET','POST'])
def question6():
	if 'names' in session:
		session['question6']='question6'
		if request.method =='POST':
			try:
				facebook=request.form['facebook']
				if facebook == '2004':
					global marks
					marks=marks+1
					print(marks)
					return redirect(url_for('question7'))
				else:
					return redirect(url_for('question7'))
			except:
				return redirect(url_for('question7'))

		else:
			if 'question6' in session:
				marks=marks-1
			return render_template('question6.html')
	else:
		return redirect(url_for('home'))

@app.route('/Question7',methods=['GET','POST'])
def question7():
	if 'names' in session:
		if request.method =='POST':
			session['question7']='question7'
			try:
				romania=request.form['romania']
				if romania == 'bucharest':
					global marks
					marks=marks+1
					print(marks)
					return redirect(url_for('question8'))
				else:
					return redirect(url_for('question8'))
			except:
				return redirect(url_for('question8'))

		else:
			if 'question7' in session:
				marks=marks-1
			return render_template('question7.html')
	else:
		return redirect(url_for('home'))

@app.route('/Question8',methods=['GET','POST'])
def question8():
	if 'names' in session:
		if request.method =='POST':
			session['question8']='question8'
			try:
				europe=request.form['europe']
				if europe == 'vaticancity':
					global marks
					marks=marks+1
					print(marks)
					return redirect(url_for('question9'))
				else:
					return redirect(url_for('question9'))
			except:
				return redirect(url_for('question9'))

		else:
			if 'question8' in session:
				marks=marks-1	
			return render_template('question8.html')
	else:
		return redirect(url_for('home'))

@app.route('/Question9',methods=['GET','POST'])
def question9():
	if 'names' in session:
		if request.method =='POST':
			session['question9']='question9'
			try:
				china=request.form['china']
				if china == '2000':
					global marks
					marks=marks+1
					print(marks)
					return redirect(url_for('question10'))
				else:
					return redirect(url_for('question10'))
			except:
				return redirect(url_for('question10'))

		else:
			if 'question9' in session:
				marks=marks-1
			return render_template('question9.html')
	else:
		return redirect(url_for('home'))

@app.route('/Question10',methods=['GET','POST'])
def question10():
	if 'names' in session:
		if request.method =='POST':
			session['question10']='question10'
			try:
				tallest=request.form['tallest']
				if tallest == '2716 feet':
					global marks
					marks=marks+1
					print(marks)
					return redirect(url_for('done'))
				else:
					return redirect(url_for('done'))
			except:
				return redirect(url_for('done'))

		else:
			if 'question10' in session:
				marks=marks-1
			return render_template('question10.html')
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
			current_names=session['names']
			#insert data into database
			cursor = mydb.connection.cursor()
			cursor.execute("INSERT INTO UserData (names,score)VALUES(%s,%s)", (names, marks))
			mydb.connection.commit()
			#reveal the data into a leaderBoard
			
			cursor.execute('SELECT ROW_NUMBER() OVER() AS num_row, names, score FROM UserData ORDER BY score DESC ')
			names=cursor.fetchall()
			return render_template('Answersheet.html',current_names = current_names,names=names,marks=marks)
		except:
			return redirect(url_for('home'))

@app.route('/leaderboard')
def leaderboard():
	cursor = mydb.connection.cursor()
	cursor.execute('SELECT ROW_NUMBER() OVER(ORDER BY score DESC) AS num_row, names, score FROM UserData')
	names=cursor.fetchall()
	return render_template('leaderboard.html',names=names,marks=marks)

@app.route('/logout')
def logout():
	session.pop('names',None)
	flash('logged out successfully')
	return redirect(url_for('home'))

if __name__=='__main__':
	app.run(debug=True)
