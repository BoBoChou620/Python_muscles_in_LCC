st = """There are moments in life when you miss someone so much that
you just want to pick them from your dreams and hug them for real! Dream what
you want to dream;go where you want to go;be what you want to be,because you have
only one life and one chance to do all the things you want to do"""

X = st.count("to")
print("to 的次數有：%d 次" % X)
print("第一次出現位置：%d" % st.find("want"))
print("最後一次出現位置：%d" % st.rfind("want"))
print("兩字之間的字串：" + st[70:279])