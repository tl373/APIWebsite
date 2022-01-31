from LoanStreetLoaner import *
from LoanStreetLoaner.models import *
import pprint


def calculateLoan(amount, interest_rate, total_months):
    owed_Monthly = float(amount) * (1 + (float(interest_rate) / 100)) / float(total_months)
    return str(round(owed_Monthly, 2))


blueprint_default = Blueprint('default', __name__, )



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# applies for loans
@app.route('/getLoan/', methods=['GET', 'POST'])
def getLoan():
    form = LoanForm()
    if request.method == 'GET':
        return render_template('getloan.html', form=form)
    else:
        if form.validate_on_submit():
            db.create_all()
            total_loan = Loan(amount=form.loan_amount.data,
                              interestRate=form.interest_rate.data,
                              LengthofLoan=form.total_months.data,
                              percentage=str(form.interest_rate.data) + "%",
                              monthlyCost=calculateLoan(form.loan_amount.data, form.interest_rate.data,
                                                        form.total_months.data)
                              )
            db.session.add(total_loan)
            db.session.commit()
            return redirect(url_for('loanSummary'))

        elif request.headers['Content-Type'] == 'application/json' and request.method == 'POST':
            new_amount = request.json['amount']
            new_interestRate = request.json['interestRate']
            new_LengthOfLoan = request.json['LengthOfLoan']

            new_loan = Loan(amount=new_amount,
                            interestRate=new_interestRate,
                            LengthofLoan=new_LengthOfLoan,
                            percentage=str(new_interestRate) + "%",
                            monthlyCost=calculateLoan(new_amount, new_interestRate, new_LengthOfLoan)
                            )

            db.session.add(new_loan)
            db.session.commit()
            # return redirect(url_for("loanSummary"))
            return jsonify(new_loan)




# displays the loans on front end
@app.route('/yourPersonalLoanSummary/', methods=['GET', 'POST'])
def loanSummary():
    total_loans = Loan.query.all()
    result = loan_schema.dump(total_loans)
    return render_template('loanSummary.html', loans=total_loans)

@app.route('/yourPersonalLoanSummary/api/all', methods=['GET'])
def allLoansapi():
    total_loans = Loan.query.all()
    result = loan_schema.dump(total_loans, many=True)
    return jsonify(result)


# update the loan on front end
@app.route('/yourPersonalLoanSummary/edit/<int:id>', methods=['GET', 'POST'])
def editLoan(id):
    form = LoanForm()
    loan_to_update = Loan.query.get_or_404(id)
    if request.method == "POST":
        loan_to_update.amount = request.form['loan_amount']
        loan_to_update.interestRate = request.form['interest_rate']
        loan_to_update.LengthofLoan = request.form['total_months']
        loan_to_update.percentage = str(loan_to_update.interestRate) + "%"
        loan_to_update.monthlyCost = calculateLoan(float(loan_to_update.amount), float(loan_to_update.interestRate),
                                                   float(loan_to_update.LengthofLoan))
        try:
            db.session.commit()
            flash("Updated the loan to specified loan amounts")
            return redirect(url_for("loanSummary"))
        except:
            flash("An error occurred try again")
            return render_template('editLoan.html', form=form, loan_to_update=loan_to_update)
    else:
        return render_template('editLoan.html', form=form, loan_to_update=loan_to_update)


# update the loan through API
@app.route('/yourPersonalLoanSummary/edit/api/<int:id>', methods=['PUT','POST'])
def editLoanAPI(id):
    loan_to_updateAPI = Loan.query.get(id)
    if request.method == "PUT":
        loan_to_updateAPI.amount = request.json['loan_amount']
        loan_to_updateAPI.interestRate = request.json['interest_rate']
        loan_to_updateAPI.LengthofLoan = request.json['total_months']
        loan_to_updateAPI.percentage = str(loan_to_updateAPI.interestRate) + "%"
        loan_to_updateAPI.monthlyCost = calculateLoan(float(loan_to_updateAPI.amount), float(loan_to_updateAPI.interestRate),
                                                   float(loan_to_updateAPI.LengthofLoan))
    db.session.add(loan_to_updateAPI)
    db.session.commit()
    result = loan_schema.dump(loan_to_updateAPI)
    return result




