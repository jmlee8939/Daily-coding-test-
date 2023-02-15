import sys

def binary_search(target, data):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True, mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return False, start

def binary_search2(target, data):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start + end) // 2

        if data[mid].name == target:
            return True, mid
        elif data[mid].name < target:
            start = mid + 1
        else:
            end = mid -1

    return False, start

class album:
    def __init__(self, name, prev_album=None):
        self.name = name
        self.albums = []
        self.pictures = []
        self.prev_al = prev_album


    def mkalb(self, S):
        search = binary_search2(S, self.albums)
        if search[0] == True:
            print("duplicated album name")
        else:
            self.albums.insert(search[1], (album(S, self)))

    def rmalb(self, S):
        if len(self.albums) == 0:
            print(0, 0)
            return

        elif S == '-1':
            tt_alb = self.albums.pop(0)
            n_alb, n_pic = tt_alb.alb_clear()
            n_alb += 1
            print(n_alb, n_pic)

        elif S == '0':
            n_alb, n_pic = len(self.albums), 0
            for i in self.albums:
                t_alb, t_pic = i.alb_clear()
                n_alb += t_alb
                n_pic += t_pic
            print(n_alb, n_pic)
            self.albums = []

        elif S == '1':
            tt_alb = self.albums.pop()
            n_alb, n_pic = tt_alb.alb_clear()
            n_alb += 1
            print(n_alb, n_pic)

        else:
            flag = 0
            for i in self.albums:
                if i.name == S:
                    n_alb, n_pic = i.alb_clear()
                    n_alb += 1
                    print(n_alb, n_pic)
                    flag = 1
            if flag == 0:
                print(0, 0)
            self.albums = [i for i in self.albums if i.name != S]

    def insert(self, S):
        search = binary_search(S, self.pictures)
        if search[0] == True:
            print("duplicated photo name")
        else:
            self.pictures.insert(search[1], S)

    def delete(self, S):
        if len(self.pictures) == 0:
            print(0)
            return

        if S == '-1':
            self.pictures.pop(0)
            print(1)

        elif S == '0':
            print(len(self.pictures))
            self.pictures = []

        elif S == '1':
            self.pictures.pop()
            print(1)

        else:
            if S in self.pictures:
                self.pictures.remove(S)
                print(1)
            else:
                print(0)

        return

    def alb_clear(self):
        alb_n = len(self.albums)
        pic_n = len(self.pictures)
        for i in self.albums:
            t_alb, t_pic = i.alb_clear()
            alb_n += t_alb
            pic_n += t_pic
        return alb_n, pic_n

main_alb = album('album')
now = main_alb

N = int(input())
for _ in range(N):
    func, S = sys.stdin.readline().rstrip().split()

    if func == 'mkalb':
        now.mkalb(S)
    elif func == 'ca':
        if S == '..':
            if now.prev_al != None:
                now = now.prev_al
            else:
                pass
        elif S == '/':
            while now.prev_al != None:
                now = now.prev_al
        else:
            for ab in now.albums:
                if ab.name == S:
                    now = ab
        print(now.name)
    elif func == 'insert':
        now.insert(S)
    elif func == 'delete':
        now.delete(S)
    elif func == 'rmalb':
        now.rmalb(S)
