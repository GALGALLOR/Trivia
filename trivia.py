from flask import Flask,request,render_template,redirect,flash,url_for,session
app=Flask(__name__)
app.secret_key='mimi'



@app.route('/')
def base():
	return redirect(url_for('home'))
@app.route('/home',methods=['GET','POST'])
def home():
	if request.method =='POST':
		names=request.form['names']
		session['names']=names
		return redirect(url_for('questions'))
	else:
			return render_template('trivia.html')

@app.route('/Questions',methods=['GET','POST'])
def questions():
	if 'names' in session:
		if request.method =='POST':
			try:
				president=request.form['president']
				ww1=request.form['ww1']
				print(ww1)
				print(president)
			finally:
				if president=='kenyatta':
					p='correct! President is Kenyatta'
				elif president !='kenyatta':
					p='Wrong!President is kenyatta'
				if ww1 == '1918':
					ww='yes, World War 1 occured in 1918'
				elif ww1 !='1918':
					ww = 'No , World War one occured in 1918'
				return f'<h1>{p},{ww}  </h1>'
		else:
			return render_template('questions.html')
	else:
		return render_template('trivia.html')

@app.route('/logout')
def logout():
	session.pop('username',None)
	flash('logged out successfully')
	return redirect(url_for('home'))

if __name__=='__main__':
	app.run(debug=True)