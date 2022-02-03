def send_email1(name,email):
    import smtplib
    from string import Template#allows for subtitution
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage

    
    
    
    def template_reader(filename):
        with open(filename,'r',encoding='utf-8') as file:
            draft=file.read()
            return Template(draft)
        
        
    template_content=template_reader("client.txt")
    password="***********"
    from_email="***********@gmail.com"
    to_email=email
    subject="Thank you for contacting Hackman & CO Chartered Certified Accountancy "
    gmail=smtplib.SMTP(host="smtp.gmail.com",port=587)
    gmail.starttls()
    gmail.login(from_email,password)
    msg=MIMEMultipart()
    message=template_content.substitute(NAME=name)
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    msg.attach(MIMEText(message,'plain'))
    
   
    gmail.send_message(msg)
    gmail.quit()
























        


