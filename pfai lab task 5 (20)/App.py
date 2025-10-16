# import pandas
# import cv2
# from matplotlib import pyplot as plt

# image_path = r"C:\Users\This PC\Downloads\978ae9c2-10bc-4a19-9287-03a22f3e6b9b.jpg"
# image = cv2.imread(image_path)
# resized_image = cv2.resize(image, (1900, 800))
# resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
# plt.imshow(resized_image_rgb)
# plt.title('Original Image')
# plt.axis('off')
# plt.show()
# Gaussian = cv2.GaussianBlur(resized_image, (15, 15), 0)  
# Gaussian_rgb = cv2.cvtColor(Gaussian, cv2.COLOR_BGR2RGB)  
# plt.imshow(Gaussian_rgb)
# plt.title('Gaussian Blurred Image')
# plt.axis('off')
# plt.show()
# median = cv2.medianBlur(resized_image, 11)  
# median_rgb = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)  

# plt.imshow(median_rgb)
# plt.title('Median Blurred Image')
# plt.axis('off')
# plt.show()
# bilateral = cv2.bilateralFilter(resized_image, 15, 150, 150)  
# bilateral_rgb = cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB)  

# plt.imshow(bilateral_rgb)
# plt.title('Bilateral Blurred Image')
# plt.axis('off')
# plt.show()

# -------------------------------------------------------------------------

# import cv2
# import numpy as np

# # Open the image.
# img = cv2.imread(r"C:\Users\This PC\Downloads\978ae9c2-10bc-4a19-9287-03a22f3e6b9b.jpg")

# # Apply log transform.
# c = 255/(np.log(1 + np.max(img)))
# log_transformed = c * np.log(1 + img)

# # Specify the data type.
# log_transformed = np.array(log_transformed, dtype = np.uint8)

# # Save the output.
# cv2.imwrite('log_transformed.jpg', log_transformed)

#-------------------------------------------------------------------------
# import cv2
# import numpy as np

# # Open the image.
# img = cv2.imread(r"C:\Users\This PC\Downloads\978ae9c2-10bc-4a19-9287-03a22f3e6b9b.jpg")

# # Trying 4 gamma values.
# for gamma in [0.1, 0.5, 1.2, 2.2]:
    
#     # Apply gamma correction.
#     gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')

#     # Save edited images.
#     cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)

#-------------------------------------------------------------------------
# import cv2
# import numpy as np

# # Function to map each intensity level to output intensity level.
# def pixelVal(pix, r1, s1, r2, s2):
#     if (0 <= pix and pix <= r1):
#         return (s1 / r1)*pix
#     elif (r1 < pix and pix <= r2):
#         return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
#     else:
#         return ((255 - s2)/(255 - r2)) * (pix - r2) + s2

# # Open the image.
# img = cv2.imread(r"C:\Users\This PC\Downloads\978ae9c2-10bc-4a19-9287-03a22f3e6b9b.jpg", 0)

# # Define parameters.
# r1 = 70
# s1 = 0
# r2 = 140
# s2 = 255

# # Vectorize the function to apply it to each value in the Numpy array.
# pixelVal_vec = np.vectorize(pixelVal)

# # Apply contrast stretching.
# contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

# # Save edited image.
# cv2.imwrite('contrast_stretch.jpg', contrast_stretched)

#-------------------------------------------------------------------------
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread(r"C:\Users\This PC\Downloads\YfV0k9.jpg")
# rows, cols, _ = img.shape

# M_left = np.float32([[1, 0, -50], [0, 1, 0]])
# M_right = np.float32([[1, 0, 50], [0, 1, 0]])
# M_top = np.float32([[1, 0, 0], [0, 1, 50]])
# M_bottom = np.float32([[1, 0, 0], [0, 1, -50]])

# img_left = cv2.warpAffine(img, M_left, (cols, rows))
# img_right = cv2.warpAffine(img, M_right, (cols, rows))
# img_top = cv2.warpAffine(img, M_top, (cols, rows))
# img_bottom = cv2.warpAffine(img, M_bottom, (cols, rows))

# plt.subplot(221), plt.imshow(img_left), plt.title('Left')
# plt.subplot(222), plt.imshow(img_right), plt.title('Right')
# plt.subplot(223), plt.imshow(img_top), plt.title('Top')
# plt.subplot(224), plt.imshow(img_bottom), plt.title('Bottom')
# plt.show()

#-------------------------------------------------------------------------
