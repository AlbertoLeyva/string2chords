import string2chords as s2c

# Chords in []
# * for line break
# $ for end of string

string = "S[G]eñor, soy jó[D/F#]ven pescador*Que viene a dejar sus re[Em]des y seguirte a tí, Señor$"

s2c.string_to_chords(string)