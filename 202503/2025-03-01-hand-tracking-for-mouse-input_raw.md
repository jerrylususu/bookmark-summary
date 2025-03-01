Title: Hand Tracking for Mouse Input

URL Source: https://chernando.com/blog/2023/07/23/hand-tracking-for-mouse-input.html

Published Time: 2023-07-23T08:55:00+00:00

Markdown Content:
The other day I saw the launch of Apple Vision Pro, the whole thing was very interesting, but one thing that caught my attention was the finger input. It seems very intuitive, by using the finger pinching as sort of like a cursor or mouse input. I figured I want to try it out, so I took it upon myself to create it.

_Apple Vision Pro input using finger pinching action_

Game Plan
---------

The goal here is to use the hand as an input device for computer. It should be able to handle clicking and moving the mouse cursor. In order to do this, we obviously need a camera, and for starter, let’s point the camera to face downwards, since that is basically where the hands will be when using a computer. Next we need some sort of way to detect the hand and fingers position for controlling the mouse. For this, I will be using [MediaPipe](https://developers.google.com/mediapipe) from Google. The best way I can describe MediaPipe is, a set of prebuilt solutions for ML, and it happens to have a hand landmarker feature, which is what we needed. Lastly we will need to somehow simulate the mouse input.

![Image 1: MediaPipe hand landmark detection](https://i.imgur.com/P19M4Ha.jpeg)

_MediaPipe hand landmark detection_

![Image 2: High level design of the system](https://i.imgur.com/CptH0au.jpeg)

_High level design of the system_

First Trial
-----------

Starting with this, we can use the python version of MediaPipe, and have [OpenCV](https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html) read the camera feed and input it to MediaPipe, then utilize the hand landmarks to simulate the mouse, simple right? Except that this doesn’t work very well. I’ve only got into the OpenCV with MediaPipe and I found that it is super laggy.

_Python version is super laggy, something to do with OpenCV_

After some researching, turns out it was because it has something to do with the OpenCV, related to how the `waitKey` function works. I still haven’t found out the fix yet, so I suppose we’re skipping python altogether to save time and sanity.

A Stupid Idea
-------------

During research for using MediaPipe, I found out about the web version of the library through its demo. And for some reason the web version ran very smoothly. I figured I can use the web version instead of the python version. Just one problem though, how would I control the mouse using a browser? So, I came up with a crazy idea, since I can run the MediaPipe locally, what if I have a python backend running to simulate the mouse? I just have to figure out how to communicate the MediaPipe frontend to the Python backend.

_Web version running smoothly_

Simulating the Mouse
--------------------

For the MediaPipe frontend to communicate with the Python backend, I need to have it work through some sort of method. I thought of 3 ways, which are simple HTTP request, [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API), and [gRPC](https://grpc.io/) with streaming. The HTTP request is immediately out of the picture, considering I need the latency to be as low as possible. This left me with 2 options that are both for streaming data. I decided to use WebSocket because it allows for realtime communication between the client and the server, which is needed for our use case, plus I’m not too familiar with gRPC.

I setup a simple WebSocket server in python which will accept a JSON string message containing the x and y coordinate to move the mouse to. I then just have to connect the coordinates of one of the finger to be sent to the backend, in this case I’ll be using the thumb tip.

![Image 3: WebSocket server receiving information to control the mouse](https://i.imgur.com/IVFKzqI.jpeg)

_WebSocket server receiving information to control the mouse_

_Using a web browser to control the mouse_

And it worked! Surprisingly very well even, however it feels very wrong though, controlling it using the browser. In any case, the latency is not that noticeable, I suppose there might be some inefficiency. But for now let’s just ignore that.

Next is the clicking logic. To detect a click, we need to detect a pinch action, between the thumb and index finger. To do this, we just have to measure the distance between the thumb tip and index finger tip, this is using [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance). If it is less than a certain threshold, we will invoke a mouse down event, and if it is greater than the threshold, we will invoke the mouse up event. Notice that we are using mouse down and up instead of click, this is to support dragging action.

This solution works fine, however, there is a problem if we were to move the hand closer to the camera. Since we are moving a 3D object in 2D space, by moving the hand closer to the camera, the distance between the finger tips also gets larger.

![Image 4: Distance between finger tip, far vs close to the camera](https://i.imgur.com/qAnCM7Q.jpeg)

_Distance between finger tip, far vs close to the camera_

To solve this issue, we can implement a workaround to use a relative distance instead. By calculating the distance between the finger tips and the respective knuckles, where the distance will get larger the closer the hand is to the camera, we can compare this distance to the distance between the tip. This way we get a proper finger tips distance regardless if the hand is closer or far away from the camera.

![Image 5: Calculating relative distance between finger tips](https://i.imgur.com/6hwT1b9.jpeg)

_Calculating relative distance between finger tips_

The Jitter
----------

Next problem to solve is the jitter. Notice that even when my hand is not moving, and rested on the table, the cursor is still shaking. This is inherently caused by the hand landmarker model, and the only way to really fix this is to use a better model. However not all hopes are lost. For now, we can implement a simple moving average for the cursor position, this way it doesn’t jitter so much, and the movement become smooth. The only thing is, the higher the buffer for the moving average, the higher the latency as well. While we are at this, I added buffer to the pinch state as well, because it usually does a false negative while doing pinching and moving at the same time.

_Cursor is jittering while no hand movement_

![Image 6: Using moving average to smoothen the movement](https://i.imgur.com/XnwQKkT.jpeg)

_Using moving average to smoothen the movement_

_Movement is much smoother with moving average_

Another improvement we can add is a safe zone for edges of the screen. As it is now, the cursor position is based on the thumb tip coordinates. Due to this, to reach the edge of the screen we need to put the hand all the way to the edge, and in doing so, the hand is no longer fully visible. To solve this, we can implement a simple linear transformation to convert the coordinates. For this, I am basically adding a padding on each side of the edges. This way we can solve the problem of the hand not being fully visible.

![Image 7: Linear transformation implementation](https://i.imgur.com/dDitISx.jpeg)

_Linear transformation implementation_

![Image 8: Before and after padding illustration](https://i.imgur.com/U8kTDTB.jpeg)

_Before and after padding illustration_

A Better idea
-------------

Let’s go back to the latency inefficiency thing I mentioned earlier. Not only am I facing this issue, but also the fact that I need to have the tab always open for the cursor to function. We want to maintain using the web version of MediaPipe and also have it running even when the tab is not active. After some researching, one suitable option is to use [Tauri](https://tauri.app/), a framework for building desktop apps using web technology and Rust, because it can run the web frontend as a standalone program and the Rust backend can be used to communicate with the frontend much more efficiently. This can be used to simulate the mouse input we had in python. I just have to adjust some of my code. Not knowing any Rust, I did use Google and ChatGPT for implementing this.

![Image 9: Tauri Github Page](https://i.imgur.com/dT9Xwma.jpeg)

_Tauri Github Page_

![Image 10: Tauri Github Page](https://i.imgur.com/FTP4cGn.jpeg)

_Rust backend to control the mouse_

![Image 11: Javascript code calling the Rust backend](https://i.imgur.com/EhBP6Yt.jpeg)

_Javascript code calling the Rust backend_

Putting it all together, here is the result.

_Using hand tracking to simulate mouse input_

Developing another mode
-----------------------

At this point, the project should’ve been finished, but I took some time to watch YouTube video related to hand tracking input. I found that Meta Quest has a hand gesture input, which is equally cool. If in the Apple Vision Pro, you need to have the eye tracking sensor to know where the cursor is pointed, in the Meta Quest, you just have to point your hand or finger to the “screen”. I figured, why not also add this mode so the camera can face forward, and user just have to point their finger towards the screen.

_Meta Quest hand tracking feature. credit: “Tricks Tips Fix” on Youtube_

In order to determine where the finger is pointing, we can’t only use where it is located in the x and y coordinates like we did for the down facing mode. Instead, first we need to know what angle is the finger pointing at. Second, we also need to know the Z distance between the camera and the finger, these values will be used for calculating where the cursor will “land” on the screen basically.

![Image 12: Illustration on determining where the cursor will land on the screen](https://i.imgur.com/2VuVSZe.jpeg)

_Illustration on determining where the cursor will land on the screen_

For the angle, we can simply pick 2 points from the hand landmark, and by using some trigonometry we can determine the angle. We do this for the YZ angle and XZ angle to have both the horizontal and vertical angle. For the distance, this is quite tricky, because the Z axis in the hand landmark does not mean how far it is from the screen, it is just the Z distance between the finger point and the wrist point. So in order to determine distance, we will have to play around with the scale. Remember earlier where I mentioned about distance between finger points is larger when hand is closer to the screen, and smaller when the hand is further from the screen. I’m basically using this information to calculate the distance from the camera to the hand.

![Image 13: Example for Y axis, using the angle of the finger, along with the distance to screen, we can find the cursor Y value](https://i.imgur.com/GxyTr84.jpeg)

_Example for Y axis, using the angle of the finger, along with the distance to screen, we can find the cursor Y value_

![Image 14: The Formula](https://i.imgur.com/BwT0mAR.jpeg)

_The Formula_

Testing the front facing mode, I am experiencing more shaking than the down facing mode. Even with the moving average, the shaking is still unbearable. So I seek a better alternative to this method, and found the [One Euro Filter](https://gery.casiez.net/1euro/). It is a type of low pass filter, which basically does smoothing for noisy input, that is our cursor. I did have to tweak some parameter to make it usable as we are adjusting for lower jittering but also reasonable latency. In addition to that, I added some thresholding for the angle in order to further reduce the jittering. And it is somewhat usable now! I also ended up changing the moving average into One Euro Filter for the down facing mode for better latency.

_Mouse is jittering like crazy even with moving average_

_After adding One Euro Filter and thresholding, the mouse movement is relatively tame, but still jittery_

In the end, however, it is not all sunshine and roses, as there are some major problems for the front facing mode. The first biggest one is the shaking input. At certain position and angle, for some reason the MediaPipe readings will be very shaky, rendering all the filter and smoothing useless. The second one is when pinching the fingers together, there is a slight drift, making it hard to click something as the cursor just drifts away. These issues are inherently present within the model, and I figured no amount of smoothing and filtering can fix this besides fixing the actual model.

_Certain position of the hand where the hand landmarks result is very shaky_

_Mouse is drifting when fingers are pinched_

Conclusion
----------

In this project, I did what I set out to make, which is to create a cursor or mouse input like the one from the Apple Vision Pro, plus the Meta Quest headset. I had fun working on this project as I get to try some cool tech like MediaPipe, Tauri, Rust and doing some maths for this to work. You can find the project in the repository below. I’ve only tested this on Windows, it may or may not work on Linux or MacOS.

[reynaldichernando/pinch](https://github.com/reynaldichernando/pinch)

Here are some video demos for the final result.

_Interacting with the down facing mode_

_Interacting with the front facing mode_

All in all, I would say the down facing mode works quite reliably, while the front facing mode is still unstable given the issues I mentioned.

Some notes

*   To minimize some of the drift when pinching, resting the thumb on the side of the middle finger tip can help.
*   For the angle calculation in front facing mode, especially vertical angle, I added an offset, due to the camera being placed at the top of the screen, this is to correct the cursor being lower than where the finger is pointing.
*   I have yet to find a way to make the Tauri app work in background, so minimizing the window will stop the cursor. So, to change window, just click the desired window without minimizing the Tauri window.
