# Author: Mikael Brudfors (brudfors@gmail.com)
# Date: Aug. 2015
# Free for anyone to use!

import time

import StopWatch

# Tests the functionality of the StopWatch library
def testTimer():
    stopWatch = StopWatch.StopWatch()
    
    print '-----------Start StopWatch Test-----------'
    assert round(stopWatch.getElapsedTime(), 1) == 0.0
    print '1. getElapsedTime  = 0.00 | %.2f' % stopWatch.getElapsedTime()
    
    stopWatch.reset()
    assert round(stopWatch.getElapsedTime(), 1) == 0.0
    print '2. reset + getElapsedTime  = 0.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.start()
    time.sleep(1)
    assert round(stopWatch.getElapsedTime(), 1) == 1.0   
    print '3. start + sleep(1) + getElapsedTime  = 1.00 | %.2f' % stopWatch.getElapsedTime()
    
    stopWatch.pause()
    time.sleep(1)
    assert round(stopWatch.getElapsedTime(), 1) == 1.0    
    print '4. pause + sleep(1) + getElapsedTime = 1.00 | %.2f' % stopWatch.getElapsedTime()
 
    stopWatch.start()
    time.sleep(2)
    assert round(stopWatch.getElapsedTime(), 1) == 3.0    
    print '5. start + sleep(2) + getElapsedTime = 3.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.pause()
    time.sleep(1)
    assert round(stopWatch.getElapsedTime(), 1) == 3.0    
    print '6. pause + sleep(1) + getElapsedTime = 3.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.start()
    time.sleep(3)
    stopWatch.pause()
    assert round(stopWatch.getElapsedTime(), 1) == 6.0    
    print '7. start + sleep(3) + pause + getElapsedTime = 6.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.start()
    time.sleep(2.5)
    assert round(stopWatch.getElapsedTime(), 1) == 8.5    
    print '8. start + sleep(2.5) + getElapsedTime = 8.50 | %.2f' % stopWatch.getElapsedTime()
 
    stopWatch.pause()
    assert round(stopWatch.getElapsedTime(), 1) == 8.5    
    print '9. pause + getElapsedTime = 8.50 | %.2f' % stopWatch.getElapsedTime()
 
    stopWatch.start()
    time.sleep(1.2)
    stopWatch.pause()
    assert round(stopWatch.getElapsedTime(), 1) == 9.7    
    print '10. start + sleep(1.2) + pause + getElapsedTime = 9.7 | %.2f' % stopWatch.getElapsedTime()
    
    stopWatch.start()
    time.sleep(1.3)
    assert round(stopWatch.getElapsedTime(), 1) == 11.0    
    print '11. start + sleep(1.3) + getElapsedTime = 11.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.start()
    time.sleep(2)
    assert round(stopWatch.getElapsedTime(), 1) == 13.0    
    print '12. start + sleep(2) + getElapsedTime = 13.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.reset()
    assert round(stopWatch.getElapsedTime(), 1) == 0.0    
    print '13. reset + getElapsedTime = 0.00 | %.2f' % stopWatch.getElapsedTime()
     
    stopWatch.reset()
    time.sleep(2)
    assert round(stopWatch.getElapsedTime(), 1) == 2.0    
    print '14. reset + sleep(2) + getElapsedTime = 2.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.pause()
    assert round(stopWatch.getElapsedTime(), 1) == 2.0    
    print '15. pause  + getElapsedTime = 2.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.reset()
    time.sleep(2)
    assert round(stopWatch.getElapsedTime(), 1) == 0.0    
    print '16. reset + getElapsedTime = 0.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.start()
    time.sleep(3)
    assert round(stopWatch.getElapsedTime(), 1) == 3.0   
    print '17. start + sleep(3) + getElapsedTime  = 3.00 | %.2f' % stopWatch.getElapsedTime()

    stopWatch.reset()
    assert round(stopWatch.getElapsedTime(), 1) == 0.0    
    print '18. reset + getElapsedTime = 0.00 | %.2f' % stopWatch.getElapsedTime()

    time.sleep(2)
    assert round(stopWatch.getElapsedTime(), 1) == 2.0   
    print '19. sleep(2) + getElapsedTime  = 2.00 | %.2f' % stopWatch.getElapsedTime()
 
    time.sleep(1)
    stopWatch.pause()
    assert round(stopWatch.getElapsedTime(), 1) == 3.0   
    print '19. sleep(1) + pause + getElapsedTime  = 3.00 | %.2f' % stopWatch.getElapsedTime()

    time.sleep(1)
    stopWatch.pause()
    assert round(stopWatch.getElapsedTime(), 1) == 3.0   
    print '20. sleep(1) + pause + getElapsedTime  = 3.00 | %.2f' % stopWatch.getElapsedTime()
  
    print '-----------StopWatch Test Finished-----------'
    
if __name__ == "__main__":
    testTimer()