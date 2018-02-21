from flask import Flask, render_template, flash,request,url_for,redirect
import pandas as pd
import marshal
import time
import test_1
import test_2
import test_3
import test_4
import solution_1
import solution_2
import solution_3
import solution_4
app = Flask(__name__)

@app.route("/createDB")
def createDB():
    global data_structure
    data_structure = test_2.put()
    return render_template('index.html')


@app.route("/runQuery1", methods=["POST","GET"])
def runQuery1():
    global data_structure
    sol_start = time.time()
    sol_first,sol_last,sol_salary = solution_1.bitboostdotcomB()
    sol_time = time.time() - sol_start
    test_start = time.time()
    data_structure,fname,lname,min_salary = test_1.get(data_structure)
    test_time = time.time()-test_start
    msg = ""
    if sol_first == fname and sol_last == lname and sol_salary == min_salary:
        msg = "Correct answer"
    else:
        msg = "Wrong answer"
    if request.method == "POST":
    	return render_template('query.html',sol_time=sol_time,test_time=test_time,message=msg)



@app.route("/runQuery2", methods=["POST","GET"])
def runQuery2():
    global data_structure
    sol_start = time.time()
    sol_list = solution_2.fuscatC()
    sol_time =  time.time() - sol_start
    test_start = time.time()
    test_list = test_2.get(data_structure)
    test_time = time.time() - test_start

    msg = ""
    correct = True
    if len(sol_list) != len(test_list):
        correct = False
    else:
        for sol, test in zip(sol_list,test_list):
            if sol[-1] != test[-1]:
                correct = False
    if correct :
        msg = "Correct answer"
    else :
        msg = "Wrong answer"

    if request.method == "POST":
        return render_template('query.html',sol_time=sol_time,test_time=test_time,message=msg)



@app.route("/runQuery3", methods=["POST","GET"])
def runQuery3():
    global data_structure
    sol_start = time.time()
    sol_ans = solution_3.ordemo6()
    sol_time = time.time() - sol_start
    test_start = time.time()
    test_ans = test_3.get(data_structure)
    test_time = time.time() - test_start
    msg = ""
    if sol_ans == test_ans :
        msg = "Correct answer"
    else :
        msg = "Wrong answer"

    if request.method == "POST":
        return render_template('query.html',sol_time=sol_time,test_time=test_time,message=msg)




@app.route("/runQuery4", methods=["POST","GET"])
def runQuery4():
    global data_structure
    sol_start = time.time()
    sol_first,sol_last,sol_salary = solution_4.ordemo9()
    sol_time = time.time() - sol_start
    test_start = time.time()
    fname,lname,salary = test_4.get(data_structure)
    test_time = time.time() - test_start
    if sol_first == fname and sol_last == lname and sol_salary == salary:
        msg = "Correct answer"
    else:
        msg = "Wrong answer"

    if request.method == "POST":
    	return render_template('query.html',sol_time=sol_time,test_time=test_time,message=msg)

'''
@app.route("/runQuery5", methods=["POST","GET"])
def runQuery5():
    global data_structure
    sol_start = time.time()
    solution5.fetch()
    sol_time = time.time() - sol_start
    test_start = time.time()
    test_query.get()
    test_time = time.time() - test_start
    # write a search function named "search", for your data_structure in test_query file,so that we can test wheter the insertion was actually done
    # the search function should return the first and last name of employee with EMployee No "300006"
    # the query time is calculated for the get that is the insert query only
    fname,lname = test_query.search()
    if fname == "Popeye" and lname == "DMello":
        msg = "Correct answer"
    else:
        msg = "Wrong answer"
    if request.method == "POST":
    	return render_template('query.html',sol_time=sol_time,test_time=test_time,message=msg)

@app.route("/runQuery6", methods=["POST","GET"])
def runQuery6():
'''



@app.route("/")
def index():
    return render_template('index.html')


if __name__ =="__main__":
    app.debug = True
    app.run(port=1234)
