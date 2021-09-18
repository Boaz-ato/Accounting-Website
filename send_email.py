def send_email(name,email,phone,enquiry):
    import smtplib
    from string import Template#allows for subtitution
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage

    
    
    
    def template_reader(filename):
        with open(filename,'r',encoding='utf-8') as file:
            draft=file.read()
            return Template(draft)
        
        
    template_content=template_reader("accountant.txt")
    password="jNCCZakJUb2v9P5"
    from_email="hackmanandco@gmail.com"
    to_email="boazmicah2@gmail.com"  #hackman email address for business
    subject="Enquiry from a potential client"
    gmail=smtplib.SMTP(host="smtp.gmail.com",port=587)
    gmail.starttls()
    gmail.login(from_email,password)
    msg=MIMEMultipart()
    message=template_content.substitute(NAME=name,EMAIL=email,PHONE=phone,ENQUIRY=enquiry)
    
       
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    msg.attach(MIMEText(message,'plain'))
    
    
    
    
    
   
    gmail.send_message(msg)
    gmail.quit()
    
   
 

#send_email("Boaz","boazmicah2@gmail.com","07469731604","I need money")






















        


