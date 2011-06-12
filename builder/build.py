# JSBuilder example

# project name (from the root folder)
copyright = ''
max_js = 'dist/jschardet.js'
min_js = 'dist/jschardet.min.js'

# file list (from the root/src folder)
files = [
"init.js",
 "constants.js",
 "codingstatemachine.js",
 "escsm.js",
 "mbcssm.js",
    
 "charsetprober.js",
 "mbcharsetprober.js",
    
 "jisfreq.js",
 "gb2312freq.js",
 "euckrfreq.js",
 "big5freq.js",
 "euctwfreq.js",
 "chardistribution.js",
    
 "jpcntx.js",
 "sjisprober.js",
 "utf8prober.js",
 "charsetgroupprober.js",
    
 "eucjpprober.js",
 "gb2312prober.js",
 "euckrprober.js",
 "big5prober.js",
 "euctwprober.js",
 "mbcsgroupprober.js",
    
 "sbcharsetprober.js",
    
 "langgreekmodel.js",
 "langthaimodel.js",
 "langbulgarianmodel.js",
 "langcyrillicmodel.js",
 "hebrewprober.js",
 "langhebrewmodel.js",
 "langhungarianmodel.js",
 "sbcsgroupprober.js",
    
 "latin1prober.js",
 "escprober.js",
 "universaldetector.js"
 ]

# execute the task
import JSBuilder
JSBuilder.compile(
    copyright,
    max_js,
    min_js,
    files
)

# let me read the result ...
import time
time.sleep(2)