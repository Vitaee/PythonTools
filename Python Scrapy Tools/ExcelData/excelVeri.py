import matplotlib.pyplot as plt
import xlrd

never = []
often = []
sometimes = []
rarely = []
always = []

all_ans = []

loc = r"C:\Users\Teknoloji\PycharmProjects\Merhaba\Tools\veri.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)


i = 0
while i < 10: #tüm excel satırlarını al.
    for b in range(sheet.nrows):
        all_ans.append(sheet.cell_value(b,i+1))
    i += 1



while all_ans: #excel içeriğine göre listelere appendle.
    if "RARELY" in all_ans[0]:
        rarely.append(all_ans[0])
    elif "SOMETIMES" in all_ans[0]:
        sometimes.append(all_ans[0])
    elif "ALWAYS" in all_ans[0]:
        always.append(all_ans[0])
    elif "NEVER" in all_ans[0]:
        never.append(all_ans[0])
    elif "OFTEN" in all_ans[0]:
        often.append(all_ans[0])

    all_ans.pop(0)

left = [1, 2, 3, 4, 5]
height = [len(rarely), len(sometimes), len(always), len(never), len(often)]

tick_label = ['Rarely', 'Sometimes', 'Always', 'Never', 'Often']

plt.bar(left, height, tick_label=tick_label,
        width=0.6, color=['red', 'green'])

plt.xlabel('x - ekseni')
plt.ylabel('y - ekseni')

plt.title('Excel Veri Analizi')
plt.show()

#yüzdelik yazma 100*len(rarely) // 100