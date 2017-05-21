# Copyright (c) 2002-2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Revision$
import urllib.request, urllib.parse, urllib.error

def add_and_edit(self, id, REQUEST):
    """Helper function to point to the object's management screen if
    'Add and Edit' button is pressed.
    id -- id of the object we just added
    """
    if REQUEST is None:
        return
    try:
        u = self.DestinationURL()
    except:
        u = REQUEST['URL1']
    if 'submit_edit' in REQUEST:
        u = "%s/%s" % (u, urllib.parse.quote(id))
    REQUEST.RESPONSE.redirect(u+'/manage_main')
