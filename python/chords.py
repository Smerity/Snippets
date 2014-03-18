import numpy as np
from scipy.io.wavfile import write

# We will have a sampling frequency of 44,100Hz
RATE = 44100
NOTES = {
    'Bf': 466, 'B': 494, 'C': 523, 'Cs': 554,
    'D': 587, 'Ds': 587, 'E': 659, 'F': 698,
    'Fs': 740, 'G': 784, 'Af': 831, 'A': 880
}


def note(freq, octave=1, duration=1, amp=1000):
  if type(freq) == str:
    freq = NOTES[freq]
  freq *= octave
  X = np.linspace(0, duration, duration * RATE)
  res = np.sin(2 * np.pi * freq * X) * amp
  return np.int16(res)

if __name__ == '__main__':
  # Let's hear what the standard 2-5-1 progression sounds like
  dm = sum([note(x) for x in 'DFA'])
  g = sum([note(x) for x in 'GBD'])
  c = sum([note(x) + note(x, octave=0.5) for x in 'CEG'])
  data = np.concatenate([dm, g, c])
  write('2-5-1.wav', 44100, np.int16(data))

  # Why don't we check out what a CEG chord looks like?
  import matplotlib.pyplot as plt
  try:
    import seaborn as sns
  except ImportError:
    pass
  for c in 'CEG':
    sound = note(c, octave=0.5 ** 6)
    plt.plot(np.arange(len(sound)), sound, label=c)
  plt.legend()
  plt.show()
