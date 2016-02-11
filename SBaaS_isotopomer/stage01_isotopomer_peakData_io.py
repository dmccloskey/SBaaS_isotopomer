# System
import json
from .stage01_isotopomer_peakData_query import stage01_isotopomer_peakData_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_isotopomer_peakData_io(stage01_isotopomer_peakData_query,sbaas_template_io):

    def import_peakData_add(self, filename, experiment_id, samplename, precursor_formula, met_id,
                            mass_units_I='Da',intensity_units_I='cps', scan_type_I='EPI', header_I=True,
                            add_data_I=True):
        '''table adds'''
        data = base_importData();
        try:
            data.read_tab_fieldnames(filename,['Mass/Charge','Intensity'],header_I);
            #data.read_tab_fieldnames(filename,['mass','intensity','intensity_percent'],header_I);
            data.format_data();
            if add_data_I:
                self.add_peakData(data.data, experiment_id, samplename, precursor_formula, met_id,
                              mass_units_I,intensity_units_I, scan_type_I);
            data.clear_data();
        except IOError as e:
            print(e);

    def import_peakList_add(self, filename, experiment_id, samplename, precursor_formula, met_id,
                            mass_units_I='Da',intensity_units_I='cps', 
                            centroid_mass_units_I='Da', peak_start_units_I='Da',
                            peak_stop_units_I='Da', resolution_I=None, scan_type_I='EPI'):
        '''table adds'''
        data = base_importData();
        data.read_tab_fieldnames(filename,['mass','centroid_mass','intensity','peak_start','peak_end','width','intensity_percent']);
        data.format_data();
        self.add_peakList(data.data, experiment_id, samplename, met_id,
                          mass_units_I,intensity_units_I, scan_type_I);
        data.clear_data();