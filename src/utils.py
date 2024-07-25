def printf(lines, text, newlines = 0, prenewl = 0):
    for i in range(prenewl):
        lines.append("")
    lines.append(text)
    for i in range(newlines):
        lines.append("")

def draw_new_line(lines, cmd, running_cmd):
    lines.pop()
    if running_cmd:
        printf(lines, "> " + cmd)
    else:
        printf(lines, "> " + cmd + "_")

def get_user():
    with open("user.txt") as data:
        lines = data.readline(-1)
        return lines.split(";")[0]
    
def get_name():
    with open("user.txt") as data:
        lines = data.readline(-1)
        return lines.split(";")[1]