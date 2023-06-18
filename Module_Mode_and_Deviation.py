import statistics as st

md = st.mode([10, 12, 20, 18, 16, 13, 16, 12, 17, 18, 14, 11])
sd = st.stdev([10, 12, 20, 18, 16, 13, 16, 12, 17, 18, 14, 11])
print("Mode: ", md)
print("Standard Deviation: ", format(sd, ".2f"))