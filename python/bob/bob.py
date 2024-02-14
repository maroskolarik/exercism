def response(hey_bob):
    if hey_bob.isupper():
        if hey_bob[-1] == '?':
            return "Calm down, I know what I'm doing!"
        return 'Whoa, chill out!'
    if hey_bob.isspace() or hey_bob == '':
        return 'Fine. Be that way!'
    if hey_bob.strip()[-1] == '?':
        return 'Sure.'
    return 'Whatever.'

