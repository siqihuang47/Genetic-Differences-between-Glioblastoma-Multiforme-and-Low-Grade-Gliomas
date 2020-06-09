import sys
import re
import json
import subprocess

# import functions from all_viz file to get the visualizations
sys.path.insert(0, 'src')
from all_viz import draw_survival_plot
sys.path.insert(0, 'src')
from all_viz import draw_focal_plots
sys.path.insert(0, 'src')
from all_viz import draw_focal_proportion_plots



# set the params to get the visualization configurations
with open("config/viz-config.json") as f:
    cfg = json.load(f)
draw_surviv = cfg['draw_survival_plot']
draw_focal = cfg['draw_focal_score_plots']
draw_focal_proportion = cfg['draw_focal_score_probability_plots']

# download data and get the visualizations
def main():
    if draw_surviv:
        draw_survival_plot
    if draw_focal:
        draw_focal_plots
    if draw_focal_proportion:
        draw_focal_proportion_plots

if __name__ == '__main__':
    main()
