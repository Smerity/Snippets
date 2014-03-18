import numpy as np
from scipy.io.wavfile import write

RATE = 44100
NOTES = {
    'A': 440, 'Bf': 466, 'B': 494, 'C': 523,
    'Cs': 554, 'D': 587, 'Ds': 587, 'E': 659,
    'F': 698, 'Fs': 740, 'G': 784, 'Af': 831,
    'A': 880
}


def note(freq, octave=1, length=1, amp=1000):
  if type(freq) == str:
    freq = NOTES[freq]
  freq *= octave
  X = np.linspace(0, length, length * RATE)
  res = np.sin(2 * np.pi * freq * X) * amp
  print res
  return np.int16(res)

dm = sum([note(x) for x in 'DFA'])
g = sum([note(x) for x in 'GBD'])
c = sum([note(x) + note(x, octave=0.5) for x in 'CEG'])
data = np.concatenate([dm, g, c])
write('test.wav', 44100, np.int16(data))

"""
import matplotlib.pyplot as plt
import seaborn as sns
for c in 'CEG':
  sound = note(c, octave=0.5 ** 6)
  plt.plot(np.arange(len(sound)), sound, label=c)
plt.legend()
plt.show()
"""
