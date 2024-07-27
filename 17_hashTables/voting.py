voters = {}
def check_voter(name):
    if voters.get(name):
        print("sorry you have voted.")
    else:
        voters[name] = True
        print("Please vote...")

check_voter("iqbal")
check_voter("ali")
check_voter("ali")