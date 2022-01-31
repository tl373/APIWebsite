from LoanStreetLoaner import *


class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    interestRate = db.Column(db.Float)
    percentage = db.Column(db.Integer)
    LengthofLoan = db.Column(db.Float)
    monthlyCost = db.Column(db.Float)


db.session.query(Loan).delete()
db.session.commit()


class LoanSchema(ma.Schema):
    class Meta:
        fields = ('id', 'amount', 'monthlyCost', 'percentage', 'LengthofLoan')


# Init schema
loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)


class LoanForm(FlaskForm):
    loan_amount = FloatField('Loan Request', validators=[DataRequired()])
    interest_rate = FloatField('Interest Rate', validators=[DataRequired()])
    total_months = FloatField('Amount of months to pay Loan', validators=[DataRequired()])
    submit = SubmitField('Submit')

