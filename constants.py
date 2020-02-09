import datetime

# 오늘 무슨 조인지
start_2020_01_01_B = datetime.datetime(2020, 1, 1)  # 1월 1일 근무조
today = datetime.datetime(2020, 2, 7)  # 오늘 날짜
which_group = ((today - start_2020_01_01_B).days + 1) % 3  # 나머지 0이면 A, 1이면 B, 2이면 C
work_group = {0: 'A', 1: 'B', 2: 'C'}  # workgroup 에 which_group을 대입하면 오늘 무슨 조인지 문자로 파악 가능
is_weekend = int(today.weekday() / 5) + 1  # 오늘 주말인지 아닌지 1이면 평일, 2이면 주말

# 근무 시간, 타수
TimeA = [6, 4, 8, 12]
WorkA = [7, 11, 8, 6]
WorkA_weekend = [6, 8, 7, 6]

TimeB = [8, 12, 2, 4]
WorkB = [11, 11, 6, 6]
WorkB_weekend = [8, 8, 6, 6]

TimeC = [10, 2, 6, 22]
WorkC = [11, 11, 11, 6]
WorkC_weekend = [8, 8, 7, 6]

Timetable = [[TimeA, WorkA, WorkA_weekend],
             [TimeB, WorkB, WorkB_weekend],
             [TimeC, WorkC, WorkC_weekend]]  # 배열로 묶어서 저장

placeA = [[2, 2, 2, 1], [5, 3, 2, 1], [3, 2, 2, 1], [2, 2, 1, 1]]  # 정출, 별정, 별후, 서남문 순서
placeB = [[5, 3, 2, 1], [5, 3, 2, 1], [2, 2, 1, 1], [2, 2, 1, 1]]
placeC = [[5, 3, 2, 1], [5, 3, 2, 1], [5, 3, 2, 1], [2, 2, 1, 1]]

placeA_weekend = [[2, 2, 1, 1], [3, 2, 2, 1], [2, 2, 2, 1], [2, 2, 1, 1]]
placeB_weekend = [[3, 2, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [2, 2, 1, 1]]
placeC_weekend = [[3, 2, 2, 1], [3, 2, 2, 1], [2, 2, 2, 1], [2, 2, 1, 1]]

placetable = [[placeA, placeA_weekend],
              [placeB, placeB_weekend],
              [placeC, placeC_weekend]]


# 선호 근무 조사
class fav:
    def __init__(self, name, t3=[], t2=[]):
        self.name = name
        self.times3 = {'A': t3[0], 'B': t3[1], 'C': t3[2]}
        self.times2 = {'A': t2[0], 'B': t2[1], 'C': t2[2]}
        self.wheres_he = [0, 0, 0, 0]
        self.work = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def __str__(self):
        return self.name

# 2분대 사람들 공백 차례로 1, 2, 3, 4분대
a1 = fav('김호송', [[6, 4, 8], [8, 12, 4], [10, 6, 22]], [[6, 8], [8, 4], [2, 22]])
a2 = fav('김수현', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[4, 8], [8, 2], [10, 2]])
a3 = fav('고동욱', [[6, 4, 8], [8, 12, 4], [2, 6, 22]], [[6, 8], [8, 4], [2, 22]])
a4 = fav('이민혁', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 4], [8, 2], [10, 2]])
a5 = fav('김건웅', [[6, 8, 12], [8, 12, 2], [10, 6, 22]], [[6, 8], [12, 2], [6, 22]])

a6 = fav('한종수', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 8], [8, 2], [10, 6]])
a7 = fav('김주환', [[6, 4, 8], [8, 12, 4], [10, 2, 6]], [[6, 4], [8, 4], [10, 2]])
a8 = fav('하석준', [[6, 8, 12], [8, 12, 4], [2, 6, 22]], [[6, 8], [12, 4], [2, 22]])
a9 = fav('이정찬', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 4], [8, 2], [6, 22]])
a10 = fav('연상헌', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 4], [8, 2], [10, 2]])

a11 = fav('유재열', [[6, 4, 8], [8, 12, 2], [10, 2, 22]], [[6, 8], [8, 2], [10, 22]])
a12 = fav('박준규', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 4], [8, 2], [10, 2]])
a13 = fav('안창원', [[6, 8, 12], [8, 12, 4], [2, 6, 22]], [[8, 12], [12, 2], [2, 22]])
a14 = fav('이기훈', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 4], [8, 2], [10, 2]])
a15 = fav('이승빈', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 4], [8, 2], [10, 2]])
a16 = fav('이유준', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 4], [8, 2], [10, 2]])

a17 = fav('유준상', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 4], [12, 2], [10, 2]])
a18 = fav('전명재', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[6, 4], [8, 2], [10, 2]])
a19 = fav('김홍익', [[6, 4, 8], [8, 12, 2], [10, 2, 6]], [[4, 8], [8, 2], [10, 2]])
a20 = fav('최정우', [[6, 4, 8], [8, 12, 2], [10, 2, 22]], [[6, 8], [12, 2], [10, 2]])
a21 = fav('최의현', [[6, 4, 8], [8, 12, 2], [10, 2, 22]], [[6, 8], [8, 2], [6, 22]])

bundae = [5, 5, 6, 5]
p2 = [a1, a2, a3, a4, a5, a6, a7, a8,
      a9, a10, a11, a12, a13, a14, a15,
      a16, a17, a18, a19, a20, a21]