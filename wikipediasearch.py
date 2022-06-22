from takecmd import*
import wikipedia
import wolframalpha

def search(query):
    try:
        # create aapId on www.wolframalpha.com
        aap_id="EXYWGR-5XEUQ69KQ5"
        Client=wolframalpha.Client(aap_id)
        res=Client.query(query)
    
        ans=next(res.resluts).text
        Speak("According to Wolframalpha...")
        print(ans)
        Speak(ans)
    except:
        result=wikipedia.summary(query,sentences=10)
        Speak("According to wikipedia...")
        print(result)
        Speak(result)


# query=takecommand().lower()
# search(query)

