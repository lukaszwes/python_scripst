import xlwt
import xlrd



book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Faktury")
sheet2 = book.add_sheet("Klienci")

sheet1.write(0,0, "Lp")
sheet1.write(1,0, "1")
sheet1.write(2,0, "2")
sheet1.write(0,1, "Numer")
sheet1.write(1,1, "FW-101")
sheet1.write(2,1, "FW-102")
sheet1.write(0,2, "Cena")
sheet1.write(1,2, "3000")
sheet1.write(2,2, "4000")

sheet2.write(0,0, "Lp")
sheet2.write(1,0, "1")
sheet2.write(2,0, "2")
sheet2.write(0,1, "Imie")
sheet2.write(1,1, "Adam")
sheet2.write(2,1, "Kamil")
sheet2.write(0,2, "Nazwisko")
sheet2.write(1,2, "Malysz")
sheet2.write(2,2, "Stoch")



book.save("tabela1.xls")
