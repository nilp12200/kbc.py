questions = [
  [
    "the international literacy is observed on?", "sep8", "nov 28", "may 2",
    "sep22",  1
  ],
  [
    "the language of lakshdeep a.union territory of india is", "tamil", "hindi", "malayalam",
    "telgu", 3
  ],
  [
    "bahubali festival is related to", "islam ", "hindusm ", "budh",
    "jain", 4
  ],
  [
    "which day is observed as the world standard day", "june 26", "oct 14", "nov 15",
    "dec2", 2
  ],
  ["september 27 s celebrated every year as","teachers day","world toursim day","environment day","cricket day",2
  ],
  [
    "when we celebrate an environment day","5june","5oct","3dec","4 june",1
  ],
  [
    "who is the authour of 'manas kahans","khuswant singh","amirkhan","amritlal nagar","jsohi yash",3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 4
  ],
  [
    "what is your country","india","aus","canada","pakistan",1
  ],
  
]
print(len(questions))
# print(len[questions])

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  
  question = questions[i]
  
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"1.{questions[i][0]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
   
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")