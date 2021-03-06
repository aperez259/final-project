while (score == 0): #question #1
    print("Here's your " + valueWon[score + 1] + " question:")
    x = random.randint(0,14) #This picks a random number to pick a random question from the list question2
    player = input(question1[x] + '\n' + multi1A[x] + '\n' + multi1B[x] + '\n' + multi1C[x] + '\n' + multi1D[x] + '\n') # the number that x is determines what question/answers is picked.
    player = player.lower()


    if player == correctAnswer1[x]: #if the player picked the correct answer between a-d, he will advance to the next one
         score = score + 1 #adds 1 to the score to keep track
         print ("Correct! You won " + valueWon[score]) #shows how much the player has won from the valueWon list
         print ('')

    elif player == 'leave': #if the player types leave, the game will end and he will get the amount of money he has already won.
         print ("Congratulations! You'll take home " + valueWon[score] +'!')
         break

    elif player != correctAnswer1[x]: #if the player gets the question incorrect, they will walk away with the last milestone (in this case it's $0)
         print ("I'm sorry, that was incorrect. You go home with " + valueWon[0])
         break
import random

# This list stores all the questions for that are used for question 1 ($100 question)
question1 = ['Scholars or intelectuals are commonly said to reside in what kind of tower?', 
'According to the proverb about hope, "Theres always a light at the end of" what?',
"In what children's game are participants chased by someone designated 'it'?",
"In the U.S., if it's not Daylight Savings Time, it's what?",
'According to the old saying, "Dont throw the baby out with the" what?',
'According to a common saying, if something is really cheap, its "a dime a" what?',
'Children are invited to roll eggs on the south lawn of the White House to celebrate what holiday?',
'Which of these gambling games required a pair of dice?',
'When refering to a commercial airline service, what do the initials TWA stand for?',
'How is a Popsicle generally served?',
'Which of the following consumer goods is the Gerber Products Co. best known for?',
"By definition, who keeps a building's premises clean and makes minor repairs?",
'A sprinkler system protects a building against what?',
'In the nursery rhyme "three blind mice," what got cut off?',
'Which of these is an example of calisthenic exercise?']

#This list stores all the 'A:' multiple choice answers for the question1 list
multi1A = ['A: Clock Tower','A: The journey','A: Tag','A: Borrowed time','A: Trash','A: Score','A: Easter','A: Craps','A: Try Wandering Around','A: In a cone','A: Potato chips','A: Chiropractor','A: Trespassing','A: Their breath','A: Jumping Jacks']

#This list stores all the 'B:' multiple choice answers for the question1 list
multi1B = ['B: Radio Tower','B: The day','B: Simon Says','B: Overtime','B: Diapers','B: Dozen','B: Haloween','B: Roulette','B: Two Winged Airplanes','B: In a bun','B: Baby food','B: Aviator','B: Burglary','B: Their tails','B: Rolling Ralphs']

#This list stores all the 'C:' multiple choice answers for the question1 list
multi1C = ['C: Ivory Tower','C: The tunnel','C: Charades','C: Standard time','C: Bathwater','C: Hundred','C: 4th of July','C: Poker','C: Trans World Airlines','C: On a stick','C: Chewing gum','C: Janitor','C: Fire','C: Their hair','C: Punching Pauls']

#This list stores all the 'D:' multiple choice answers for the question1 list
multi1D = ['D: Water Tower',"D: E.T's finger",'D: Hopscotch','D: Party time','D: Baby carriage','D: Too many','D: Election Day','D: Blackjack','D: The White Album','D: On wheat toast','D: Beer','D: Garbage collector','D: Flood','D: Their allowance','D: Jumping Jacks']

#This list stores the correct answers from the question1 list
correctAnswer1 = ['c','c','a','c','c','b','a','a','c','c','b','c','c','b','a']


# This list stores all the questions that are used for questions 2-5 ($200-$1,000 questions)
question2 = ['When an actor is said to chew up the scenery, what is he doing?',
'Which State has the Rocky Mountains going through it?',
'Which of these following organizations oversees competitive intercollege athletics in the U.S.?',
'Which of the following designs are traditionally found on candy canes?',
'In polo, what do players normally use to hit the ball?',
'What is the first letter of the Greek alphabet?',
'By definition, what does a meteorologist predict?',
'In baseball, what is the term for the fourth batter in a lineup?',
'Which of the following might you normally do with a "feather boa"?',
'Residents of Los Angeles are collectively called what?',
'A person with a tendency to drop things is commonly referred to as a what?',
'Which of the following groups made its victims "walk the plank"?',
'Useful inventions are often said to be "the greatest thing since" what?',
'The EPS urges people to produce less waste by engaging in efforts to Reduce, Reuse and what?',
'The cartoon character Bugs Bunny is often seen wating what kind of food?',
'An individual leaf of grass is usually refered to as a what?',
'Traditionally, "He loves me, he loves me not" would be said while plucking what?',
'According to the old saying, "a chain is only as strong as" what?',
'In the 1939 movie the "Wizard of Oz," what do Dorothy and her companions declare after "Lions and tigers and bears"?',
'If today is Friday the 13th, the first of the month fell on what day of the week?',
'Which of the following telephone area codes is not a toll-free call in the Unites States?',
'In U.S. personal ads, what do the letters ISO traditionally represent?',
'The Earth rotates towards which direction?',
'In baseball, what is the term for the player slated to bat after the on deck hitter?',
'What article of clothing is a garter belt typically used to hold up?',
'Which of the following U.S. coins in current circulation has a smooth, unnotched edge?',
"Which of the following is a part of the legislative branch of the U.S?",
'Which sign of the zodiac is represented by a bull?',
'A person who earns a Ph.D is literally a cerified doctor of what?',
'Which of the following is a Russian monetary unit?']

#This list stores all the 'A:' multiple choice answers for the question2 list
multi2A = ['A: Taking a lunch break','A: Wyoming','A: NCAA','A: Polka dots','A: Mallets','A: Alpha','A: Stock fluctuations','A: Show','A: Cage it','A: Angelenos','A: Oil hands','A: Knights','A: The light bulb','A: Recycle','A: Lettuce','A: Ear','A: Leafs','A: Its material','A: Oh my!','A: Thursday','A: 800',"A: I'm someone ordinary",'A: East','A: In the groove','A: Pants','A: Penny','A: FBI','A: Gemini','A: Photography','A: Schiling']

#This list stores all the 'B:' multiple choice answers for the question2 list
multi2B = ['B: Damaging the set','B: Tennessee','B: NFL','B: Stripes','B: Hands','B: Aleph','B: Earthquakes','B: Cleanup','B: Read it','B: Lost Angels','B: Grease mitts','B: Gladiators','B: The toaster','B: Rewrap','B: Apple','B: Blade','B: Flower petals','B: Its craftsman','B: Goodness gracious!','B: Saturday','B: 828','B: In search of','B: West ','B: Out on the field','B: Stockings','B: Nickel','B: President','B: Scorpio','B: Pharmacology','B: Rupee']

#This list stores all the 'C:' multiple choice answers for the question2 list
multi2C = ['C: Overacting','C: Ohio','C: NRA','C: Stars','C: Feet','C: Aye','C: Weather changes','C: Hopefull','C: Eat it','C: The Angels','C: Butter fingers','C: Monks','C: Baseball','C: Reprocess','C: Carrot','C: Staff','C: Grass','C: Its weakest link','C: Run!','C: Sunday','C: 877','C: I seek one','C: North','C: In a slump',"C: Men's girdle",'C: Dime','C: Department of Commerce','C: Pisces','C: Philosophy','C: Dutche mark']

#This list stores all the 'D:' multiple choice answers for the question2 list
multi2D = ['D: Memorizing his lines','D: Washington','D: NAACP','D: Crosses','D: Bats','D: Allah','D: Meteors','D: Babe','D: Wear it','D: Dudes','D: Teflon palms','D: Pirates','D: Sliced bread','D: Redo','D: Bugs','D: Twig','D: Eyebrows','D: Its metal','D: Who cares!','D: Monday','D: 888','D: It seems odd','D: South','D: In the hole','D: Necktie','D: Quarter','D: Senate','D: Taurus','D: Psychology','D: Ruble']

#This list stores the correct answers from the question2 list
correctAnswer2 = ['c','a','a','b','b','a','c','b','d','a','c','d','d','a','c','b','b','c','a','c','b','b','a','d','b','b','d','d','c','d']


# This list stores all the questions that are used for questions 6-10 ($2,000-$32,000 questions)
question3 = ['Which of the following landlocked countries in entirely contained within another country?',
'Which country is only a "de facto" state with little or no international recognition?',
'If you drive your car five kilometers, you will have traveled how many miles?',
'The orange blossom is the official flower of what state?',
"What chemical element's symbol is Pb?",
"In a classic children's book, where is the entrance to the magical land of narnia?",
'The abundance of lactic acid in your body will usually produce what sensation?',
'The piece of cartilage that separates the two nostrils in a human nose is called what?',
'What is the only Great Lake that lies wholly within the U.S.?',
'After teaming up professionally in 1957, which of these duos published several studies on human sexuality?',
'What color is most closely associated with alabaster?',
'In the 1970s and 1980s, what major fast food chain used the word "scrumpdillyishus" as its sligan?',
'Which of the following observances is part of the Islamic faith?',
'A renal transplant involves the replacement of what human organ?',
'Which of the following is thought to be directly formed by a collapsed star?',
'What collor is the leftmost in the NBC logo?',
'What is the capital of the U.S. state of Texas?',
'What brand of battery is sometimes referred to as the "Copper Top"?',
'Which of these precious metals or semiprecious stones is usually not blue?',
'On the TV show "Friends," Phoebe often performed which of these songs?',
'Which of these events occured in what is known as the "antebellum South"',
'Which of these Wachington D.C. buildings was called "The Palace" in its original palns?',
'At the beginning of a game of standard checkers, how many pieces are on the board?',
'What animal is represented by the constellation Lepus?',
'A scientific barometer measures pressure in which of the following units?',
'The Hindenburg was filled with what type of gas?',
'Go-Gurt, yogurt in a tube, is manufactured by what brand?',
'In the film "The Godfather Part II," mobster Hyman Roth declares, "Were bigger than" what?',
'What gaseous plant hormone helps trigger the fall of leaves in the autumn?',
'Which of the following saints is often portrayed holding the keys to heaven?']

#This list stores all the 'A:' multiple choice answers for the question13 list
multi3A = ['A: Lesotho','A: San Marino','A: 3.1 miles','A: California','A: Gold','A: Under a mountain','A: Fatigue','A: Septum','A: Lake Erie','A: Kinsey and Horney','A: Brown','A: Dairy Queen','A: Sukkoth','A: Kidney','A: Black hole','A: Red','A: Dallas','A: Energizer','A: Sapphire','A: Scaredy Cat','A: Radical Reconstruction','A: White House','A: 16','A: Hare','A: Baroms','A: Helium','A: Dannon','A: General Motors','A: Nitric oxide','A: St. Peter']

#This list stores all the 'B:' multiple choice answers for the question3 list
multi3B = ['B: Burkina Fasko','B: Andora','B: 4.0 miles','B: Georgia','B: Lead','B: In a phone booth','B: Sadness','B: Sinus','B: Lake Huron','B: The Mitchell Brothers','B: Red',"B: Hardee's",'B: Ramadan','B: Liver','B: Supernova','B: Green','B: Houston','B: Rayovac','B: Amethyst','B: Grouchy Cat','B: Ole Miss desegregated','B: Pentagon','B: 18','B: Dog','B: Farads','B: Hydrogen',"B: Breyer's",'B: Coca-Cola','B: Ethylene','B: St. Paul']

#This list stores all the 'AC:' multiple choice answers for the question3 list
multi3C = ['C: Mongolia','C: Transnistria','C: 6.2 miles','C: Hawaii','C: Tin','C: At the bottom of a well','C: Itchiness','C: Corpus','C: Lake Michigan','C: Hite and Brown','C: Blue','C: Roy Rogers','C: Vesakha','C: Pancreas','C: Nebula','C: Yellow','C: Austin','C: Eveready','C: Turquoise','C: Smelly Cat','C: Sherman burns Atlanta','C: Capitol Building','C: 24','C: Swan','C: Angstroms','C: Nitrogen','C: Yoplait','C: U.S. Steel','C: Chlroform','C: St. Luke']

#This list stores all the 'D:' multiple choice answers for the question3 list
multi3D = ['D: Luxembourg','D: Bhutan','D: 10.0 miles','D: Florida','D: Polonium','D: In a wardrobe','D: Goose bumps','D: Pharynx','D: Lake Superior','D: Masters and Johnson',"D: White","D: Popeye's",'D: Purim','D: Heart','D: Pulsar','D: Purple','D: San Antonio','D: Duracell','D: Lapis Lazuli','D: Ugly Cat','D: Siege at Harpers Ferry','D: Library of Congress','D: 32','D: Bear','D: Milibars','D: Oxygen','D: TCBY','D: General Electric','D: Abscisic Acid','D: St. Joseph']

#This list stores the correct answers from the question3 list
correctAnswer3 = ['a','c','a','d','b','d','a','a','c','d','d','a','b','a','b','c','c','d','b','c','d','c','c','a','d','b','c','c','b','a']


# This list stores all the questions that are used for questions 11-14 ($64,00-$500,000 questions)
question4 =  ['Which of the following men does not have a chemical element named for him?',
'What is the state capital of Pennsylvania?',
'Which African statesman received the Freedom of the City of Cardiff in a ceremony in 1998?',
"What illness has been linked to the use of aspirin in treating a child's fever?",
'The 1972 "Bloody Sunday" incident refers to the killing of unarmed demonstrators in what country?',
'Which of the following types of beer is typically the darkest in color?',
"The National Hockey League's trophy for league's leading goal scorer is named for what player?",
'What material makes up the bulk of the human umbilical cord?',
'What is a biretta?',
"The site of the Statue of Liberty was formerly named what?",
"What southern U.S. city contains a full-scale replica of Greece's Parthenon?",
'Freedom Summer was a 1964 effort to increase African-American voter registration in which state?',
'Which of the following mythological deities was born inside the brain of Zeus?',
'What parts of Antarctica are named Filchner, Larsen and Shackleton?',
'In 1945, the United Nations Charter was drawn up and signed in what city?',
'Where did baseballs infamous 1979 "Disco Demolition Night" riots occur?',
'When a players strike ended the 1994 baseball season, what major league team had the best record?',
'Which of the following states borders the most other states?',
'The Western Wall in Jerusalem was originally part of what structure?',
'In "Back to the Future," what was printed on the time machine`s license plate?',
'What unit of currency is used in Panama?',
'What nationality was the inventor of the Centigrade temperature scale?',
"When it's 5:00 PM EST in China's easternmost part, what time is it in its westernmost part?",
'How many Super Bowl games have gone into overtime?',
'The highest mountain in South America is located in what country?',
'In Norse mythology, Mjölnir was the name of what?',
'What oil painting technique created by Leonardo da Vinci is used in the "Mona Lisa"?',
'Reacting with virtually every other element, what is the most reactive chemical element?',
"What is the only U.S. state which doesn't have two separate houses in its state legislature?",
'In what European nation is Romansh a recognized national language?']

#This list stores all the 'A:' multiple choice answers for the question4 list
multi4A = ['A: Albert Einstein','A: Pittsburgh','A: Pele','A: Hepatitis','A: Greece','A: Pilsner','A: Wayne Gretzky','A: Fat cells','A: Firearm','A: Ellis Island','A: Nashville, Tennessee','A: Mississippi','A: Apollo','A: Islands','A: San Francisco','A: Comiskey Park','A: Chicago White Sox','A: Nebraska','A: Dome of the Rock','A: GETBACK','A: Balboa','A: Swedish','A: 2:00 PM','A: 0','A: Argentina',"A: Odin's horse",'A: Sprezzatura','A: Oxygen','A: Idaho','A: Austria']

#This list stores all the 'B:' multiple choice answers for the question4 list
multi4B = ['B: Niels Bohr','B: Harrisburg','B: Nelson Mandela','B: Pneumonia','B: Istael','B: Stout','B: Maurice Richard','B: Lymph','B: Tropical bird','B: Roosevelt Island','B: Savahah, Georgia','B: Alabama','B: Hermes','B: Mountains','B: Washington D.C.','C: Tiger stadium','B: Montreal Expos','B: Pensylvania','B: Walled city of Jericho','B: TIMESUP','B: Cortes','B: French','B: 3:00 PM','B: 1','B: Brazil',"B: Sigmund's sword",'B: Sfumato','B: Phosphorus','B: Hawaii','B: Switzerland']

#This list stores all the 'C:' multiple choice answers for the question4 list
multi4C = ['C: Isaac Newton','C: Gettysburg','C: Thurgood Marshall','C: Diabetes','C: Northern Ireland','C: Bitter','C: Gordie Howe','C: Collagen','C: Clerical cap',"C: Bedloe's Island",'C: Athens, Georgia','C: South Carolina','C: Aphrodite','C: Ice shelves','C: New York City','C: Country Stadium','C: Atlanta Braves','C: Idaho','C: Masada','C: OUTATIME','C: Pizarro','C: Scottish','C: 4:00 PM','C: 2','C: Peru',"C: Loki's magic necklace",'C: Sfregazzi','C: Fluorine','C: Alaska','C: Albania']

#This list stores all the 'D:' multiple choice answers for the question4 list
multi4D = ['D: Enrico Fermi','D: Philadelphia','D: Reggie Jackson',"D: Reye's syndrome",'D: Angola','D: Ale','D: Mario Lemieux','D: Mucous tissue',"D: Lumberjack's Tool","D: Governor's Island",'D: Jacksonville, Florida','D: Georgia','D: Athena','D: Scientific stations','D: Los Angeles','D: Dodger Stadium','D: Toronto Blue Jays','D: Tennesse','D: The Second Temple','D: BACKINTIME','D: Cabral','D: German','D: 5:00 PM','D: 3','D: Ecuador',"D: Thor's hammer",'D: Serliano','D: Sodium','D: Nebraska','D: Bulgaria']

#This list stores the correct answers from the question4 list
correctAnswer4 = ['c','b','b','d','c','b','b','d','c','c','a','a','d','c','a','a','b','d','d','c','a','a','d','a','a','d','b','c','d','b']


# This list stores all the questions that are used for question 15 ($1,000,000 question)
question5 = ["In the children's book series, where is Paddington Bear originally from?", # question5 will be used for question 15 ($1 million) only
'What letter must appear at the beginning of the reguatration number of all non-militaty aircraft in the U.S.?',
"Who delivered the less famous two-hour speech that preceded Abraham Lincoln's two-minute Gettysburg Address?",
'"Nephelococcygia" is the practice of doing what?',
'Which insect shorted out an early supercomputer and inspired the term "computer bug"?',
'Which one of these ships was not one of the three taken over by colonists during the Boston Tea Party?',
'Now used to refer to a cat, the word "tabby" is derived from the name of a distinct of what world capital?',
'According to the Population Reference Bureau, what is the approximate number of people who have ever lived on earth?',
'Khrushevs Famous 1960 "shoe-banging" outburst at the U.N. was in response to a delegate from what nation?',
'For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office "coffee,""tea,""Coke" and what?']

#This list stores all the 'A:' multiple choice answers for the question5 list
multi5A = ['A: India','A: N','A: Wendell Phillips','A: Finding shapes in clouds','A: Moth','A: Eleanor','A: Cairo','A: 75 Billion','A: Australia','A: Fresca']

#This list stores all the 'B:' multiple choice answers for the question5 list
multi5B = ['B: Peru','B: A','B: Daniel Webster','B: Sleeping with your eyes open','B: Roach','B: Darmouth','B: Baghdad','B: 100 Billion','B: The Netherlands','B: V8']

#This list stores all the 'C:' multiple choice answers for the question5 list
multi5C = ['C: Canada','C: U','C: Robert G. Ingersoll','C: Breaking glass with your voice','C: Fly','C: Beaver','C: New Delhi','C: 150 Billion','C: The Philippines','C: Yoo-hoo']

#This list stores all the 'D:' multiple choice answers for the question5 list
multi5D = ['D: Iceland','D: L','D: Edward Everett','D: Swimming in freezing water','D: Beetle','D: William','D: Moscow','D: 300 Billion','D: Turkey','D: A&W']

#This list stores the correct answers from the question5 list
correctAnswer5 = ['b','a','d','a','a','d','b','b','c','a']

#This list stores the values that you can win throughout the game.          
valueWon = ['$0','$100','$200','$300','$500','$1,000','$2,000','$4,000','$8,000','$16,000','$32,000','$64,000','$125,000','$250,000','$500,000','$1,000,000']

score = 0


#the first question is the $100 question.
def firstquestion ():
    global score
    while (score < 1): #while the score is below 1, this loop will keep going.
        print("Here's your " + valueWon[score + 1] + " question:") #prints what this question is worth, which is based on the 'valueWon' list and your current score + 1.
        x = random.randint(0,14) #randomly picks a question from the question1 list.
        player = input(question1[x] + '\n' + multi1A[x] + '\n' + multi1B[x] + '\n' + multi1C[x] + '\n' + multi1D[x] + '\n') #prints the question and 4 possible answers from lists multi1A, multi1B, multi1C, and multi1D based on the random value of x. The player value is based on the player's input.
        player = player.lower() #the player value will be put lower case so even if the player types an uppercase responce, it will turnout lowercase to compare it to the correstAnswer1


        if player == correctAnswer1[x]: #compares the player's response to the answer to the question that's stored in correctAnswer1
            score = score + 1 #if the player got it right, it will add 1 to the score
            print ("Correct! You won " + valueWon[score]) #It will also print the next value on the valueWon list since the score just increased by 1
            print ('')
            if score == 1: #If the score is 1 (first question is answered)
                secondquestion () #Then it will go to the 'secondquestion' function.
            else: # if it doesn't
                continue # then it continues.
        elif player == 'leave': #if the player types in 'leave', it will end the game.
            print ("Congratulations! You'll take home " + valueWon[score] +'!') #it will also print that the player will take home the money he won from the previous question he answered.
            break

        elif player != correctAnswer1[x]: #If the response the player gave does not match up with the correct answer to the question.
            print ("I'm sorry, that was incorrect. You go home with " + valueWon[0]) #Then it will say he got it wrong and drop it all the way down to his last milestone (in this case, its $0).
            break


#The secondquestion is the $200-$1,000 questions.
def secondquestion ():
    global score
    while (score >= 1 and score < 5): #while the score is greater than or equal to 1 and also less than 5, this loop will keep going.
        print("Here's your " + valueWon[score + 1] + " question:") #prints what this question is worth, which is based on the 'valueWon' list and your current score + 1.
        x = random.randint(0,29) #randomly picks a question from the question2 list.
        player = input(question2[x] + '\n' + multi2A[x] + '\n' + multi2B[x] + '\n' + multi2C[x] + '\n' + multi2D[x] + '\n')  #prints the question and 4 possible answers from lists multi2A, multi2B, multi2C, and multi2D based on the random value of x. The player value is based on the player's input.
        player = player.lower() #the player value will be put lower case so even if the player types an uppercase responce, it will turnout lowercase to compare it to the correstAnswer2


        if player == correctAnswer2[x]: #compares the player's response to the answer to the question that's stored in correctAnswer2
            score = score + 1 #if the player got it right, it will add 1 to the score
            print ("Correct! You won " + valueWon[score]) #It will also print the next value on the valueWon list since the score just increased by 1
            print ('')
            if score == 5: #If the score is 5 (fifth question is answered)
                secondquestion () #Then it will go to the 'areyoureadyone' function.
            else: # if it doesn't
                continue # then it continues.

        elif player == 'leave': #if the player types in 'leave', it will end the game.
            print ("Congratulations! You'll take home " + valueWon[score] +'!') #it will also print that the player will take home the money he won from the previous question he answered.
            break
        elif player != correctAnswer2[x]: #If the response the player gave does not match up with the correct answer to the question.
            print ("I'm sorry, that was incorrect. You go home with " + valueWon[0]) #Then it will say he got it wrong and drop it all the way down to his last milestone (in this case, its $0).
            break

#this part basically shows the player's progress and ask them if they are ready to continue
def areyoureadyone ():
    print ('')
    print ('Prize Ladder') #printing out the remaining prize ladder for the player's reference.
    print ('15- $1,000,000')
    print ('14- $500,000')
    print ('13- $250,000')
    print ('12- $100,000')
    print ('11- $64,000')
    print ('10- $32,000*')
    print ('9- $16,000')
    print ('8- $8,000')
    print ('7- $4,000')
    print ('6- $2,000')
    print ('')
    print ('')
    print ('You have reached a milestone! you cannot walk out with less than $1,000!') #Encouraging the player.
    print ('Remember, if you want to keep your winnings instead of risking it, type "leave" at any question.')
    print ('The questions are going to get a little harder, are you ready? (yes or no)?')
    ready = input() #gives a chance for the player to interact with the game and type whatever they want.
    ready = ready.lower()
    if ready == 'yes': #If the player types in yes to the question, then this specific encouragement is printed.
        print ('')
        print ('Great, then lets continue playing Millionaire!')
        print ('')

    else: # if anything exept yes is typed, then we just print that they have to keep going.
        print ('')
        print ('Well we gotta keep going, so lets continue playing Millionaire!')
        print ('')

    print ('')
    thirdquestion () # when the player is ready, it will direct to the 'thirdquestion' function

#The thirdquestion are the $2,000-$32,000 questions.
def thirdquestion ():
    global score
    while (score >= 5 and score < 10): #while the score is greater than or equal to 5 and also less than 10, this loop will keep going.
        print("Here's your " + valueWon[score + 1] + " question:") #prints what this question is worth, which is based on the 'valueWon' list and your current score + 1.
        x = random.randint(0,29) #randomly picks a question from the question3 list.
        player = input(question3[x] + '\n' + multi3A[x] + '\n' + multi3B[x] + '\n' + multi3C[x] + '\n' + multi3D[x] + '\n') #prints the question and 4 possible answers from lists multi3A, multi3B, multi3C, and multi3D based on the random value of x. The player value is based on the player's input.
        player = player.lower() #the player value will be put lower case so even if the player types an uppercase responce, it will turnout lowercase to compare it to the correstAnswer3



        if player == correctAnswer3[x]: #compares the player's response to the answer to the question that's stored in correctAnswer3
            score = score + 1 #if the player got it right, it will add 1 to the score
            print ("Correct! You won " + valueWon[score]) #It will also print the next value on the valueWon list since the score just increased by 1
            print ('')
            if score == 10: #If the score is 10 (tenth question is answered)
                secondquestion () #Then it will go to the 'areyoureadytwo' function.
            else: # if it doesn't
                continue # then it continues.


        elif player == 'leave': #if the player types in 'leave', it will end the game.
            print ("Congratulations! You'll take home " + valueWon[score] +'!') #it will also print that the player will take home the money he won from the previous question he answered.
            break
        
        elif player != correctAnswer3[x]: #If the response the player gave does not match up with the correct answer to the question.
            print ("I'm sorry, that was incorrect. You go home with " + valueWon[5]) #Then it will say he got it wrong and drop it all the way down to his last milestone (in this case, its $1,000).
            break


def areyoureadytwo ():
#another part where it shows the player's progress and ask them if they are ready to continue
    print ('')
    print ('Prize Ladder') #printing out the remaining prize ladder for the player's reference.
    print ('15- $1,000,000')
    print ('14- $500,000')
    print ('13- $250,000')
    print ('12- $100,000')
    print ('11- $64,000')
    print ('')
    print ('')
    print ('You have reached another milestone! you cannot walk out with less than $32,000!') #Encouraging the player.
    print ('Remember, if you want to keep your winnings instead of risking it, type "leave" at any question.')
    print ('Questions are going to get very dificult, are you sure your ready?')
    print ('')
    print ('')
    ready = input() #gives a chance for the player to interact with the game and type whatever they want.
    ready = ready.lower()
    if ready == 'yes': #If the player types in yes to the question, then this specific encouragement is printed.
        print ('')
        print ('Great, then lets continue playing Millionaire!') 
        print ('')

    else: # if anything exept yes is typed, then we just print that they have to keep going.
        print ('')
        print ('Well we gotta keep going, so lets continue playing Millionaire!')
        print ('')

    print ('')
    fourthquestion () # when the player is ready, it will direct to the 'fourthquestion' function


#The fourthquestion are the $64,000-$500,000 questions.
def fourthquestion ():
    global score
    while (score >= 10 and score < 14): #while the score is greater than or equal to 10 and also less than 14, this loop will keep going.
        print("Here's your " + valueWon[score + 1] + " question:") #prints what this question is worth, which is based on the 'valueWon' list and your current score + 1.
        x = random.randint(0,29) #randomly picks a question from the question4 list.
        player = input(question4[x] + '\n' + multi4A[x] + '\n' + multi4B[x] + '\n' + multi4C[x] + '\n' + multi4D[x] + '\n') #prints the question and 4 possible answers from lists multi4A, multi4B, multi4C, and multi4D based on the random value of x. The player value is based on the player's input.
        player = player.lower() #the player value will be put lower case so even if the player types an uppercase responce, it will turnout lowercase to compare it to the correstAnswer4


        if player == correctAnswer4[x]: #compares the player's response to the answer to the question that's stored in correctAnswer4
            score = score + 1 #if the player got it right, it will add 1 to the score
            print ("Correct! You won " + valueWon[score]) #It will also print the next value on the valueWon list since the score just increased by 1
            print ('')
            if score == 14: #If the score is 14 (Fourteenth question is answered)
                secondquestion () #Then it will go to the 'areyoureadythree' function.
            else: # if it doesn't
                continue # then it continues.          

        elif player == 'leave': #if the player types in 'leave', it will end the game.
            print ("Congratulations! You'll take home " + valueWon[score] +'!') #it will also print that the player will take home the money he won from the previous question he answered.
            break

        elif player != correctAnswer4[x]: #If the response the player gave does not match up with the correct answer to the question.
            print ("I'm sorry, that was incorrect. You go home with " + valueWon[10]) #Then it will say he got it wrong and drop it all the way down to his last milestone (in this case, its $1,000).
            break


def areyoureadythree ():
#the last part where it shows the player's progress and ask them if they are ready to continue
    print ('')
    print ('Prize Ladder') #printing out the remaining prize ladder for the player's reference.
    print ('15- $1,000,000')
    print ('')
    print ('')
    print ('You have Won $500,000!!! Your just 1 question away from $1,000,000!!!') #Encouraging the player.
    print ("We've never had anyone reach this high in the money ladder. This is a historic moment!")
    print ('Remember, if you want to keep your winnings instead of risking it, type "leave" at any question.')
    print ('Are you ready to see your $1 Million question? (yes or no)')
    print ('')
    print ('')
    ready = input() #gives a chance for the player to interact with the game and type whatever they want.
    ready = ready.lower()
    if ready == 'yes': #If the player types in yes to the question, then this specific encouragement is printed.
        print ('')
        print ('Great, I wish you the best of luck on your $1 Million question!')
        print ('')

    else: # if anything exept yes is typed, then we just print that they have to keep going.
        print ('')
        print ('Well I hope your ready, so lets play your $1 Million question!')
        print ('')

    print ('')
    fifthquestion () # when the player is ready, it will direct to the 'fifthquestion' function
    
#The fifthquestion is the $1,000,000 questions.
def fifthquestion ():
    global score
    while (score == 14): #while the score is equal to 14, this loop will keep going.
        print("Here's your " + valueWon[score + 1] + " question:") #prints what this question is worth, which is based on the 'valueWon' list and your current score + 1.
        x = random.randint(0,9) #randomly picks a question from the question5 list.
        player = input(question5[x] + '\n' + multi5A[x] + '\n' + multi5B[x] + '\n' + multi5C[x] + '\n' + multi5D[x] + '\n') #prints the question and 4 possible answers from lists multi5A, multi5B, multi5C, and multi5D based on the random value of x. The player value is based on the player's input.
        player = player.lower() #the player value will be put lower case so even if the player types an uppercase responce, it will turnout lowercase to compare it to the correstAnswer5

        if player == correctAnswer5[x]: #compares the player's response to the answer to the question that's stored in correctAnswer5
            print ("Correct! You won $1,000,000!") # if the player got it correct, then it will say he won the million!
            print('')
            print ("Congratulations! You're a Millionaire!!!")
            print ('how happy are you right now?') #host asks if the contestant is happy
            happiness = input () #player can enter anything
            print ('')
            print ("Well I'm happy to hear it! Did you expect that you were going to win the million today?") # Host asks what the player will do with the money
            happiness2 = input () # player can enter anything
            print ('')
            print("Well ejoy your Million dollars! Tune in next week to see if another contestant can take home the Million!")
            break

        elif player == 'leave': #if the player types in 'leave', it will end the game.
            print ("Congratulations! You'll take home " + valueWon[score] +'!') #it will also print that the player will take home the money he won from the previous question he answered.
            print ('')
            print ("Well it's not a Million, but its still a lot of money, wwhy did  you decide to back out") #Since the player didn't want to answer the million dollar question, we gotta ask him why
            doit = input ()
            print ('')
            print ('Well I wish you luck on your future endeavors!') # printing host giveing final remarks
            print ("We were so close to having a Millionaire. Tune in next week to see if a contestant can take home the Million!")
            break

        elif player != correctAnswer5[x]: #If the response the player gave does not match up with the correct answer to the question.
            print ("I'm sorry, that was incorrect. You'll drop all the way down and go home with " + valueWon[10]) #Then it will say he got it wrong and drop it all the way down to his last milestone (in this case, its $1,000).

            break
#The playgame function is opened from the game_runner file
def playgame ():

    print ('Welcome to "Who Wants to Be A Millionaire!" The game show where you answer a series of questions and climb your way to the million!') #prints out rules for the player to read
    print ('')
    print ('Rules: If you get 15 questions right in a row, you will win $1,000,000!')
    print ('No using the internet to look up answers please')
    print ('Rules: If you want to take your money and not risk losing it, you may do so by typing "leave".')
    print ('Rules: If you get a question wrong, you will drop down ant take home your last milestone ($0, $1,000, $32,000).')

    print ('')

    print ('Prize Ladder:') #prints out the money ladder for the player
    print ('15- $1,000,000')
    print ('14- $500,000')
    print ('13- $250,000')
    print ('12- $100,000')
    print ('11- $64,000')
    print ('10- $32,000*')
    print ('9- $16,000')
    print ('8- $8,000')
    print ('7- $4,000')
    print ('6- $2,000')
    print ('5- $1,000*')
    print ('4- $500')
    print ('3- $300')
    print ('2- $200')
    print ('1- $100')
    print ('')
    print ('Are you ready to play?') #Asks if the player is ready
    ready1 = input () # If the player types anything, the game will start and he will receive their first question.
    print ('')
    print ('Then lets play Millionaire!')
    print ('')
    firstquestion () # when the player is ready, it will direct to the 'firstquestion' function
