#!/usr/bin/env python


# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# NOTE: you must have a localconstants.py that, minimally, defines
# BASE_DIR; all your checkouts should be under BASE_DIR, ie
# BASE_DIR/aaa BASE_DIR/bbb etc.
from localconstants import *

ANALYZER='org.apache.lucene.analysis.en.EnglishAnalyzer'

BENCH_BASE_DIR = '%s/util' % BASE_DIR
WIKI_LINE_FILE = '%s/data/enwiki-20100302-pages-articles-lines-1k.txt' % BASE_DIR
WIKI_FILE = '%s/data/enwiki-20100302-pages-articles.xml.bz2' % BENCH_BASE_DIR
INDEX_DIR_BASE = '%s/indices' % BASE_DIR
JAVA_COMMAND = 'java -Xbatch -Xms1g -Xmx1g -client'
JRE_SUPPORTS_SERVER_MODE = True
INDEX_NUM_THREADS = 2

# import again in case you want to override any of the vars set above
from localconstants import *