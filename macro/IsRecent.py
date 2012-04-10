# -*- coding: iso-8859-1 -*-
u"""
    IsRecent - Check if a page was recently modified and highlight that fact

    @copyright: 2012 by Alan Snelson
    @license: BSD, see LICENSE for details.

"""

from datetime import datetime
from MoinMoin.Page import Page

Dependencies = ['pages']

def macro_IsRecent(macro, pageName=''):
  fmt = macro.formatter
  if (pageName == ''):
    return fmt.text('No page supplied')

  request = macro.request
  page = Page(request,pageName)
  log = page.lastEditInfo(request)
  now = datetime.now()
  delta = now - datetime.strptime(log['time'], "%Y-%m-%d %H:%M:%S")
  if (delta.days > 7):
      return fmt.rawHTML("<a href='http://mywiki" + pageName + "'>" + pageName + "</a>")
  else:
      return fmt.rawHTML("<a style='color:black;font-size:20px;' href='http://mywiki" + pageName + "'>" + pageName + "</a>")
