subject = ["國文","英文","微積分","體育","程式設計"]
score = []
for i in range(5):
    score.append(int(input(subject[i]+":")))
    a=(sum(score)/5)
print("平均分數：%.2f"%a)
print()
print("最高分科目："+subject[score.index(max(score))],max(score),"分")
print()
print("最低分科目："+subject[score.index(min(score))],min(score),"分")