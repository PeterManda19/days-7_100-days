print("Welcome to Fake Fan Question Generator!")
print()
print("""Let's find out if you are a true superfan of the same show or movie that interests me?""")
print()
name = input("Please enter 'show' or 'movie' without the quotes? ")
print()
if name.lower() == "show":
  print("The American show that was hosted by a famous South African?")
  print()
  showName = input("Please enter the name of the show: ")
  print()
  if showName.lower() == "the daily show with trevor noah." or showName.lower() == "the daily show" or showName.lower() == "daily show":
    print("You got it!!! You are a true fan of Trevor Noah.😀")
  else: 
    print("Fake Fan!😀")
elif name.lower() == "movie":
  print("""This black American actor is one of the best if not the best ever. 
He is famous for his looks and the phrase 'My man', that he says in my best movie of his.""")
  print()
  movieName = input("What is the name of the movie he stars in? ")
  print()
  if movieName.lower() == "american gangster":
    print("You are true fan of Denzel Washington!!!")
  else:
    print("Fake Fan!")
else:
  print("Fake Fan!")