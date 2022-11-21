def jerigonzo(string):
    string = string.lower()
    con_a = string.replace("a", "apa")
    con_e = con_a.replace("e", "epe")
    con_i = con_e.replace("i", "ipi")
    con_o = con_i.replace("o", "opo")
    con_u = con_o.replace("u", "upu")
    string = con_u
    return string
