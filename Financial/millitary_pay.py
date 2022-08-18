# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 								UPDATES TO MAKE	TO AIRMAN CLASS
#    Create a variable called inflation_annual_pay_raise and set it equal to 3% to account
#    for future year pay increases.

#    Only apply the raise to the base pay. Because BAH and BAS don't go up alot and the annual raise is
#    usually 2.6 percent or less

#    So 3% on base pay should be more than enough to account for any and all differences

#    Calculate the Net Pays
#    To Step up your game learn how to use the requests and bs4 library to pull this information
#    from the site links below to have this code dynamically change over time

#    Will get the Gross and Net Pays
#    Get the difference in pay between the ranks and display that information.
#
#    Maybe I should have the user input their bah rates even for the pay examples method,
#    that way this code will be more dynamic and pay examples can apply to people who are not at Barksdale afb
#
#    make a cut off-line using the print function after the loop goes through all the enlisted,
#    then one for after the loop goes through all the officer enlisted

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# 				    2020 Gross Pay SrA Mandy, Shaquille
# 			__________________________________________________________
#    			Categories		    Monthly		            Annual
# 			------------------- --------------------  ----------------
# 			Base Pay		        $2378.40		        $30,085
# 			BAH		                $1068		            $12,816
# 			BAS			            $372.71		            $4,473
# 		    Clothing Allowance       N/A			        $548.06
# 		    Total Compensation      $3918		            $46,377
#
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def disclaimer():
    """
    prints the disclaimer
    """

    print(
        """
    ==============================================================================================================\n
    # 						                DISCLAIMER:												               #												
    #               This class will output to you how much money you make Annually,						           #
    #               how much of your money is taxable and how much is not taxable	                               #
    #               how much you need to make to to keep the same pay if you decide to leave the Military,         #
    #               takes into consideration health insurance, untaxed income,					                   #
    #               may include TA but I'm not sure if I should.					                               #
    #               this only factors in base pay, bah, bas, clothing allowance and does not take into account     #
    #               extra pay like sign on reenlistment bonuses,						                           #
    #               clothing allowance(might add that), separation pay, etc					                       #
    ==============================================================================================================\n
        """
    )


class Airman:
    """
    This class will take:
    pay_grade for example: E3, O1
    airman's_name, you can choose whether to use your first name, last name or both
    for example: Shaquille Mandy or Shaquille or Mandy
    base_pay, for example: 1982.20
    basic_allowance_for_housing(bah), for example: 1068
    basic allowance_for_subsistence(bas), for example: 369.99
    years_of_service in the military, for example: 3
    Will get the Gross and Net Pays

    After it gets all this information it will compile all the data and display useful information

    Useful Links:
    Base Pays:
        - https://militarypay.defense.gov/Portals/3/Documents/ActiveDutyTables/2020%20Military%20Basic%20Pay%20Table.pdf
    BAH: https://www.defensetravel.dod.mil/site/bahCalc.cfm
    BAS: https://www.dfas.mil/militarymembers/payentitlements/Pay-Tables/BAS.html

    """

    def __init__(self):
        # test attributes, use the commented ones when testing is done
        self.name = "Mandy, Shaquille"
        self.pay_grade = 'e4'
        self.base_pay = 2378.40
        self.bah = 1068
        self.bas = 372.71
        self.years_of_service = 2
        # self.name = input("What is your name? ")
        # self.pay_grade = input("Pay Grade: ").lower()
        # self.base_pay = float(input("Base Pay: "))
        # self.bah = float(input("BAH: "))
        # self.bas = float(input("BAS: "))
        # self.years_of_service = input("Years of Service: ")

        # this is the standard clothing allowance pay for Air-Force according to
        # https://www.military.com/benefits/military-pay/allowances/clothing-allowances.html
        # you only get this 548.06 if you have been in for 3 of more years. If you have been in less than
        # the amount will be lower
        self.clothing_allowance = 548.06

        # your annual pays
        self.annual_base_pay = self.base_pay * 12
        self.annual_bah = self.bah * 12
        self.annual_bas = self.bas * 12
        self.total_compensation = self.annual_base_pay + self.annual_bah + self.annual_bas + self.clothing_allowance

        # pay grades keys followed by their respective rank values
        self.grades = {
            "e1": {
                "rank": "AB", "years_of_service": 1, "base_pay": 1733.10,
                "bah_single": 1068, "bah_dependents": 1326, 'bas': 372.71},
            "e2": {
                "rank": "Amn", "years_of_service": 1, "base_pay": 1942.50,
                "bah_single": 1068, "bah_dependents": 1326, 'bas': 372.71},
            "e3": {
                "rank": "A1C", "years_of_service": 2, "base_pay": 2171.10,
                "bah_single": 1068, "bah_dependents": 1326, 'bas': 372.71},
            "e4": {
                "rank": "SrA", "years_of_service": 3, "base_pay": 2507.10,
                "bah_single": 1068, "bah_dependents": 1326, 'bas': 372.71},
            "e5": {
                "rank": "SSgt", "years_of_service": 4, "base_pay": 2891.40,
                "bah_single": 1161, "bah_dependents": 1428, 'bas': 372.71},
            "e6": {
                "rank": "TSgt", "years_of_service": 8, "base_pay": 3653.10,
                "bah_single": 1302, "bah_dependents": 1737, 'bas': 372.71},
            "e7": {
                "rank": "MSgt", "years_of_service": 14, "base_pay": 4621.50,
                "bah_single": 1326, "bah_dependents": 1755, 'bas': 372.71},
            "e8": {
                "rank": "SMSgt", "years_of_service": 18, "base_pay": 5394.60,
                "bah_single": 1494, "bah_dependents": 1764, 'bas': 372.71},
            "e9": {
                "rank": "CMSgt", "years_of_service": 24, "base_pay": 6935.10,
                "bah_single": 1587, "bah_dependents": 1809, 'bas': 372.71},
            "o1e": {
                "rank": "2LT_e", "years_of_service": 4, "base_pay": 4136.40,
                "bah_single": 1431, "bah_dependents": 1758, 'bas': 256.68},
            "o2e": {
                "rank": "1LT_e", "years_of_service": 6, "base_pay": 5241.30,
                "bah_single": 1560, "bah_dependents": 1767, 'bas': 256.68},
            "o3e": {
                "rank": "Capt_e", "years_of_service": 8, "base_pay": 6435,
                "bah_single": 1731, "bah_dependents": 1848, 'bas': 256.68},
            "o1": {
                "rank": "2LT", "years_of_service": 1, "base_pay": 3287.10,
                "bah_single": 1221, "bah_dependents": 1470, 'bas': 256.68},
            "o2": {
                "rank": "1LT", "years_of_service": 2, "base_pay": 4313.40,
                "bah_single": 1395, "bah_dependents": 1734, 'bas': 256.68},
            "o3": {
                "rank": "Capt", "years_of_service": 4, "base_pay": 5847.30,
                "bah_single": 1623, "bah_dependents": 1770, 'bas': 256.68},
            "o4": {
                "rank": "Maj", "years_of_service": 12, "base_pay": 7831.80,
                "bah_single": 1740, "bah_dependents": 1977, 'bas': 256.68},
            "o5": {
                "rank": "Lt Col", "years_of_service": 18, "base_pay": 9277.50,
                "bah_single": 1749, "bah_dependents": 2142, 'bas': 256.68},
            "o6": {
                "rank": "Col", "years_of_service": 24, "base_pay": 11467.80,
                "bah_single": 1752, "bah_dependents": 2160, 'bas': 256.68},
            "o7": {
                "rank": "Brig Gen", "years_of_service": 30, "base_pay": 13656,
                "bah_single": 1764, "bah_dependents": 2181, 'bas': 256.68},
            "o8": {
                "rank": "Lt Gen", "years_of_service": 30, "base_pay": 15471.30,
                "bah_single": 1764, "bah_dependents": 2181, 'bas': 256.68},
            "o9": {
                "rank": "Maj Gen", "years_of_service": 30, "base_pay": 16441.80,
                "bah_single": 1764, "bah_dependents": 2181, 'bas': 256.68},
            "o10": {
                "rank": "General", "years_of_service": 30, "base_pay": 16441.80,
                "bah_single": 1764, "bah_dependents": 2181, 'bas': 256.68},
        }

    def my_pay(self):
        """
        you input your actual pay values (Base Pay, BAH, BAS) and you get the most accurate results

        This Method will display:

        SrA Mandy Shaquille:
        3 Years of Service
        Base Pay: $2431.80/month, $29181.6/year
        BAH: $1068/month, $12816/year
        BAS: $372.71/month, $4472.52/year
        Clothing Allowance: $548.06/year
        Total Compensation: $46394/year
        You need to make $XXX to maintain the same pay outside the military
        """
        print(f"\n\t\t\t\t{self.years_of_service} Years of Service")
        print(f"\n\t\t2020 Gross Pay {self.grades[self.pay_grade]['rank']} {self.name}: ")
        print("_" * 50)
        print("\tCategories\t\t\tMonthly\t\t\tAnnual")
        print("\t" + "-" * 10 + "\t\t\t" + "-" * 7 + "\t\t\t" + "-" * 7)
        print(f"\tBase Pay\t\t\t${self.base_pay}\t\t\t${round(self.annual_base_pay)}")
        print(f"\tBAH \t\t\t\t${self.bah}\t\t\t${self.annual_bah}")
        print(f"\tBAS \t\t\t\t${self.bas}\t\t\t${round(self.annual_bas)}")
        print(f"\tClothing Allowance\tN/A\t\t\t\t${self.clothing_allowance}")
        print(
            f"\tTotal Compensation\t${round((self.total_compensation - self.clothing_allowance) / 12)}"
            f"\t\t\t${round(self.total_compensation)}\n\n"
        )

    def pay_examples(self):
        """

        This method will display pay examples for all ranks
        For Example:
        YEAR 2020
        =====================
        SrA Mandy Shaquille:
        3 Years of Service
        Base Pay: $2431.80/month, $29181.6/year
        BAH: $1068/month, $12816/year
        BAS: $372.71/month, $4472.52/year
        Clothing Allowance: $548.06/year
        Total Compensation: $46394/year
        You need to make $XXX to maintain the same pay outside the military

        """

        # prints the disclaimer
        disclaimer()

        # loops through the self.grades dictionary and prints the information for Airman with Bah Single rates
        for each_pay_grade in self.grades:
            rank = self.grades[each_pay_grade]['rank']
            years_of_service = self.grades[each_pay_grade]['years_of_service']
            base_pay = round(self.grades[each_pay_grade]['base_pay'])
            bah_single = self.grades[each_pay_grade]['bah_single']
            bas = self.grades[each_pay_grade]['bas']
            total_compensation = round((base_pay + bah_single + bas) * 12 + self.clothing_allowance)
            # Printing the information
            # BAH Single Rates are shown in this for loop, will do another with the bah dependent rates

            # prints enlisted banner
            if each_pay_grade == "e1":
                print("\n" * 5)
                print("/" * 100 + "\n" * 3)
                print("\t" * 10 + "ENLISTED PAY" + "\n" * 3)
                print("/" * 100 + "\n" * 5)

            # prints the information in a table like structure
            print(f"\n\t\t\t\t{years_of_service} Years of Service")
            print(f"\n\t\t2020 Gross Pay {rank} {self.name}: ")
            print("_" * 50)
            print("\tCategories\t\t\tMonthly\t\t\tAnnual")
            print("\t" + "-" * 10 + "\t\t\t" + "-" * 7 + "\t\t\t" + "-" * 7)
            print(f"\tBase Pay\t\t\t${base_pay}\t\t\t${round(base_pay * 12)}")
            print(f"\tBAH \t\t\t\t${bah_single}\t\t\t${bah_single * 12}")
            print(f"\tBAS \t\t\t\t${bas}\t\t\t${round(bas * 12)}")
            print(f"\tClothing Allowance\tN/A\t\t\t\t${self.clothing_allowance}")
            print(
                f"\tTotal Compensation\t${round((total_compensation - self.clothing_allowance) / 12)}"
                f"\t\t\t${round(total_compensation)}\n\n"
            )

            # prints officer banner
            if each_pay_grade == "e9":
                print("\n" * 5)
                print("/" * 100 + "\n" * 3)
                print("\t" * 10 + "OFFICER PAY" + "\n" * 3)
                print("/" * 100 + "\n" * 5)

        # cut off-line for Airman with BAH Single Rates
        # cut off-line for Airman with BAH Single Rates
        # cut off-line for Airman with BAH Single Rates
        # loops through the self.grades dictionary and prints the information for Airman with Bah Dependent rates
        for each_pay_grade in self.grades:
            rank = self.grades[each_pay_grade]['rank']
            years_of_service = self.grades[each_pay_grade]['years_of_service']
            base_pay = round(self.grades[each_pay_grade]['base_pay'])
            bah_dependents = self.grades[each_pay_grade]['bah_dependents']
            bas = self.grades[each_pay_grade]['bas']
            total_compensation = round((base_pay + bah_dependents + bas) * 12 + self.clothing_allowance)
            # Printing the information
            # BAH Single Rates are shown in this for loop, will do another with the bah dependent rates

            # prints enlisted banner
            if each_pay_grade == "e1":
                print("\n" * 5)
                print("/" * 100 + "\n" * 3)
                print("\t" * 10 + "ENLISTED PAY BAH WITH DEPENDENTS" + "\n" * 3)
                print("/" * 100 + "\n" * 5)

            # prints the information in a table like structure
            print(f"\n\t\t\t\t{years_of_service} Years of Service")
            print(f"\n\t\t2020 Gross Pay {rank} {self.name}: ")
            print("_" * 50)
            print("\tCategories\t\t\tMonthly\t\t\tAnnual")
            print("\t" + "-" * 10 + "\t\t\t" + "-" * 7 + "\t\t\t" + "-" * 7)
            print(f"\tBase Pay\t\t\t${base_pay}\t\t\t${round(base_pay * 12)}")
            print(f"\tBAH \t\t\t\t${bah_dependents}\t\t\t${bah_dependents * 12}")
            print(f"\tBAS \t\t\t\t${bas}\t\t\t${round(bas * 12)}")
            print(f"\tClothing Allowance\tN/A\t\t\t\t${self.clothing_allowance}")
            print(
                f"\tTotal Compensation\t${round((total_compensation - self.clothing_allowance) / 12)}"
                f"\t\t\t${round(total_compensation)}\n\n"
            )

            # prints officer banner
            if each_pay_grade == "e9":
                print("\n" * 5)
                print("/" * 100 + "\n" * 3)
                print("\t" * 10 + "OFFICER PAY BAH WITH DEPENDENTS" + "\n" * 3)
                print("/" * 100 + "\n" * 5)


shaquille = Airman()
shaquille.my_pay()
shaquille.pay_examples()
