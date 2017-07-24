import tkinter, tkconstants, tkFileDialog
import winsound

class MusicPlayer(tkinter.Frame):

  def __init__(self, root):

    tkinter.Frame.__init__(self, root)

    # options for buttons
    button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

    # define buttons
    tkinter.Button(self, text='Play', command=self.play).pack(**button_opt)
    tkinter.Button(self, text='Stop', command=self.stop).pack(**button_opt)    
    # define options for opening or saving a file
    self.file_opt = options = {}
    options['defaultextension'] = '*.wav'
    options['filetypes'] = [('WAV Sound Files', '*.wav')]
    options['initialdir'] = 'C:\\'
    options['initialfile'] = '.wav'
    options['parent'] = root
    options['title'] = 'Pick a File'

    # This is only available on the Macintosh, and only when Navigation Services are installed.
    #options['message'] = 'message'

    # if you use the multiple file version of the module functions this option is set automatically.
    #options['multiple'] = 1

    # defining options for opening a directory
    self.dir_opt = options = {}
    options['initialdir'] = 'C:\\'
    options['mustexist'] = False
    options['parent'] = root
    options['title'] = 'Pick a Dir'

  def askopenfile(self):

    return tkFileDialog.askopenfile(mode='r', **self.file_opt)

  def askopenfilename(self):

    # get filename
    filename = tkFileDialog.askopenfilename(**self.file_opt)

    # open file on your own
    if filename:
      return open(filename, 'r')
    

  def asksaveasfile(self):

    return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)

  def asksaveasfilename(self):

    # get filename
    filename = tkFileDialog.asksaveasfilename(**self.file_opt)

    # open file on your own
    if filename:
      return open(filename, 'w')

  def askdirectory(self):


    return tkFileDialog.askdirectory(**self.dir_opt)

  def play(self):
    soundfile = self.askopenfilename
    winsound.PlaySound(soundfile, soundfile)

  def stop(self):
    winsound.PlaySound(None, SND_PURGE)

if __name__=='__main__':
  root = Tkinter.Tk()
  MusicPlayer(root).pack()
  root.wm_title('Music Player')
  root.mainloop(
