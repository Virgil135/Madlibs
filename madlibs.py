# string concatenation (aka hot to put strings together)

# a few ways to do this
# course = "Python"
# print("Hello to " + course)
# print("Hello to {}".format(course))
# print(f"Hello to {course}")

adj = input("Adjective: ")
verb1 = input('Verb: ')
verb2 = input('Verb: ')
famous_person = input('Famous person: ')

madlib =  f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)