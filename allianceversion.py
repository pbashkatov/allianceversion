#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import re
import platform
#----------------------------------------------------------------------------
def fmtprt(str1, str2, len, val) :
    a = (str1 + ' ' + str2).ljust(len, ' ') + ':'
    print(a, val)
#----------------------------------------------------------------------------
def get_str(mask, text) :
    regex = mask + r'(.*)\n'
    try :    
        return re.compile(regex).search(text).group(1)
    except :
        return ''
#----------------------------------------------------------------------------
def get_info(swprod) :
    if swprod == 'Access' :
        swprod_instpro = path_saa + instpro
    if swprod == 'Entry' :
        swprod_instpro = path_sae + instpro
    if swprod == 'Gateway' :
        swprod_instpro = path_sag + instpro
    if swprod == 'WebPlatform' :
        swprod_instpro = path_swp + instpro
        
    swprod_instpro_text = open(swprod_instpro, 'rt').read()
  
    app_owner = get_str(r'application.owner.name=', swprod_instpro_text)
    if app_owner :
        fmtprt(swprod, 'Owner Name', 33, app_owner)
        
    app_owner_name_cred = get_str(r'application.owner.name.credentials=', swprod_instpro_text)
    if app_owner_name_cred :
        fmtprt(swprod, 'Owner Credentials', 33, app_owner_name_cred)
  
    swprod_base = get_str(r'application.base.buildnumber=', swprod_instpro_text)
    if swprod_base :
        fmtprt(swprod, 'Base Version', 33, swprod_base)

    saa_delta_base = get_str(r'application.delta.base=', swprod_instpro_text)
    if saa_delta_base :
        fmtprt(swprod, 'Delta Base Version', 33, saa_delta_base)

    saa_delta_patch = get_str(r'application.delta.patch.version=', swprod_instpro_text)
    if saa_delta_patch :
        fmtprt(swprod, 'Delta Patch Version', 33, saa_delta_patch)

    num_of_patches = get_str(r'application.patches.count=', swprod_instpro_text)
    if num_of_patches :
        print('\nNumber of patches installed:', num_of_patches)
        i = 0
        while 1 :
            app_patch_bldnum = get_str(r'application.patches\[' + str(i) + r'\].buildnumber=', swprod_instpro_text)
            app_patch_vrsn = get_str(r'application.patches\[' + str(i) + r'\].version=', swprod_instpro_text)
            i += 1
            if app_patch_bldnum == '' :
                break
            print('(' + str(i) + ')', 'build number :', app_patch_bldnum, '\tversion :', app_patch_vrsn)

    num_of_secupd = get_str(r'security.update.count=', swprod_instpro_text)
    if num_of_secupd :
        print('\nNumber of security updates installed :', num_of_secupd)
        i = 0
        while 1 :
            secupd = get_str(r'security.update\[' + str(i) + r'\]=', swprod_instpro_text)
            i += 1
            if secupd == '' :
                break
            print('(' + str(i) + ')', 'update version :', secupd)
#----------------------------------------------------------------------------       
opersys = platform.system()

swift_path = 'swift'
if opersys== 'Windows':
   swift_path = 'C:\\Program Files (x86)\\Common Files\\swift'
   instpro = '\\data\\installation.properties'
elif opersys == 'Linux' :
    swift_path = '/var/opt/swift'
    instpro = '/data/installation.properties'
elif opersys == 'AIX' :
    swift_path = '/var/opt/swift'
    instpro = '/data/installation.properties'
elif opersys == 'Soralis' :
    swift_path = '/var/opt/swift'
    instpro = '/data/installation.properties'
else :
    swift_path = 'Unknown platform -- exiting'
    sys.exit()

is_saa = False
is_sae = False
is_sag = False
is_snl = False
is_swp = False
path_saa = ''
path_sae = ''
path_sag = ''
path_snl = ''
path_swp = ''

for name in os.listdir(swift_path) :
    file_name = os.path.join(swift_path, name)
    if os.path.isfile(file_name) :
        if file_name.find('sae') > -1 :
            is_sae = True
            path_sae = open(file_name, 'r').read()
        if file_name.find('saa') > -1 :
            is_saa = True
            path_saa = open(file_name, 'r').read()
        elif file_name.find('sag') > -1 :
            is_sag = True
            path_sag = open(file_name, 'r').read() 
        elif file_name.find('swpe') > -1 :
            is_swp = True
            path_swp = open(file_name, 'r').read() 
        elif file_name.find('snl') > -1 :
            is_snl = True
            path_snl = open(file_name, 'r').read() 

print('\n=====     Found installed SWIFTAlliance products     =====\n')
if is_snl :
    print('SWIFTNet Link'.ljust(40, ' '),':', path_snl)
if is_sag :
    print('SWIFTAlliance Gateway'.ljust(40, ' '),':', path_sag)
if is_saa :
    print('SWIFTAlliance Access'.ljust(40, ' '),':', path_saa)
if is_sae :
    print('SWIFTAlliance Entry'.ljust(40, ' '),':', path_saa)
if is_swp :
    print('SWIFTAlliance WebPlatform'.ljust(40, ' '),':', path_swp)

if is_snl :
    print('\n=====     SWIFTNet Link     =====\n')
    print("for SNL version info use 'swiftnet version -a' command from SNL command line")
    print('this command must be run under the SNL owner credentials')
if is_sag :
    print('\n=====     SWIFTAlliance Gateway     =====\n')
    get_info('Gateway')
if is_saa :
    print('\n=====     SWIFTAlliance Access     =====\n')
    get_info('Access')
if is_sae :
    print('\n=====     SWIFTAlliance Entry     =====\n')
    get_info('Entry')
if is_swp :
    print('\n=====     SWIFTAlliance WebPlatform     =====\n')
    get_info('WebPlatform')
