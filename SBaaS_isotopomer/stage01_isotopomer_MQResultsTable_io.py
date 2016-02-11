# System
import json
from .stage01_isotopomer_MQResultsTable_query import stage01_isotopomer_MQResultsTable_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from quantification_analysis.MQResultsTable import MQResultsTable

class stage01_isotopomer_MQResultsTable_io(stage01_isotopomer_MQResultsTable_query,sbaas_template_io):
    def import_dataStage01IsotopomerMQResultsTable_add(self,filename):
        '''table adds'''

        #OPTION1:
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01IsotopomerMQResultsTable(data.data);
        data.clear_data();
        ##OPTION2: 
        #resultstable = MQResultsTable();
        #resultstable.import_resultsTable(filename);
        #self.add_dataStage01IsotopomerMQResultsTable(resultstable.resultsTable);
    
    def import_dataStage01IsotopomerMQResultsTable_update(self,filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01IsotopomerMQResultsTable(data.data);
        data.clear_data();