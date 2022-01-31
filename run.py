from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse,fields,marshal_with

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)
api = Api(app)

class LoanModel(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    interestRate = db.Column(db.Integer)
    LengthofLoan = db.Column(db.Integer)
    monthlyCost = db.Column(db.Integer)




input_args = reqparse.RequestParser()
input_args.add_argument("amount", type=int, help = "Please enter amount",required=True)
input_args.add_argument("interestRate", type=int, help = "Please enter interestRate",required=True)
input_args.add_argument("LengthofLoan", type=int, help = "Please enter Length of Loan in months",required=True)
input_args.add_argument("monthlyCost", type=int, help = "Please enter Monthly Cost amount",required=True)

update_input_args = reqparse.RequestParser()
update_input_args.add_argument("id", type=int, help = "Please enter id of loan",required=True)
update_input_args.add_argument("monthlyCost", type=int, help = "Please enter new Monthly payment amount",required=True)

loan_fields = {
    'id':fields.Integer,
    'amount':fields.Integer,
    'interestRate':fields.Integer,
    'LengthofLoan':fields.Integer,
    'monthlyCost':fields.Integer
}

class Loan(Resource):
    @marshal_with(loan_fields)
    def get(self):
        return LoanModel.query.all(),200

    @marshal_with(loan_fields)
    def post(self):
        args = input_args.parse_args()
        loan = LoanModel(amount=args['amount'],interestRate=args['interestRate'],LengthofLoan = args['LengthofLoan'],monthlyCost = args['monthlyCost'])
        db.session.add(loan)
        db.session.commit()
        return loan, 201

    @marshal_with(loan_fields)
    def put(self):
        args = update_input_args.parse_args()
        query = LoanModel.query.filter_by(id=args['id']).first()
        query.monthlyCost = args['monthlyCost']
        if not query:
            return f'Loan id:{id} does not exist',404

        db.session.commit()
        return query,202

    @marshal_with(loan_fields)
    def delete(self):
        db.session.query(LoanModel).delete()
        db.session.commit()
        return '',204



api.add_resource(Loan, '/getLoan')


if __name__ == "__main__":

    app.run(debug=True)
