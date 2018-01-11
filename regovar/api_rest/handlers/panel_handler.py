 
#!env/python3
# coding: utf-8
import ipdb; 


import os
import json
import aiohttp
import datetime
import time


from aiohttp import web

from config import *
from core.framework.common import *
from core.framework.tus import *
from core.model import *
from api_rest.rest import *





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# PANEL HANDLER
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 





class PanelHandler:



    def list(self, request):
        """
            Get list of all panels (allow search parameters)
        """
        from core.core import core
        fields, query, order, offset, limit = process_generic_get(request.query_string, Panel.public_fields)
        depth = 0
        # Get range meta data
        range_data = {
            "range_offset" : offset,
            "range_limit"  : limit,
            "range_total"  : Subject.count(),
            "range_max"    : RANGE_MAX,
        }
        panels = core.panels.get(fields, query, order, offset, limit, depth)
        return rest_success([p.to_json() for p in panels], range_data)


        
    
    async def create_or_update(self, request):
        """
            Create or update a panel with provided data
        """
        from core.core import core
        panel_id = request.match_info.get('panel_id', -1)
        data = await request.json()

        if isinstance(data, str) : data = json.loads(data)
        # If provided by the query parameter, ensure that we use the query panel_id
        if panel_id != -1:
        	data["id"] = panel_id
        # Create or update the panel
        try:
            panel = core.panels.create_or_update(data)
        except RegovarException as ex:
            return rest_exception(ex)
        if panel is None:
            return rest_error("Unable to create a new panel.")
        return rest_success(panel.to_json())
        
        
    def get(self, request):
        """
            Get details about the panel
        """
        panel_id = request.match_info.get('panel_id', -1)
        version = request.match_info.get('version', "")
        panel = Panel.from_id(panel_id, 1)
        if not panel:
            return rest_error("Unable to find the panel (id={})".format(panel_id))
        return rest_success(panel.to_json())
        
    
    
    
    def delete(self, request):
        """
            Delete the panel
        """
        from core.core import core
        panel_id = request.match_info.get('panel_id', -1)
        panel = core.panels.delete(panel_id)
        if not panel:
            return rest_error("Unable to delete the panel (id={})".format(panel_id))
        return rest_success(panel.to_json())
    
    



    def search(self, request):
        """
            Search gene and phenotype that match the query (used to help user to populate panel regions)
        """
        search_query = request.match_info.get('query', None)
        if search_query is None :
            return rest_error("Nothing to search...")
        
        try:
            result = core.panels.search(search_query)
        except RegovarException as ex:
            return rest_error("Error occured while trying to search", e)
        
        return rest_success(result)
    
    
    
    def import_file(self, request):
        """
            Import region from a bed file already in database
        """
        pass











