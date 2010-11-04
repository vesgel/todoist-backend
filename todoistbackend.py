#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010, Volkan Esgel
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

"""
A todoist backend which is written in Python.
Please read the README file for more information.
"""

import urllib


class Iface:
    def __init__(self):
        self.baseurl = "https://todoist.com/API/"

    def login(self, email, password):
        lasturl = 'login?' + urllib.urlencode({ 'email' : email,
                                                'password' : password })

        return self._getData(lasturl, "dict")

    def getTimezones(self):
        lasturl = 'getTimezones'
        return self._getData(lasturl)

    def register(self, email, fullname, password, timezone):
        # untested yet
        lasturl = 'register?' + urllib.urlencode({ 'email' : email,
                                                   'full_name' : fullname,
                                                   'password' : password,
                                                   'timezone' : timezone })

        return self._getData(lasturl, "dict")

    def updateUser(self, token, email=None, full_name=None, password=None, timezone=None):
        lasturl = 'updateUser?' + urllib.urlencode({ 'token' : token })

        optional_parameters = { 'email' : email,
                                'full_name' : full_name,
                                'password' : password,
                                'timezone' : timezone }

        for param in optional_parameters.items():
            if not param[1] == None:
                lasturl += "&%s=%s" % (param[0], param[1])

        return self._getData(lasturl, "dict")

    def getProjects(self, token):
        lasturl = 'getProjects?' + urllib.urlencode({ 'token' : token })

        return self._getData(lasturl, "dict")

    def getProject(self, token, project_id):
        lasturl = 'getProject?' + urllib.urlencode({ 'token' : token,
                                                     'project_id': project_id })

        return self._getData(lasturl, "dict")

    def addProject(self, token, name, color=None, indent=None, order=None):
        lasturl = 'addProject?' + urllib.urlencode({ 'token' : token,
                                                     'name' : name })

        optional_parameters = { 'color' : color,
                                'indent' : indent,
                                'order' : order }

        for param in optional_parameters.items():
            if not param[1] == None:
                lasturl += "&%s=%s" % (param[0], param[1])

        return self._getData(lasturl, "dict")

    def updateProject(self, token, project_id, name=None, color=None, indent=None):
        lasturl = 'updateProject?' + urllib.urlencode({ 'token' : token,
                                                     'project_id' : project_id })

        lasturl = "%s?token=%s&project_id=%s" % ("updateProject", token, project_id)

        optional_parameters = { 'name' : name,
                                'color' : color,
                                'indent' : indent }

        for param in optional_parameters.items():
            if not param[1] == None:
                lasturl += "&%s=%s" % (param[0], param[1])

        return self._getData(lasturl, "dict")

    def deleteProject(self, token, project_id):
        lasturl = 'deleteProject?' + urllib.urlencode({ 'token' : token,
                                                        'project_id' : project_id })

        return self._getData(lasturl)

    def getLabels(self, token, project_id):
        lasturl = 'getLabels?' + urllib.urlencode({ 'token' : token,
                                                    'project_id' : project_id })

        return self._getData(lasturl, "dict")

    def updateLabel(self, token, old_name, new_name):
        lasturl = 'updateLabel?' + urllib.urlencode({ 'token' : token,
                                                      'old_name' : old_name,
                                                      'new_name' : new_name })

        return self._getData(lasturl)

    def deleteLabel(self, token, name):
        lasturl = 'deleteLabel?' + urllib.urlencode({ 'token' : token,
                                                      'name' : name })

        return self._getData(lasturl)

    def getUncompletedItems(self, token, project_id):
        lasturl = 'getUncompletedItems?' + urllib.urlencode({ 'token': token,
                                                              'project_id' : project_id })

        return self._getData(lasturl, "dict")

    def getCompletedItems(self, token, project_id):
        lasturl = 'getCompletedItems?' + urllib.urlencode({ 'token' : token,
                                                            'project_id' : project_id })

        return self._getData(lasturl, "dict")

    def getItemsById(self, token, ids):
        lasturl = 'getItemsById?' + urllib.urlencode({ 'token' : token,
                                                       'ids' : ids })

        return self._getData(lasturl, "dict")

    def addItem(self, token, project_id, content, date_string=None, priority=None):
        lasturl = 'addItem?' + urllib.urlencode({ 'token' : token,
                                                  'project_id' : project_id,
                                                  'content' : content })

        optional_parameters = { 'date_string' : date_string,
                                'priority' : priority }

        for param in optional_parameters.items():
            if not param[1] == None:
                lasturl += "&%s=%s" % (param[0], param[1])

        return self._getData(lasturl, "dict")

    def updateItem(self, token, id, content=None, date_string=None, priority=None, indent=None, item_order=None):
        lasturl = 'updateItem?' + urllib.urlencode({ 'token' : token,
                                                     'id' : id })
        #lasturl = "%s?token=%s&id=%s" % ("updateItem", token, id)

        optional_parameters = { 'content' : content,
                                'date_string' : date_string,
                                'priority' : priority,
                                'indent' : indent,
                                'item_order' : item_order }

        for param in optional_parameters.items():
            if not param[1] == None:
                lasturl += "&%s=%s" % (param[0], param[1])

        return self._getData(lasturl, "dict")

    def updateOrders(self, token, project_id, item_id_list):
        lasturl = 'updateOrders?' + urllib.urlencode({ 'token' : token,
                                                       'project_id' : project_id,
                                                       'items_id_list' : items_id_list })

        return self._getData(lasturl)

    def deleteItems(self, token, ids):
        lasturl = 'deleteItems?' + urllib.urlencode({ 'token' : token,
                                                      'ids' : ids })

        return self._getData(lasturl)

    def completeItems(self, token, ids):
        lasturl = 'completeItems?' + urllib.urlencode({ 'token' : token,
                                                        'ids' : ids })

        return self._getData(lasturl)

    def uncompleteItems(self, token, ids):
        lasturl = 'uncompleteItems?' + urllib.urlencode({ 'token' : token,
                                                          'ids' : ids})

        return self._getData(lasturl)

    def query(self, token, queries):
        lasturl = 'query?' + urllib.urlencode({ 'token' : token,
                                                'queries' : queries })

        return self._getData(lasturl)



    def _getData(self, lasturl, return_type=None):
        url = self.baseurl + lasturl
        socket = urllib.urlopen(url)

        if return_type == "dict":
            data = self._convertStrToDict(socket.read())
        else:
            data = socket.read()

        return data

    def _convertStrToDict(self, string):
        return eval(string.replace("null", "None"))
