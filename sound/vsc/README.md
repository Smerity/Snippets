Experimental Music from Very Short C Programs
#############################################

This is a cleaner (i.e. less short) implementation that works on Ubuntu and compiles cleanly without errors. As _/dev/dsp_ and _/dev/audio_ no longer exist on the Ubuntu stack, it is necessary to run an emulation layer.

To run on Ubuntu, simply type:

     padsp ./sound

If you wish to cat a file, such as your hard drive, directly to /dev/audio then you can run:

    sudo cat /dev/sda | `padsp tee /dev/audio` >& /dev/null

Running this on other distributions that directly support _/dev/dsp_ should be trivial.

For a Youtube link to a large collection of these implementations, see http://www.youtube.com/watch?v=GtQdIYUtAHg
Also relevant is the Javascript SoftSynth in 140 bytes, available https://gist.github.com/1285255
