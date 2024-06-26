import os 
import shutil
import time

def main(j,video_formats,image_formats,pdf_formats):
    i = j.split(".")[-1]
    #docx files
    if "docx" in i or "doc" in i:
        Download_docx(j)

    #Video files
    elif i.lower() in video_formats:
        Download_video(j)

    #image files
    elif i.lower() in image_formats:
        Download_image(j)
    
    #pdf files
    elif i.lower() in pdf_formats:
        Download_pdf(j)

    #powerpoint files
    elif "ppt" in i:
        Download_powerpoint(j)
    
    #exe files
    elif "exe" in i:
        Download_exe(j)

    #any other files like zip files or something any miscellaneous files if you will...
    else:
        Download_miscellaneous(j)

def Download_docx(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\docx")
def Download_video(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\video")
def Download_image(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\image")
def Download_pdf(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\pdf")
def Download_powerpoint(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\powerpoint")
def Download_exe(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\execu")
def Download_miscellaneous(i):
    shutil.move(f"C:\\Users\\ldogb\\Downloads\\{i}",r"C:\Users\ldogb\Desktop\Downloads_sorted\miscellaneous")

if __name__ == '__main__':
    
    video_formats = ["mp4", "avi", "mov", "wmv", "flv", "mkv", "webm", "mpeg"]
    image_formats = ["jpg", "png", "gif", "bmp", "tiff", "svg", "webp", "heif"]
    pdf_formats = ['pdf', 'html']

    dir = r"C:\Users\ldogb\Downloads"
    while 1:
        time.sleep(600)
        files = os.listdir(dir)
        if files:
            for i in files:
                main(i,video_formats,image_formats,pdf_formats)
