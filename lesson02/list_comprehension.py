""" a lil bit lesser code of solving 1 task in cw02.py"""

st = 'as 23 fdfdg544'
dict_of_st = {}
list_of_st = [dict_of_st.update({i: st.count(i)}) for i in st]
for k, v in dict_of_st.items():
    print(f"'{k}' -> {v}")
