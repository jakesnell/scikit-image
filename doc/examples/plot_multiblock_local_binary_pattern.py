"""
===========================================================
Multi-Block Local Binary Pattern for texture classification
===========================================================

This example shows how to compute multi-block local binary
pattern (MB-LBP) features as well as how to visualize them.

The features are calculated similarly to local binary patterns (LBPs),
except that summed blocks are used instead of individual pixel values.

MB-LBP is an extension of LBP that can be computed on multiple scales
in constant time using the integral image.
9 equally-sized rectangles are used to compute a feature.
For each rectangle, the sum of the pixel intensities is computed.
Comparisons of these sums to that of the central rectangle determine
the feature, similarly to LBP (See `LBP <plot_local_binary_pattern.html>`_).

First, we generate an image to illustrate the functioning of MB-LBP:
we take a (9, 9) rectangle and divide it into (3, 3) block,
upon which we then apply MB-LBP.


"""
from __future__ import print_function
from skimage.feature import multiblock_local_binary_pattern
import numpy as np
from skimage.transform import integral_image

# Create test matrix where first and fifth
# rectangles starting from top left clockwise
# have greater value than the central one.
test_img = np.zeros((9, 9), dtype='uint8')
test_img[3:6, 3:6] = 1
test_img[:3, :3] = 50
test_img[6:, 6:] = 50

# MB-LBP is filled in reverse order.
# So the first and fifth bits from the end should
# be filled.
correct_answer = 0b10001000

int_img = integral_image(test_img)

lbp_code = multiblock_local_binary_pattern(int_img, 0, 0, 3, 3)

print(correct_answer)
print(lbp_code)

"""
Now let's apply the operator to a real image and see how the visualization works.
"""
from skimage import data
from matplotlib import pyplot as plt
from skimage.feature import draw_multiblock_lbp

test_img = data.coins()

int_img = integral_image(test_img)

lbp_code = multiblock_local_binary_pattern(int_img, 0, 0, 90, 90)

img = draw_multiblock_lbp(test_img, 0, 0, 90, 90,
                          lbp_code=lbp_code, alpha=0.5)


plt.imshow(img, interpolation='nearest')

"""
.. image:: PLOT2RST.current_figure

On the above plot we see the result of computing a MB-LBP and visualization
of the computed feature. The rectangles that have less intensity than the central
rectangle are marked in cyan. The ones that have bigger intensity values
are marked in white. The central rectangle is left untouched.
"""
