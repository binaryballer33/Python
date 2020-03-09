import re

# message = 'Call me 813-813-8138 tomorrow, or at 843-843-8438'
#
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # use the r strings so that it doesn't treat the \ as a escape character
# mo = phoneNumRegex.search(message) # the .search method shows you the first occurence of the phone number in the message
# mo_all = phoneNumRegex.findall(message) # .findall method shows you everything that matches the regex
# print(mo) # shows you this is a regex match object
# print(mo.group())
# print(mo_all)

message2 = 'Call me 813-8138 tomorrow, or at 843-8438, test to see if regex see\'s this phone number as well 813-813-8138'
phoneNumRegex2 = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search(message2)
mo2_all = phoneNumRegex2.findall(message2)
print(mo2)
print(mo2.group())
print(mo2_all)
