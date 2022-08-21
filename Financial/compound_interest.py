#!/usr/local/bin/python3
"""
This is an application that will calculate compound interest over a certain amount of time
given certain interest rates, starting amounts, weekly rate of returns and your tax rate.
I could use A = P(1 + r/n)^(nt) for the compound interest
But that would be no fun, I wouldn't be able to customize the application the way I wanted to
also I didn't think about it before I coded this :)

Calculator I used to verify my numbers:
    - https://www.thecalculatorsite.com/finance/calculators/compoundinterestcalculator.php
"""

# ************************************* Need To Implement Or Fix **********************************
# currently when using monthly contributions at the start of month there is a
# 2%-2.5% error in the calculation
# ************************************* Need To Implement Or Fix **********************************

from termcolor import colored


def user_input_validation():
    """
    Get All the user input in one place and make sure the data is valid before passing
    it off to the other functions to do their calculations
    """
    # user input validation for all the prompts, this will validate the input for:
    # starting_capitals, monthly_contribution, time_frame_for_investment,
    # tax_rate & weekly_rate_of_returns

    while True:
        try:
            print("\nPlease Enter 1 Or More Number(s) Separated By Space Ex: 10000 15000 20000")
            starting_capitals = [
                int(string_num) for string_num in input(
                    "Enter The Starting Capital(s) Separated By Space: ").split()
            ]
            # if starting capital == None because you hit enter, keep asking into you get good data
            if not starting_capitals:
                print("\nYou Have To Enter At Least 1 Value For Starting Capital(s)")
                continue
            break
        except ValueError:
            print("\nPlease Only Enter 1 Or More Number(s)"
                  " Separated By Space, No Strings Are Allowed"
            )

    while True:
        try:
            # This contribution will be added on to your current investment
            # at the start of every month
            print("\nEnter 1 Number That You Would Like Your Monthly Contribution"
                  " To Be WITHOUT Commas Ex: 1000"
            )
            monthly_contribution = int(input("What Is Your Monthly Contribution? "))
            break
        except ValueError:
            print("\nPlease Only Enter A Singular Number, No Strings Are Allowed")

    while True:
        try:
            # This will determine the amount of years that you want to invest your money
            print("\nPlease Enter 1 Whole Number And NOT A Decimal Ex: 5")
            time_frame_for_investment = \
                int(input("How Many Years Do You Want To Invest Your Money? "))
            break
        except ValueError:
            print("\nPlease Only Enter A Singular Number, No Strings Are Allowed")

    while True:
        try:
            # This will be the rate at which your money will be taxed at the end of each year
            print("\nPlease Enter 1 Number Without The % Symbol, You Can Also Enter A Decimal "
                  "Tax Rate Ex: 10 12 22 24 32 35 37 50.51")
            tax_rate = float(input("Please Enter Your Projected Tax Rate: "))
            break
        except ValueError:
            print("\nPlease Only Enter A Number or Decimal, No Strings Are Allowed")

    while True:
        try:
            # Enter your Desired Weekly Rate of Returns Ex: 1 1.5 2 2.5 (Without the percent sign)
            print("\nInput the Weekly Rate of Return(s) as a Percentage --> Ex: 1 1.5 2 ")
            weekly_rate_of_returns = list(
                float(num) for num in
                input("Enter the Different Weekly Rate of Returns(s) separated by space ").split()
            )
            # if weekly_rate_of_returns == None because you hit enter,
            # keep asking into you get good data
            if not weekly_rate_of_returns:
                print("\nYou Have To Enter At Least 1 Value For The Weekly Rate Of Return")
                continue
            break
        except ValueError:
            print("\nPlease Only Enter Number(s) or Decimal(s), No Strings Are Allowed")

    # return all the validated user input for the program to be able to run
    return \
        starting_capitals, monthly_contribution,\
        time_frame_for_investment, tax_rate,\
        weekly_rate_of_returns


def brief_summary(financial_report, years, net_realized_gains, total_capital,
                  initial_investment, weekly_rate_of_return,
                  monthly_contribution, tax_rate):
    """
    Displays a less detailed Summary report of your investments, Displays these values:
    Initial Investment, Additional Monthly Contribution, Weekly Rate Of Return, Tax Rate,
    Net Investment, Total Contributions To Date, Rate of Return over the time
    period of your investment

    :param financial_report: File object that this program will be appending text to

    :param years: integer value that represents how many years you invested the money

    :param net_realized_gains: int value for the net profits at the
    end of the investment period

    :param total_capital: int value for the total amount of money that
    you contributed over the length of the investment

    :param initial_investment: integer value for
    tracking the actual initial investment

    :param weekly_rate_of_return: float value that
    determines your weekly return each week

    :param monthly_contribution: integer value that represents monthly contribution to investment

    :param tax_rate: float value that represent tax rate at the end of the year

    :return: None


            Printing Summary Report For Year 3
            **********NET SUMMARY************************
            Initial Investment: $100,000
            Additional Monthly Contribution: $8,334
            Weekly Rate Of Return: 1.25%
            Tax Rate: 33.0%
            Net Investment: $1,100,145
            Total Contributions To Date: $400,024
            1,100,145 / 400,024 = (2.75X Return)
            **********NET SUMMARY************************
    """

    # Prints the Net Summary Report information for the year
    print(f"\nPrinting Summary Report For Year {years + 1}")
    print("**********NET SUMMARY************************")
    print(f"Initial Investment: ${initial_investment:,d}")
    print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
    print(f"Weekly Rate Of Return: {round(weekly_rate_of_return * 100, 2)}%")
    print(f"Tax Rate: {tax_rate}%")
    print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
    print(f"Total Contributions To Date: ${total_capital:,d}")
    print(f"{int(net_realized_gains):,d} / {total_capital:,d} = "
          f"({round(net_realized_gains / total_capital, 2)}X Return)"
    )
    print("**********NET SUMMARY************************")

    # write all of this output to the financial_investments_report_brief.txt file
    financial_report.write(f"\n\nPrinting Summary Report For Year {years + 1}")
    financial_report.write("\n**********NET SUMMARY************************")
    financial_report.write(f"\nInitial Investment: ${initial_investment:,d}")
    financial_report.write(f"\nAdditional Monthly Contribution: ${monthly_contribution:,d}")
    financial_report.write(
        f"\nWeekly Rate Of Return: {round(weekly_rate_of_return * 100, 2)}%"
    )
    financial_report.write(f"\nTax Rate: {tax_rate}%")
    financial_report.write(f"\nNet Investment: ${int(net_realized_gains):,d}")
    financial_report.write(f"\nTotal Contributions To Date: ${total_capital:,d}")
    financial_report.write(f"\n{int(net_realized_gains):,d} / {total_capital:,d} = "
                           f"({round(net_realized_gains / total_capital, 2)}X Return)"
    )
    financial_report.write("\n**********NET SUMMARY************************")


def summary(financial_report, years, start_of_the_year_capital, total_capital,
            net_realized_gains, tax_rate, ending_capital, total_profits_current_year,
            tax_amount, total_profits_all_time, initial_investment,
            weekly_rate_of_return, monthly_contribution):
    """
    Display a Summary report of your investments,
    takes in the variable as parameters from your compound() function

    :param financial_report: File object that this program will be appending text to

    :param years: integer value that represents
    how many years you invested the money

    :param start_of_the_year_capital: int value that shows the
    amount of money you have at the start of the current year

    :param total_capital: int value for the total amount
    of money that you contributed over the length of the investment

    :param net_realized_gains: int value for the net
    profits at the end of the investment period

    :param tax_rate: float value that represent tax rate at the end of the year

    :param ending_capital: int value that displays the amount of gross capital you have

    :param total_profits_current_year: int value that stores the
    value of the total profits for the current year

    :param tax_amount: int value that stores the value
    of the tax amount due at the end of each year

    :param total_profits_all_time: int value that stores the value
     for the total profits you made on the investment

    :param initial_investment:
    integer value for tracking the actual initial investment

    :param weekly_rate_of_return: float value
    that shows the human-readable % value Ex: 1.5% not .015

    :param monthly_contribution: integer value that represents monthly contribution to investment
    :return: None

    ******************************EXAMPLE OUTPUT*****************************

                    Printing Summary Report For Year 5
                    **********GROSS SUMMARY**********************
                    Initial Investment: $1,000
                    Start of The Current Year Investment: $190,461
                    Additional Monthly Contribution: $1,000
                    Weekly Rate Of Return: 1.5%
                    Profits for the Year: $229,781
                    Ending Investment: $432,243
                    $432,243 / $61,000 = 7.09X Return
                    **********GROSS SUMMARY**********************

                    **********NET SUMMARY************************
                    Tax Rate: 37.0%
                    Tax Amount Due: $85,019
                    Net Investment: $347,224
                    Total Contributions To Date: $61,000
                    Profits for the Year: $144,762
                    Total Profits All Time: $286,224
                    347,224 / 61,000 =  5.69X Return
                    **********NET SUMMARY************************


    ******************************EXAMPLE OUTPUT*****************************
    """

    # Prints the Gross Summary information for the year
    print(f"\nPrinting Summary Report For Year {years + 1}")
    print("**********GROSS SUMMARY**********************")
    print(f"Initial Investment: ${initial_investment:,d}")
    print(f"Start Of Year {years + 1} Investment: ${int(start_of_the_year_capital):,d}")
    print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
    print(f"Weekly Rate Of Return: {round(weekly_rate_of_return * 100, 2)}%")
    print(f"{colored('Profits For The Year: ', 'green')}${int(total_profits_current_year):,d}")
    print(f"{colored('Ending Investment: ', 'green')}${int(ending_capital):,d}")
    print(f"${round(ending_capital):,d} / ${round(total_capital):,d} = "
          f"{round(ending_capital / total_capital, 2)}X Return")
    print("**********GROSS SUMMARY**********************\n")

    # write all the Gross Summary Information to the financial_investments_report_detailed.txt file
    financial_report.write(f"\n\nPrinting Summary Report For Year {years + 1}")
    financial_report.write("\n**********GROSS SUMMARY**********************")
    financial_report.write(f"\nInitial Investment: ${initial_investment:,d}")
    financial_report.write(
        f"\nStart Of Year {years + 1} Investment: ${int(start_of_the_year_capital):,d}"
    )
    financial_report.write(f"\nAdditional Monthly Contribution: ${monthly_contribution:,d}")
    financial_report.write(
        f"\nWeekly Rate Of Return: {round(weekly_rate_of_return * 100, 2)}%"
    )
    financial_report.write(f"\nProfits for The Year: ${int(total_profits_current_year):,d}")
    financial_report.write(f"\nEnding Investment: ${int(ending_capital):,d}")
    financial_report.write(
        f"\n${round(ending_capital):,d} / ${round(total_capital):,d} = "
        f"{round(ending_capital / total_capital, 2)}X Return"
    )
    financial_report.write("\n**********GROSS SUMMARY**********************\n")

    # Prints the Net Summary information for the year
    print("**********NET SUMMARY************************")
    print(f"Tax Rate: {tax_rate}%")
    print(f"{colored('Tax Amount Due:', 'red')} ${round(tax_amount):,d}")
    print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
    print(f"Total Contributions To Date: ${total_capital:,d}")
    print(f"Profits for the Year: ${round(total_profits_current_year - tax_amount):,d}")
    print(f"Total Profits All Time: ${round(total_profits_all_time):,d}")
    print(f"{int(net_realized_gains):,d} / {total_capital:,d} = "
          f" {round(net_realized_gains / total_capital, 2)}X Return")
    print("**********NET SUMMARY************************")

    # write all the Net Summary Information to the financial_investments_report_detailed.txt file
    financial_report.write("\n**********NET SUMMARY************************")
    financial_report.write(f"\nTax Rate: {tax_rate}%")
    financial_report.write(f"\nTax Amount Due: ${round(tax_amount):,d}")
    financial_report.write(f"\nNet Investment: ${int(net_realized_gains):,d}")
    financial_report.write(f"\nTotal Contributions To Date: ${total_capital:,d}")
    financial_report.write(
        f"\nProfits for the Year: ${round(total_profits_current_year - tax_amount):,d}"
    )
    financial_report.write(
        f"\n{int(net_realized_gains):,d} / {total_capital:,d} = "
        f" {round(net_realized_gains / total_capital, 2)}X Return"
    )
    financial_report.write("\n**********NET SUMMARY************************")


def compound_weekly(financial_report, current_capital, weekly_profits_of_the_month,
                    weekly_rate_of_return, brief_or_detailed):
    """
    This function calculates the interest on a weekly basis
     and feeds that information to function compound_monthly()

    :param financial_report: File object that this program will be appending text to

    :param current_capital: the current capital amount that you have at this very moment.
    It increases each week

    :param weekly_profits_of_the_month: a list of the profits for each week of the month

    :param weekly_rate_of_return: Enter a float value for your weekly rate of return

    :param brief_or_detailed: string val that prints a brief summary or long summary
    depending on what the user selected

    :return: current_capital Holds the current amount of money
    that you have after a month of investing
    """

    # Loops 4 times because there are 4 weeks in a month (weekly compound interest)
    for each_week in range(4):
        weekly_profits_of_the_month.append(round(current_capital * weekly_rate_of_return))

        # will only print the print statements if you declared that you wanted a detailed summary
        if 'detailed' in brief_or_detailed or 'd' in brief_or_detailed:
            print(
                f"Start of Week {each_week + 1}: ${round(current_capital):,d} [+] Profits: "
                f"${int(weekly_profits_of_the_month[each_week]):,d} "
            )
            financial_report.write(
                f"\nStart of Week {each_week + 1}: ${round(current_capital):,d} [+] Profits: "
                f"${int(weekly_profits_of_the_month[each_week]):,d} "
            )

        # changes current_capital so that it add the current weeks profits
        # to the current capital amount
        current_capital = current_capital * (1 + weekly_rate_of_return)

    # adds up all the profits for each week in the current month
    # and stores it in a variable monthly_profits_total
    monthly_profits_total = 0
    for each_weekly_profit in weekly_profits_of_the_month:
        monthly_profits_total = monthly_profits_total + each_weekly_profit

    # will only print the print statements if you declared that you wanted a detailed summary
    if 'detailed' in brief_or_detailed or 'd' in brief_or_detailed:
        print(f"Total Profits for the Month: ${monthly_profits_total:,d}")
        print(f"{colored('End of Month:', 'green')} ${int(current_capital):,d}")
        financial_report.write(f"\nTotal Profits for the Month: ${monthly_profits_total:,d}")
        financial_report.write(f"\nEnd of Month: ${int(current_capital):,d}")

    return current_capital


def compound_monthly(financial_report, current_capital, monthly_contribution,
                     brief_or_detailed, years, weekly_rate_of_return):
    """
    compound_monthly function will run for each month in the year
    that you want to invest your money

    :param financial_report: File object that this program will be appending text to

    :param current_capital: integer value this is the current
    capital amount that will be constantly changed

    :param monthly_contribution: integer value that represents monthly contribution to investment

    :param brief_or_detailed: string val that prints a brief summary or long summary
    depending on what the user selected

    :param years: int value that holds the value of the current year you are in

    :param weekly_rate_of_return: float value weekly rate of return
    after it has been divided by 100 Ex: .015 = 1.5%

    :return: current_capital Holds the current amount of money
    that you have after a month of investing
    """

    months_of_the_year = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY',
                          'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

    # loops through each month of the year
    for each_month in months_of_the_year:
        # first thing, add the monthly contribution before doing any other math
        current_capital = current_capital + monthly_contribution

        if 'detailed' in brief_or_detailed or 'd' in brief_or_detailed:
            print(f"\n\t\tYEAR {years + 1} {each_month}")
            print(f"Adding Monthly Contribution: [+] ${monthly_contribution:,d}")
            financial_report.write(f"\n\n\t\tYEAR {years + 1} {each_month}")
            financial_report.write(
                f"\nAdding Monthly Contribution: [+] ${monthly_contribution:,d}"
            )

        # resets the value for the weekly profits for the current month
        weekly_profits_of_the_month = []

        # This function calculates the interest on a weekly basis
        current_capital = compound_weekly(
            financial_report, current_capital, weekly_profits_of_the_month,
            weekly_rate_of_return, brief_or_detailed
        )

    if 'detailed' in brief_or_detailed or 'd' in brief_or_detailed:
        # compound_weekly needs to be called once here so that I can get the extra 4 weeks
        # without this it will only be 48 weeks, but I need it to be 52 weeks
        print(f"\n\t\tExtra 4 Weeks Of Year {years + 1}")
        financial_report.write(f"\n\n\t\tExtra 4 Weeks Of Year {years + 1}")

    weekly_profits_of_the_month = []

    current_capital = compound_weekly(
        financial_report, current_capital,
        weekly_profits_of_the_month, weekly_rate_of_return, brief_or_detailed
    )

    return current_capital


def compound_yearly(financial_report, time_frame_for_investment, current_capital,
                    tax_amount, brief_or_detailed, monthly_contribution, weekly_rate_of_return,
                    tax_rate):
    """
    compound_yearly function will run for each year that you want to invest your money

    :param financial_report: File object that this program will be appending text to

    :param time_frame_for_investment: integer value that determines
    how many years you will invest your money

    :param current_capital: integer value this is the current
    capital amount that will be constantly changed

    :param tax_amount: int value that stores the value of the
    tax amount due at the end of each year

    :param brief_or_detailed: string val that prints a brief summary or long summary
    depending on what the user selected

    :param monthly_contribution: integer value that represents
    monthly contribution to investment

    :param weekly_rate_of_return: float value weekly rate of return
     after it has been divided by 100 Ex: .015 = 1.5%

    :param tax_rate: float value that represent tax rate
     at the end of the year

    :param weekly_rate_of_return: float value that shows
     the human-readable % value Ex: 1.5% not .015

    :return: None
    """

    # for brief_summary can keep track of initial investment
    initial_investment = current_capital

    # This specifies how many years you will be investing your money
    for years in range(time_frame_for_investment):
        # helps me keep track of the profits for just the current year
        start_of_the_year_capital = current_capital - tax_amount
        current_capital = start_of_the_year_capital

        if 'detailed' in brief_or_detailed or 'd' in brief_or_detailed:
            print(f"\nStarting Capital = ${int(start_of_the_year_capital):,d}")
            print(f"Monthly Additional Contribution = ${monthly_contribution:,d}")
            financial_report.write(f"\n\nStarting Capital = ${int(start_of_the_year_capital):,d}")
            financial_report.write(
                f"\nMonthly Additional Contribution = ${monthly_contribution:,d}"
            )

        current_capital = compound_monthly(
            financial_report, current_capital, monthly_contribution,
            brief_or_detailed, years, weekly_rate_of_return
        )

        # total profits for the current year
        total_profits_current_year = \
            current_capital - start_of_the_year_capital - monthly_contribution * 12

        # total amount of your own contribution
        total_capital = \
            initial_investment + monthly_contribution * 12 * (years + 1)

        # This will be the tax amount that you will pay at the end of each year
        tax_amount = total_profits_current_year * (tax_rate / 100)

        # all time total profits total
        total_profits_all_time = current_capital - total_capital - tax_amount
        # set ending capital as a place-holder for the value in current capital
        ending_capital = current_capital
        # net profits after taxes are taken out for that specific year
        net_realized_gains = ending_capital - tax_amount

        # Prints the brief summary report at the end of the time frame
        # you selected to invest your money
        if (years + 1) == time_frame_for_investment \
                and brief_or_detailed != 'detailed' and brief_or_detailed != 'd':
            brief_summary(
                financial_report, years, net_realized_gains, total_capital,
                initial_investment, weekly_rate_of_return,
                monthly_contribution, tax_rate
            )
        elif 'detailed' not in brief_or_detailed and 'd' not in brief_or_detailed:
            pass
        # Prints the detailed summary for the year,
        # displays gross and net information for that year
        else:
            summary(
                financial_report, years, start_of_the_year_capital, total_capital,
                net_realized_gains, tax_rate, ending_capital, total_profits_current_year,
                tax_amount, total_profits_all_time, initial_investment,
                weekly_rate_of_return, monthly_contribution
            )


def compound(brief_or_detailed, financial_report):
    """
    This function will call compound_yearly and pass over all the needed values over.
    The for loop will run x amount of times depending on how many values
    the user entered for starting_capitals and weekly_rate_of_returns

    :param brief_or_detailed: string val that prints a brief summary or long summary
    depending on what the user selected

    :param financial_report: File object that this program will be appending text to

    :return: None
    """

    # get all the correct input from the user using the user_input_validation function
    starting_capitals, monthly_contribution,\
        time_frame_for_investment, tax_rate, weekly_rate_of_returns = user_input_validation()

    # after getting all the values and verifying that they are accurate, write once to the file
    financial_report.write(f"\n\nStarting Capital(s): {starting_capitals}")
    financial_report.write(f"\nMonthly Contribution: ${monthly_contribution:,d}")
    financial_report.write(f"\nTime Frame For Investment: {time_frame_for_investment} Years")
    financial_report.write(f"\nTax Rate: {tax_rate}%")
    financial_report.write(f"\nWeekly Rate Of Returns (Percentages): {weekly_rate_of_returns}")

    for weekly_rate_of_return in weekly_rate_of_returns:
        # This is done so that the user can enter a human-readable decimal
        # like 1.5 instead of 1.015 or .015
        weekly_rate_of_return = weekly_rate_of_return / 100

        # loop through all the starting capital values that were requested from the user input
        for current_capital in starting_capitals:
            # resets tax amount each time you get a new starting value
            # from the starting_capitals list
            tax_amount = 0

            # compounds the money by calling the compound_yearly function
            compound_yearly(
                financial_report, time_frame_for_investment,
                current_capital, tax_amount, brief_or_detailed,
                monthly_contribution, weekly_rate_of_return, tax_rate
            )


def main():
    """ This is the main function, and it will provide the flow for all of our code """

    while True:
        try:
            print("\nIf You Want The Detailed Summary Type: 'detailed' or 'd' "
                  "\nIf You Want The Brief Summary Press Any Other Key"
            )

            brief_or_detailed = \
                input("\nDo You Want The Brief Summary Or The Detailed Summary? ").lower()

            try:
                # only opens the brief or detailed file depending on the
                # summary report the user chooses
                if 'd' not in brief_or_detailed \
                        and 'detailed' not in brief_or_detailed:
                    with open(
                            'financial_report_brief.txt', 'a', encoding='UTF-8'
                    ) as financial_report:
                        compound(brief_or_detailed, financial_report)
                else:
                    with open(
                            'financial_report_detailed.txt', 'a', encoding='UTF-8'
                    ) as financial_report:
                        compound(brief_or_detailed, financial_report)
            except IOError:
                print("Error With Opening Or Closing The financial_investments_report.txt File")
                break
            except KeyboardInterrupt:
                print("\nYou Must Want To Change Your Investments, Go Ahead And Enter The Values")
                continue

            # Ask the user if they run the program to be re-ran,
            # if the answer is no, break out of the while loop
            run_program_again = \
                input("\n\n\nDo You Want To Run Another Calculation? Enter Yes Or No: ").lower()
            if 'no' in run_program_again or 'n' in run_program_again:
                break
        except KeyboardInterrupt:
            print("\nThank You For Planning Out Your Investment Goals With Me, GoodBye :)")
            break


main()
