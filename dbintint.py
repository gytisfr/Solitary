import dbint

currin = dbint.currin
payload = dbint.payload

#dbint.createdb()



while True:
    choice = input("What:").lower()
    if choice in ["x", "currin", "payload"]:
        if choice == "x":
            exit()
        elif choice == "currin":
            choice2 = input("What2:").lower()
            if choice2 in ["insert", "update", "remove", "get", "fetch", "check"]:
                if choice2 == "insert":
                    userid = input("Userid:")
                    time = input("Time:")
                    ret = dbint.currin.insert(userid, time)
                if choice2 == "update":
                    userid = input("Userid:")
                    time = input("Time:")
                    dbint.currin.update(userid, time)
                if choice2 == "remove":
                    userid = input("Userid:")
                    dbint.currin.remove(userid)
                if choice2 == "fetch":
                    ret = dbint.currin.fetch()
                    print(ret)
                if choice2 == "get":
                    userid = input("Userid:")
                    ret = dbint.currin.get(userid)
                    print(ret)
                if choice2 == "check":
                    userid = input("Userid:")
                    ret = dbint.currin.check(userid)
                    print(ret)
        elif choice == "payload":
            pass