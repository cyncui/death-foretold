import random
import sys
import os

# CHOOSE CHARACTER > FACED WITH CHOICE > MAKE A CHOICE > OUTCOME OF THAT CHOICE (SIG EVENT)
character_list = ["SANTIAGO NASAR", "BAYARDO SAN ROMAN", "ANGELA", "TWINS", "CRISTO", "NARRATOR"]
santiago_choice_one_list = ["crack open a cold one with the boys", "be a party pooper and go home"]
santiago_choice_two_list = ["go serenade the couple", "suggest a game of truth or dare"]
santiago_choice_three_list = ["go home and get some sleep", "go have breakfast"]
santiago_choice_four_list = ["go to your fiancee Flora Miguel's house", "hop on a boat and see if you can catch up with the bishop"]
santiago_choice_five_list = ["go out and face the twins", "hide in your fiancee's family's house"]
bayardo_choice_one_list = ["take a risk and go to this Colombian town", "stay in your hometown"]
bayardo_choice_two_list = ["yes", "no"]
bayardo_choice_three_list = ["produce your entire family", "suggest a game of twenty questions"]
bayardo_choice_four_list = ["have the wedding at the vicario household", "find a place on airbnb.com"]
bayardo_choice_five_list = ["return her to her family", "pretend you didn't notice"]
angela_choice_one_list = ["let him pursue you", "friendzone him"]
angela_choice_two_list = ["suck it up and marry him", "pursue true love elsewhere"]
angela_choice_three_list = ["not care about hiding it", "try and fake your virginity"]
angela_choice_four_list = ["let him do so", "plead with him to keep it lowkey"]
angela_choice_five_list = ["give them Santiago's name", "keep your mouth shut"]
twins_choice_one_list = ["join Santiago for a drink at Maria Cervantes' brothel", "continue with the wedding festivities"]
twins_choice_two_list = ["go home to your mother because you are the most obedient sons in all of the land", "keep the party going"]
twins_choice_three_list = ["sharpen your knives and announce your plan to kill the man", "just let it go... it's been a long day"]
twins_choice_four_list = ["continue with the murder", "talk it out"]
cristo_choice_one_list = ["go out", "stay at the wedding"]
cristo_choice_two_list = ["double back and find Santiago", "laugh it off"]
cristo_choice_three_list = ["be safe... guns aren't toys", "pull the trigger, it can't be that bad"]
narrator_choice_one_list = ["start", "forget it"]

class person:
    def __init__(self, character, santiago_first_choice, santiago_second_choice, santiago_third_choice, santiago_fourth_choice, santiago_fifth_choice, bayardo_first_choice, bayardo_second_choice, bayardo_third_choice, bayardo_fourth_choice, bayardo_fifth_choice, angela_first_choice, angela_second_choice, angela_third_choice, angela_fourth_choice, angela_fifth_choice, twins_first_choice, twins_second_choice, twins_third_choice, twins_fourth_choice, cristo_first_choice, cristo_second_choice, cristo_third_choice, narrator_first_choice):
        self.character = character
        self.santiago_first_choice = santiago_first_choice
        self.santiago_second_choice = santiago_second_choice
        self.santiago_third_choice = santiago_third_choice
        self.santiago_fourth_choice = santiago_fourth_choice
        self.santiago_fifth_choice = santiago_fifth_choice
        self.bayardo_first_choice = bayardo_first_choice
        self.bayardo_second_choice = bayardo_second_choice
        self.bayardo_third_choice = bayardo_third_choice
        self.bayardo_fourth_choice = bayardo_fourth_choice
        self.bayardo_fifth_choice = bayardo_fifth_choice
        self.angela_first_choice = angela_first_choice
        self.angela_second_choice = angela_second_choice
        self.angela_third_choice = angela_third_choice
        self.angela_fourth_choice = angela_fourth_choice
        self.angela_fifth_choice = angela_fifth_choice
        self.twins_first_choice = twins_first_choice
        self.twins_second_choice = twins_second_choice
        self.twins_third_choice = twins_third_choice
        self.twins_fourth_choice = twins_fourth_choice
        self.cristo_first_choice = cristo_first_choice
        self.cristo_second_choice = cristo_second_choice
        self.cristo_third_choice = cristo_third_choice
        self.narrator_first_choice = narrator_first_choice

    def choose_character(self):
        i = 1
        print("CHARACTERS:")
        for item in self.character:
            print("    " + str(i) + ".", item)
            i += 1

    def santiago_one(self):
        i = 1
        for item in self.santiago_first_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def santiago_two(self):
        i = 1
        for item in self.santiago_second_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def santiago_three(self):
        i = 1
        for item in self.santiago_third_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def santiago_four(self):
        i = 1
        for item in self.santiago_fourth_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def santiago_five(self):
        i = 1
        for item in self.santiago_fifth_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def bayardo_one(self):
        i = 1
        for item in self.bayardo_first_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def bayardo_two(self):
        i = 1
        for item in self.bayardo_second_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def bayardo_three(self):
        i = 1
        for item in self.bayardo_third_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def bayardo_four(self):
        i = 1
        for item in self.bayardo_fourth_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def bayardo_five(self):
        i = 1
        for item in self.bayardo_fifth_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def angela_one(self):
        i = 1
        for item in self.angela_first_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def angela_two(self):
        i = 1
        for item in self.angela_second_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def angela_three(self):
        i = 1
        for item in self.angela_third_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def angela_four(self):
        i = 1
        for item in self.angela_fourth_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def angela_five(self):
        i = 1
        for item in self.angela_fifth_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def twins_one(self):
        i = 1
        for item in self.twins_first_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def twins_two(self):
        i = 1
        for item in self.twins_second_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def twins_three(self):
        i = 1
        for item in self.twins_third_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def twins_four(self):
        i = 1
        for item in self.twins_fourth_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def cristo_one(self):
        i = 1
        for item in self.cristo_first_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def cristo_two(self):
        i = 1
        for item in self.cristo_second_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def cristo_three(self):
        i = 1
        for item in self.cristo_third_choice:
            print("    " + str(i) + ".", item)
            i += 1

    def narrator_one(self):
        i = 1
        for item in self.narrator_first_choice:
            print("    " + str(i) + ".", item)
            i += 1

# MAIN CODE
player = person(character_list, santiago_choice_one_list, santiago_choice_two_list, santiago_choice_three_list, santiago_choice_four_list, santiago_choice_five_list, bayardo_choice_one_list, bayardo_choice_two_list, bayardo_choice_three_list, bayardo_choice_four_list, bayardo_choice_five_list, angela_choice_one_list, angela_choice_two_list, angela_choice_three_list, angela_choice_four_list, angela_choice_five_list, twins_choice_one_list, twins_choice_two_list, twins_choice_three_list, twins_choice_four_list, cristo_choice_one_list, cristo_choice_two_list, cristo_choice_three_list, narrator_choice_one_list)
running = True

print("\n" + "WELCOME TO CHRONICLE OF A DEATH FORETOLD: THE RPG." + "\n" + "IN THIS GAME, YOU MAY CHOOSE YOUR CHARACTER AND FOLLOW HIM/HER THROUGH HIS/HER MOST SIGNIFICANT EVENTS ON THE DAY OF SANTIAGO NASAR'S MURDER." + "\n" + "BEFORE EACH SIGNIFICANT EVENT, YOU WILL BE GIVEN A CHOICE BETWEEN TWO DIFFERENT ACTIONS." + "\n" + "THIS IS AN ILLUSION. THERE IS NO FREEDOM OF CHOICE." + "\n" + "THE RIGHT ANSWERS ARE FOUND IN THE NOVELLA AS THE ACTUAL ACTIONS THAT YOUR CHARACTER TOOK ON THAT FATEFUL DAY." + "\n" + "GOOD LUCK AND MAY THE ODDS BE WITH YOU." + "\n" + "WE WOULD LIKE TO ACKNOWLEDGE THAT CODING THIS GAME WOULD NOT HAVE BEEN POSSIBLE WITHOUT EXTERNAL ASSISTANCE," + "\n" + "AND WE ARE IN NO WAY CLAIMING EVERY SINGLE LINE OF CODE AS OUR OWN, ORIGINAL WORK.")

while running:
    print("==============================")
    player.choose_character()
    choice = int(input("WHO WOULD YOU LIKE TO BE? "))

    if choice == 1: # SANTIAGO PATHWAY
        print("\n" + "HELLO, SANTIAGO. NICE TO MEET YOU. YOU ARE THE RICH AND HANDSOME SON OF PLACIDA LINERO." + "\n" + "YOU ARE CURRENTLY ATTENDING ANGELA VICARIO’S WEDDING BUT THE PARTY IS GETTING A LITTLE DEAD." + "\n" + "YOUR FRIENDS INVITE YOU TO GO TO MARIA CERVANTES’ FOR SOME DRINKING AND DANCING." + "\n" + "YOU ARE MET WITH TWO CHOICES:")
        print("==============================")
        player.santiago_one()
        santiago_choice_one = int(input("WHAT ARE YOU GOING TO DO? ")) # SIGNIIFICANT EVENT NO. 1

        if santiago_choice_one == 1:
            print("\n" + "GOOD CHOICE; YOU’RE ROCKING THOSE SICK DANCE MOVES." + "\n" + "BUT YOU’RE GETTING BORED AND YOU GET THE IDEA TO SING TO THE NEWLYWEDS AT XIUS’ HOUSE." + "\n" + "YOU ARE MET WITH TWO MORE CHOICES:")
            print("==============================")
            player.santiago_two()
            santiago_choice_two = int(input("CHOOSE WISELY... ")) # SIG EVENT NO 2

            if santiago_choice_two == 1:
                print("\n" + "IT’S YOUR CHOICE… YOU GO TO XIUS’ HOUSE." + "\n" + "YOU GUYS SET OFF FIREWORKS AND ROCKETS AND SING TO THE NEWLYWEDS." + "\n" + "YOU ARE FEELING QUITE TIRED BUT LUIS INVITES YOU TO GET BREAKFAST OF FRIED FISH AT THE LUNCH STAND." + "\n" + "YOU ARE MET WITH TWO CHOICES,")
                print("==============================")
                player.santiago_three()
                santiago_choice_three = int(input("CHOOSE WISELY... "))

                if santiago_choice_three == 1:
                    print("\n" + "NICE ONE. YOU WALK WITH CRISTO ALONG THE RIVERBANK TO GET HOME AND SLEEP FOR AN HOUR AND VICTORIA GUZMAN WAKES YOU UP AT 5:30." + "\n" + "YOU GO TO THE DOCKS TO SEE THE BISHOP BUT HE DOESN’T STOP AND GOES PAST THE DOCKS." + "\n" + "A LITTLE DISAPPOINTING. WHERE WILL YOU GO NEXT?" + "\n" + "YOU ARE MET WITH TWO CHOICES:")
                    print("==============================")
                    player.santiago_four()
                    santiago_choice_four = int(input("CHOOSE WISELY... "))

                    if santiago_choice_four == 1:
                        print("\n" + "OKAY THEN. YOU GO TO FLORA MIGUEL’S HOUSE AND YOU GET YELLED AT BY YOUR FIANCEE." + "\n" + "NAHIR MIGUEL, FLORA’S FATHER, ALSO BREAKS IT TO YOU THAT THE VICARIO TWINS ARE LOOKING FOR YOU TO KILL YOU." + "\n" + "TODAY IS NOT YOUR DAY! YOU ARE MET WITH TWO CHOICES:")
                        print("==============================")
                        player.santiago_five()
                        santiago_choice_five = int(input("CHOOSE WISELY... "))

                        if santiago_choice_five == 1:
                            print("\n" + "DARN, YOU’VE BEEN SPOTTED BY THE VICARIO TWINS." + "\n" + "COUNTLESS VOICES ARE CALLING DOWN TO YOU, GIVING YOU INSTRUCTIONS, BUT YOU’RE TOO CONFUSED TO REGISTER ANY OF THE INFORMATION." + "\n" + "YOU RUN TO GET INSIDE YOUR HOUSE, BUT THE DOOR IS LOCKED." + "\n" + "YOU ARE STABBED COUNTLESS TIMES BY THE VICARIO TWINS." + "\n" + "YOU HOLD YOUR HANGING INTESTINES AND WALK TO THE KITCHEN WHERE YOU COLLAPSE." + "\n" + "WELL, THIS IS GAME OVER FOR YOU. CONDOLENCES FOR YOUR BRUTAL DEATH. TOUGH LUCK BUDDY;" + "\n" + "BETTER LUCK NEXT TIME?")
        print("\n" + "\n" + "\n" + "\n")
        print("START GAME (AGAIN):")
        continue # PUT THIS AT THE END OF YOUR CHARACTER PATHWAY IF FUNCTIONS AND IT WILL PROMPT YOU TO PICK ANOTHER CHARACTER

    elif choice == 2: # BAYARDO PATHWAY
        print("\n" + "HELLO, BAYARDO. NICE TO MEET YOU." + "\n" + "YOU HAVE BEEN GOING FROM TOWN TO TOWN LOOKING FOR SOMEONE TO MARRY, BUT YOU HAVE HAD NO LUCK." + "\n" + "AS A LAST RESORT, YOU SPIN A GLOBE AND YOUR FINGER LANDS ON A SMALL COLOMBIAN TOWN." + "\n" + "YOU ARE MET WITH TWO CHOICES,")
        print("==============================")
        player.bayardo_one()
        bayardo_choice_one = int(input("SO? WHAT'S IT GOING TO BE? "))

        if bayardo_choice_one == 1:
            print("\n" + "OKAY, YOUR CHOICE…" + "\n" + "A MONTH LATER, YOU SEE A BEAUTIFUL WOMAN WHO YOU WILL LATER KNOW AS ANGELA VICARIO." + "\n" + "IS SHE 'THE ONE?'")
            print("==============================")
            player.bayardo_two()
            bayardo_choice_two = int(input("YES OR NO? "))

            if bayardo_choice_two == 1:
                print("\n" + "WOW, THAT WAS QUICK." + "\n" + "SINCE THEN, YOU HAVE BEEN TRYING TO WIN HER OVER." + "\n" + "YOU EVEN BOUGHT ALL THE RAFFLE TICKETS AT A CHARITY BAZAAR JUST TO GIVE HER A MUSIC BOX INSTEAD OF JUST FINDING A WINGMAN." + "\n" + "LUCKILY FOR YOU, IT SEEMED TO HAVE WORKED. BUT NOW, HER FAMILY WANTS TO KNOW MORE ABOUT YOU BEFORE ANGELA AND YOU GET MARRIED." + "\n" + "WHAT SHOULD YOU DO?")
                print("==============================")
                player.bayardo_three()
                bayardo_choice_three = int(input("WELL....? "))

                if bayardo_choice_three == 1:
                    print("\n" + "WOW, YOU’RE DOING EERILY WELL." + "\n" + "THE TOWN LOVES YOUR FAMILY, FOR THE MOST PART." + "\n" + "YOU’RE ALL SET TO BE MARRIED; HOWEVER, THE LOCATION HAS YET TO BE DECIDED." + "\n" + "YOU HAVE AN OPTION IN EITHER HAND, WHAT'S IT GONNA BE?")
                    print("==============================")
                    player.bayardo_four()
                    bayardo_choice_four = int(input("AIR BNB DOESN'T SOUND TOO PROMISING... "))

                    if bayardo_choice_four == 1:
                        print("\n" + "COOL! THE WEDDING IS A HUGE SUCCESS." + "\n" + "NEARLY EVERYONE FROM THE TOWN IS HERE, AND THE FESTIVITIES SEEM TO NEVER END." + "\n" + "BUT IN THE BLINK OF AN EYE, IT’S YOUR WEDDING NIGHT." + "\n" + "YOU BRING ANGELA TO XIUS’ HOUSE, WHICH YOU HAD MANAGED TO BUY OFF OF HIM BEFORE THE WEDDING." + "\n" + "ALL IS WELL UNTIL YOU FIND OUT THAT YOUR BELOVED BRIDE IS NOT A VIRGIN." + "\n" + "OH, NO! SHOULD YOU:")
                        print("==============================")
                        player.bayardo_five()
                        bayardo_choice_five = int(input("QUICK! "))

                        if bayardo_choice_five == 1:
                            print("\n" + "OUCH, THAT HURTS." + "\n" + "WELL, THIS IS WHERE YOUR CHOICES HAVE TAKEN YOU." + "\n" + "YOU END UP OVERWEIGHT, BALDING, AND SOMEHOW, ON ANGELA’S DOORSTEP." + "\n" + "THAT’S RIGHT: THE VERY GIRL YOU RETURNED AFTER DISCOVERING THAT SHE HAD SUPPOSEDLY ENGAGED IN PREMARITAL SEX." + "\n" + "LIFE REALLY DOES COME FULL CIRCLE, HEY?")
        print("\n" + "\n" + "\n" + "\n")
        print("START GAME (AGAIN):")
        continue

    elif choice == 3: # ANGELA PATHWAY
        print("\n" + "HELLO, ANGELA. NICE TO MEET YOU." + "\n" + "THE NEWCOMER IN TOWN BAYARDO SAN ROMÁN HAS FALLEN IN LOVE WITH YOU RATHER QUICKLY." + "\n" + "WHAT ARE YOU GOING TO DO ABOUT THIS?")
        print("==============================")
        player.angela_one()
        angela_choice_one = int(input("WHAT'S IT GONNA BE? "))

        if angela_choice_one == 1:
            print("\n" + "LEARN HOW TO SAY NO! BAYARDO WILL NOW STOP AT NOTHING TO MARRY YOU." + "\n" + "HE TRIES TO WIN YOU OVER AT A CHARITY BAZAAR BY BUYING ALL THE RAFFLE TICKETS TO WIN A MUSIC BOX FOR YOU." + "\n" + "YOU DON’T RECIPROCATE HIS FEELINGS, BUT YOUR FAMILY LOVES HIM." + "\n" + "THEY WANT YOU TO MARRY HIM." + "\n" + "YOU ARE MET WITH TWO CHOICES:")
            print("==============================")
            player.angela_two()
            angela_choice_two = int(input("CHOOSE WISELY... "))

            if angela_choice_two == 1:
                print("\n" + "ALRIGHT. WELL, NOW YOU’RE STUCK IN A MARRIAGE THAT YOU DON’T REALLY ENJOY." + "\n" + "THE WEDDING AND OTHER FESTIVITIES ENSUE. THERE’S ONLY ONE SMALL PROBLEM: YOU’RE NOT A VIRGIN." + "\n" + "YOU CONSIDER TELLING YOUR MOTHER, BUT YOUR TWO CONFIDANTES CONVINCE YOU THAT IT’S NORMAL." + "\n" + "THEY EVEN TEACH YOU TRICKS TO FAKE YOUR VIRGINITY ON YOUR WEDDING NIGHT." + "\n" + "WHAT SHOULD YOU DO?")
                print("==============================")
                player.angela_three()
                angela_choice_three = int(input("CHOOSE WISELY... "))

                if angela_choice_three == 1:
                    print("\n" + "RISKY… COME WEDDING NIGHT, BAYARDO DISCOVERS YOUR SECRET." + "\n" + "OH NO… HE IS NOW DRAGGING YOU BACK TO YOUR MOTHER’S HOUSE TO RETURN YOU." + "\n" + "YOU ARE MET WITH TWO CHOICES:")
                    print("==============================")
                    player.angela_four()
                    angela_choice_four = int(input("WHAT TO DO?! "))

                    if angela_choice_four == 1:
                        print("\n" + "AS A RESULT OF THIS CHOICE, YOU GET BEATEN BY YOUR MOTHER." + "\n" + "THEN, YOUR BROTHERS COME RUSHING IN AND ASK YOU TO NAME THE MAN WHO TOOK YOUR VIRGINITY." + "\n" + "YOU KNOW THIS ISN'T GOING TO END WELL, BUT YOU'RE TORN BETWEEN:")
                        print("==============================")
                        player.angela_five()
                        angela_choice_five = int(input("A MAN'S LIFE IS IN YOUR HANDS... "))

                        if angela_choice_five == 1:
                            print("\n" + "YOUR BROTHERS ARE NOW AFTER SANTIAGO NASAR’S LIFE." + "\n" + "AFTER A SPECTACLE WITNESSED BY NEARLY THE WHOLE TOWN, SANTIAGO IS KILLED ON HIS OWN DOORSTEP." + "\n" + "YOUR BROTHERS GO TO PRISON FOR MURDER. WELL, THIS IS WHERE YOUR CHOICES HAVE LED YOU." + "\n" + "BUT DON’T WORRY! SOMEHOW, YOU STILL SUPPOSEDLY END UP WITH BAYARDO.")

        print("\n" + "\n" + "\n" + "\n")
        print("START GAME (AGAIN):")
        continue

    elif choice == 4: # TWINS PATHWAY
        print("\n" + "HELLO, TWINS. NICE TO MEET YOU." + "\n" + "YOU ARE THE DASHING BROTHERS OF THE BEAUTIFUL ANGELA VICARIO AND SONS OF SEÑORA PURA VICARIO!" + "\n" + "YOU ARE CURRENTLY ATTENDING YOUR SISTER AND BAYARDO’S WEDDING, BUT IT IS GETTING BORING." + "\n" + "NOT TO MENTION, YOU BOTH ARE PARCHED." + "\n" + "YOU ARE MET WITH TWO CHOICES,")
        print("==============================")
        player.twins_one()
        twins_choice_one = int(input("WHAT ARE YOU GOING TO DO? "))

        if twins_choice_one == 1:
            print("\n" + "NICE CHOICE! KEEP THE DRINKS COMING... BUT WAIT..." + "\n" + "YOUR MOTHER KEEPS TRYING TO GET YOU GUYS HOME, AND SHE SAYS IT’S URGENT. UGH!" + "\n" + "YOU’VE BEEN ENJOYING YOURSELVES WITH SANTIAGO AND THE BOYS." + "\n" + "YOU ARE MET WITH TWO CHOICES,")
            print("==============================")
            player.twins_two()
            twins_choice_two = int(input("WHAT ARE YOU GOING TO DO? "))

            if twins_choice_two == 1:
                print("\n" + "RIGHT ON! I’M SURE ALL MOTHERS WOULD WANT CHILDREN LIKE YOU TWO." + "\n" + "YOU HAVE JUST REACHED HOME AND SEE THAT YOUR SISTER IS LYING ON THE COUCH, BRUISES ALL OVER HER FACE." + "\n" + "AS IT TURNS OUT, SOMEBODY HAS TAKEN HER VIRGINITY." + "\n" + "YOU ASK HER TO NAME THE MAN RESPONSIBLE AND SHE SAYS IT WAS SANTIAGO NASAR." + "\n" + "YOUR FAMILY’S HONOUR IS NOW DESTROYED… BUT, YOU CAN AVENGE THIS TERRIBLE DOING." + "\n" + "YOU ARE MET WITH TWO CHOICES,")
                print("==============================")
                player.twins_three()
                twins_choice_three = int(input("WHAT ARE YOU GOING TO DO? "))

                if twins_choice_three == 1:
                    print("\n" + "EXCELLENT CHOICE! I KNEW YOU HAD THE MACHISMO IN YOU TO DO IT." + "\n" + "YOU HAVE JUST ANNOUNCED YOUR MURDER PLAN TO THE WHOLE TOWN AND WAIT AT CLOTILDE’S SHOP." + "\n" + "UNFORTUNATELY, THE COLONEL TAKES AWAY YOUR KNIVES." + "\n" + "BUT, THAT’S NEVER STOPPED A MURDERER BEFORE. YOU RETURN HOME AND GRAB A DIFFERENT PAIR OF KNIVES." + "\n" + "SOON AFTER, YOU LOCATE YOUR TARGET EMERGING FROM FLORA MIGUEL’S HOUSE. THIS IS YOUR LAST CHANCE TO PUT AN END TO ALL OF THIS." + "\n" + "YOU ARE MET WITH TWO CHOICES,")
                    print("==============================")
                    player.twins_four()
                    twins_choice_four = int(input("WHAT ARE YOU GOING TO DO? "))

                    if twins_choice_four == 1:
                            print("\n" + "COOL. YOU CHASE SANTIAGO TO HIS HOUSE WHERE, THANKFULLY, THE DOOR IS LOCKED." + "\n" + "THEN, YOU STAB AT HIM COUNTLESS TIMES, WONDERING WHY HE JUST WON’T DIE." + "\n" + "FINALLY, INTESTINES HANGING OUT, HE WALKS AWAY." + "\n" + "YOUR HONOUR HAS NOW BEEN RESTORED. WHAT DID IT COST?" + "\n" + "*EVERYTHING*")
                            print("==============================")

        print("\n" + "\n" + "\n" + "\n")
        print("START GAME (AGAIN):")
        continue

    elif choice == 5: # CRISTO PATHWAY
        print("\n" + "HELLO, CRISTO. NICE TO MEET YOU." + "\n" + "YOU ARE A FRIEND OF SANTIAGO’S, AND YOU ARE WITH HIM THE DAY OF ANGELA AND BAYARDO’S WEDDING." + "\n" + "THE PARTY’S DYING DOWN, AND SOME FRIENDS INVITE YOU TO GET DRINKS AT MARIA CERVANTES’ WITH SANTIAGO, LUIS, AND THE VICARIO TWINS." + "\n" + "YOU ARE MET WITH TWO CHOICES,")
        print("==============================")
        player.cristo_one()
        cristo_choice_one = int(input("WHAT ARE YOU GOING TO DO? "))

        if cristo_choice_one == 1:
            print("\n" + "NICE, YOU WERE GETTING THIRSTY ANYWAY." + "\n" + "YOUR FRIENDS SLOWLY TRICKLE OUT, AND SANTIAGO GOES HOME TO GET SOME REST." + "\n" + "SOON AFTER, YOU GO OUT WITH HIM ON A WALK ALONG THE RIVERBANK, TRYING TO CALCULATE THE COST OF THE WEDDING." + "\n" + "YOU GIVE SANTIAGO A FINAL ESTIMATE, AND YOU PART WAYS AFTER HE TELLS YOU THAT HE WANTS TO CHANGE BEFORE BREAKFAST." + "\n" + "ALL OF A SUDDEN, YAMIL TELLS YOU THAT SANTIAGO’S LIFE IS IN DANGER." + "\n" + "YOU ARE MET WITH TWO CHOICES,")
            print("==============================")
            player.cristo_two()
            cristo_choice_two = int(input("WHAT ARE YOU GOING TO DO? "))

            if cristo_choice_two == 1:
                print("\n" + "AT LEAST SOMEONE IN THIS TOWN HAS SOME COMMON SENSE." + "\n" + "YOU GET A HOLD OF SANTIAGO’S GUN, AND YOU ARE HOPING TO GET IT TO HIM SO HE CAN DEFEND HIMSELF." + "\n" + "PEDRO VICARIO IS LITERALLY RIGHT THERE, AND HE TELLS YOU THAT HE AND HIS BROTHER WAITING FOR SANTIAGO TO KILL HIM." + "\n" + "YOU LOOK DOWN AT THE GUN IN YOUR HAND THAT YOU DON’T KNOW HOW TO SHOOT." + "\n" + "YOU ARE MET WITH TWO CHOICES,")
                print("==============================")
                player.cristo_three()
                cristo_choice_three = int(input("WHAT ARE YOU GOING TO DO? "))

                if cristo_choice_three == 1:
                    print("\n" + "THAT’LL COST YOU." + "\n" + "FLUSTERED, YOU DECIDE TO HEAD TO THE NARRATOR’S HOUSE; MAYBE SANTIAGO ENDED UP DECIDING TO HAVE BREAKFAST BEFORE CHANGING." + "\n" + "ON THE WAY, YOU ARE DELAYED BY THE ARANGOS FOR WHAT FEELS LIKE THE LONGEST 7 MINUTES OF YOUR LIFE." + "\n" + "BEFORE YOU KNOW IT, IT’S TOO LATE. SANTIAGO’S BEEN MURDERED." + "\n" + "SO CLOSE, YET SO FAR, HEY? WELL, THAT’S THE END OF YOUR STORY.")
                    print("==============================")

        print("\n" + "\n" + "\n" + "\n")
        print("START GAME (AGAIN):")
        continue

    elif choice == 6: # NARRATOR PATHWAY
        print("\n" + "HELLO, NARRATOR. NICE TO MEET YOU." + "\n" + "FOR THE LAST 27 YEARS, THE DAY THAT SANTIAGO NASAR WAS MURDERED HAS BEEN ALL YOU CAN THINK ABOUT." + "\n" + "YOU FINALLY DECIDE TO RETURN TO THAT LITTLE TOWN AND FIGURE OUT WHAT REALLY HAPPENED." + "\n" + "AFTER SOME INVESTIGATION, YOU DEDUCE THAT THE FOLLOWING EVENTS PLAYED THE BIGGEST ROLES IN SANTIAGO’S MURDER." + "\n" + "YET, THE MYSTERY IS FAR FROM BEING SOLVED." + "\n" + "AT A LOSS, YOU DECIDE TO ARRANGE THESE EVENTS INTO AN RPG WITH CHARACTERS REPRESENTING THAT DAY’S MOST SIGNIFICANT PEOPLE." + "\n" + "MAYBE IT WILL HELP TO SEE EVENTS FROM DIFFERENT PERSPECTIVES.")
        print("==============================")
        player.narrator_one()
        narrator_choice_one = int(input("WHAT WOULD YOU LIKE TO DO? "))

        if narrator_choice_one == 1:
            print("\n" + "6 MONTHS BEFORE THE MURDER, BAYARDO ARRIVED, LOOKING FOR A WIFE. HE EVENTUALLY FALLS IN LOVE WITH ANGELA AND AFTER A SHORT FOUR MONTHS, THEY ARE TO BE MARRIED." + "\n" + "ANGELA AND BAYARDO’S WEDDING HAPPENED A DAY BEFORE THE DAY OF THE MURDER. THE WEDDING WAS HUGE, WITH NEARLY THE WHOLE TOWN IN ATTENDANCE." + "\n" + "THAT NIGHT, ANGELA WAS RETURNED AFTER BAYARDO HAD DISCOVERED THAT SHE WAS NOT A VIRGIN." + "\n" + "AT HOME, ANGELA PROCEEDED TO RECEIVE A BEATING BY HER MOTHER. HER BROTHERS, THE VICARIO TWINS, THEN SET OUT ON THEIR QUEST TO MURDER SANTIAGO, THE MAN SUPPOSEDLY RESPONSIBLE FOR DEFLOWERING THEIR SISTER." + "\n" + "THE VICARIO TWINS, SHARPENED KNIVES IN HAND, WENT TO CLOTILDE’S SHOP FOR A DRINK." + "\n" + "COLONEL APONTE, THE TOWN’S POLICE OFFICER, STOPPED THE VICARIO TWINS AND TOOK THEIR KNIVES AWAY, THINKING THAT WOULD BE ENOUGH TO PREVENT THE MURDER." + "\n")
            print("AT SOME POINT, SOMEONE SLIPPED AN ANONYMOUS NOTE UNDER SANTIAGO’S FRONT DOOR, WARNING HIM OF WHAT THE VICARIO TWINS HAVE BEEN PLOTTING." + "\n" + "ANOTHER WARNING. THIS TIME, IT WAS SENT BY CLOTILDE TO VICTORIA GUZMAN, ONE OF THE NASAR FAMILY’S SERVANTS, VIA A BEGGAR." + "\n" + "EVEN AFTER SEEING SANTIAGO WITH CRISTO ON THE RIVERBANK, SEVERAL PEOPLE REFRAIN FROM WARNING HIM, NAMELY INDALECIO PARDO AND YAMIL SHAIUM. CROWDS OF PEOPLE, ALL AWARE OF WHAT WAS TO COME, AVOIDED SANTIAGO AND CRISTO." + "\n" + "COLONEL APONTE SAW THE VICARIO TWINS AND REALIZED THAT THEY HAD RETURNED WITH NEW KNIVES. BUT, HE DECIDED TO CHECK ON HIS GAME OF DOMINOES FIRST." + "\n" + "AFTER SANTIAGO LEFT CRISTO, YAMIL TOLD CRISTO ABOUT THE VICARIO TWINS’ PLAN. CRISTO THEN DEPARTED TO FIND SANTIAGO’S GUN AND LEFT TO GIVE IT TO HIM, IN HOPES THAT HE COULD DEFEND HIMSELF." + "\n")
            print("THE VICARIO TWINS TOLD CRISTO TO TELL SANTIAGO THAT THEY WERE WAITING TO KILL HIM. UNFORTUNATELY, CRISTO DID NOT KNOW HOW TO USE THE GUN IN HIS HAND. CRISTO CONTINUED ON HIS WAY TO TRY AND PREVENT THE TRAGEDY. BUT, HE WAS DELAYED FOR A FATEFUL 7 MINUTES." + "\n" + "DURING THIS TIME, SANTIAGO HAD BEEN IN HIS FIANCEE’S HOUSE. HIS FIANCEE, FLORA MIGUEL, WAS OUTRAGED BECAUSE SHE HAD HEARD ABOUT THE MOTIVES FOR SANTIAGO’S IMMINENT MURDER. SANTIAGO WAS STILL IN THE DARK. THIS WAS WHEN NAHIR MIGUEL FINALLY TOLD HIM ABOUT THE VICARIO TWINS’ PLAN TO MURDER HIM. IN A MOMENT OF UTTER CONFUSION, SANTIAGO DECIDED TO LEAVE THE HOUSE." + "\n" + "WHEN SANTIAGO LEFT, NEARLY THE ENTIRE TOWN HAD GATHERED TO SEE THE MURDER. AFTER THE TWINS SAW HIM, HE BEGAN TO RUN TO HIS HOUSE. SECONDS AWAY FROM SAFETY, SANTIAGO WAS MISTAKENLY LOCKED OUT OF HIS HOUSE BY HIS OWN MOTHER." + "\n")
            print("THE VICARIO TWINS CAUGHT UP TO SANTIAGO AND CARVED HIM UP LIKE A PIG ON HIS DOORSTEP. SOMEHOW, SANTIAGO MADE HIS WAY BACK TO HIS HOUSE, INTESTINES IN HAND, WHERE HE FINALLY COLLAPSED." + "\n" + "HM. CLEAR AS MUD. MAYBE TRY WRITING A NOVELLA NEXT…")
            print("\n" + "\n" + "\n")

    running = False
    
