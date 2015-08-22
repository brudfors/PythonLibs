import time

class Timer():

  def __init__(self):
    self.startTime = 0.0
    self.startedTime = 0.0
    self.timerIsRunning = False
    
  def startTimer(self):
    if not self.timerIsRunning:
      self.startTime = time.clock()
      self.timerIsRunning = True
    else:
      print 'Timer alredy running!'
    
  def stopTimer(self):
    if self.timerIsRunning:
      stopTime = time.clock()
      self.startedTime += (stopTime - self.startTime)
      self.timerIsRunning = False
    else:
      print 'Timer not running!'
      
  def getElapsedTime(self):
    if self.startTime == 0.0:
      return 0.0
    elif self.timerIsRunning:
      return time.clock() - self.startTime + self.startedTime
    elif not self.timerIsRunning:
      return self.startedTime
      
  def resetTimer(self):
    self.startTime = time.clock()
    self.startedTime = 0.0