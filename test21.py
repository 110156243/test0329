id=['123','456','789','321','654']
name=['Tom','Cat','Nana','Lim','Won']
series=['DTGD','CSIE','ASIE','DBA','FDD']
a=input('輸入查詢學號為:')
b=id.index(a)
print('學生資料為:'+a+' '+name[b]+' '+series[b])