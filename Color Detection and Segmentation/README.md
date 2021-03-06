# How does this algorithm work ?

<h3>
The algorithm is very similar in principle to green screening. But unlike green screening where we remove the background, in this application, we remove the foreground! 
<br>
As everyone is a fan of <i>Harry Potter World and Hogwartz</i>. So today, I am going to show you the magic of <u>Invisibility Cloak</u> of Harry with Computer Vision.
</h3>
<br>
<br>
<i>The project comprises of 5 simple steps:</i>
<ol>
    <li>Importing the required libraries.</li>
    <li>Capture and store the background frame [This will be done for some seconds]</li>
    <li>Detect the red colored cloth using color detection and segmentation algorithm.</li>
    <li>Segment out the red colored cloth by generating a mask. [used in code]</li>
    <li>Generate the final augmented output to create a magical effect. [output.avi]</li>
</ol>