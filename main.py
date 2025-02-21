import fpdf, streamlit, pandas

pdf=fpdf.FPDF(orientation="p",unit="mm",format="A4")
pdf.add_page()
pdf.set_font(family="Times",style="B",size=12)#,style="B"
pdf.cell(w=0,h=12,txt="Hello I am Tullia",align="L",ln=1,border=0)
pdf.set_font(family="Times",size=10)
pdf.cell(w=0,h=12,txt="Hello I am Tullia",align="L",ln=1,border=0)


pdf.output("test.pdf")
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
