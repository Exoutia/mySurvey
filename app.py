from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"


class myForm(FlaskForm):

    formname = "Investment Form"

    name = StringField("Name")
    age = IntegerField("Age")

    # Occupation
    occupation_choices = RadioField(
        "Select one of occupation",
        choices=[
            ("student", "Student"),
            ("self_employed", "Self Employed"),
            ("unemployed", "Unemployed"),
            ("business_owner", "Business Owner"),
        ],
    )
    investment_purpose_tools = RadioField(
        "For Investment Purpose Which of the following will you choose.",
        choices=[
            ("fixed_deposit", "Fixed Deposit"),
            ("mutual_funds", "Mutual Funds"),
            ("stocks", "Stocks"),
            ("government_schemes", "Government Schemes"),
        ],
    )
    investment_tools = RadioField(
        "If you want to achieve financial freedom, which of the following instrument you will choose.",
        choices=[
            ("mutual_funds", "Mutual Funds"),
            ("stocks", "Stocks"),
            ("real_state", "Real State"),
            ("oters", "Others"),
        ],
    )

    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    form = myForm()
    if form.validate_on_submit():
        # do something
        print(form.name.data)
        print(form.age.data)
        print(form.occupation_choices.data)
        print(form.investment_purpose_tools.data)
        print(form.investment_tools.data)
        return render_template("form_success.html", formname=form.formname)

    print(form.errors)
    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
