import smtplib

# list of email_id to send the mail
li = ["atul.rai@bulkmro.com"]

for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("kishan.sampat@bulkmro.com", "adggrznvgohhwxmd")
    message = "Just a small check of SMTP sending to multiple recipents"
    s.sendmail("kishan.sampat@bulkmro.com", li[i], message)
    s.quit()


