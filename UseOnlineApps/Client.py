import requests,time
print("Client started!")
print("Disclaimer: All the files you download can do what they want! Be careful!")

jaj = input("Enter website: ")
page = input("Enter Page (standart: getApp): ")

if page == "": page = "getApp"
try:
        resp = requests.get(f"http://{jaj}/{page}",timeout=(10,30))
        result = resp.text
        exec(result)
        try:
                print("Program is end. Program will end after 15 seconds(or you can use Ctrl+C)")
                time.sleep(15)
                exit()
        except: exit()
except requests.exceptions.ConnectionError:
        print("Cant load website! Check website and page correct! (If you are an admin, check is the server is enabled.)")
        while True: pass
except requests.exceptions.Timeout:
        print("Timeout!")
        print("Press  Ctrl+C for exit!")
        while True: pass
except KeyboardInterrupt: exit()
