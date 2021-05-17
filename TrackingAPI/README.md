# Tracking APIs in OpenCV

## Description:
The script shows 5 of the many tracking algorithms that come built-in with Python's OpenCV that ease the process of object detection and tracking.
Sit facing the camera and select your region to track and press 'enter'. Based on the movements captured in the live camera, each tracking algorithm will do its work.

The trackers used in this script are:<br>
* Boosting Tracker
* MIL Tracker
* KCF Tracker
* TLD Tracker
* Median Flow Tracker

## Understanding the trackers:

### Boosting Tracker:
* <b>PROS</b>:
    * Very well known and studied algorithm.
* <b>CONS</b>:
    * Doesn't know when tracking has failed.
    * Much better techniques available.

![GIF](https://media.giphy.com/media/MxuRuvhG4eNaP7Tgcp/giphy.gif)
    
### MIL Tracker:
* <b>PROS</b>:
    * Good performance and doesn't drift as much as Boosting.
* <b>CONS</b>:
    * Doesn't know when tracking has failed.
    * Can't recover from full obstruction.

![GIF](https://media.giphy.com/media/GD7DkYfEU0NZQ2dDFg/giphy.gif)

### KCF Tracker:
* <b>PROS</b>:
    * Great first choice as it is better than Boosting or MIL.
* <b>CONS</b>:
    * Can't recover from full obstruction.
    
![GIF](https://media.giphy.com/media/T4zvppkaFk9EX7fH74/giphy.gif)

### TLD Tracker:
* <b>PROS</b>:
    * Good at tracking even with obstructions.
    * Tracks well under large changes in scale.
* <b>CONS</b>:
    * Can provide many false positives.

![GIF](https://media.giphy.com/media/zOm0X7zNlaS00J6FHf/giphy.gif)

### Median Flow Tracker:
* <b>PROS</b>:
    * Good at reporting back false tracking.
    * Tracks well with predictable motion.
* <b>CONS</b>:
    * False under large motions.
    
![GIF](https://media.giphy.com/media/Q1RGEIS65uAt7Avgkz/giphy.gif)

## Author
[Rohini Rao](https://github.com/RohiniRG)

