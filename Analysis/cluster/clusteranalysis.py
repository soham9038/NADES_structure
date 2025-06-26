# Requirement: all c.o.m files of molecule for which cluster analysis is about to be done, like OW_1.txt, OW_2.txt till OW_111.txt


import numpy as np
import os
from sklearn.cluster import DBSCAN

# Constants
NUM_FILES = 111  # total number of molecules or c.o.m files
NUM_FRAMES = 10001 # total number of frames per file
DIST_THRESHOLD = 0.35  # distance cut-off in nm

# Load data: List of 111 arrays (10001 x 3)
def load_all_data():
    data = []
    for i in range(1, NUM_FILES + 1):
        filename = f"OW_{i}.txt" # name of input files
        coords = np.loadtxt(filename)
        data.append(coords)
    return data

# Cluster for each frame
def cluster_frame(coords_frame):
    clustering = DBSCAN(eps=DIST_THRESHOLD, min_samples=1).fit(coords_frame)
    labels = clustering.labels_
    unique_labels = set(labels)
    cluster_sizes = [np.sum(labels == label) for label in unique_labels]
    return len(unique_labels), cluster_sizes

# Main function
def analyze_clusters():
    all_data = load_all_data()  # all_data[i][j] is the j-th frame of i-th molecule
    output_lines = []

    for frame_idx in range(NUM_FRAMES):
        # Build the coordinate list for all molecules at this frame
        coords_frame = np.array([mol[frame_idx] for mol in all_data])
        
        # Cluster them
        num_clusters, cluster_sizes = cluster_frame(coords_frame)
        
        # Format: Frame <idx>: <num_clusters> clusters - [size1, size2, ...]
        cluster_sizes.sort(reverse=True)
        line = f"Frame {frame_idx + 1}: {num_clusters} clusters - {cluster_sizes}"
        output_lines.append(line)
        print(line)

    # Write to file
    with open("cluster_output.txt", "w") as f:
        for line in output_lines:
            f.write(line + "\n")

if __name__ == "__main__":
    analyze_clusters()

