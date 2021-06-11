# This is a application that will calculate compound interest over a certain amount of time
# given certain interest rates, starting amounts, weekly rate of returns and your tax rate
from termcolor import colored

# need to figure out more information on why this worked and a for loop did not work for me to convert the
# strings from input() into integers but list comprehension did...?
print("\nDo not use commas when entering your Desired Starting Capital(s) Ex: 10000 15000 20000 etc")
starting_capital = list(int(num) for num in input("Enter the Starting Capital(s) separated by space ").split())


# want to display just a little bit of information for different interest rates, starting capitals, etc
def brief_summary(years, net_realized_gains, total_capital, initial_investment_for_brief_summary,
                  each_weekly_rate_of_return, monthly_contribution, tax_rate):
    """
    Display a less detailed Summary report of your investments, takes in the variable as parameters from your
    compound() function
    :param tax_rate:
    :param monthly_contribution:
    :param each_weekly_rate_of_return:
    :param initial_investment_for_brief_summary:
    :param years:
    :param net_realized_gains:
    :param total_capital:
    :return:
    """
    print()
    print(f"Printing Summary Report For Year {years + 1}")
    print("**********NET SUMMARY************************")
    print(f"Initial Investment: ${initial_investment_for_brief_summary:,d}")
    print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
    print(f"Weekly Rate Of Return: {round(each_weekly_rate_of_return, 2)}%")
    print(f"Tax Rate: {tax_rate}%")
    print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
    print(f"Total Contributions To Date: ${total_capital:,d}")
    print(f"{int(net_realized_gains):,d} / {total_capital:,d} ({round(net_realized_gains / total_capital, 2)}X Return)")
    print("**********NET SUMMARY************************")


def summary(years, start_of_the_year_capital, total_capital, net_realized_gains, tax_rate, ending_capital,
            total_profits, tax_amount, total_profits_total, initial_investment_for_brief_summary,
            each_weekly_rate_of_return, monthly_contribution):
    """
    Display a Summary report of your investments, takes in the variable as parameters from your compound() function
    :param tax_rate:
    :param monthly_contribution:
    :param each_weekly_rate_of_return:
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

    print("**********GROSS SUMMARY**********************")
    print(f"Initial Investment: ${initial_investment_for_brief_summary:,d}")
    print(f"Start of The Current Year Investment: ${int(start_of_the_year_capital):,d}")
    print(f"Additional Monthly Contribution: ${monthly_contribution:,d}")
    print(f"Weekly Rate Of Return: {round(each_weekly_rate_of_return, 2)}%")
    print(f"{colored('Profits for the Year: ', 'green')}${int(total_profits):,d}")
    print(f"{colored('Ending Investment: ', 'green')}${int(ending_capital):,d}")
    print(f"${round(ending_capital):,d} / ${round(total_capital):,d} = "
          f"{round(ending_capital / total_capital, 2)}X Return")
    print("**********GROSS SUMMARY**********************")
    print()

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


# fix the shadow names and the tax_amount=0 parameter value not being used
def compound(brief='', *starting_capitals):  # needs starting capital(s) in order to work
    """
    This function will figure out how much money you will make after a certain amount of time, will take into
    consideration how much money you started with and your interest rate every week, etc

    :param brief: print brief summary or long summary, prints long summary by default
    :return: nothing
    """
    year = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']
    # This total will be added on to your Investments every month on the start of the first week
    print("\nEnter 1 Number that you would like your Monthly Contribution to be WITHOUT Commas Ex: 1000")
    monthly_contribution = int(input("What is your Monthly Contribution? "))
    # number of years that you want to invest
    print("\nPlease Enter a Whole Number and NOT a Decimal Ex: 5")
    time_frame_for_investment = int(input("How Many Years do you want to invest your money? "))
    print("\nPlease Enter a Number Without the Percentage Symbol Ex: 22 24.5 37 30.5 etc")
    tax_rate = float(input("Please enter you projected Tax Rate: "))  # Example 37 or 37.5 or 22 or 24.6 etc
    # need to figure out more information on why this worked and a for loop did not work for me to convert the
    # strings from input() into integers but list comprehension did...?
    # Enter your Desired Weekly Rate of Returns Ex: 1 1.5 2 2.5 (Without the percent sign)
    print("\nDo not use percent signs when entering your Weekly Rate of Return(s) Ex: 1 1.5 2 etc")
    weekly_rate_of_returns_list = list(float(num) for num in
                                       input(
                                           "Enter the Different Weekly Rate of Returns(s) separated by space ").split())

    for each_weekly_rate_of_return in weekly_rate_of_returns_list:
        weekly_rate_of_return = each_weekly_rate_of_return
        weekly_profits_calculator = weekly_rate_of_return / 100

        for each_starting_capital in starting_capitals:  # gets me the first parameter in the *args
            for current_capital in each_starting_capital:  # gets me the first element in the first parameter in *args
                # resets tax amount each time you get a new starting value from the starting_capitals_list
                tax_amount = 0
                # for brief_summary can keep track of initial inv
                initial_investment_for_brief_summary = current_capital

                # This specifies how many years you will be investing your money
                for years in range(time_frame_for_investment):
                    # helps me keep tracking of the profits for just the current year
                    start_of_the_year_capital = current_capital - tax_amount
                    current_capital = start_of_the_year_capital
                    if brief.lower() == 'brief':
                        pass
                    else:
                        print(f"\nStarting Capital = ${int(start_of_the_year_capital):,d}")
                        print(f"Monthly Additional Contribution = ${monthly_contribution:,d}")

                    for month in year:  # the month of the loop that we are currently on
                        current_capital = current_capital + monthly_contribution
                        if brief.lower() == 'brief':
                            pass
                        else:
                            print(f"\n\t\tYEAR {years + 1} {month.upper()}")
                            print(f"Adding Monthly Contribution: [+] ${monthly_contribution:,d}")
                        weekly_profits = []

                        for week in range(4):  # 4 weeks in a month (weekly compound interest)
                            weekly_profits.append(round(current_capital * weekly_profits_calculator))
                            if brief.lower() == 'brief':
                                pass
                            else:
                                print(f"Start of Week {week + 1}: ${round(current_capital):,d} "
                                      f"[+] ${int(weekly_profits[week]):,d} ")
                            current_capital = current_capital * (1 + weekly_profits_calculator)

                        weekly_profits_total = 0  # get the total for the week and display the profits(This is gross)
                        for each_weekly_profit in weekly_profits:
                            weekly_profits_total = weekly_profits_total + each_weekly_profit
                        if brief.lower() == 'brief':
                            pass
                        else:
                            print(f"Total Profits for the Month: ${weekly_profits_total:,d}")
                            print(f"{colored('End of Month:', 'green')} ${int(current_capital):,d}")

                    # THIS IS THE TAX INFORMATION SECTION THAT HELPS GET THE NET AMOUNT, PROFITS, TAXES DUE EACH YEAR
                    # WITH TAXES THIS IS THE ACTUAL INCREASE ON YOUR MONEY, TAXES ARE DONE ANNUALLY
                    # total profits for the current year
                    total_profits = current_capital - start_of_the_year_capital - monthly_contribution * 12
                    total_capital = initial_investment_for_brief_summary + monthly_contribution * 12 * (years + 1)
                    # just blindly assuming you are paying a total of 37% taxes
                    tax_amount = total_profits * (tax_rate / 100)
                    # total profits total (since week 1)
                    total_profits_total = current_capital - total_capital - tax_amount
                    ending_capital = current_capital
                    net_realized_gains = ending_capital - tax_amount

                    # on year 5 print the brief summary
                    if (years + 1) == time_frame_for_investment and brief.lower() == 'brief':
                        brief_summary(years, net_realized_gains, total_capital, initial_investment_for_brief_summary,
                                      each_weekly_rate_of_return, monthly_contribution, tax_rate)

                    if brief.lower() != 'brief':  # print the long summary
                        summary(years, start_of_the_year_capital, total_capital, net_realized_gains, tax_rate,
                                ending_capital, total_profits, tax_amount, total_profits_total,
                                initial_investment_for_brief_summary, each_weekly_rate_of_return, monthly_contribution)


def compound_summary_brief():  # needs current_capital and tax_amount in order to work
    """
    Calls the Compound Function
    This function will display the 5 year summaries. It will not display the monthly information or gross information
    """
    compound('brief', starting_capital)


def compound_summary_long():
    """
    Calls the Compound Function and it will display all the information available
    :return:
    """
    compound('', starting_capital)


def main():
    """
    Runs the code, calls the neccessary function within the script
    Run main() and the program will walk you through the rest of the steps for entering user information
    :return:
    """
    print("\nIf you want the Detailed Summary type: 'detailed' or 'd' "
          "if you want the Brief Summary Press Any Key and Hit Enter:)")
    brief_or_detailed_summary_answer = input("Do you want the Brief Summary or the Detailed Summary? ")

    if brief_or_detailed_summary_answer.lower() == 'detailed' or brief_or_detailed_summary_answer.lower() == 'd':
        compound_summary_long()
    else:
        compound_summary_brief()


main()





















# # This is a application that will calculate compound interest over a certain amount of time
# from termcolor import colored
#
# # THE USER INPUTED VARIABLES
# starting_capital_user_inputed = int(input("What is your Starting Capital(Without Commas)? "))
# monthly_contribution_user_inputed = int(input("What is your Monthly Contribution(Without Commas)? "))
# time_frame_for_investment_user_inputed = int(input("How Many Years do you want to invest your money? "))  # number of years that you want to invest
# weekly_rate_of_return_user_inputed = float(input("Please enter your Weekly Rate Of Return(Without % symbol): "))  # weekly_rate_of_return_user_inputed = 1.01
# tax_rate_user_inputed = int(input("Please enter you projected Tax Rate(Without % symbol): "))  # example 37
# current_capital = starting_capital_user_inputed
# ending_capital = 0
# total_profits = 0
# total_contribution = monthly_contribution_user_inputed * 12 * time_frame_for_investment_user_inputed
# weekly_profits_calculator = weekly_rate_of_return_user_inputed / 100
# tax_amount = 0
# year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
#
# def summary():
#     print()
#     print(f"Printing Summary Report For Year {years + 1}")
#
#     print("**********GROSS SUMMARY**********************")
#     print(f"Starting Investment: ${int(start_of_the_year_capital):,d}")
#     print(f"Additional Monthly Contribution: ${monthly_contribution_user_inputed:,d}")
#     print(f"Weekly Rate Of Return: {weekly_rate_of_return_user_inputed}%")
#     print(f"{colored('Profits for the Year: ', 'green')}${int(total_profits):,d}")
#     print(f"{colored('Ending Investment: ', 'green')}${int(ending_capital):,d}")
#     print(f"${round(ending_capital):,d} / ${round(total_capital):,d} = {round(ending_capital / total_capital, 2)}X Your Money")
#     print("**********GROSS SUMMARY**********************")
#     print()
#
#     print("**********NET SUMMARY************************")
#     print(f"Tax Rate: {int(tax_rate_user_inputed)}%")
#     print(f"{colored('Tax Amount Due:', 'red')} ${round(tax_amount):,d}")
#     print(f"{colored('Profits for the Year: ', 'green')}${round(total_profits - tax_amount):,d}")
#     print(f"{colored('Net Investment:', 'green')} ${int(net_realized_gains):,d}")
#     print(f"{int(net_realized_gains):,d} / {total_capital:,d} {round(net_realized_gains / total_capital, 2)}X Your Money")
#     print(f"Total Contributions: ${total_capital: ,d}(All time Total Contribution)")
#     print("**********NET SUMMARY************************")
#
#
# for years in range(time_frame_for_investment_user_inputed):  # This specifies how many years you will be investing your money
#     # helps me keep tracking of the profits for just the current year
#     start_of_the_year_capital = current_capital - tax_amount
#     current_capital = start_of_the_year_capital
#     print(f"\nStarting Capital = ${int(start_of_the_year_capital):,d}")
#     print(f"Monthly Additional Contribution = ${monthly_contribution_user_inputed:,d}")
#
#     for month in year:  # the month of the loop that we are currently on
#         current_capital = current_capital + monthly_contribution_user_inputed
#         print(f"\n\t\tYEAR {years + 1} {month.upper()}")
#         print(f"Adding Monthly Contribution: [+] ${monthly_contribution_user_inputed:,d}")
#         weekly_profits = []
#
#         for week in range(4):  # 4 weeks in a month (weekly compound interest)
#             weekly_profits.append(round(current_capital * weekly_profits_calculator))
#             print(f"Start of Week {week + 1}: ${round(current_capital):,d} [+] ${int(weekly_profits[week]):,d} ")
#             current_capital = current_capital * (weekly_rate_of_return_user_inputed / 100 + 1)
#
#         weekly_profits_total = 0  # get the total for the week and display the profits(This is gross)
#         for each_weekly_profit in weekly_profits:
#             weekly_profits_total = weekly_profits_total + each_weekly_profit
#         print(f"Total Profits for the Month: ${weekly_profits_total:,d}")
#         print(f"{colored('End of Month:', 'green')} ${int(current_capital):,d}")
#
#     # WITH TAXES THIS IS THE ACTUAL INCREASE ON YOUR MONEY, TAXES ARE DONE ANNUALY
#     total_profits = current_capital - start_of_the_year_capital - monthly_contribution_user_inputed * 12  # total profits for the current year
#     total_profits_total = current_capital - starting_capital_user_inputed - total_contribution  # total profits total
#     total_capital = starting_capital_user_inputed + monthly_contribution_user_inputed * 12 * (years + 1)
#     tax_amount = total_profits * (tax_rate_user_inputed / 100)
#     ending_capital = current_capital
#     net_realized_gains = ending_capital - tax_amount
#
#     summary()
