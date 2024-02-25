import numpy as np

import matplotlib.pyplot as plt

x_coords = np.linspace(- 100, 100, 500)

y_coords = np.linspace(- 100, 100, 500)

points = []

for y in y_coords:

    for x in x_coords:

        if ((x * 0.03) ** 2 + (y * 0.03) ** 2 - 1) ** 3 - (x * 0.03) ** 2 * (y * 0.03) ** 3 <= 0:

            points.append({"x": x, "y": y})

heart_x = list(map(lambda point: point["x"], points))

heart_y = list(map(lambda point: point["y"], points))

# plt.scatter(heart_x, heart_y, s=10, alpha=0.5)
# 通过改变"cmap"这个参数，就可以定制不同款色的高级爱心啦！
plt.scatter(heart_x, heart_y, s=10, alpha=0.5, c=range(len(heart_x)), cmap='autumn')

plt.show()

"""
<cmap = “autumn”> 橙色-热情洋溢的她
<cmap = “spring”> 青春-充满朝气的她
<cmap = “rainbow”> 彩虹-充满绚丽幻想的她
<cmap = “cool”> 紫色-优雅宁静的她
<cmap = “magma”> 晚霞-醇厚脱俗的她
<cmap = “Reds”> 炽热-热烈奔放的
<cmap = “viridis”> 翡翠-平静柔和的她
<cmap = “gist_rainbow”> 五彩缤纷-多姿多彩的她

values: Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, 

BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, 

Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, 

Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, 

Set3, Set3_r, Spectral, Spectral_r, Vega10, Vega10_r, Vega20, Vega20_r, Vega20b, Vega20b_r, Vega20c, Vega20c_r, Wistia, Wistia_r, YlGn, 

YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, 

brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, 

gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, 

gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, 

magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, 

seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, 

terrain, terrain_r, viridis, viridis_r, winter, winter_r
"""