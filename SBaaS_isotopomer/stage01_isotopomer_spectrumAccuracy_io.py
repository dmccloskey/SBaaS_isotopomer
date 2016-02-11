# System
import json
from .stage01_isotopomer_spectrumAccuracy_query import stage01_isotopomer_spectrumAccuracy_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_isotopomer_spectrumAccuracy_io(stage01_isotopomer_spectrumAccuracy_query,sbaas_template_io):
    def export_compareAveragesSpectrumToTheoretical(self, experiment_id_I, filename, sample_name_abbreviations_I=None,scan_types_I=None,met_ids_I = None):
        '''export a comparison of calculated spectrum to theoretical spectrum'''
        # query the data
        data = [];
        # get time points
        time_points = self.get_timePoint_experimentID_dataStage01Averages(experiment_id_I);
        for tp in time_points:
            print('Reporting average precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            if sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                # query sample types from sample name abbreviations and time-point from _dataStage01Averages
            else:
                # get sample names and sample name abbreviations
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01Averages(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Reporting average precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
                # get the scan_types
                if scan_types_I:
                    scan_types = [];
                    scan_types_tmp = [];
                    scan_types_tmp = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Averages(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                    scan_types = [st for st in scan_types_tmp if st in scan_types_I];
                else:
                    scan_types = [];
                    scan_types = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Averages(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                for scan_type in scan_types:
                    print('Reporting average precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Averages( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Reporting average precursor and product spectrum for metabolite ' + met);
                        data_tmp = [];
                        data_tmp = self.get_dataPrecursorFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01Averages(\
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        data.extend(data_tmp);
                        data_tmp = [];
                        data_tmp = self.get_dataProductFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01Averages(\
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        data.extend(data_tmp);
        # write the comparison to file
        headerL1 = ['sample_name_abbreviation','time_point','met_id','fragment_formula','C_pos','scan_type','theoretical'] + ['' for i in range(49)]\
            + ['measured'] + ['' for i in range(49)]\
            + ['measured_cv'] + ['' for i in range(49)]\
            + ['abs_difference'] + ['' for i in range(49)];
        headerL2 = ['' for i in range(6)] + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)];
        header = [];
        header.append(headerL1);
        header.append(headerL2);
        export = base_exportData(data);
        export.write_headersAndElements2csv(header,filename);
    def export_compareAveragesNormSumSpectrumToTheoretical(self, experiment_id_I, filename, sample_name_abbreviations_I=None,scan_types_I=None,met_ids_I = None):
        '''export a comparison of calculated spectrum to theoretical spectrum'''
        # query the data
        data = [];
        # get time points
        time_points = self.get_timePoint_experimentID_dataStage01AveragesNormSum(experiment_id_I);
        for tp in time_points:
            print('Reporting average precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            if sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                # query sample types from sample name abbreviations and time-point from data_stage01_isotopomer_normalized
            else:
                # get sample names and sample name abbreviations
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01AveragesNormSum(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Reporting average precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
                # get the scan_types
                if scan_types_I:
                    scan_types = [];
                    scan_types_tmp = [];
                    scan_types_tmp = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01AveragesNormSum(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                    scan_types = [st for st in scan_types_tmp if st in scan_types_I];
                else:
                    scan_types = [];
                    scan_types = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01AveragesNormSum(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                for scan_type in scan_types:
                    print('Reporting average precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Reporting average precursor and product spectrum for metabolite ' + met);
                        data_tmp = [];
                        data_tmp = self.get_dataPrecursorFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum(\
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        data.extend(data_tmp);
                        data_tmp = [];
                        data_tmp = self.get_dataProductFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum(\
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        data.extend(data_tmp);
        # write the comparison to file
        headerL1 = ['sample_name_abbreviation','time_point','met_id','fragment_formula','C_pos','scan_type','theoretical'] + ['' for i in range(49)]\
            + ['measured'] + ['' for i in range(49)]\
            + ['measured_cv'] + ['' for i in range(49)]\
            + ['abs_difference'] + ['' for i in range(49)]\
            + ['average_accuracy'];
        headerL2 = ['' for i in range(6)] + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + ['a' + str(i) for i in range(50)]\
            + [''];
        header = [];
        header.append(headerL1);
        header.append(headerL2);
        export = base_exportData(data);
        export.write_headersAndElements2csv(header,filename);
   