# System
import json
from .stage01_isotopomer_peakSpectrum_query import stage01_isotopomer_peakSpectrum_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_isotopomer_peakSpectrum_io(stage01_isotopomer_peakSpectrum_query,sbaas_template_io):
    def import_dataStage01IsotopomerPeakSpectrum_add(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01IsotopomerPeakSpectrum(data.data);
        data.clear_data();

    def import_dataStage01IsotopomerPeakSpectrum_update(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01IsotopomerPeakSpectrum(data.data);
        data.clear_data();