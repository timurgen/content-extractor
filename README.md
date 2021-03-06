[![Build Status](https://travis-ci.org/sesam-community/content-extractor2.svg?branch=master)](https://travis-ci.org/sesam-community/content-extractor2)

# content-extractor

Simple Apache Tika and Tesseract OCR powered file content extractor service. Service runs on port 5000 by default and has two endpoints:  

* post_file_list - consumes POST request with one or more files
* post_json_list - consumes POST request with JSON payload which contains URL's to files needed to be downloaded and parsed

To run it on local machine Python 3+, Java 8+, Tesseract and Norwegian language support for Tesseract needed. 

### configuration options: 

All configuration options passes via environmental variables.   
* TIKA_VERSION = 1.20 (required)
* UPLOAD_URL - where to upload parsed data (only for post_json_list endpoint). All files will preserve their names with ".txt" added
* FILE_URL - which data entity attribute contains url to file
* FILE_NAME - which data entity attribute contains name of file
* LOG_LEVEL - logging level ("INFO" by default)
* FAIL_ON_ERROR - If need fail fast on parsing or other processing errors or not. True by default
* TESSERACT_OCR_LANG - Language(s) to be used by tesseract OCR (need to be installed)
* PDF_EXTRACT_INLINE_IMG instruct Tika to retrieve text from images in PDF file true/fals, true by default
* PRESERVE_FILE_TYPE if resulted file name will carry information about original file type or not, False by default
