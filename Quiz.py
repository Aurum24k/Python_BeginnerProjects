#This program is created by Aniket Ullewar. The Quiz program contain category and difficulty.

def result(q,answers):
    counter=0
    print("Answer sheet:")
    for i in range(len(answers)):
        if q[i]==answers[i]:
            print(f"Q.{i+1}: correct")
            counter+=1
        else:
            print(f"Q.{i+1}: wrong")
    print(f"Your final score:{counter}/{len(answers)}")

def geography_easy():
    answers=["c","b","c"]
    q=[]

    q.append(input('''1} Which is the name of one of the 7 continents?
    a)China
    b)India
    c)Asia
    Your Answer:''').lower())
    q.append(input('''2} what is the largest planet in our solar system?
    a)Earth
    b)Jupiter
    c)Mars
    Your Answer:''').lower())
    q.append(input('''3} what is the capital of India?
    a)Mumbai
    b)Kolkata
    c)New Delhi
    Your Answer:''').lower())
    result(q,answers)

def geography_normal():
    answers=["a","b","c"]
    q=[]

    q.append(input('''1} Which is the highest mountain peak in India?
    a)Kanchenjunga
    b)Mount everest
    c)Sahyadri range
    Your Answer:''').lower())
    q.append(input('''2} Which is the smallest country in the world by area?
    a)Sri Lanka
    b)Vatican City
    c)New Zealand
    Your Answer:''').lower())
    q.append(input('''3} Which country is known as the Land of the Rising Sun?
    a)Australia
    b)China
    c)Japan
    Your Answer:''').lower())
    result(q,answers)

def geography_hard():
    answers=["b","b","c"]
    q=[]

    q.append(input('''1} What is the capital city of Uruguay?
    a)Minnesota
    b)Montevideo
    c)Montana
    Your Answer:''').lower())
    q.append(input('''2} What is the only flag to not have four sides?
    a)Sri Lanka
    b)Nepal
    c)New Zealand
    Your Answer:''').lower())
    q.append(input('''3} How many timezones are there in China?
    a)Four
    b)Two
    c)One
    Your Answer:''').lower())
    result(q,answers)


def science_easy():
    answers=["a","c","c"]
    q=[]
    q.append(input('''1} what is the Powerhouse of the cell?
    a)mitochondria
    b)lysosomes
    c)endoplasmic rectacilum
    Your Answer:''').lower())
    q.append(input('''2} what is Omniverse?
    a)Plant eater
    b)living organism eater
    c)both
    Your Answer:''').lower())
    q.append(input('''3}which is the smallest bone?
    a)Nose
    b)Cheek
    c)Pinna(ears)
    Your Answer:''').lower())
    result(q,answers)

def science_normal():
    answers=["b","b","c"]
    q=[]
    q.append(input('''1} How many senses do humans have?
    a)Seven
    b)Five
    c)Four
    Your Answer:''').lower())
    q.append(input('''2} what is the largest desert in the world?
    a)Sahara
    b)Antartica
    c)Gobi
    Your Answer:''').lower())
    q.append(input('''3}which is the only planet to spin clockwise?
    a)Jupiter
    b)Mars
    c)Venus
    Your Answer:''').lower())
    result(q,answers)

def science_hard():
    answers=["a","c","c"]
    q=[]
    q.append(input('''1} Which blood type is the rarest in humans?
    a)AB negative
    b)A positive
    c)AB positive
    Your Answer:''').lower())
    q.append(input('''2} Bees are not present in which continent?
    a)Africa
    b)Asia
    c)Antarctica
    Your Answer:''').lower())
    q.append(input('''3}At what temperature are Celsius and Fahrenheit equal?
    a)-30
    b)30
    c)-40
    Your Answer:''').lower())
    result(q,answers)

def history_easy():
    answers=["b","b","a"]
    q=[]
    q.append(input('''1} who is the austrian painter?
    a)lenordo di caprio
    b)Adolf hitler
    c)chandragupta
    Your Answer:''').lower())
    q.append(input('''2} who passed the bill article 360?
    a)Monmohan singh
    b)Narendra Modi
    c)None of the above
    Your Answer:''').lower())
    q.append(input('''3}when did india got its independence?
    a)1947
    b)1936
    c)1950
    Your Answer:''').lower())
    result(q,answers)

def history_normal():
    answers=["c","c","a"]
    q=[]
    q.append(input('''1} Who was the first President of the Indian National Congress?
    a)Kamala Nehru
    b)Indira Gandhi
    c)Womesh Chandra Banerjee
    Your Answer:''').lower())
    q.append(input('''2} Which of the following events is considered a turning point in the Indian freedom struggle?
    a)battle of plassey
    b)The sepoy Mutiny
    c)The Non-cooperation movement
    Your Answer:''').lower())
    q.append(input('''3} Who is known as the "Father of the Indian Renaissance"?
    a)Raja Ram Mohan Roy
    b)Jawahralal nehru
    c)Subash Chandra Bose
    Your Answer:''').lower())
    result(q,answers)

def history_hard():
    answers=["a","a","a"]
    q=[]
    q.append(input('''1} The rulers of which among the following dynasties adopted the title Devaputra ?
    a)Kushana
    b)Maurya
    c)Saka-Kshatrapa
    Your Answer:''').lower())
    q.append(input('''2} Where was the second Jain council held?
    a)Vallabhi
    b)Patliputra
    c)Vaishali
    Your Answer:''').lower())
    q.append(input('''3} The “Battle of Ten Kings” is depicted in which mandala of Rig Veda?
    a)Seventh
    b)Ninth
    c)Eighth
    Your Answer:''').lower())
    result(q,answers)

while True:
    category=input('''Which Category do you like to choose:
    a)geography
    b)science
    c)history
    Your choice:''').lower()

    difficulty=input('''what difficulty do you prefer:
    a)Easy
    b)Normal
    c)Hard
    Your choice:''').lower()

    if category=="a":
        if difficulty=="a":
            geography_easy()
        elif difficulty=="b":
            geography_normal()
        elif difficulty=="c":
            geography_hard()
        else:
            print("invalid difficulty option")
    elif category=="b":
        if difficulty=="a":
            science_easy()
        elif difficulty=="b":
            science_normal()
        elif difficulty=="c":
            science_hard()
        else:
            print("invalid difficulty option")
    elif category=="c":
        if difficulty=="a":
            history_easy()
        elif difficulty=="b":
            history_normal()
        elif difficulty=="c":
            history_hard()
        else:
            print("invalid difficulty")
    else:
        print("invaild category")
    
    choice=input("press any key to play and press n to stop:").lower()
    if choice=="n":
        break