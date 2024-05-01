from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"


class myForm(FlaskForm):

    formname = "Investment Form"

    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField(
        "Age", validators=[InputRequired(), NumberRange(min=18, max=100)]
    )

    # Occupation
    occupation_choices = RadioField(
        "Select one of occupation",
        choices=[
            ("student", "Student"),
            ("self_employed", "Self Employed"),
            ("unemployed", "Unemployed"),
            ("business_owner", "Business Owner"),
        ],
        validators=[DataRequired()],
    )
    investment_purpose_tools = RadioField(
        "For Investment Purpose Which of the following will you choose.",
        choices=[
            ("fixed_deposit", "Fixed Deposit"),
            ("mutual_funds", "Mutual Funds"),
            ("stocks", "Stocks"),
            ("government_schemes", "Government Schemes"),
        ],
        validators=[DataRequired()],
    )
    financial_freedom_tools = RadioField(
        "If you want to achieve financial freedom, which of the following instrument you will choose.",
        choices=[
            ("mutual_funds", "Mutual Funds"),
            ("stocks", "Stocks"),
            ("real_state", "Real State"),
            ("oters", "Others"),
        ],
        validators=[DataRequired()],
    )
    mutual_fund_knowledge = RadioField(
        "How much knowledge do you have about mutual funds?",
        choices=[
            ("no_knowledge", "No Knowledge"),
            ("little_knowledge", "Little Knowledge"),
            ("good_knowledge", "Good Knowledge"),
            ("excellent_knowledge", "Excellent Knowledge"),
        ],
        validators=[DataRequired()],
    )
    prarameter_to_take_note_of = RadioField(
        "While Selecting a mutual fund which parameter do you take note of most?",
        choices=[
            ("expense_ratio", "Expense Ratio"),
            ("value_of_nav", "Value of NAV"),
            ("past_performance", "Past Performance"),
            ("total_asset_under_management", "Total Asset Under Management"),
        ],
        validators=[DataRequired()],
    )
    mutual_fund_category = RadioField(
        "Which of the following mutual fund category you will choose?",
        choices=[
            ("large_cap", "Large Cap"),
            ("mid_cap", "Mid Cap"),
            ("small_cap", "Small Cap"),
            ("flexi_cap", "Flexi Cap"),
        ],
        validators=[DataRequired()],
    )
    investing_currently = RadioField(
        "Are you investing currently?",
        choices=[
            ("yes", "Yes"),
            ("no", "No"),
            ("planning_to_invest", "Planning To Invest"),
            ("not_interested", "Not Interested"),
        ],
        validators=[DataRequired()],
    )
    long_term_investment_choise = RadioField(
        "Which of the following you will choose for long term investment?",
        choices=[
            ("mutual_funds", "Mutual Funds"),
            ("equity_shares", "Equity Shares"),
            ("real_state", "Real State"),
            ("gold_and_silver", "Gold and Silver"),
        ],
        validators=[DataRequired()],
    )
    retirement_planing_investment = RadioField(
        "Which of the following do you think is more appropriate for retirement planning?",
        choices=[
            ("ppf_epf", "PPF/EPF"),
            ("mutual_funds", "Mutual Funds"),
            ("nps", "NPS"),
            ("bonds_and_term_deposit", "Bonds and Term Deposit"),
        ],
        validators=[DataRequired()],
    )
    risk_factor_mutual_funds = IntegerField(
        "On a scale of 1 to 10, how risky do you think Mutual Fund is?",
        validators=[DataRequired(), NumberRange(min=1, max=10)],
    )
    highest_return_in_long_term = RadioField(
        "Which of the following you think will give highest return in long term?",
        choices=[
            ("mutual_funds", "Mutual Funds"),
            ("bonds_or_others", "Bonds or Others"),
            ("real_state", "Real State"),
            ("gold_and_silver", "Gold and Silver"),
        ],
        validators=[DataRequired()],
    )


@app.route("/", methods=["GET", "POST"])
def index():
    form = myForm()
    for field in form:
        print(field)
        print()
    if form.validate_on_submit():
        # do something
        print(form.name.data)
        print(form.age.data)
        print(form.occupation_choices.data)
        print(form.investment_purpose_tools.data)
        print(form.financial_freedom_tools.data)
        return render_template("form_success.html", formname=form.formname)
    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
