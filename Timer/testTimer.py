import time

import Timer

def testTimer():
    timer = Timer.Timer()
    
    print '-----------Start Timer Test-----------'
    assert round(timer.getElapsedTime(), 1) == 0.0
    print '1. getElapsedTime  = 0.00 | %.2f' % timer.getElapsedTime()
    
    timer.resetTimer()
    assert round(timer.getElapsedTime(), 1) == 0.0
    print '2. resetTimer + getElapsedTime  = 0.00 | %.2f' % timer.getElapsedTime()

    timer.startTimer()
    time.sleep(1)
    assert round(timer.getElapsedTime(), 1) == 1.0   
    print '3. startTimer + sleep(1) + getElapsedTime  = 1.00 | %.2f' % timer.getElapsedTime()
    
    timer.stopTimer()
    time.sleep(1)
    assert round(timer.getElapsedTime(), 1) == 1.0    
    print '4. stopTimer + sleep(1) + getElapsedTime = 1.00 | %.2f' % timer.getElapsedTime()
 
    timer.startTimer()
    time.sleep(2)
    assert round(timer.getElapsedTime(), 1) == 3.0    
    print '5. startTimer + sleep(2) + getElapsedTime = 3.00 | %.2f' % timer.getElapsedTime()

    timer.stopTimer()
    time.sleep(1)
    assert round(timer.getElapsedTime(), 1) == 3.0    
    print '6. stopTimer + sleep(1) + getElapsedTime = 3.00 | %.2f' % timer.getElapsedTime()

    timer.startTimer()
    time.sleep(3)
    timer.stopTimer()
    assert round(timer.getElapsedTime(), 1) == 6.0    
    print '7. startTimer + sleep(3) + stopTimer + getElapsedTime = 6.00 | %.2f' % timer.getElapsedTime()

    timer.startTimer()
    time.sleep(2.5)
    assert round(timer.getElapsedTime(), 1) == 8.5    
    print '8. startTimer + sleep(2.5) + getElapsedTime = 8.50 | %.2f' % timer.getElapsedTime()
 
    timer.stopTimer()
    assert round(timer.getElapsedTime(), 1) == 8.5    
    print '9. stopTimer + getElapsedTime = 8.50 | %.2f' % timer.getElapsedTime()
 
    timer.startTimer()
    time.sleep(1.25)
    timer.stopTimer()
    assert round(timer.getElapsedTime(), 2) == 9.75    
    print '10. startTimer + sleep(1.25) + stopTimer + getElapsedTime = 9.75 | %.2f' % timer.getElapsedTime()
    
    timer.startTimer()
    time.sleep(1.25)
    assert round(timer.getElapsedTime(), 1) == 11.0    
    print '11. startTimer + sleep(1.25) + getElapsedTime = 11.00 | %.2f' % timer.getElapsedTime()

    timer.startTimer()
    time.sleep(2)
    assert round(timer.getElapsedTime(), 1) == 13.0    
    print '12. startTimer + sleep(2) + getElapsedTime = 13.00 | %.2f' % timer.getElapsedTime()

    timer.resetTimer()
    assert round(timer.getElapsedTime(), 1) == 0.0    
    print '13. resetTimer + getElapsedTime = 0.00 | %.2f' % timer.getElapsedTime()
     
    timer.resetTimer()
    time.sleep(2)
    assert round(timer.getElapsedTime(), 1) == 2.0    
    print '14. resetTimer + sleep(2) + getElapsedTime = 2.00 | %.2f' % timer.getElapsedTime()

    timer.stopTimer()
    assert round(timer.getElapsedTime(), 1) == 2.0    
    print '15. stopTimer  + getElapsedTime = 2.00 | %.2f' % timer.getElapsedTime()

    timer.resetTimer()
    time.sleep(2)
    assert round(timer.getElapsedTime(), 1) == 0.0    
    print '16. resetTimer + getElapsedTime = 0.00 | %.2f' % timer.getElapsedTime()

    timer.startTimer()
    time.sleep(3)
    assert round(timer.getElapsedTime(), 1) == 3.0   
    print '17. startTimer + sleep(3) + getElapsedTime  = 3.00 | %.2f' % timer.getElapsedTime()

    timer.resetTimer()
    assert round(timer.getElapsedTime(), 1) == 0.0    
    print '18. resetTimer + getElapsedTime = 0.00 | %.2f' % timer.getElapsedTime()

    time.sleep(2)
    assert round(timer.getElapsedTime(), 1) == 2.0   
    print '19. sleep(2) + getElapsedTime  = 2.00 | %.2f' % timer.getElapsedTime()
 
    time.sleep(1)
    timer.stopTimer()
    assert round(timer.getElapsedTime(), 1) == 3.0   
    print '19. sleep(1) + stopTimer + getElapsedTime  = 3.00 | %.2f' % timer.getElapsedTime()

    time.sleep(1)
    timer.stopTimer()
    assert round(timer.getElapsedTime(), 1) == 3.0   
    print '20. sleep(1) + stopTimer + getElapsedTime  = 3.00 | %.2f' % timer.getElapsedTime()
  
    print '-----------Timer Test Finished-----------'
    
if __name__ == "__main__":
    testTimer()