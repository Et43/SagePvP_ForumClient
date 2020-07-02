#`
# Creator = <Et43>
# Name = <SagePvP Thread Watcher>
# 
#  `


from bs4 import BeautifulSoup
import requests
import time 
from win10toast import ToastNotifier

print("""

        |S|+|A|+|G|+|E| |F|+|O|+|R|+|U|+|M|
            C _ R _ A _ W _ L _ E _ R

    This little script will notify you when there
         is a new forum post on sagepvp.org

            By: Et43 ( African Gandalf )
            Sage PvP Discord: sagepvp.org/discord
            Sage PvP Website: sagepvp.org
            Sage PvP TeamSpeak: ts.sagepvp.org
            
""")


#############################################################################
#                                                                           #
#                           C.O.R.E A.P.L.I.C.A.T.I.O.N                     #
#                                                                           #
#############################################################################

toast = ToastNotifier()

def get_current_threads():

    page = requests.get("https://sagepvp.org/forum/")
    soup = BeautifulSoup(page.text, features="lxml")

    aot = soup.find("div", {"class": "contentRow"})
    nT = aot.find("div", {"class": "contentRow-main contentRow-main--close"})
    current_thread = nT.find("a").get_text()
	
    thread_document = open("thread.txt", "w")
    thread_document.write(current_thread)
    thread_document.close

def get_new_threads():
    page = requests.get("https://sagepvp.org/forum/")
    soup = BeautifulSoup(page.text, features="lxml")

    aot = soup.find("div", {"class": "contentRow"})
    nT = aot.find("div", {"class": "contentRow-main contentRow-main--close"})
    new_thread = nT.find("a").get_text()

    current_time = time.strftime("%H:%M:%S", time.gmtime())
    if new_thread == open("thread.txt").read():
        print("[" + current_time + "]" + " No new threads have been posted.")
    else:
        print("[" + current_time + "]" + " \u001b[31m ALERT!!! \u001b[0m --- New thread has been posted.")
        print(" ")
        print(" Thread Name: \u001b[36m " + new_thread + " \u001b[0m")
        toast.show_toast("NEW THREAD ALER!!!","New Thread Has Been Posted on SagePvP",duration=20)
    
def reset_text():
    file = open("thread.txt", "w")
    file.truncate(0)
    file.close

#############################################################################
#                                                                           #
#                           M.A.I.N L.O.O.P                                 #
#                                                                           #
#############################################################################

while True:
    # Get the current post name on sagepvp.org and write it to thread.txt
    get_current_threads()
    #Sleep to wait for updates
    time.sleep(300)
    # Check if the new name is the same to the one in the txt file.
    get_new_threads()
    # Put a small sleep here becuase i think i am mos poes cool
    time.sleep(2)
    # Clear everything in the txt file.
    reset_text()
    # EZ LOOOOOOOOOOOOOOOOOOOOOOP