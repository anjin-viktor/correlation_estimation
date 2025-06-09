import csv
import calc_correlations
import numpy as np

watermarks = [ "dct_watermark" ] 

watermark_levels = { 
    "dct_watermark": [5, 10, 15]
}

filters = {
    "blur": "unsharp=3:3:-0.25:3:3:-0.25",
    "sharp": "unsharp=3:3:0.25:3:3:0.25",
#    "dctdnoiz_5": "dctdnoiz=s=5",
    "dctdnoiz_10": "dctdnoiz=s=10",
#    "light": "colorlevels=rimax=0.902:gimax=0.902:bimax=0.902",
#    "dark": "colorlevels=rimin=0.039:gimin=0.039:bimin=0.039:rimax=0.96:gimax=0.96:bimax=0.96",
#    "contrast": "colorlevels=rimin=0.058:gimin=0.058:bimin=0.058",
#    "bright": "colorlevels=romin=0.05:gomin=0.05:bomin=0.05",
#    "noise": "noise=alls=25:allf=u",
    "nlmeans_10": "nlmeans=s=10",
 #   "nlmeans_5": "nlmeans=s=5",
    "pixelize": "pixelize=w=3:h=3",
    "fftdnoiz_15": "fftdnoiz=sigma=15",
#    "fftdnoiz_5": "fftdnoiz=sigma=5"
}

def loadCorrelations(filename):
    y = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            y.append(row[1])
    
    return np.array(y, dtype=np.float64)

for watermark_name in watermarks:
    for level in watermark_levels[watermark_name]:
        print("%s: %d" % (watermark_name, level))

        y = loadCorrelations(calc_correlations.get_results_file_name(watermark_name, level, ""))
        print("\t(TP) mean: %.15f std-dev: %.15f" % (np.mean(y), np.std(y)))
##        print("\t(TP) mean: {:.2e} std-dev: {:.2e}".format(np.mean(y), np.std(y)))
#        print("{:.2e} {:.2e}".format(np.mean(y), np.std(y)))

        y = loadCorrelations(calc_correlations.get_results_file_name_wo_embedding(watermark_name, level, ""))
        print("\t(FP) mean: %.15f std-dev: %.15f" % (np.mean(y), np.std(y)))
##        print("\t(FP) mean: {:.2e} std-dev: {:.2e}".format(np.mean(y), np.std(y)))
#        print("{:.2e} {:.2e}".format(np.mean(y), np.std(y)))

        for filter_name, filter_params in filters.items():
            print("\t%s" % (filter_name))
            y = loadCorrelations(calc_correlations.get_results_file_name(watermark_name, level, filter_name))
            print("\t\t(TP) mean: %.15f std-dev: %.15f" % (np.mean(y), np.std(y)))
##            print("\t(TP) mean: {:.2e} std-dev: {:.2e}".format(np.mean(y), np.std(y)))
#            print("{:.2e} {:.2e}".format(np.mean(y), np.std(y)))

            y = loadCorrelations(calc_correlations.get_results_file_name_wo_embedding(watermark_name, level, filter_name))
            print("\t\t(FP) mean: %.15f std-dev: %.15f" % (np.mean(y), np.std(y)))
##            print("\t(FP) mean: {:.2e} std-dev: {:.2e}".format(np.mean(y), np.std(y)))
#            print("{:.2e} {:.2e}".format(np.mean(y), np.std(y)))
