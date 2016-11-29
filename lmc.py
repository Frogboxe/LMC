
class P:
    # Consts
    DBG = True
    ADDRESS_MAX = 10**3    -1
    MEMORY_MAX = 10**3     -1
    INPUT_MAX = 10**3      -1
    # Vars
    acc = 0
    pc = 0
    hlt = False
    tags = {}
    memory = {}
    scriptRaw = ""
    script = []

def CheckLoc(loc):
    loc = int(loc)
    if loc > P.ADDRESS_MAX:
        raise MemoryError("INSUFFICIENT MEMORY:: {} DOES NOT EXIST"
                          .format(str(loc)))
    return loc

def CheckVal(val):
    val = int(val)
    if val > P.MEMORY_MAX:
        raise ValueError("INSUFFICIENT SPACE:: {} TOO LARGE"
                         .format(str(val)))
    return val

def CheckScript(line):
    line = int(line)
    #if P.tags[line] > len(P.script)-1:
    #    raise MemoryError("INVALID LINE:: LINE {} DOES NOT EXIST"
    #                      .format(str(line)))
    return line

def CheckAcc():
    while P.acc > P.MEMORY_MAX:
        P.acc -= P.MEMORY_MAX + 1
    
def Inc():
    P.pc += 1

def INP():
    P.acc = CheckVal(input(""))
    CheckAcc()
    Inc()

def OUT():
    if P.DBG: print("OUT:: ", end="")
    print(P.acc)
    Inc()

def SET(val):
    P.acc = val
    Inc()

def STA(at):
    P.memory[at] = P.acc
    Inc()

def LDA(at):
    P.acc = P.memory[at]
    Inc()

def ADD(loc):
    P.acc += P.memory[loc]
    CheckAcc()
    Inc()

def SUB(loc):
    P.acc -= P.memory[loc]
    CheckAcc()
    Inc()

def GOTO(line):
    P.pc = P.tags[line]

def BRP(line):
    if P.acc >= 0:
        GOTO(line)
    else:
        Inc()
        
def BRZ(line):
    if P.acc == 0:
        GOTO(line)
    else:
        Inc()

def HLT():
    P.hlt = True

def ReadLine():
    line = P.script[CheckScript(P.pc)]
    cmd = line[0:3]
    arg = line[3::]
    if cmd == "INP":
        INP()
    elif cmd == "OUT":
        OUT()
    elif cmd == "SET":
        SET(CheckVal(arg))
    elif cmd == "STA":
        STA(CheckLoc(arg))
    elif cmd == "LDA":
        LDA(CheckLoc(arg))
    elif cmd == "ADD":
        ADD(CheckVal(arg))
    elif cmd == "SUB":
        SUB(CheckVal(arg))
    elif cmd == "BRA":
        GOTO(CheckScript(arg))
    elif cmd == "BRP":
        BRP(CheckScript(arg))
    elif cmd == "BRZ":
        BRZ(CheckScript(arg))
    elif cmd == "HLT":
        HLT()
    else:
        Inc()

def ParseTags():
    for line, pc in zip(P.script, range(len(P.script))):
        if line.isdecimal():
            P.tags[int(line[0:len(line)])] = pc
            
def Read():
    line = ""
    for char in P.scriptRaw:
        if char != ";":
            line += char
        else:
            P.script.append(line)
            line = ""
    ParseTags()
    while not P.hlt:
        ReadLine()

def DbgOut(mem):
    val = []
    tmp = []
    con = []
    for key in mem:
        if key > 80:
            con.append("{} = {}".format(key, mem[key]))
        elif key > 60:
            tmp.append("{} = {}".format(key, mem[key]))
        else:
            val.append("{} = {}".format(key, mem[key]))
    val, tmp, con = sorted(val), sorted(tmp), sorted(con)
    print("MAIN_VALUES:: " + str(val))
    print("TEMPORARY::   " + str(tmp))
    print("CONSTANTS::   " + str(con))

def Main(script):
    P.scriptRaw = script.replace("\n", "").replace(" ", "")
    Read()
    if P.DBG: DbgOut(P.memory)

Main("""


""")

