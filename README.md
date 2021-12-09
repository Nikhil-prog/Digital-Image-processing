# Digital-Image-processing
Digital image processing deals with manipulation of digital images through a digital computer. It is a subfield of signals and systems but focus particularly on images. DIP focuses on developing a computer system that is able to perform processing on an image. The input of that system is a digital image and the system process that image using efficient algorithms, and gives an image as an output. The most common example is Adobe Photoshop. It is one of the widely used application for processing digital images.
## Interpolation
Image interpolation occurs in all digital photos at some stage — whether this be in bayer demosaicing or in photo enlargement. It happens anytime you resize or remap (distort) your image from one pixel grid to another. Image resizing is necessary when you need to increase or decrease the total number of pixels, whereas remapping can occur under a wider variety of scenarios: correcting for lens distortion, changing perspective, and rotating an image.

- #### _NEAREST NEIGHBOR INTERPOLATION_ 
>Nearest neighbor is the most basic and requires the least processing time of all the interpolation algorithms because it only considers one pixel — the closest one to the interpolated point. This has the effect of simply making each pixel bigger.

- #### _BILINEAR INTERPOLATION_
>Bilinear interpolation considers the closest 2x2 neighborhood of known pixel values surrounding the unknown pixel. It then takes a weighted average of these 4 pixels to arrive at its final interpolated value. This results in much smoother looking images than nearest neighbor.

- #### _BIQUADRATIC INTERPOLATION_
>Bilinear interpolation considers the closest 3X3 neighborhood of known pixel values surrounding the unknown pixel. It then takes a weighted average of these 9 pixels to arrive at its final interpolated value. This results in much smoother looking images than nearest neighbor.

- #### _BICUBIC INTERPOLATION_
>Bicubic goes one step beyond bilinear by considering the closest 4x4 neighborhood of known pixels — for a total of 16 pixels. Since these are at various distances from the unknown pixel, closer pixels are given a higher weighting in the calculation. Bicubic produces noticeably sharper images than the previous two methods, and is perhaps the ideal combination of processing time and output quality. For this reason it is a standard in many image editing programs (including Adobe Photoshop), printer drivers and in-camera interpolation.
