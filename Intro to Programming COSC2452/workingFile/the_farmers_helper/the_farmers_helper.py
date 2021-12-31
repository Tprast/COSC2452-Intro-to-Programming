import sys

from collections import deque

#main code block
def main():
#Introduction to game   
   sys.stdout.write("\
\n...The Farmers Helper is now loaded and ready to begin...\n\
\nEnter your first name to get started: \n")                  
#Input asks for players name - to be used through-out the program
#input is defined as string.
   player_name=str(sys.stdin.readline().strip())
#Code will ask for name if no input is given - name is required for the
#game to run
   while not player_name:
#repeats question to player again asking for input
            sys.stdout.write("\
What is your first name?\n")
            player_name=str(sys.stdin.readline().strip())
#Welcomes player to game, repeating input from above.
   sys.stdout.write("\
\nHi " + player_name + "! \nWelcome to...\n")
#Below is the insert space for ascii art.
#Ascii art reference:
#Patorjk.com. 2021. Text to ASCII Art Generator (TAAG). [online] Available at: <https://patorjk.com/software/taag/#p=display&f=Big&t=The%20%0AFarmers%20%0AHelper> [Accessed 30 September 2021].
   title_art="             _______  __   __  _______ \n"                 
   title_art+="           |       ||  | |  ||       |\n"    
   title_art+="           |_     _||  |_|  ||    ___|\n"        
   title_art+="             |   |  |       ||   |___ \n"         
   title_art+="             |   |  |       ||    ___|\n"
   title_art+="             |   |  |   _   ||   |___ \n"
   title_art+="             |___|  |__| |__||_______|\n"
   title_art+=" _______  _______  ______    __   __  _______  ______    _______ \n"
   title_art+="|       ||   _   ||    _ |  |  |_|  ||       ||    _ |  |       |\n"
   title_art+="|    ___||  |_|  ||   | ||  |       ||    ___||   | ||  |  _____|\n"
   title_art+="|   |___ |       ||   |_||_ |       ||   |___ |   |_||_ | |_____ \n"
   title_art+="|    ___||       ||    __  ||       ||    ___||    __  ||_____  |\n"
   title_art+="|   |    |   _   ||   |  | || ||_|| ||   |___ |   |  | | _____| |\n"
   title_art+="|___|    |__| |__||___|  |_||_|   |_||_______||___|  |_||_______|\n"
   title_art+="     __   __  _______  ___      _______  _______  ______  \n"      
   title_art+="    |  | |  ||       ||   |    |       ||       ||    _ |\n"       
   title_art+="    |  |_|  ||    ___||   |    |    _  ||    ___||   | ||\n"       
   title_art+="    |       ||   |___ |   |    |   |_| ||   |___ |   |_||_\n"     
   title_art+="    |       ||    ___||   |___ |    ___||    ___||    __  |\n"      
   title_art+="    |   _   ||   |___ |       ||   |    |   |___ |   |  | |\n"      
   title_art+="    |__| |__||_______||_______||___|    |_______||___|  |_|\n"
   title_art+="\n"
#Inserts ascii art into opening text introduction
   sys.stdout.write(""+title_art+"\nThe Farmers Helper is text based adventure \n\
game with a focus on solving Math problems in a fun and interactive way.\n")
#input required to continue text flow - breaks up the speed in which information is displayed to the player.
   input("\n[Press ENTER key to continue]\n")
#hash below is code character counter for creator to follow guidelines on limits                      
################################################################################
#I have used sys.stdout.write throughout the program as I am still learning the
#most effective techniques to introduce large bodies of text to the output/user.
#In future, to keep code tidy and well presented I would either keep sys.stdout.write
#to a minimum by using a similar technique to the ascii art above or I would use file imports (which we have not yet explored).
#Story begins.
   sys.stdout.write("\
This summer holidays your parents have sent you to stay with your Uncle \n\
and Aunty on their farm outside Cowaraump, about 4 hours South of Perth. \n\
You arrived late in the evening with your parents, whom dropped you off \n\
before continuing their journey further south-east to Albany for a little \n\
holiday. You’ve spent many summers on the farm swimming in the dam, learning \n\
to ride horses, climbing trees and going on hikes.\n\
\nDuring dinner with your Uncle and Aunty shortly after you arrive, your \n\
Uncle mentions that he and your Aunty will be taking a drive to Dunsborough \n\
(the local town) for some early morning shopping the next day, and wonders if \n\
you can take care of a few odd jobs for him while they are gone.\n\
\nUncle:'We won’t be back until just before lunch-time and I wouldn’t usually \n\
ask but the animals can get pretty cranky if they aren’t fed on-time. \n\
I’m happy to pay you for the mornings work.. say $50.. and any other mornings \n\
you can help out. I’d really appreciate it'.\n\
\nDo you want to help your Uncle out with his list \
of jobs?\n\
[Type 'yes' or 'no']\n")
#Asks player if they want to help uncle, Boolean "yes" or "no". Asks for direct input from player.
   uncle_question= str(sys.stdin.readline().strip())
#Establishes validation protocol. Yes being the qualifier.
   uncle_question_correct_answer=("yes")
#compares user input to required validator, if incorrect input the program will repeat question.
   while uncle_question!=uncle_question_correct_answer:
         sys.stdout.write("\
\n*Are you sure? $50 for a mornings work is pretty fair.. think of all the \n\
computer games I’ll be able to buy when I get back home.. plus it doesn’t \n\
sound too hard..I’d better say yes*\n\
\nDo you want to help your Uncle out with his list \
of jobs?\n\
[Type 'yes' or 'no']\n")
         uncle_question= str(sys.stdin.readline().strip())

#will repeat question if no answer given or invalid input.
   else:
      if uncle_question==uncle_question_correct_answer:
#Continues exposition of story with correct answer
         sys.stdout.write("\
\nUncle:'Great! I’ll leave you a note with some instructions in the morning, \n\
it shouldn’t take you too long and we will be back from town in time to have a \n\
swim in the dam after you're finished.'\n\
\nAunty:'I've got some fresh baked savoury muffins I will leave out for your \n\
breakfast too!'\
Uncle:'And they sure are delicious!. But we'd better get an early night.\n\
We all have a big morning tomorrow.'\n\
\n\
*You say your goodnights and head up to bed and go to sleep for the evening.*\
\n")

#input to continue story, active prompt
   input("\n[Press ENTER key to continue]")
   sys.stdout.write("\n..The next morning..\n")
#Input to continue story, active prompt and to give space before more text.
   input("\n[Press ENTER key to continue]\n")
#Exposition continues.
   sys.stdout.write("\
*The rooster crows and you awaken, wiping the sleep from \
your eyes*\n\"I'd better go see about that list of jobs Uncle left for me, \n\
I'd love to be finished in time to have a swim in the dam! Plus he did say \n\
he'd pay me..*\n*You head downstairs and collect the note from upon the \n\
kitchen table*\n")
#input to continue story, active prompt
   input("\n[Press ENTER key to continue]\n")
   
#THE NOTE - Key story beat and introduces the player to narrative hook.
#repeats player_name input from start of program to personalise the narrative  
   sys.stdout.write("\
\n'Good morning "+ player_name +"',\n'Here is the list of jobs I needed you\n\
to take care of while your Aunty and I are in town;\n\
-Feed the Chickens and collect any eggs they may have laid [chickens].\n\
-Feed the Horses and let them out into the paddock [horses].\n\
Please make sure you don't overfeed the animals!\n\
We will see you later-on today,'\n\
\nLove, Uncle.\n\
\n'PS. The neighbours dog tends to join me when I start my jobs for the day. \n\
The dog is always a great help.'\n")
   
#Code below creates the list of jobs given in the note narrative hook.
   job_list=["chickens","horses"]
   show_job_list=job_list

#Requires user input before continuing story   
   input("\n[Press ENTER key to continue]\n")
#Narrative exposition  
   sys.stdout.write("\
\n*That doesn't seem too hard* you think to yourself...\n\
*but I best get started.*\n\
\nYou head out the front door to get started on your list of jobs. \n\
You're greeted by an excited bark and the wagging of a bushy red tail.\n\
*It must be the neighbours dog Uncle mentioned.* \n\
You bend down to give it a pat on the head and read the name tag on it's collar.\n\
*What is the name on the collar?*\n\
\n[Enter the dogs name:]\n")
#Requires player input to name the dog - introducing another player named character.
   dog_name=str(sys.stdin.readline().strip())
#This code section means the user MUST enter a valid name or program will not execute

   while not dog_name:
            sys.stdout.write("\
What does the dog's name collar say?\n")
            dog_name=str(sys.stdin.readline().strip())
   sys.stdout.write("\
\n*" +dog_name+ " Barks excitedly and follows you out to \
the verandah*.\n\
\nSo " +dog_name+ ", Where should we start first on this \
list:?\n")
#Program displays the job_list for refrence for the player
   show_job_list
#code below is used to identify if list is empty
   if len(job_list)==(0):
       sys.stdout.write("\
\nLooks like all the jobs have been finished!\n")
#Code to display the job_list for the player
   sys.stdout.write("\
\n[Choose an option from the list - eg type 'horses'to go to the 'stables']\n")
#Displays code in easy to understand and simply presented manner.
   for j in job_list:
       sys.stdout.write("\n-The "+j)
   sys.stdout.write("\n")
#The below is an example of storing large narrative blocks as a variable. In future, I would use this
#in place of all the large narrative sys.stdout.write blocks seen through-out this program.
#Time and skills were a factor in using this later in the dev cycle of this program.
   wrap_up_text=("\
\n"+dog_name+" perks up, looking towards the drive-way to the farmhouse, \
\nyou hear it too now.\n\
Your Uncle and Aunty have returned from their shopping trip to town.\n\
\nYou head back to the house to let them know you’ve finished your list of \n\
jobs and give them a hand with their shopping,"+dog_name+" bounds up to your\
\n Uncle and Aunty as soon as they are out of the car, spinning circles around\
\n them and barking excitedly in your direction.Uncle:"+dog_name+ " help you \
\nout this morning did he? He does that for me too. Uncle hands you a large\
\n beef bone from the butchers and a crisp $50 note for completing your jobs.\n\
“I got" +dog_name+ "this for the help I knew youd get..\n\
\nShall we head to the dam for a swim now " +player_name+"?\n\
\nThis is going to be a good summer you think to yourself while \n\
sitting on the bank of the dam.\n\
"+dog_name+"'s new bone hanging from its mouth as you give it a scratch \n\
around the ears. “Tomorrow I can teach you how to fish in this \n\
dam if you’d like " +player_name+"?”\n\
Your uncle calls to you from waist deep water.“yup, definitely a good \n\
summer..”" +dog_name+" barks excitedly.\
\nThe End.\
\n\
\nThanks for playing The Farmers Helper")
       
                          
#BRANCHING STORYLINES START HERE
#CHICKENS CHICKENS CHICKENS CHICKENS
#While-loop is used to construct the branching stories.\
#By nesting lists inside of eachother we create a branchable\
#story that is approachable from different angles and avenues\
#they also allow me to create tasks within the branches nested\
#in more while loops.
#while loop that locks moving forward until requirements and validators are met.
   while True:
#player chooses first path here
        direction=sys.stdin.readline().strip()       
#Player chooses the 'Chicken' branch from the list\
#The code below executes that branch choice
        if direction==("chickens"):
                    sys.stdout.write("\
\nOff to the "+direction+" it is then.\n")
#hash below is code character counter for creator to follow guidelines on limits                      
################################################################################
                    sys.stdout.write("\
\nYou make your way to the Chicken Coop, passing near to the large Gum tree \n\
in the centre of the property.\
\nOutside the Chicken Coop you see a large wooden chest with the words\n\
'Chicken Feed' paitned on the front. Upon opening the chest you see a large bag \n\
of chicken feed with a scoop next to it, a large empty bucket that looks like\n\
the farmer puts the feed in it, and a stack of cardboard egg holders \n\
(each of which can carry up to 6 eggs).\n\
\n*You inspect the bag of 'chicken feed' and notice the instructions for feeding \n\
on the back;*\
\n\'Each Chicken should be fed: 50 grams of Mr Sanders Chicken Feed each day to \n\
stay health and strong.'""\n\
*You look at the scoop included in the bag that reads '100 grams Maximum.\
\n*That makes things a bit tricky*\
\n*You know from looking into the Chicken Coop that there are 25 chickens \n\
to be fed*\
\nIn numbers, how many scoops are required to be added to the bucket to feed \n\
25 chickens 50grams of feed each?\n")
#Chicken feed question in a nested while loop
#requires float input from user.
                    chicken_feed_question=float(sys.stdin.readline().strip())
                    chicken_feed_correct_answer=(12.5)
#creates a validator that must be met by the user.
                    while chicken_feed_question!=(chicken_feed_correct_answer):
                        sys.stdout.write("\
Incorrect.\nHow many scoops could it be?\n")
                        chicken_feed_question=float(sys.stdin.readline().strip())
#User inputs chicken_feed_question
#user must input number or program will give ValueError
#Correct answer to proceed
#if statement comparing values of chicken_feed_question\
#to chicken_feed_correct_answer
#when input is correct the validator is met and narrative moves forward                        
                    else:
                        if chicken_feed_question==chicken_feed_correct_answer:
#inserts answer from the question in float format
                            sys.stdout.write("\
You fill the bucket with "+(str(chicken_feed_question))+" Scoops of chicken feed. \n\
That looks perfect!\n")
#narrative moves forward.                               
                    sys.stdout.write("\
\n" +dog_name+ " *barks excitedly* \n\
Seems like the dog knew the right answer all along. You spread the chicken \n\
feed over the grass in the coop for the chickens to eat.\
\nWhile the chickens are busy eating you decide to collect the eggs \n\
they may have laid. On inspecting the coop you notice that only one of the \n\
chickens in the whole coop hasn't laid an egg.\
\nHow many egg holders will you need to carry all of the eggs that \n\
have been laid?")
                    sys.stdout.write("\
\n(Remember, each egg holder can carry up to 6 eggs.]\n")
#nested loop within Chickens branch for new task
#uses whole number Int as answer - Int is the only accepted input.
                    egg_holder_question_input=int(sys.stdin.readline().strip())
                    egg_holder_correct_answer=(4)
                    while egg_holder_question_input!=egg_holder_correct_answer:
                        sys.stdout.write("\
[Incorrect]\nHow many egg holders will you need to carry all of the eggs that\n\
have been laid?\n")
                        egg_holder_question_input=int(sys.stdin.readline().strip())
#Validates input Vs correct answer value and returns
#response  and continues branch on correct answer
                    else:
                        if egg_holder_question_input==egg_holder_correct_answer:
                            sys.stdout.write("\
Thats all of them! And not one space too many.. that seems a bit too perfect to \n\
be coincidence..\nYou take the egg cartons back to the house and leave them on \n\
the back verandah.You shouldn't carry them around all morning.\n\
\nYou check your list to decide where to go next.\n")
                            
#removes chickens from job_list
                    job_list.remove("chickens")
#presents player with the list, modified to have Chickens branch
#removed. The remaining options are available.
#if branches all completed will run finishing text                    
                    show_job_list
                    if len(job_list)==(0):
                        sys.stdout.write("\
\nIt looks like we’ve finished everything!\n\
\n"+dog_name+" looks up at you triumphantly and rolls onto it's belly for a belly rub.\n\
“Want to come for a swim in the dam with me when Uncle and Aunty get back dog_name?”\n\
“dog_name rolls back over onto it's legs and spins around excitedly* \n\
“that looks like a yes to me!")
                    else:
#If job_list not finished provides user with remaining items  
                        sys.stdout.write("\
\n[Choose an option from the list - eg type 'horses'to go to the 'stables']\n")
                        for j in job_list:
                            sys.stdout.write("\n-The "+j)
                        sys.stdout.write("\n")
                        direction=sys.stdin.readline().strip()
  
#Horses Horses Horses
#new branch in while loop below
#branch contains nested while loops for tasks within branches                   
        if direction==("horses"):
                       sys.stdout.write("\
\nThe Horse stable is on the opposite side of the property to the \n\
Chicken Coop, next to a large stockple of firewoord for the house. It's a big \n\
wooden building painted the traditional 'Barn Red' and you remember helping \n\
Uncle to paint it last summer.\n\
*He always seems to get me doing jobs for him over my summer*\n\
break.*\nThe back door of the stable opens out into a large enclosed \n\
pasture for the horses to play and graze in during the day.\n\
"+dog_name+" jumps excitedly as you open the stable doors. You find all the \n\
horses in their stalls, whineying loudly about their awaiting breakfast.\n\
"+dog_name+" runs up to a bag of oats in the corner and sniffs excitedly at it.\n\
The front of the bag reads 'Farmers Fresh Oats - 10kg'\n\
and pinned to the mouth of one of the bags of oats you see a note written\n\
in your uncles handwriting:\n\
'Per horse;\n2.5kg of oats,\n1/2 bail of hay'\n\
\nYou see the bundles of hay uncle must be tlaking about stacked next to the \n\
oats and a large feeding trough in the middle of the stable.\
\nThere are 6 horses in the stable.\n\
\nIn Numbers, How many bags of oats will you need to put into the feeding trough?\n")
 #Nested while loop for user task
#user must input a number or program will give ValueError
#Oats question - requires float answer. Float only calid response.                       
                       oats_user_input=float(sys.stdin.readline().strip())
                       oats_correct_answer=(1.5)
                       while oats_user_input!=oats_correct_answer:
                             sys.stdout.write("\
[Input cannot be left blank]\
\nHow many bags of oats (in numbers) will you need to put into the feeding trough?\n")
                             oats_user_input= float(sys.stdin.readline().strip())
                                
#code does not allow user invalid input
                       if oats_user_input==oats_correct_answer:
                                sys.stdout.write("\
"+dog_name+" wags their tail excitedly, thats the right amount isn't it!\n\
" +(str(oats_user_input))+ " "+dog_name+" always seems to know these things..\n")
#nested while loop question, follows same principles as above
                       sys.stdout.write("\
\n... now... \nhow many bundles of Hay (in numbers) should be put in the trough?\n\
[Remember - 1/2 a bail of hay per horse]\n")
#Hay question - requires INT input. Otherwise error ensues.
                       hay_user_input=int(sys.stdin.readline().strip())
                       hay_correct_answer=(3)
                       while hay_user_input!=hay_correct_answer:
                                sys.stdout.write("[Input cannot be left blank]\
\nHow many bundles of Hay should be put in the trough\n")
                                hay_user_input=int(sys.stdin.readline().strip())
                                                                
                       if hay_user_input==hay_correct_answer:
                                sys.stdout.write("\
3 Bales for 6 horses seems right to me.\n"+dog_name+" barks excitedly\n\
in agreement, their bushy tail sweeps at the hay covering the stable floors.\n\
\nOnce the food is in the trough, you let the horses out of their stables to\n\
start having their breakfast.\nBefore leaving the stables you open the back\n\
doors to the stables to let the horses roam in their pasture once they are\n\
finished eating.\
\n"+dog_name+" runs around your legs excitedly as you close front stable doors\n\
behind you as youleave the stable.\
\nWhats left on this list now "+dog_name+"\n")
#removes Horses branch from the job_list 
                       job_list.remove("horses")
#displays job_list with the changes from previous branches.
#if branches all completed will run finishing text                       
                       show_job_list
                       if len(job_list)==(0):
                           sys.stdout.write("\
\nIt looks like we’ve finished everything!\n"+dog_name+" looks up at you \n\
triumphantly and rolls onto its belly for a belly rub.“Want to come for a \n\
swim in the dam with me when Uncle and Aunty get back "+dog_name+"?”\n\
"+dog_name+" rolls back over onto its legs and spins around excitedly* \n\
“that looks like a yes to me!")
                       else:
                            sys.stdout.write("\
\n[Choose an option from the list - eg type 'chickens'\n\
to go to the 'chicken coop']\n")
                            for j in job_list:
                               sys.stdout.write("\n-The "+j)
                            sys.stdout.write("\n")
#if branches all completed will run finishing text
        show_job_list
        if len(job_list)==(0):
#combination of hoiw sys.stdout.write should be used vs how it shouldn't be used
#as it makes code quite untidy and unclear.
            sys.stdout.write("\
\nIt looks like we’ve finished everything!\
\n"+dog_name+" looks up at you triumphantly and rolls onto \n\
their belly for a belly rub.\
“Want to come for a swim in the dam with me when Uncle and Aunty get back \n\
"+dog_name+"?”"+dog_name+" rolls back over onto it's legs and spins \n\
around excitedly* “that looks like a yes to me!")
            sys.stdout.write(wrap_up_text)
#displays branch options if requirements not yet met.
        else:
            sys.stdout.write("\n[Choose an option from \
the list - eg type 'horses' to go to the 'stables']\n")
            for j in job_list:
                sys.stdout.write("\n-The "+j)
            sys.stdout.write("\n")
                                   
                                   
                                                                                                                     
                #If no valid input made on branches will ask for valid input on repeat       
            if direction!=("chickens","horses"):
                        sys.stdout.write("[Please select a valid location]\n")
            
        
            


          
           
main()


###The below is a third branch called Vegetables that was unused.
#This branch gave me a large amount of issues with 4 while loops nested inside the larger
#branch loop. While I could make all the loops work seperately I was not able to have the
#loops all work together nicely to round out the game. I believe it is an issue with indentations
#and will investigate this further. As it is, the assignment is late as I spent far too long
#trying to get this code to work and run properly.



######        if direction==("vegetables"):
#                               sys.stdout.write("\
#\nThe vegetable garden is just next to the house, 4 plots of raised garden\n\
#beds are arranged in a small grid with lettuce’s, herbs, tomatoes and potatoes \n\
#all growing in their own garden beds. The garden itself is surrounded by \n\
#a high fence to keep out the Rabbits and Kangaroos with a small open shed \n\
#in the corner.\n ")
#                               input("\n[Press ENTER key to continue]\n")
#                               #list is created here for the nested while loops for this branch
#                               #watering_list of jobs
#                               watering_list=("lettuces","herbs","tomatoes",
#"potatoes")
#                               sys.stdout.write("\
#\n"+dog_name+" leads you over to the shed, he seems to know what we are here to do.\n\
#The Shed is filled to the brim with gardening tools, bags of fertilisers and a\n\
#watering can. There is a note taped above the watering can, it looks like its\n\
#been there for a while.\nThe note reads:\n\
#“Uncle,\n\
#Make sure you read the fertiliser instructions!\nIts only one watering \n\
#cans worth of water per garden bed or else you’ll over water and kill my \n\
#veggies again!\n\
#In another style of handwriting just under the first part of the note is \n\
#written just the words\
#\n“sorry love”\n\You grab the bucket of fertiliser and roll it over to read the back\n\
#“McClure’s fertiliser helps your plants grow big and strong. Simply follow \n\
#the recommended dilutions for each type of plant and watch them blossom!”. \n\
#On the list of recommended dilutions, you spot the ones you will need;\n\
#\n-25ml per 500ml of water for lettuce.\n-45ml per 500ml of water for Mixed Herbs.\n-90ml per 500ml \
#of water for Tomatoes.\n-75ml per 500ml of water for Potatoes.\n\
#\nYou grab the watering can, noting its 4.5L marking at the top and look to"+dog_name+".\n\
#“Which Garden bed should we water and fertilise first then "+dog_name+"?\n\
#*"+dog_name+" looks up at you expectantly, seemingly wanting you to decide..*\n\
#Which garden bed do you want to start with?\n")
#                               sys.stdout.write("\
#\n[Choose an option from the list. eg: to start with The herbs type 'herbs'.]")                               
#                            #shows list for this nested while loop of for Vegetable branch                             
#                               job_list.remove("vegetables")
#                               garden_list=["lettuces","herbs","tomatoes",
#                                                  "potatoes"]
#                               show_garden_list=garden_list
 #                              for g in garden_list:
#                                sys.stdout.write("\n-The "+g)
#                               sys.stdout.write("\n")
#                               watering_list=sys.stdin.readline().strip()
#                              # while True:   
#                                #Lettuces listed while loop
#                                if watering_list==("lettuces"):
##                                       sys.stdout.write("\
#In litres, how much of the McClures liquid fertiliser do you need to add to the\
#watering can for the lettuce?:\n")                                          
#while loop for watering_list lettuces with nested while loops inside of it
#bounces back to user on incorrect inputs                                           
#                                       l_water=float(sys.stdin.readline().strip())
#                                       l_water_correct_answer=(0.225)
#                                       while l_water!= l_water_correct_answer:
#                                           sys.stdout.write("I'll kill the \
#lettuces if I add the wrong amount of fertiliser.\nHow much fertiliser (in liters) should I add?\n")
#                                           l_water=float(sys.stdin.readline().strip())
#                                       if l_water== l_water_correct_answer:
#                                           sys.stdout.write("\
#“Perfect! Im a real green thumb.”\n"+str(l_water)+" liters is the right amount.\n")
#                                           sys.stdout.write("\
#\nWhich garden should we water next?:")
#                                           
#removes completed task from list
#                                           garden_list.remove("lettuces")
#                                           if len(garden_list)==(0):
#                                               sys.stdout.write("\
#\nYou finish watering all the garden beds and put the watering can away.\n\
#"+dog_name+" eyes the scarecrow menancingly.\
#\n“time to go is it buddy? Shall we see what’s next on the list?""")
#                                           else:       
#Prints the list to the user of the remaining tasks in the \
#Garden_list tasks yet to be completed
#                                               for g in garden_list:
#                                                   sys.stdout.write("\n-The "+g)
#                                               sys.stdout.write("\n")
#                                           
# 
#herbs
#while loop for watering_list herbs with nested while loops inside of it
#bounces back to user on incorrect inputs
#                                           
#                                                                                               
#                               if watering_list==("herbs"):
#                                       sys.stdout.write("\
#In litres, how much of the McClures liquid fertiliser do you need to add to the\n\
#watering can for the herbs?:\n")
#                                       h_water=float(sys.stdin.readline().strip())
#                                       h_water_correct_answer=(0.405)
#                                       while h_water!=h_water_correct_answer:
##                                           sys.stdout.write("\
#I'll kill the herbs with that much fertiliser.\n")
#                                           h_water=float(sys.stdin.readline().strip())
##                                       if h_water==h_water_correct_answer:
#                                           sys.stdout.write("\
#“These will be some good herbs!”\n"+str(h_water)+" liters is the right amount.\n")
#                                           sys.stdout.write("\
#\nWhich garden should we water next?:\n")
#                                            #removes completed task from list
#                                           garden_list.remove("herbs")
#                                           if len(garden_list)==(0):
##                                               sys.stdout.write("\
#\nYou finish watering all the garden beds and put the watering can away.\n\
#"+dog_name+" eyes the scarecrow menancingly.\
#\n“time to go is it buddy? Shall we see what’s next on the list?""")
#                                           else:
#                                               for g in garden_list:
#                                                   sys.stdout.write("\n-The "+g)
 #                                              sys.stdout.write("\n")
 #                                          
#                                            #tomatoes
#                                            #while loop for watering_list tomatoes with nested while loops inside of it
#                                            #bounces back to user on incorrect inputs                                                
#                                
#
#                               if watering_list==("tomatoes"):
#                                       sys.stdout.write("\
#In mililitres, how much of the McClures liquid fertiliser do you need to add to\
#the watering can for the tomatoes?:\n")
#                                       t_water=int(sys.stdin.readline().strip())
#                                       t_water_correct_answer=(810)
#                                       while t_water!=t_water_correct_answer:
#                                           sys.stdout.write("\
#I'll kill the tomatoes with that much fertiliser.\n")
#                                           t_water=int(sys.stdin.readline().strip())
#                                       if t_water==t_water_correct_answer:
##                                           sys.stdout.write("\
#“These tomatoes are going to be so big and juicy.”\n"+str(t_water)+" mililiters is the right amount.\n")
#  
#                                            #removes completed task from list
#                                           garden_list.remove("tomatoes")
#                                           if len(garden_list)==(0):
#                                               sys.stdout.write("\
#\nYou finish watering all the garden beds and put the watering can away.\n\
#"+dog_name+" eyes the scarecrow menancingly.\
#\n“time to go is it buddy? Shall we see what’s next on the list?""")
#                                           else:        
#                                            #Prints the list to the user of the remaining tasks in the \
#                                               sys.stdout.write("Let's move \
#on with our list!\n")
#                                               for g in garden_list:
#                                                   sys.stdout.write("\n-The "+g)
#                                               sys.stdout.write("\n")
#                                           
#                                   
#                                    #potatoes#
 #                                   #while loop for watering_list tomatoes with nested while loops inside of it
#                                    #bounces back to user on incorrect inputs                                                  
#                                    
#                               if watering_list==("potatoes"):
#                                       sys.stdout.write("\
#In Litres, how much of the McClures liquid fertiliser do you need to add to \nthe watering can for the potatoes?:\n")
#                                       p_water = float(sys.stdin.readline().strip())
#                                       p_water_correct_answer = (0.675)
#                                      while p_water != p_water_correct_answer:
#                                           sys.stdout.write("\
#I'll kill the potatoes with that much fertiliser.\n")
#                                           p_water = float(sys.stdin.readline().strip())
#                                       if p_water == p_water_correct_answer:
#                                           sys.stdout.write("\
#“Maybe this is the secret to Auntys Roast Potatoes?”\n"+str(p_water)+" liters is the right amount.\n")
#                                           sys.stdout.write("\
#\nWhich garden should we water next?:\n")
#removes completed task from list
#                                           
#                                           garden_list.remove("potatoes")
#                                           if len(garden_list)==(0):
#                                               sys.stdout.write("\
#\nYou finish watering all the garden beds and put the watering can away.\n\
#"+dog_name+" eyes the scarecrow menancingly.\
#\n“time to go is it buddy? Shall we see what’s next on the list?""")
#                                           else:    
 #                                              for g in garden_list:
#                                                   sys.stdout.write("\n-The "+g)
#                                               sys.stdout.write("\n")
#                                           
                                              

                               # watering_list!=("lettuces","tomatoes","herbs","potatoes",):
                                 #  sys.stdout.write("\
#Please select a valid Garden bed to water\n")
                                 

                              
                                #   if len(garden_list)==(0):
                                           #sys.stdout.write("\
#\nYou finish watering all the garden beds and put the watering can away.\n\
#"+dog_name+" eyes the scarecrow menancingly.\
#\n“time to go is it buddy? Shall we see what’s next on the list?""")
                    #removes vegetables from lsit of branches

                #if branches all completed will run finishing text
