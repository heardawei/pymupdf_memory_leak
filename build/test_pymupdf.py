# coding: utf-8
# Created by hujian on 2024/1/26 14:08
#
import gc
import time
import fitz
import logging
import os
import pdf2docx
import psutil
import pymupdf

import pdf2docx.image
import pdf2docx.image.ImagesExtractor

# files = ["build/红星新闻.pdf", "build/test_2791_content.pdf"]
files = "build/PDF"


def test_get_text(temp_file_path):
    """
    @param if_include_shape:
    @param uuid:
    @param temp_file_path:
    """
    pdf_obj = None
    with fitz.open(temp_file_path) as pdf_obj:
        # pdf_obj = fitz.open(temp_file_path)
        for pid, one_page in enumerate(pdf_obj, start=1):
            raw = one_page.get_text("rawdict")
    return 1


def test_get_texttrace(temp_file_path):
    """
    @param if_include_shape:
    @param uuid:
    @param temp_file_path:
    """
    pdf_obj = None
    with fitz.open(temp_file_path) as pdf_obj:
        # pdf_obj = fitz.open(temp_file_path)
        for pid, one_page in enumerate(pdf_obj, start=1):
            raw = one_page.get_texttrace()
    return 1


def test_get_pixmap(temp_file_path):
    """
    @param if_include_shape:
    @param uuid:
    @param temp_file_path:
    """
    pdf_obj = None
    with fitz.open(temp_file_path) as pdf_obj:
        # pdf_obj = fitz.open(temp_file_path)
        for pid, one_page in enumerate(pdf_obj, start=1):
            raw = one_page.get_pixmap()
            raw = None
    return 1


def test_get_cdrawings(temp_file_path):
    """
    @param if_include_shape:
    @param uuid:
    @param temp_file_path:
    """
    pdf_obj = None
    with fitz.open(temp_file_path) as pdf_obj:
        # pdf_obj = fitz.open(temp_file_path)
        for pid, one_page in enumerate(pdf_obj, start=1):
            raw = one_page.get_cdrawings()
            raw = None
    return 1


def test_get_images(temp_file_path):
    """
    @param if_include_shape:
    @param uuid:
    @param temp_file_path:
    """
    pdf_obj = None
    with fitz.open(temp_file_path) as pdf_obj:
        # pdf_obj = fitz.open(temp_file_path)
        for pid, one_page in enumerate(pdf_obj, start=1):
            raw = one_page.get_images()
            raw = None
    return 1


def test_get_image_info(temp_file_path):
    """
    @param if_include_shape:
    @param uuid:
    @param temp_file_path:
    """
    pdf_obj = None
    with fitz.open(temp_file_path) as pdf_obj:
        # pdf_obj = fitz.open(temp_file_path)
        for pid, one_page in enumerate(pdf_obj, start=1):
            raw = one_page.get_image_info()
            raw = None
    return 1


def test_get_clip_pixmap(temp_file_path):
    """
    @param if_include_shape:
    @param uuid:
    @param temp_file_path:
    """
    pdf_obj = None
    with fitz.open(temp_file_path) as pdf_obj:
        # pdf_obj = fitz.open(temp_file_path)
        for pid, one_page in enumerate(pdf_obj, start=1):
            ie = pdf2docx.ImagesExtractor.ImagesExtractor(one_page)
            try:
                pix = ie.clip_page_to_pixmap()
                pix = None
            except:
                break
    return 1


def test_pdf2docx(file):
    pdf2docx.parse(file)


def init_logger():
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(f"{__file__}.log", mode="w")
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


logger = init_logger()

process = psutil.Process()
stats = [1] * 30
stats[0] = process.memory_info().rss

logger.info(f"{stats[0]/1024/1024:.3f}MB initial")

for i in range(1, 30):
    for f in os.listdir(files):
        file = os.path.join(files, f)

        test_get_text(file)
        pymupdf.TOOLS.store_shrink(100)
        gc.collect()

        # test_get_texttrace(file)
        # pymupdf.TOOLS.store_shrink(100)
        # gc.collect()

        # test_get_pixmap(file)
        # pymupdf.TOOLS.store_shrink(100)
        # gc.collect()

        # test_get_cdrawings(file)
        # pymupdf.TOOLS.store_shrink(100)
        # gc.collect()

        # test_get_images(file)
        # pymupdf.TOOLS.store_shrink(100)
        # gc.collect()

        # test_get_image_info(file)
        # pymupdf.TOOLS.store_shrink(100)
        # gc.collect()

        # test_get_clip_pixmap(file)
        # pymupdf.TOOLS.store_shrink(100)
        # gc.collect()

        # test_pdf2docx(file)
        # pymupdf.TOOLS.store_shrink(100)
        # gc.collect()

        # stats[i] = process.memory_info().rss
        # logger.info(f'{i} {stats[0]/1024/1024:.3f}MB -> {stats[i]/1024/1024:.3f}MB, {100*stats[i]/stats[0]:.4f}% ↑')

        stats[i] = process.memory_info().rss
        logger.info(
            f"{i} {stats[0]/1024/1024:.3f}MB -> {stats[i]/1024/1024:.3f}MB, {100*stats[i]/stats[0]:.4f}% ↑"
        )


logger.info(stats)
logger.info(
    f"{stats[0]/1024/1024:.3f}MB -> {stats[-1]/1024/1024:.3f}MB, {100*stats[-1]/stats[0]:.4f}% ↑"
)
# time.sleep(120)
