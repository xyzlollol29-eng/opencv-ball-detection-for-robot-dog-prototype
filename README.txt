->(WHAT I HAVE BUILT)I have built a python program using OpenCV library, this detects a ball precisely of color red. it makes a circle around the ball and the circle follows wherever we take the ball which is used for detection.it barks when it sees the ball for the first time and can tell whether the ball is to its right or to its left.

->(HOW IT WORKS AND LOGIC)it works via OpenCV.. first it converts the ball frame into black and white then we set a range of color which will stand out in black and white basically the part it needs to focus on.. then it creates an outline around the ball.. after thats is done it will choose the biggest the outline it can find and finds the centre and radius of that outline then we use these points to make a circle around the ball then we compare the x axis of the centre points of the ball to the x axis of the centre of screen this is how we determine the location. 

->(THE PART I FOUND HARD)because im new to this library this was the hardest part to find the most suitable functions and objects for this specific project.
i am familiar with python even though my main language is CPP for now. I wont hide the fact that i used AI for this but ALL THE CODE IS HANDWRITTEN. only the functions and objects were picked by AI but i know the logic behind everything and i will eventually figure out the ENTIRE LIBRARY aswell.

->(WHAT I WILL ADD NEXT) because im already into electronics the next step would be to run this code on an raspberry pi and instead of printing "left-right" i will make it give out actual GPIO output so that we can connect the software with the hardware and also i will explore this YOLO i have very little idea about this and IM WILLING TO FIND EVERYTHING OUT 	

(PERSONAL NOTE)-> I WANT TO WORK ON THIS..
THANK YOU