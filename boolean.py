print "Type 't' for True or 'f' for False."

def ask(question, answer):
	
	while True:	
		print question
		ans = raw_input("> ")
		if ans == "t":
			ans = "True"
			break
					
		elif ans == "f":
			ans = "False"
			break
			
		else:
			print "Please type 't' for True or 'f' for False"
				
	if ans == answer:
		print "CORRECT, %r is %s.\n" % (question, answer)
		
	else:
		print "WRONG, %r is %s.\n" % (question, answer)
		
ask("not False", "True")
ask("not True", "False")
ask("True or False", "True")
ask("True or True", "True")
ask("False or True", "True")
ask("False or False", "False")
ask("True and False", "False")
ask("True and True", "True")
ask("False and True", "False")
ask("False and False", "False")
ask("not (True or False)", "False")
ask("not (True or True)", "False")
ask("not (False or True)", "False")
ask("not (False or False)", "True")
ask("not (True and False)", "True")
ask("not (True and True)", "False")
ask("not (False and True)", "True")
ask("not (False and False )", "True")
ask("1 != 0", "True")
ask("1 != 1", "False")
ask("0 != 1", "True")
ask("0 != 0", "False")
ask("1 == 0", "False")
ask("1 == 1", "True")
ask("0 == 1", "False")
ask("0 == 0", "True")
