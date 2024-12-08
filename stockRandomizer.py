import smtplib, ssl
import random
from datetime import date

ticker = ['IBM','XOM','CVX','PG','MMM','JNJ','MCD','WMT',
        'UTX','KO','BA','CAT','JPM','HPQ','VZ','T',
        'KFT','DD','MRK','DIS','HD','MSFT','AXP','BAC',
        'PFE','GE','INTC','AA','C','GM']

stockpick = random.choice(ticker)

print (stockpick)
#  erikjeggedev@gmail.com
#  arfmeyctpqjhqtan

# port = 465  # For SSL
# password = 'arfmeyctpqjhqtan'
# sender_email = "erikjeggedev@gmail.com"
# receiver_email = "erikjegge@gmail.com" 
# message = """\
# Subject: Stock Pick %s

# Today's stock pick: %s

# This message is sent from Python.""" % (date.today(), stockpick)

# # Create a secure SSL context
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)