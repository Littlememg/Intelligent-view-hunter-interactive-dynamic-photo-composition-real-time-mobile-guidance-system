#coding=utf-8
import os, sys
import pickle
import numpy as np


def get_pdefined_anchors(anchor_file):
    anchors = pickle.load(open(anchor_file, 'rb'), encoding = 'latin1')
    anchors = np.array(anchors)
    return anchors
   # with open(anchor_file, 'rb') as f:
   #     anchors = pickle._Unpickler(f)
   #     anchors.encoding = 'iso-8859-1'
   #     p = anchors.load()
   #     p = np.array(p)
   #     return p


#def get_pdefined_anchors():
#    cur_path = os.path.dirname(os.path.realpath(__file__))
##    with open('datasets/pdefined_anchor.pkl', 'rb') as f:
##        anchors = pickle._Unpickler(f)
##        anchors.encoding = 'latin1'
##        p = anchors.load()
##        p = np.array(p)
##        return p
#    anchors = pickle.load(open(os.path.join(cur_path, 'datasets/pdefined_anchor.pkl'), 'rb'))
#    anchors = np.array(anchors)
#    return anchors

def get_pdefined_anchors_xywh():
    anchors = get_pdefined_anchors()
    anchors_xywh = []
    for s_anchor in anchors:
        s_anchor_xywh = [s_anchor[0], s_anchor[1], s_anchor[2]-s_anchor[0], s_anchor[3]-s_anchor[1], s_anchor[4]]
        anchors_xywh.append(s_anchor_xywh)

    anchors_xywh = np.array(anchors_xywh)
    return anchors_xywh


if __name__ == '__main__':
    anchors = get_pdefined_anchors_xywh()
    print ("DEBUG")