import subprocess

dct_watermark_exe = "D:/projects/watermarks/project/apps/RelWithDebInfo/dct_watermark.exe"

#levels = [1, 2, 3, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

detection_levels = [0.00025, 0.0005, 0.00075, 0.001, 0.00125, 0.0015, 0.00175, 0.002, 0.00225, 0.0025, 0.00275, 0.003, 0.00325, 0.0035, 0.00375, 0.004, 0.00425, 0.0045, 0.00475, 0.005, 0.00525, 0.0055, 0.00575, 0.006, 0.00625, 0.0065, 0.00675, 0.007, 0.00725, 0.0075]
dct_skip = 16

#correlation_type:
#0 - linear correlation
#1 - normalized correlation
#2 - correlation coefficient

def gen_reference(path_source, path_output, level):
    subprocess.call([dct_watermark_exe, "--gen_reference", "--reference_max=" + str(levels[level]), "--skip_count=" + str(dct_skip), "--in=" + path_source, "--out=" + path_output])

def embed(path_source, path_reference, path_output):
    subprocess.call([dct_watermark_exe, "--embed", "--in=" + path_source, "--reference=" + path_reference, "--out=" + path_output, "--skip_count=" + str(dct_skip), "--alpha=1.0"])

def detect(path, path_reference, correlation_type, threshold_level=-1, ):
    exe_params = [dct_watermark_exe, "--detect", "--in=" + path, "--reference=" + path_reference, "--skip_count=" + str(dct_skip), "--correlation=" + str(correlation_type)]
    if threshold_level != -1:
        exe_params.append("--threshold=" + str(detection_levels[threshold_level]))

    out = subprocess.run(exe_params, capture_output=True, text=True)

    if "TRUE" in out.stdout:
        return True
    else:
        return False

def detect_threshold(path, path_reference, threshold):
    exe_params = [dct_watermark_exe, "--detect", "--in=" + path, "--reference=" + path_reference, "--skip_count=" + str(dct_skip)]
    exe_params.append("--threshold=" + str(threshold))
    out = subprocess.run(exe_params, capture_output=True, text=True)

    if "TRUE" in out.stdout:
        return True
    else:
        return False

def get_correlation(path, path_reference):
    exe_params = [dct_watermark_exe, "--get_correlation", "--in=" + path, "correlation=1", "--reference=" + path_reference, "--skip_count=" + str(dct_skip)]
    out = subprocess.run(exe_params, capture_output=True, text=True)

    correlcation = 0
    try:
        correlcation = float(out.stdout)
    except ValueError:
        correlcation = 0

    return correlcation

if __name__ == "__main__":
    gen_reference("agriculture-hd.jpg", "reference.bmp", 10)
    embed("agriculture-hd.jpg", "reference.bmp", "watermarked.png")
    print(get_correlation("watermarked.png", "reference.bmp"))
    print(get_correlation("agriculture-hd.jpg", "reference.bmp"))
    print(detect_threshold("watermarked.png", "reference.bmp", 100))
    print(detect_threshold("agriculture-hd.jpg", "reference.bmp", 100))
