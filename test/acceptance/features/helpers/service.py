# -*- coding: utf-8 -*-
# Copyright (c) 2013, 2014 Corvusoft

from ctypes import *

library = cdll.LoadLibrary('distribution/library/libhelpers.dylib')

class Service(object):
    def __init__(self, port):
    	library.create_service.restype = c_void_p
        self.obj = library.create_service(port)

    def __del__(self):
    	library.release_service.argtypes = [c_void_p]
        library.release_service(self.obj)

    def publish_method_handler(self, path, method):
        library.publish_method_handler.argtypes = [c_void_p, c_char_p, c_char_p]
    	library.publish_method_handler(self.obj, path, method)

    def publish_json_resource(self, path):
        library.publish_json_resource.argtypes = [c_void_p, c_char_p]
    	library.publish_json_resource(self.obj, path)

    def publish_xml_resource(self, path):
        library.publish_xml_resource.argtypes = [c_void_p, c_char_p]
    	library.publish_xml_resource(self.obj, path)

    def publish_api_1_0_resource(self, path):
        library.publish_api_1_0_resource.argtypes = [c_void_p, c_char_p]
    	library.publish_api_1_0_resource(self.obj, path)

    def publish_api_1_1_resource(self, path):
        library.publish_api_1_1_resource.argtypes = [c_void_p, c_char_p]
    	library.publish_api_1_1_resource(self.obj, path)