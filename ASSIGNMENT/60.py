def start_process(p):
    if(p.upper()=="YES"):
        return "Start Process"
    elif(p.upper()=="No"):
        return "Start Process Aborted"
    else:
        return "Sorry wrong input"

print(start_process("yes"))
#Copyright @Amol Paliwal