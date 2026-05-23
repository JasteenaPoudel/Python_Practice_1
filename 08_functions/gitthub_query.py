def create_query(langauge = "Python", stars = 50, sort = "desc"):
    return f"Language:{langauge}, Stars:{stars}, Sort:{sort}"

print(create_query())
print(create_query("Javascript", 100, "asc"))

