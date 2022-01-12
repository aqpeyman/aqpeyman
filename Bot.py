
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler,Filters
import random

updater=Updater('5034840682:AAEPQ2dkWrU2ANCa8VDxs4XxOaAidWtuWbU', use_context=True)



def nato ( update , context):
	d= ["nato","godfader","karagah","takavar","negahban","gerogangir","doctor","shahrvand","shahrvand","Tofangdar"]	
	a= random.sample(d,len(d))
	b=('\n'.join(f'{i} {j}'for i, j in enumerate(a,start=1)))
	update.message.reply_text(b)
	
	
def natasha ( update , context):
	d= ["natasha","godfader","karagah","sniper","keshish","teror","doctor","shahrvand","shahrvand","Tofangdar", "kharbkar","ghazi"]
	a= random.sample(d,len(d))
	b=('\n'.join(f'{i} {j}'for i, j in enumerate(a,start=1)))
	update.message.reply_text(b)
	
	
def mason ( update , context):
	d= ["mason","tiler","godfader","farmandeh","sniper","keshish","teror","doctor","natasha","Tofangdar", "kharbkar","ghazi","saghi","jasos","mohafez"]
	a= random.sample(d,len(d))
	b=('\n'.join(f'{i} {j}'for i, j in enumerate(a,start=1)))
	update.message.reply_text(b)
	
	

def dozd ( update , context):
	d= ["kaboy","neghban","godfader","farmandeh","sniper","saghi","ridler","doctor","teror","Tofangdar", "kharbkar","ghazi","saghi","dozd","mohafez"]
	a= random.sample(d,len(d))
	b=('\n'.join(f'{i} {j}'for i, j in enumerate(a,start=1)))
	update.message.reply_text(b)
	
		
def karoler ( update , context):
	d= ["karoler","antilady","godfader","farmandeh","sniper","ladyvodo","teror","doctor","shahrvand","Tofangdar", "kharbkar","ghazi","mohafez"]
	a= random.sample(d,len(d))
	b=('\n'.join(f'{i} {j}'for i, j in enumerate(a,start=1)))
	update.message.reply_text(b)




dp = updater.dispatcher
dp.add_handler(CommandHandler("nato", nato))
dp.add_handler(CommandHandler("natasha", natasha))
dp.add_handler(CommandHandler("mason", mason))
dp.add_handler(CommandHandler("dozd", dozd))
dp.add_handler(CommandHandler("karoler", karoler))





updater.start_polling()
updater.idle()
