import smtplib
alici = ["adres1@gmail.com","adres2@gmail.com"]
mailim = "16ebruarslan@gmail.com"
passwd = "parola"
topic = "mailin konusu"
mail = smtplib.SMTP("smtp.gmail.com",587)
#587 and 25 open property
mail.ehlo()
mail.starttls()
mail.login(mailim,passwd)

mail.sendmail(mailim,alici,topic)
print("işlem başarılı")
