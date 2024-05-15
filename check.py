# when you write eval, its take a expression and it evaluates
# print(1+2, eval('1+2'), "asdfasdf")
# print(True == False)
# False		else
# None			in
# True
# and		for
# as
# not
# elif	if or

# a = None
# print(a)
# import django_rest_frame_work as drf

# print( 'san' in 'santosh')
# a = True
# print(not 1!=1)


# if condtion:
#     pass
# ----
# if condtion:
#     pass
# else:
#     pass
# ---
# if condtion:
#     pass
#     if or if else
# else:
#     pass
#     if or if else
#
# a = 5
# b = 4
# password = "some"
# if password == "some":
#     print("this is true")
#     print("inside A")
#
#     if b > 8:
#         print("inside B")
#     else:
#         print("Else B")
#
#     print("end of A")
# else:
#     if co:
#         if:
#
#     else:
#         if :
#         else:
#
#     if check_email:
#         pass
#     print("your password is wrong try one more")
#
# print("i am outside")

b = "xyx"
a = 2
if b == "abc":
    print("True")
else:
    print("false")

# if a > 5:
#     print("True")
# elif b < 4:
#     print("false")
#  there are something datatype:

a = 3
b = '3'
# str - string
# print(type(a))
# print(type(b))
# print(type('asdf'))
# print(type(2.2))
##########
# c = []  # empty list
# c = list()
print("---")
# print(c)
# eg
# c = ['santosh', 1, 2.4, [], {}, ()]
# print(type(c))
# print(len(c))
# print(c[0])
# print(c)
# c[1] = 435
# print(c)
##########
# d = ()  # tuples
# d = tuple()
d = ('santosh', 1, 2.4, [], {}, ())
# print(type(d))
# print(len(d))
print(d[0])
# print(d)
# d[1] = 435 # this is not going to work because tuples can't be modified

##########
e = {2, 5, 7, 'a', 2.3}  # set
# e = set()
# print(e)
f = {"key": "value"}  # dict
# f = dict() # empty dictionary

input_list = [2, 3, 35, 56, "santosh", 2, ["minhaas", 2, 4, 3.3], 4, 3.3, ["somename", 2, 4, 3.3],
              {"key": "value"}, {"key1": "value1"}]
# print(len(input_list))
# # print(input_list[1])
# print(input_list[0:len(input_list):1])
#
# print(input_list[15:0:34])  # [2] -->
print(input_list)
# for i in input_list:
#     print(i)
abc = [3, 4, [2, 3, 4, 5], 23]
for i in abc:
    if isinstance(i, list):
        print(i[0])
    print(i)
print("end")
