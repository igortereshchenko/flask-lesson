from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# TODO
@app.route('/customers')
def customers():

   return ''



# TODO
@app.route('/vendors')
def customers():
    return ''


@app.route('/jobs')
def hello_world():
   return render_template('jobs.html', jobs=jobs)



@app.route('/addjob',methods = ['POST', 'GET'])
def addjob():
    if request.method == 'POST':


        jobs['new_code'] ={
                     'title': request.form['title'],
                     'salary': request.form['salary'],
                     'skills': set(request.form['skill'].split(','))
                  }

        return jsonify({'status':'ok', 'errors':None,'redirect': request.url_root+'/jobs'});

    else:

        return render_template('addjob.html')


if __name__ == '__main__':


   # dao emulation

   jobs = {
      'job code1': {
                     'title':'SQL developer',
                     'salary':1000,
                     'skills':{'pl/sql','Oracle'}
                  },


      'job code2': {
                  'title': 'Teacher',
                  'salary': 1,
                  'skills': {'pl/sql', 'Oracle','Excel','Word'}
      }

   }


   app.run()