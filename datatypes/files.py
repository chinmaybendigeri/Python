with open("C:\\Users\\Vivek\\PycharmProjects\\PythonTutorials\\resources\\input.txt","a") as f:
    f.write("this is fifth line")

with open("C:\\Users\\Vivek\\PycharmProjects\\PythonTutorials\\resources\\input.txt", "r") as fr:
    contents = fr.readlines()
print(contents)