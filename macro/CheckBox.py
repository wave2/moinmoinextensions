#format python
# -*- coding: iso-8859-1 -*-
'''
    MoinMoin - CheckBox Macro
    Author: Alan Snelson
    @copyright: 2011-2012 by Alan Snelson
    @license: BSD, see LICENSE for details.

    Purpose: To provide an on/off checkbox icon
'''

import os, StringIO
from MoinMoin.Page import Page

def countcheck(fname):
    #saved in PageName/attachments and can be viewed as normal attachments
    try:
        f = open(fname, 'r')
        result = int(f.read())
        f.close()
    except:
        result = 0
    return result

def savecheck(fname, checknum):
    try:
        f = open(fname, 'w')
        f.write(str(checknum))
        f.close()
        return True
    except:
        return False

def execute(macro, args):
    thisPage = macro.formatter.page
    thisPageName = thisPage.page_name
    thisUrl = thisPage.url(macro.request)
    thisForm = macro.request.values
    fname = os.path.join(thisPage.getPagePath("attachments"), 'Check-' + str(args) + ".txt")

    src_cross = 'http://mywiki/moin_static194/modern/img/cross.png'
    src_tick = 'http://mywiki/moin_static194/modern/img/tick.png'

    formname = 'C' + args + 'form'
    checkval = 'C' + args + 'val'
    result=''

    if thisForm.has_key(checkval):
        checknum=int(thisForm[checkval][0])
        if not savecheck(fname,checknum):
            result += "Error saving file!"
    else:
        checknum=countcheck(fname)

    result += '<a name="%s">' % args
    result += '<table width="30"><tr><form method="get" name=%(formname)s action="%(url)s#%(anc)s">' % {
        'url': thisUrl, 'anc': args, 'formname':formname}
    result += '<input type="hidden" name=%s value=1>' % checkval
    btncheck = '<input type="image" src=%(src)s OnClick="document.%(form)s.%(name)s.value=%(value)s">'
    if checknum == 0:
        result += btncheck % {'src':src_cross, 'form':formname, 'name':checkval, 'value': 1}
    else:
        result += btncheck % {'src':src_tick, 'form':formname, 'name':checkval, 'value': 0}
    result += '</form></tr></table></a>'
    return result
