# 

favorite_languages = {
    "jen": "python",
    "sarah": "",
    "edward": "ruby",
    "phil": "python",
}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# make a list of prople who should take the languages poll
# include names in the list and not in the list
print()
take_poll = ["sam", "bill", "phil", "sarah"]
print(take_poll)
for person in take_poll:
    value = favorite_languages.get(person)
    if person in favorite_languages.keys() and value == "":
        print(f"Hi {person.title()}, please take our preferred language poll.")
    elif person not in favorite_languages.keys():
        print(f"Hi {person.title()}, please take our preferred language poll.")
    else:
        print(
            f"Hi {person.title()}, thank you for taking our language preference poll."
        )
