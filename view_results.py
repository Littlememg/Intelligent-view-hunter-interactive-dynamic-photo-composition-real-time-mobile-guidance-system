import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import project_utils
# from datasets.get_test_image_list import get_test_list, get_pdefined_anchors, getImagePath
from py_utils import dir_utils, load_utils


def viewBBoxes(image_file, bboxes, titles, showImageName=True):

    n_items_per_row = 4
    image = Image.open(image_file)
    image = np.array(image, dtype=np.uint8)
    n_crops = len(bboxes)
    n_rows = n_crops // n_items_per_row + 1

    fig = plt.figure(figsize=[20, 20])
    if showImageName:
        fig.suptitle(os.path.basename(image_file))

    for idx, s_bbox in enumerate(bboxes):
        ax =fig.add_subplot(n_rows, n_items_per_row, idx+1)
        ax.imshow(image)
        ax.set_axis_off()

        ax.set_title(titles[idx])

        rect_i = patches.Rectangle((s_bbox[0], s_bbox[1]), s_bbox[2]-s_bbox[0], s_bbox[3]-s_bbox[1], 
                                   linewidth=2, edgecolor='yellow', facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect_i)
    plt.show(block=False)
    #raw_input("Press Enter to continue...")
    #plt.close()



annotation_path = 'ProposalResults/ViewProposalResults-tmp.txt'
image_path_root = 'example_images/'

image_data = load_utils.load_json(annotation_path)
image_name_list = sorted(image_data)

names = []
marks = []
bbboxes = []

photo_number = 7
for idx, image_name in enumerate(image_name_list):
    #if idx<20:4444444
    #    continue
    
    bboxes = image_data[image_name]['bboxes']
    scores = image_data[image_name]['scores']
    names.append(image_name)
    bbboxes.append(bboxes)
    marks.append(scores)
    
for i in range(photo_number):
    if marks[i]<marks[i+photo_number] and marks[i+photo_number*2] < marks[i+photo_number]:
        bboxes = bbboxes[i+photo_number]
        scores = marks[i+photo_number]
    
        img = Image.open("example_images/"+names[i+photo_number])
        for j in range(3):
            cropped = img.crop(bbboxes[i+photo_number][j])
            cropped.save("result_image/cv_cut"+str(j)+names[i+photo_number])
        s_image_path = os.path.join(image_path_root, names[i+photo_number])
        viewBBoxes(s_image_path, bboxes, scores)
    elif marks[i+photo_number]<marks[i] and marks[i+photo_number*2] < marks[i]:
        bboxes = bbboxes[i]
        scores = marks[i]
    
        img = Image.open("example_images/"+names[i])
        for j in range(3):
            cropped = img.crop(bbboxes[i][j])
            cropped.save("result_image/cv_cut"+str(j)+names[i])
        s_image_path = os.path.join(image_path_root, names[i])
        viewBBoxes(s_image_path, bboxes, scores)
    elif marks[i]<marks[i+photo_number*2] and marks[i+photo_number] < marks[i+photo_number*2]:
        bboxes = bbboxes[i+photo_number*2]
        scores = marks[i+photo_number*2]
    
        img = Image.open("example_images/"+names[i+photo_number*2])
        for j in range(3):
            cropped = img.crop(bbboxes[i+photo_number*2][j])
            cropped.save("result_image/cv_cut"+str(j)+names[i+photo_number*2])
        s_image_path = os.path.join(image_path_root, names[i+photo_number*2])
        viewBBoxes(s_image_path, bboxes, scores)
        

print("DEBUG")