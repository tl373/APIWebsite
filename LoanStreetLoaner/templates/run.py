from LoanStreetLoaner import *
from LoanStreetLoaner.views import *

if __name__ == "__main__":
    #app.register_blueprint(API_Calls, url_prefix="api/")
    app.run(host="localhost", port=8000, debug=True)
