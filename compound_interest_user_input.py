# This is a application that will calculate compound interest over a certain amount of time
# given certain interest rates, starting amounts, weekly rate of returns and your tax rate

# *****************UPDATE************************
# Need to implement Error handling throughout the script
# figure out why the list comprehension lines of code worked but my for loop didn't
# fix all of the docstrings for each function to give accurate descriptions what the function does and each parameter
from termcolor import colored


# want to display just a little bit of information for different interest rates, starting capitals, etc
def brief_summary(years, net_realized_gains, total_capital, initial_investment_for_brief_summary,
                  each_percentage_weekly_rate_of_return, monthly_contribution, tax_rate):
    """
    Display a less detailed Summary report of your investments, takes in the variable as parameters from your
    compound() function
    :param tax_rate:
    :param monthly_contribution:
    :param each_percentage_weekly_rate_of_return:
    :param initial_investment_for_brief_summary:
    :param years:
    :param net_realized_gains:
    :param total_capital:
    :return:
    """

    # Prints the Net Summary Report information for the year
    print()
    print(f"Printing Summary Report For Year {years + 1}")
    print("**********NET SUMMARY************************")
    print(f"Initial Investment: ${initial_investment_for_brief_summary:,d}")
    print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
    print(f"Weekly Rate Of Return: {round(each_percentage_weekly_rate_of_return, 2)}%")
    print(f"Tax Rate: {tax_rate}%")
    print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
    print(f"Total Contributions To Date: ${total_capital:,d}")
    print(f"{int(net_realized_gains):,d} / {total_capital:,d} ({round(net_realized_gains / total_capital, 2)}X Return)")
    print("**********NET SUMMARY************************")


def summary(years, start_of_the_year_capital, total_capital, net_realized_gains, tax_rate, ending_capital,
            total_profits, tax_amount, total_profits_total, initial_investment_for_brief_summary,
            each_percentage_weekly_rate_of_return, monthly_contribution):
    """
    Display a Summary report of your investments, takes in the variable as parameters from your compound() function
    :param each_percentage_weekly_rate_of_return:
    :param tax_rate:
    :param monthly_contribution:
    :param initial_investment_for_brief_summary:
    :param total_profits_total:
    :param years:
    :param start_of_the_year_capital:
    :param total_capital:
    :param net_realized_gains:
    :param ending_capital:
    :param total_profits:
    :param tax_amount:
    :return:
    """
    print()
    print(f"Printing Summary Report For Year {years + 1}")

    # Prints the Gross Summary information for the year
    print("**********GROSS SUMMARY**********************")
    print(f"Initial Investment: ${initial_investment_for_brief_summary:,d}")
    print(f"Start of The Current Year Investment: ${int(start_of_the_year_capital):,d}")
    print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
    print(f"Weekly Rate Of Return: {round(each_percentage_weekly_rate_of_return, 2)}%")
    print(f"{colored('Profits for the Year: ', 'green')}${int(total_profits):,d}")
    print(f"{colored('Ending Investment: ', 'green')}${int(ending_capital):,d}")
    print(f"${round(ending_capital):,d} / ${round(total_capital):,d} = "
          f"{round(ending_capital / total_capital, 2)}X Return")
    print("**********GROSS SUMMARY**********************")
    print()

    # Prints the Net Summary information for the year
    print("**********NET SUMMARY************************")
    print(f"Tax Rate: {tax_rate}%")
    print(f"{colored('Tax Amount Due:', 'red')} ${round(tax_amount):,d}")
    print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
    print(f"Total Contributions To Date: ${total_capital:,d}")
    print(f"Profits for the Year: ${round(total_profits - tax_amount):,d}")
    print(f"Total Profits All Time: ${round(total_profits_total):,d}")
    print(f"{int(net_realized_gains):,d} / {total_capital:,d}"
          f" {round(net_realized_gains / total_capital, 2)}X Return")
    print("**********NET SUMMARY************************")


def compound_weekly(current_capital, weekly_profits, weekly_rate_of_return, brief_or_detailed):
    """
    This function calculates the interest on a weekly basis

    :param brief_or_detailed: do you want a brief or detailed summary
    :param weekly_rate_of_return:
    :param weekly_profits:
    :param current_capital:
    :return: current_capital
    """
    for week in range(4):  # 4 weeks in a month (weekly compound interest)
        weekly_profits.append(round(current_capital * weekly_rate_of_return))
        if brief_or_detailed == 'detailed' or brief_or_detailed == 'd':
            print(f"Start of Week {week + 1}: ${round(current_capital):,d} [+] ${int(weekly_profits[week]):,d} ")
        else:
            pass

        # changes current_capital so that it add the current weeks profits to the current capital amount
        current_capital = current_capital * (1 + weekly_rate_of_return)

        monthly_profits_total = 0  # get the total for the week and display the profits(This is gross)
        for each_weekly_profit in weekly_profits:
            monthly_profits_total = monthly_profits_total + each_weekly_profit

    if brief_or_detailed == 'detailed' or brief_or_detailed == 'd':
        print(f"Total Profits for the Month: ${monthly_profits_total:,d}")
        print(f"{colored('End of Month:', 'green')} ${int(current_capital):,d}")
    else:
        pass

    return current_capital


def compound_monthly(current_capital, monthly_contribution, brief_or_detailed, months_of_the_year,
                     years, weekly_rate_of_return):
    """

    :return:
    """

    for month in months_of_the_year:  # the month of the loop that we are currently on
        current_capital = current_capital + monthly_contribution
        if brief_or_detailed == 'detailed' or brief_or_detailed == 'd':
            print(f"\n\t\tYEAR {years + 1} {month.upper()}")
            print(f"Adding Monthly Contribution: [+] ${monthly_contribution:,d}")
        else:
            pass
        weekly_profits = []

        # This function calculates the interest on a weekly basis
        current_capital = compound_weekly(current_capital, weekly_profits, weekly_rate_of_return, brief_or_detailed)

    return current_capital


def compound_yearly(time_frame_for_investment, current_capital, tax_amount, brief_or_detailed,
                    monthly_contribution, weekly_rate_of_return, initial_investment_for_brief_summary,
                    tax_rate, each_percentage_weekly_rate_of_return):

    months_of_the_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                          'August', 'September', 'October', 'November', 'December']

    # This specifies how many years you will be investing your money
    for years in range(time_frame_for_investment):
        # helps me keep tracking of the profits for just the current year
        start_of_the_year_capital = current_capital - tax_amount
        current_capital = start_of_the_year_capital

        if brief_or_detailed == 'detailed' or brief_or_detailed == 'd':
            print(f"\nStarting Capital = ${int(start_of_the_year_capital):,d}")
            print(f"Monthly Additional Contribution = ${monthly_contribution:,d}")
        else:
            pass

        current_capital = compound_monthly(current_capital, monthly_contribution, brief_or_detailed,
                                           months_of_the_year, years, weekly_rate_of_return)

        # total profits for the current year
        total_profits = current_capital - start_of_the_year_capital - monthly_contribution * 12
        # total amount of your own contribution
        total_capital = initial_investment_for_brief_summary + monthly_contribution * 12 * (years + 1)

        # This will be the tax amount that you will pay at the end of each year
        tax_amount = total_profits * (tax_rate / 100)

        # all time total profits total
        total_profits_total = current_capital - total_capital - tax_amount
        # set ending capital as a place holder for the value in current capital
        ending_capital = current_capital
        # net profits after taxes are taken out for that specific year
        net_realized_gains = ending_capital - tax_amount

        # Prints the brief summary report at the end of the time frame you selected to invest your money
        if (years + 1) == time_frame_for_investment and brief_or_detailed != 'detailed' and brief_or_detailed != 'd':
            brief_summary(years, net_realized_gains, total_capital, initial_investment_for_brief_summary,
                          each_percentage_weekly_rate_of_return, monthly_contribution, tax_rate)
        # Prints the detailed summary for the year, displays gross and net information for that year
        elif brief_or_detailed != 'detailed' and brief_or_detailed != 'd':
            pass
        else:
            summary(years, start_of_the_year_capital, total_capital, net_realized_gains, tax_rate,
                    ending_capital, total_profits, tax_amount, total_profits_total,
                    initial_investment_for_brief_summary, each_percentage_weekly_rate_of_return, monthly_contribution)


# fix the shadow names and the tax_amount=0 parameter value not being used
def compound(brief_or_detailed, *initial_investment_amounts):  # needs starting capital(s) in order to work
    """
    This function will figure out how much money you will make after a certain amount of time, will take into
    consideration how much money you started with and your interest rate every week, etc

    :param brief_or_detailed: print brief summary or long summary, prints long summary by default
    :return: nothing
    """

    # This contribution will be added on to your current investment at the start of every month
    print("\nEnter 1 Number that you would like your Monthly Contribution to be WITHOUT Commas Ex: 1000")
    monthly_contribution = int(input("What is your Monthly Contribution? "))

    # This will determine the amount of years that you want to invest your money
    print("\nPlease Enter a Whole Number and NOT a Decimal Ex: 5")
    time_frame_for_investment = int(input("How Many Years do you want to invest your money? "))

    # This will be the rate at which your money will be taxed at the end of each year
    print("\nPlease Enter a Number Without the Percentage Symbol Ex: 22 24.5 37 30.5 etc")
    tax_rate = float(input("Please enter you projected Tax Rate: "))

    # need to figure out more information on why this worked and a for loop did not work for me to convert the
    # strings from input() into integers but list comprehension did...?
    # Enter your Desired Weekly Rate of Returns Ex: 1 1.5 2 2.5 (Without the percent sign)
    print("\nInput the Weekly Rate of Return(s) as a Percentage --> Ex: 1 1.5 2 ")
    weekly_rate_of_returns_list = list(float(num) for num in
                                       input(
                                           "Enter the Different Weekly Rate of Returns(s) separated by space ").split())

    for each_percentage_weekly_rate_of_return in weekly_rate_of_returns_list:
        # This is done so that the user can enter a human readable decimal like 1.5 instead of 1.015 or .015
        # This is the only reason that this is done
        weekly_rate_of_return = each_percentage_weekly_rate_of_return / 100

        # need to figure out more information on why this worked and a for loop did not work for me to convert the
        # strings from input() into integers but list comprehension did...?
        # gets me the first parameter in the *args
        for each_starting_capital in initial_investment_amounts:
            # gets me the first element in the first parameter in *args
            for current_capital in each_starting_capital:
                # resets tax amount each time you get a new starting value from the starting_capitals_list
                tax_amount = 0
                # for brief_summary can keep track of initial inv
                initial_investment_for_brief_summary = current_capital

                # compounds the money by calling the compound_yearly function
                compound_yearly(time_frame_for_investment, current_capital, tax_amount,
                                brief_or_detailed, monthly_contribution, weekly_rate_of_return,
                                initial_investment_for_brief_summary, tax_rate, each_percentage_weekly_rate_of_return)


# Does a short summary of the results
def compound_summary_brief():
    """
    Calls the Compound Function
    This function will display the 5 year summaries. It will not display the monthly information or gross information
    """
    compound(brief_or_detailed_summary_answer, starting_capital)


# Does a long summary of the results
def compound_summary_long():
    """
    Calls the Compound Function and it will display all the information available
    :return:
    """
    compound(brief_or_detailed_summary_answer, starting_capital)


print("\nIf you want the Detailed Summary type: 'detailed' or 'd' "
      "\nIf you want the Brief Summary Hit Enter or Press any Key")
brief_or_detailed_summary_answer = input("\nDo you want the Brief Summary or the Detailed Summary? ")

# need to figure out more information on why this worked and a for loop did not work for me to convert the
# strings from input() into integers but list comprehension did...?
print("\nDo not use commas when entering your Desired Starting Capital(s) Ex: 10000 15000 20000 etc")
starting_capital = [int(num) for num in input("Enter the Starting Capital(s) separated by space ").split()]

if brief_or_detailed_summary_answer.lower() == 'detailed' or brief_or_detailed_summary_answer.lower() == 'd':
    compound_summary_long()
else:
    compound_summary_brief()
