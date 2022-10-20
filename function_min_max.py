tist = ["Rishav","Gaurav","Sarad","Arnav","Praveen"]
max_len = 0
result = ""
for gist in tist:
    print(f"current member name : {gist} || length of the member name : {len(gist)}")
    if len(gist) > max_len:
        max_len = len(gist)
        result = gist
print(f"MAXIMUM LENGTH : {max_len} | NAME : {result}")
print(f"MINIMUM LENGTH : {len(tist)} | NAME :  {min(tist)}")