quiet = False

def toggle():
    global quiet
    if quiet:
        quiet = False
    else:
        quiet = True

toggle()
print(quiet)
toggle()
print(quiet)
