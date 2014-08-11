# Author: Camyll Harajli
# Date:   7/3/14
# Purpose: To get more practice with python
# Description:  

import sys
import random

def response():
	answer = raw_input()
	if answer == "quit":
		sys.exit(0)
	return answer
def sortingHat():
	Gryffindor = False
	print "Hmm.. let's see, let me think.."
	print "..."
	house = random.randrange(1,6)
	if house == 1:
		print "You're a Gryffindor!"
		Gryffindor = True
	elif house == 2:
		print "You belong in Hufflepuff!"
	elif house == 3:
		print "Definitely a Ravenclaw!"
	elif house == 4:
		print "Slytherin."
	elif house == 5:
		print "This is a tough one... Gryffindor!"
		Gryffindor = True
	return Gryffindor

def dungeon():
	print "Ron says, \"I'm not sure if we should go down there.. There are spiders down there!\""
	print "Hermione says \"Sorry that Ronald is being such a child, but maybe you should choose somewhere else\""

def great_hall():
	print "Harry says, \"Sounds brilliant, let's go!\""
	print "The four of you approach the large wooden door at the entrance of the hall.  It appears to be locked.",
	print " Hermione reccommends that you cast a spell to unlock it since you have your wand out."
	answer = response()
	while answer != "alohomora":
		print "Harry says, \"Try one of the spells from your book!\""
		answer = response()
	print "The door begins to open"
	print "Ron says \"Brilliant!\""
	print "As you enter into the hall, you see a dark, cloaked figure.",
	print "The person immediately runs through a small door at the other end of the hall and slams it behind him."
	print "Harry turns to you and asks, \"Should we follow them?\""
	answer = response()
	if "ye" not in answer and "Ye" not in answer and "yes" not in answer:
		print "Ok so you don't want to follow the cloaked figure, I guess you can just stay in the",
		print " hall until supper. There's not much to see in here anyway."
		return
	print "You make your way over to the small door. It doesn't seem to be locked so you enter it."
	print "The door creeks shut behind you guys. You find yourselves in a completely dark room."
	answer = response()
	while answer != "lumos":
		light = random.randrange(1,3)
		if light == 1:
			print "Ron says, \"Can someone please turn on a light?\""
		elif light == 2:
			print "Hermione says, \"I'm sure you have a spell for light in your book.\""
		else:
			print "Harry says, \"Come on, I know you know a spell for this\""
		answer = response()
	print "Lumos! Well done.  This light has exposed a torch on the wall. The torch just needs fire to be lit."
	answer = response()
	while answer != "incendio":
		print "Hermione says, \"Use your fire casting spell! I would if I had my wand with me.\""
		answer = response()
	print "Harry says, \"Well done! Now we can see the whole room. Let's take a look around!\""
	print "You look around and see many bookshelves around you.  There is a small table in the middle of the room.",
	print "On the table is a note"
	answer = response()
	while "ead" not in answer and "ote" not in answer and "ick up" not in answer:
		message = random.randrange(1,4)
		if message == 1:
			print "As you look around more, you see that all of the books are dusty."
		if message == 2:
			print "Harry points out that most of the room must not have been touched in years."
		if message == 3:
			print "Hermione says, \"That note is intriguing.  Maybe we should read it.\""
		answer = response()
	print "The note reads: \"Severus, if all goes according to plan, meet me in the Forbidden Forest at dusk. -P ",
	print "PS. Please remember, not a word of this to anyone.\""
	print "\n\"I knew it!\" Harry exclaimed, \"I always knew Snape was up to no good!\""
	print "You remind Harry that he shouldn't jump to conclusions."
	print "Hermione thinks that you guys should go to the forbidden forest. What do you think?"
	answer = response()
	if "es" not in answer and "eah" not in answer and "go" not in answer and "ure" not in answer and "ok" not in answer:
		print "Hermione says, \"I guess there's not really much else to explore. I think I'll head back to ",
		print "the commons before dinner time.  We had an excellent time exploring with you!\""
	print "The four of you start to make your way to the forbidden forest.",
	print "As you head down a hill, Ron trips and falls over a rock. He has scraped his arm and is now bleeding."
	answer = response()
	while answer != "episkey" and answer != "Episkey":
		print "Hermione says, \"He's bleeding, can you help him?\""
		answer = response()
	print "Ron says, \"Thanks mate.\""
	print "As you pass by Hagrid's hut, you are approached by Neville."
	print "Neville says, \"Harry you're early! You weren't supposed to be arriving for another 10 minutes.\""
	print "Harry says, \"What are you talking about Neville?\""
	print "Neville responds, \"For your surpirise party of course. Since we couldn't celebrate your Birthday in the summer.\""
	print "Harry is excited, but you remind him that you must figure out what Snape is up to in the forbidden forest. ",
	print "You guys continue your path toward the forest when you see Snape emerge."
	answer = response()
	while answer != "expelliarmus" and answer != "Expelliarmus":
		message = random.randrange(1,4)
		if message == 1:
			print "Hermione says, \"Quick, you should disarm him!\""
		elif message == 2:
			print "Ron says, \"Oh no it's Snape! Do something!\""
		elif message == 3:
			print "Harry says, \"Watch out, Snape is coming toward you!\""
		answer = response()
	print "You have disarmed Snape, but you see another figure approaching from behind him."
	print "Harry exclaims, \"Sirius! What are you doing here?!\""
	print "Sirius responds, \"I've come to see you for your surprise party of course. Severus here was helping me to ",
	print "make my transformation. I still have to travel discretely."
	print "So Snape was doing good after all. You and your new friends enjoyed the rest of the night at Harry's surprise party. ",
	print "There were even fireworks!"


def library_():
		print "Ron groans, \"Aww that's my least favorite place.\""
		print "\"Understandable for someone who can't read Ronald.\" chimes Hermione."
		print "The four of you head to the library. When you get there, you come across a section that looks ",
		print "closed off and has a sign that reads \'Restricted\'."
		print "Harry asks you, \"Should we go in there?\""
		answer = response()
		if "eah" not in answer and "es" not in answer and "ure" not in answer and "ok" not in answer:
			print "Are you sure you don't want to continue your adventure?"
			answer = response()
			if "es" in answer or "eah" in answer:
				print "Hermione decides to sit down and start reading. You decide to join her. ",
				print "You pick up a book with an interesting cover and start to read it. The story is about ",
				print "a boy who discovers he's a wizard. You have decided to abandon your adventure and continue ",
				print "reading this encapsulating book."
			else:
				print "Hermione says, \"Come on let's go in!\""
		print "You enter into the restricted section, which is surprisingly easy to get into. ",
		print "You start to look around and notice that a book is out of place."
		answer = response()
		if "ick" not in answer and "ead" not in answer and "rab" not in answer:
			print "Hermione says, \"This book looks very suspicious, do you think we should open it?\""
			answer = response()
			if "yea" not in answer and "es" not in answer:	
				print "Hermione picks up the book anyway because she never really cared about you opinion in the first place"
		print "As you examine the book, you see that it is a book on pyrotechnics. Ron starts to look through it. ",
		print "As he opens the pages, a note slips out."
		answer = response()
		while "ead" not in answer and "ote" not in answer:
			print "Harry says, \"Well go on, read it.\""
			answer = response()
		print "You pick up the note and unfold it. It is a blank sheet of paper."
		answer = response()
		while "revelio" not in answer:
			print "Ron says, \"Maybe it's message is hidden. Do you have any spells for that?\""
			answer = response()
		print"A message appears. It reads: \"Sundown, 1st September, Hagrid's.\""	
		print "Ron gasps, \"September first, but that's today!\""
		print "Harry says, \"I think someone's going after hagrid.. We need to go and stop them!\""
		print "You and the gang head outside to Hagrid's hut. Darkness has just fallen. As you approach the hut, ",
		print "you hear a loud explosion. Harry jumps and drops his glasses."
		print "Harry says, \"Oh no! They've broken!\""
		answer = response()
		while  answer != "reparo" and answer != "Reparo":
			print "Hermione says, \"You should help Harry fix his glasses.\""
			answer = response()
		print "Harry says, \"Thanks!\""
		print "As you go closer to Hagrid's hut, you see that the explosions are just fireworks."
		print "You hear someone moving around in the distance but it's too dark to see anyone."
		answer = response()
		while answer != "lumos" and answer != "Lumos":
			if answer == "incendio" or answer == "incendio":
				print "Harry says, \"Let's not start a fire, maybe just some light?\""
			else:
				message = random.randrange(1,3)
				if message == 1:
					print "Hermione says, \"I can't see a thing!\""
				elif message == 2:
					print "Ron says, \"Can someone please make some light or something?\""
			answer = response()
		print "You can now see the figure of a large person."
		print "Hagrid shouts, \"Surprise!!!\""
		print "The four of you are startled. You see familiar figures start to appear, including Dumbledore, Snape, Neville, and Luna."
		print "Hagrid approaches Harry: \"Happy Birthday Harry! I know it's a little late but I wanted to make sure you got a proper celebration."
		print "Everything becomes clear to you now that for once, this might be a normal year of school."


def common_room():
	print "Hermione says, \"Let's show you the Gryffindor common room!\""
	print "The four of you approach a vast stairway. You ascend one of the flights and stop at a painting of a fat lady."
	print "Ron says, \"The password is fortuna major. Try it if you want to go in!\""
	answer = response()
	while answer != "fortuna major":
		print "Hermione says, \"That's not the password.\""
		answer = response()
	print "The painting opens into an entryway that leads you to the common room. ",
	print "You look around the room and see a fire burning in the fireplace, a large bookshelf, and a large and comfortable seeming couch ",	
	print "with a backpack resting on it."
	search = True
	answer = response()
	while search:
		if "ire" in answer or "lace" in answer:
			print "There is one log in the fireplace but it does not appear to be burning. There is also a piece of paper in the fire."
			answer = response()
			while answer != "accio":
				print "Harry says, \"You should get that paper out of the fire and read it!\""
				answer = response()
				print "You pick up the note, it is half burned, but you can make out a few words: hut, Thursday, secret."
				print "Ron says, \"Thursday, that's today! I think it is referring to Hagrid's hut?\""
				print "Hermione says, \"Brilliant Ronald, I think you're right.\""
				search = False
		elif "ook" in answer or "helf" in answer:
			print "You see many books about potions and spells that haven't been touched in years. There are also many ",
			print "children's tales on the bottom shelf."
			print "Harry says, \"You can read some of those books later. Let's check out who this backpack belongs to!"
			backpack()
			search = False
		elif "ack" in answer:
			backpack()
			search = False
		else:
			print "Try exploring the room."
			answer = response()
	print "The four of you head down to Hagrid's hut. It has gotten darker outside. As you approach, you see Neville."
	print "Neville says, \"Harry you're early! Well, Surprise!\""
	print "He raised his wand in an attempt to make sparks appear, but instead, a fire erupted."
	answer = response()
	while answer != "aguamenti":
		message = random.randrange(1,4)
		if message == 1:
			print "Hermione says, \"Quick, do something!\""
		elif message == 2:
			print "Neville shouts, \"Help, my wand's on fire!\""
		elif message == 3:
			print "Ron says, \"Someone do something!\""
		answer = response()
	print "Neville says, \"Thank you so much, you saved my wand! What are you guys doing here so early?\""
	print "Harry says, \"Neville, exactly what is going on here?\""
	print "Neville responds, \"Well it's a surprise party for you of course, because we didn't get a chance to celebrate your ",
	print "birthday with you.\""
	print "Harry is touched by this. More familiar faces start to appear, there are even real fireworks. You enjoy the rest of the ",
	print "evening with your new friends."


def backpack():
	print "The backpack looks old and worn down."
	print "Harry says, \"The bag is already open, we might as well look inside.\""
	print "The bag contains a planner, a small box that is gift wrapped, a remembrall that is glowing red."
	print "Hermione says, \"I think that's Neville's backpack. What good is his remembrall if it's the very thing that he forgot.\""
	print "Ron says, \"We should look in his planner to see where he is so we can give it back to him\""
	print "The planner is locked."
	answer = response()
	while answer != "alohomora":
		print "Hermione says, \"I know it seems wrong, but we should unlock it.\""
		answer = response()
	print "You open the planner to today's date. On his agenda, Neville has \'Hagrid's\' written in the slot for 7:00\""
	print "Harry says, \"Very curious. We need to go to Hagrid's and see what Neville is up to.\""


def chamber_of_secrets(): #done
		print "Hermione says, \"Actually, they sealed off the chamber of secrets after Harry fought off Tom Riddle there.\""

def courtyard(): #done
		print "Ron says, \"There's nothing to explore in the courtyard, let's try somewhere else!\""

def dumbledores_office(): #done
		print "Harry says, \"I don't think Professor Dumbledore wants to be bothered right now.\""

def hagrids_hut(): #done
		print "Harry says, \"I don't think Hagrid's home right now.  Maybe we can try him later.\""

def forbidden_forest(): #done
		print "Harry says, \"I don't want to disturb any of the creatures there.\""

def quidditch(): #done
		print "Harry says, \"I believe Hufflepuff is practicing there right now, maybe we can go there later.\""

def room_requirement():
		print "hi"

def explore(Gryffindor):

	print "Perfect timing, here comes Harry and the gang!"
	print "What part of the castle should we explore first?"
	part = response()
	good = True
	while good:
		if "ungeon" in part or "basement" in part:
			dungeon()
			part = response()
		elif "reat" in part or "hall" in part or "ining" in part:
			great_hall()
			good = False
		elif "ibrary" in part or "books" in part or "restricted" in part or "read" in part:
			library_()
			good = False
		elif "ommon" in part:
			if Gryffindor:
				common_room()
				good = False
			else:
				print "Hermione says, \"I'm afraid you cannot come into our commons because you are not a Gryffindor. ",
				print "Perhaps we should go somewhere where we can all explore.\""
				part = response()
		elif "hamber" in part or "ecrets" in part:
			chamber_of_secrets()
			good = False
		elif "ourt" in part or "outside" in part:
			courtyard()
			good = False
		elif "dumb" in part or "dore" in part or "office" in part:
			dumbledores_office()
			part = response()
			#good = False
		elif "hagrid" in part or "Hagrid" in part or "hut" in part:
			hagrids_hut()
			part = response()
			#good = False;
		elif "forb" in part or "Forb" in part or "orrest" in part or "forest" in part:
			forbidden_forest()
			part = response()
		elif "quid" in part or "Quid" in part or "stadium" in part or "field" in part:
			quidditch()
			part = response()
		elif "requ" in part or "Requi" in part or "oom of" in part:
			room_requirement()
			good = False
		elif "quit" == part or "Quit" == part:
			return 0 
		else:
			print "Harry says \"I don't think we can go to that part of the castle right now.", 
			print "Why don't you choose somewhere else like the library, Dumbledore's office, Hagrid's hut, or the Room of Requirement.\""
			part = response()

def addSpells(spells, newSpell):
	spells.append(newSpell)
def printSpells():
	spells = []
	addSpells(spells, ['SPELL:', 'FUNCTION:'])
	addSpells(spells, ['accio', 'summons an object'])
	addSpells(spells, ['aguamenti', 'produces water from the wand'])
	addSpells(spells, ['alohomora', 'unlocks and opens doors'])
	addSpells(spells, ['diffindo', 'cuts or rips things'])
	addSpells(spells, ['engorgio', 'causes an object to grow'])
	addSpells(spells, ['episkey', 'heals minor injuries'])
	addSpells(spells, ['expelliarmus', 'disarms another wizard'])
	addSpells(spells, ['incendio', 'produces fire'])
	addSpells(spells, ['lumos', 'produces light from the wand'])
	addSpells(spells, ['reducio', 'makes an object smaller'])
	addSpells(spells, ['reparo', 'repairs broken objects'])
	addSpells(spells, ['silencio', 'silences something'])
	addSpells(spells, ['specialis revelio', 'shows an objects\' hidden properties'])
	for spell in spells:
		print '{0:4s}{1:20s}{2:8s}'.format(' ', spell[0], spell[1]) 

def main(argv):
	print "Hello and welcome to Hogwarts!"
	print "If it ever seems like nothing is happening, try typing in some relevant input! ",
	print "If at any point you want to leave your adventure, just type \'quit\'."
	print "Now we will place you in your house by use of the sorting hat."
	Gryffindor = sortingHat()
	print "Professor McGonagall hands you a book of spells, you should familiarize yourself with these spells."
	print "After you get settled in and learn your spells, you should go explore the castle with your new friends, Harry, Hermione, and Ron."
	printSpells()

	print "Say \"explore\" whenever you're ready!"
	enter = raw_input()
	if enter == "explore":
		explore(Gryffindor)






if __name__ == "__main__":
    main(sys.argv)

