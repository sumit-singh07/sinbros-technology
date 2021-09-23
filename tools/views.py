from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os
import shutil

# import numpy as np
# import imageio
# import scipy.ndimage
# import cv2

from PyPDF2 import PdfFileReader, PdfFileWriter

def youtube_embed_code_generator(request):
    return render(request, 'tools/youtube-embed-code-generator.html')


# def grayscale(rgb):
#     return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
#
#
# def dodge(front, back):
#     result = front * 255 / (255 - back)
#     result[result > 255] = 255
#     result[back == 255] = 255
#     return result.astype('uint8')
#
#
# def adjust_gamma(image, gamma=1.0):
#     invGamma = 1.0 / gamma
#     table = np.array([((i / 255.0) ** invGamma) * 255
#                       for i in np.arange(0, 256)]).astype("uint8")
#
#     return cv2.LUT(image, table)
#
#
# def image_to_sketch(request):
#     if os.path.isdir("media/sketch"):
#         shutil.rmtree('media/sketch')
#
#     if request.method == 'POST' and request.FILES['select-image']:
#         myfile = request.FILES['select-image']
#         fs = FileSystemStorage(location='media/sketch/')
#         filename = fs.save(myfile.name, myfile)
#
#         # image to sketch code start
#         img = 'media/sketch/' + filename
#         s = imageio.imread(img)
#         g = grayscale(s)
#         i = 255 - g
#
#         b = scipy.ndimage.filters.gaussian_filter(i, sigma=20)
#         r = dodge(b, g)
#         cv2.imwrite('media/sketch/sketch-' + filename, r)
#
#         # dark image start
#         x = 'media/sketch/sketch-' + filename  # location of the image
#         original = cv2.imread(x, 1)
#         gamma = 0.5  # change the value here to get different result
#         adjusted = adjust_gamma(original, gamma=gamma)
#         cv2.imwrite('media/sketch/sketch-to-image-' + filename, adjusted)
#         # dark image end
#         # image to sketch code end
#
#         params = {"image1": '../../media/sketch/' + filename,
#                   "image2": '../../media/sketch/sketch-to-image-' + filename}
#
#         return render(request, 'tools/image-to-sketch.html', params)
#
#     return render(request, 'tools/image-to-sketch.html')
#
#
# def image_to_blackwhite(request):
#     if os.path.isdir("media/blackwhite"):
#         shutil.rmtree('media/blackwhite')
#
#     if request.method == 'POST' and request.FILES['select-image']:
#         myfile = request.FILES['select-image']
#         fs = FileSystemStorage(location='media/blackwhite/')
#         filename = fs.save(myfile.name, myfile)
#
#         # image to sketch code start
#         img = 'media/blackwhite/' + filename
#         s = imageio.imread(img)
#         g = grayscale(s)
#         i = 255 - g
#
#         b = scipy.ndimage.filters.gaussian_filter(i, sigma=20)
#         r = dodge(b, g)
#         cv2.imwrite('media/blackwhite/temp-' + filename, g)
#
#         # dark image start
#         x = 'media/blackwhite/temp-' + filename  # location of the image
#         original = cv2.imread(x, 1)
#         gamma = 1.2  # change the value here to get different result
#         adjusted = adjust_gamma(original, gamma=gamma)
#         cv2.imwrite('media/blackwhite/blackwhite-' + filename, adjusted)
#         # dark image end
#         # image to sketch code end
#
#         params = {"image1": '../../media/blackwhite/' + filename,
#                   "image2": '../../media/blackwhite/blackwhite-' + filename}
#
#         return render(request, 'tools/image-to-blackwhite.html', params)
#
#     return render(request, 'tools/image-to-blackwhite.html')
#
#
# def remove_bg(request):
#     if os.path.isdir("media/remove_bg"):
#         shutil.rmtree('media/remove_bg')
#
#     if request.method == 'POST' and request.FILES['select-image']:
#         myfile = request.FILES['select-image']
#         fs = FileSystemStorage(location='media/remove_bg/')
#         filename = fs.save(myfile.name, myfile)
#         filenameonly = os.path.splitext(filename)[0]
#
#         BLUR = 21
#         CANNY_THRESH_1 = 10
#         CANNY_THRESH_2 = 200
#         MASK_DILATE_ITER = 10
#         MASK_ERODE_ITER = 10
#         MASK_COLOR = (0.0, 0.0, 1.0)  # In BGR format
#
#         # == Processing =======================================================================
#
#         # -- Read image -----------------------------------------------------------------------
#         img = cv2.imread('media/remove_bg/' + filename)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#         # -- Edge detection -------------------------------------------------------------------
#         edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
#         edges = cv2.dilate(edges, None)
#         edges = cv2.erode(edges, None)
#
#         # -- Find contours in edges, sort by area ---------------------------------------------
#         contour_info = []
#         contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#         # Previously, for a previous version of cv2, this line was:
#         #  contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#         # Thanks to notes from commenters, I've updated the code but left this note
#         for c in contours:
#             contour_info.append((
#                 c,
#                 cv2.isContourConvex(c),
#                 cv2.contourArea(c),
#             ))
#         contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
#         max_contour = contour_info[0]
#
#         # -- Create empty mask, draw filled polygon on it corresponding to largest contour ----
#         # Mask is black, polygon is white
#         mask = np.zeros(edges.shape)
#         cv2.fillConvexPoly(mask, max_contour[0], (255))
#
#         # -- Smooth mask, then blur it --------------------------------------------------------
#         mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
#         mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
#         mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
#         mask_stack = np.dstack([mask] * 3)  # Create 3-channel alpha mask
#
#         # -- Blend masked img into MASK_COLOR background --------------------------------------
#         mask_stack = mask_stack.astype('float32') / 255.0  # Use float matrices,
#         img = img.astype('float32') / 255.0  # for easy blending
#
#         masked = (mask_stack * img) + ((1 - mask_stack) * MASK_COLOR)  # Blend
#         masked = (masked * 255).astype('uint8')  # Convert back to 8-bit
#
#         c_red, c_green, c_blue = cv2.split(img)
#
#         # merge with mask got on one of a previous steps
#         img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))
#
#         cv2.imwrite('media/remove_bg/remove_bg-' + filenameonly + '.png', img_a * 255)
#
#         params = {"image1": '../../media/remove_bg/' + filename,
#                   "image2": '../../media/remove_bg/remove_bg-' + filenameonly + '.png'}
#
#         return render(request, 'tools/remove-bg.html', params)
#     return render(request, 'tools/remove-bg.html')
#
# def bulk_rename(request):
#     # os.rename(r'D:\3.jpg', r'D:\sumit.jpg')
#     if request.method == 'POST' and request.FILES['select-image']:
#         prefix = request.POST.get('prefix')
#         filename = request.POST.get('filename')
#         suffix = request.POST.get('suffix')
#         path = request.POST.get('path')
#
#         l = len(path)
#         if path[l-1]!='/':
#             path=path+'/'
#
#         create_folder=path+'Bulk Rename by Sinbros/'
#         if not os.path.exists(create_folder):
#             os.makedirs(create_folder)
#
#         i=1
#         for f in request.FILES.getlist('select-image'):
#             ex=os.path.splitext(f.name)[1]
#             name = prefix + filename + f.name + suffix + ex
#             if filename:
#                 name = prefix+filename+'('+str(i)+')'+suffix+ex
#             i=i+1
#             # os.rename(r'D:\sumit\'+name, r'D:\sumit.jpg')
#             # os.rename(os.path.join(path, f.name), os.path.join(create_folder, name))
#             shutil.copy2(path+f.name,create_folder+name)
#         # return HttpResponse(path)
#
#
#
#     return render(request, 'tools/bulk-rename.html')

def protect_pdf(request):
    if os.path.isdir("media/protectpdf"):
        shutil.rmtree('media/protectpdf')

    if request.method == 'POST' and request.FILES['select-pdf']:
        myfile = request.FILES['select-pdf']
        password = request.POST.get('pdf-password')
        fs = FileSystemStorage(location='media/protectpdf/')
        filename = fs.save(myfile.name, myfile)

        pdfwriter = PdfFileWriter()
        pdf = PdfFileReader("media/protectpdf/"+filename)

        for page_num in range(pdf.numPages):
            pdfwriter.addPage(pdf.getPage(page_num))

        pdfwriter.encrypt(password)

        filename = filename.replace(" ", "")

        with open('media/protectpdf/Protected_' + filename, "wb") as f:
            pdfwriter.write(f)
            f.close()

        params = {"file": '../../media/protectpdf/Protected_' + filename}

        return render(request, 'tools/protect-pdf.html', params)

    return render(request, 'tools/protect-pdf.html')


def split_pdf(request):
    # if os.path.isdir("media/splitpdf"):
    #     shutil.rmtree('media/splitpdf')

    if request.method == 'POST' and request.FILES['select-pdf']:
        myfile = request.FILES['select-pdf']
        fs = FileSystemStorage(location='media/splitpdf/')
        fname = myfile.name
        fname = fname.replace(" ", "")
        filename = fs.save(fname, myfile)

        params = {"file": filename}

        return render(request, 'tools/split-pdf.html', params)

    return render(request, 'tools/split-pdf.html')


def split_pdf_name(request, pdf_name):
    page = request.GET.get('page-no')

    pdfwriter = PdfFileWriter()
    pdf = PdfFileReader("media/splitpdf/" + pdf_name)

    list = []
    if "-" in page:
        page = page.split("-")
        start = page[0]
        end = page[1]

        start = int(start)
        end = int(end)
        for i in range(start, end + 1):
            list.append(i)
        for page_num in list:
            pdfwriter.addPage(pdf.getPage(int(page_num) - 1))

        with open('media/splitpdf/split_' + pdf_name, "wb") as f:
            pdfwriter.write(f)
            f.close()

        params = {"file2": '../../media/splitpdf/split_' + pdf_name}
        return render(request, 'tools/split-pdf.html', params)

    elif "," in page:
        list = page.split(",")
        for page_num in list:
            pdfwriter.addPage(pdf.getPage(int(page_num) - 1))

        with open('media/splitpdf/split_' + pdf_name, "wb") as f:
            pdfwriter.write(f)
            f.close()

        params = {"file2": '../../media/splitpdf/split_' + pdf_name}
        return render(request, 'tools/split-pdf.html', params)
    else:

        pdfwriter.addPage(pdf.getPage(int(page) - 1))

        with open('media/splitpdf/split_' + pdf_name, "wb") as f:
            pdfwriter.write(f)
            f.close()

        params = {"file2": '../../media/splitpdf/split_' + pdf_name}
        return render(request, 'tools/split-pdf.html', params)







