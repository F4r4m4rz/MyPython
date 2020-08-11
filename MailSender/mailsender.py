

def mailTest():
    SERVER = "smtp-mail.outlook.com"
    FROM = "faramarz.bodaghi@outlook.com"
    TO = ["bodaghi_faramarz@yahoo.com"] # must be a list

    SUBJECT = "First mail"
    TEXT = "this is a text"

    # Prepare actual message
    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\
    Hello world
    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    import smtplib
    server = smtplib.SMTP(SERVER, 587)
    server.starttls()
    server.login("faramarz.bodaghi@outlook.com", "Far1898859AI")
    server.sendmail(FROM, TO, message)
    server.quit()

if __name__ == "__main__":
    mailTest()