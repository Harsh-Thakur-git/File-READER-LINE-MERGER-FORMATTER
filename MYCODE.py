path_Domain = "D:\\working\\Input\\"
pro_Domain = "D:\\working\\Process\\"
dist_Domain = "D:\\working\\Output\\"
def output_one(statement1, statement2, counter, filename):
    output_path = dist_Domain + filename + ".txt"
    with open(output_path, 'a') as outputfile:
        outputfile.writelines("<doctypehtml" + counter + ">" + "\n" + "<html>" + "\n" + "<body>" + "\n" + statement1)
        if count < 100:
            outputfile.writelines('\n' + statement2 + "</body>" + "\n" + "</html>" + "\n")
        else:
            outputfile.writelines('\n' + statement2 + "</body>" + "\n" + "</html>")

    return


def output_two(p1, p2, statement2, counter, filename):
    output_path = dist_Domain + filename + ".txt"
    with open(output_path, 'a') as outputfile:
        outputfile.writelines("<doctypehtml" + counter + ">" + "\n" + "<html>" + "\n" + "<body>" + "\n" + p1 + '\n' + p2)
        if count < 100:
            outputfile.writelines('\n' + statement2 + "</body>" + "\n" + "</html>" + "\n")
        else:
            outputfile.writelines('\n' + statement2 + "</body>" + "\n" + "</html>")
    return

def upper_h(statement1, statement2, c, filename):
    counter = 0
    wrd_count = 0
    flag = False
    locate = 0
    for i in statement1:
        if counter > len(statement1):
            break
        if i.isupper():
            flag = True
        if not flag:
            locate = counter
        if flag:
            wrd_count += 1
        counter += 1
    if wrd_count > 3:
        a1 = line1[0:locate+1]
        a2 = line1[locate+1:]
        output_two(a1, a2, statement2, c, filename)
    else:
        output_one(line1, statement2, c, filename)
    return

def lower_h(statement1, statement2, c, filename):
    counter = 0
    wrd_count = 0
    flag = False
    locate = 0
    lower_flow = False
    for i in statement1:
        if counter > len(statement1):
            break
        if i.islower():
            flag = True
        if not flag:
            lower_flow = False
            locate = counter
        if flag:
            lower_flow = True
            wrd_count += 1
        if i.isnumeric():
            lower_flow = False
            wrd_count = 0
            locate = counter
        counter += 1
    if wrd_count > 3 and lower_flow:
        a1 = line1[0:locate + 1]
        a2 = line1[locate + 1:]
        output_two(a1, a2, statement2, c, filename)
    else:
        output_one(line1, statement2, c, filename)
    return


print("#"*20+"\n")
print("#"*20+"\n")
print("#"*20+"\n")
y = int(input("Press  1 ---> MultiFile MODE OR 0---> SingleFile MODE \n\n"))
print("\n"+"#"*20+"\n")
print("#"*20+"\n")
print("#"*20+"\n")
if y == 1:
    s = int(input("Starting file name\n"))
    e = int(input("\nEnding file name\n"))
    file_name_list = list(range(s, e + 1))
    from linecache import getline
    for name in file_name_list:
        file_name = str(name)
        Input_path = path_Domain + file_name + ".txt"
        # making empty line removed
        with open(Input_path, 'r+') as fd:
            lines = fd.readlines()
            fd.seek(0)
            fd.writelines(line for line in lines if line.strip())
            fd.truncate()
        with open(Input_path, "r") as fp:
            count = 1
            while True:
                if count <= 100:
                    pass
                else:
                    break
                # GOT THE LINES HERE
                from linecache import getline

                line1 = getline(Input_path, count)
                line1 = line1.rstrip("\n")
                line2 = getline(Input_path, count + 100)
                # LETS USE THESE VALUES NOW
                if line1.isnumeric():
                    output_one(line1, line2, str(count), file_name)
                elif any(x.isupper() for x in line1):
                    upper_h(line1, line2, str(count), file_name)
                else:
                    lower_h(line1, line2, str(count), file_name)
                count += 1
else:
    print("WRONG INPUT")
    exit()




