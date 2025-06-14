with open("results.txt", "r") as file:
    file_content = file.readlines()
total_result = []
b_mas = []
for line in file_content:
    a, b = line.split()
    result1, result2 = b.split(":")
    if result1 == result2:
        res = str(line.strip()) +" "+ str(b_mas[-2:][-1])+" "
        if len(b_mas) >1:
            res+=str(b_mas[-2:][-2])
        total_result.append(res)

    b_mas.append(b)
with open("sample.txt", "w") as outfile:
    for item in total_result:
        if isinstance(item, list):
            outfile.write(" ".join(item) + "\n")
        else:
            outfile.write(item + "\n")

