# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
import re
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#print(email_three)
def strip_phrase(email):
    return email.replace("learning algorithms", "[CLASSIFIED]")

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", " her ", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
def cato(lst, mail):
    for i in lst:
      #mail = mail.replace(i.casefold(), "[REDACTED]")
      mail = re.sub(i, '[REDACTED]', mail)
    return mail
#print(cato(proprietary_terms, email_two))

test = email_three.lower().split()
lst_mail = [i.strip(",").strip(".") for i in test]
#counter = 0
#for i in negative_words:
 #   counter += test.count(i)
  #  if counter >= 2:
   #     email_three = re.sub(i.casefold(), '****', email_three)
#print(counter)
#print(email_three)

nefas = []
nefas_title = []
for x in lst_mail:
    for i in negative_words:
        if x == i:
            nefas.append(x)
            nefas_title.append(x.title())
nefas_master = nefas + nefas_title
#counter = 0
#for i in nefas_master:
 #   counter += lst_mail.count(i)
  #  if counter >= 2:
   #     del nefas[0]
#for i in nefas:
 #   email_three = re.sub(i.casefold(), '****', email_three)


print(nefas_master)
#print(email_three)
