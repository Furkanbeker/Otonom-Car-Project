#!/usr/bin/env python
# coding: utf-8

# In[17]:


import cv2

# Load the image file
image = cv2.imread("C:\\Users\\mfb36\\Desktop\\5")



# Check if the image is valid
if image is None:
    print('Error: Could not load image')
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the traffic sign template images
    stop_template = cv2.imread("C:\\Users\\mfb36\\Desktop\\stop", cv2.IMREAD_GRAYSCALE)
    speed_limit_template = cv2.imread("C:\\Users\\mfb36\\Desktop\\5", cv2.IMREAD_GRAYSCALE)
    
    # Use cv2.matchTemplate to compare the traffic sign image to the stop template
    result = cv2.matchTemplate(gray_image, stop_template, cv2.TM_CCOEFF_NORMED)
    _, stop_score, _, _ = cv2.minMaxLoc(result)
    
    # Use cv2.matchTemplate to compare the traffic sign image to the speed limit template
    result = cv2.matchTemplate(gray_image, speed_limit_template, cv2.TM_CCOEFF_NORMED)
    _, speed_limit_score, _, _ = cv2.minMaxLoc(result)
    
    # Check if the traffic sign image matches either template
    if stop_score > 0.7:
        print('Stop sign')
    elif speed_limit_score > 0.7:
        print('Speed limit sign is')
    else:
        print('Unrecognized traffic sign')


# In[ ]:




