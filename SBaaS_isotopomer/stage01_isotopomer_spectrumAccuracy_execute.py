#SBaaS
from .stage01_isotopomer_spectrumAccuracy_io import stage01_isotopomer_spectrumAccuracy_io
#Remove after refactor
from .stage01_isotopomer_spectrumAccuracy_postgresql_models import *

class stage01_isotopomer_spectrumAccuracy_execute(stage01_isotopomer_spectrumAccuracy_io):
    def execute_analyzeSpectrumAccuracy(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average spectrum accuracy'''

        mids = mass_isotopomer_distributions();
        
        print('execute_analyzeSpectrumAccuracy...')
        # get time points
        time_points = self.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Calculating spectrum accuracy from isotopomer normalized for time-point ' + str(tp));
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                # query sample types from sample name abbreviations and time-point from data_stage01_isotopomer_normalized
            else:
                # get sample names and sample name abbreviations
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01Normalized(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Calculating spectrum accuracy from isotopomer normalized for sample name abbreviation ' + sna);
                # get the scan_types
                if scan_types_I:
                    scan_types = [];
                    scan_types_tmp = [];
                    scan_types_tmp = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Normalized(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                    scan_types = [st for st in scan_types_tmp if st in scan_types_I];
                else:
                    scan_types = [];
                    scan_types = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Normalized(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                for scan_type in scan_types:
                    print('Calculating spectrum accuracy for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Calculating spectrum accuracy for metabolite ' + met);
                        replicate_numbers = [];
                        replicate_numbers = self.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Calculating spectrum accuracy for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        peakSpectrum_accuracy = mids.calculate_fragmentSpectrumAccuracy(peakSpectrum_normalized_lst);
                        # update data_stage01_isotopomer_spectrumAccuracy
                        for frag,accuracy in peakSpectrum_accuracy.items():
                            if accuracy:
                                row = [];
                                row = data_stage01_isotopomer_spectrumAccuracy(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, accuracy, scan_type, True);
                                self.session.add(row);
            self.session.commit();
    def execute_analyzeSpectrumAccuracyNormSum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average spectrum accuracy'''

        mids = mass_isotopomer_distributions();
        
        print('execute_analyzeSpectrumAccuracy...')
        # get time points
        time_points = self.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Calculating spectrum accuracy from isotopomer normalized for time-point ' + str(tp));
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                # query sample types from sample name abbreviations and time-point from data_stage01_isotopomer_normalized
            else:
                # get sample names and sample name abbreviations
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01Normalized(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Calculating spectrum accuracy from isotopomer normalized for sample name abbreviation ' + sna);
                # get the scan_types
                if scan_types_I:
                    scan_types = [];
                    scan_types_tmp = [];
                    scan_types_tmp = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Normalized(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                    scan_types = [st for st in scan_types_tmp if st in scan_types_I];
                else:
                    scan_types = [];
                    scan_types = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Normalized(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                for scan_type in scan_types:
                    print('Calculating spectrum accuracy for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Calculating spectrum accuracy for metabolite ' + met);
                        replicate_numbers = [];
                        replicate_numbers = self.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Calculating spectrum accuracy for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normSum(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        peakSpectrum_accuracy = mids.calculate_fragmentSpectrumAccuracy_normSum(peakSpectrum_normalized_lst);
                        # update data_stage01_isotopomer_spectrumAccuracy
                        for frag,accuracy in peakSpectrum_accuracy.items():
                            if accuracy:
                                row = [];
                                row = data_stage01_isotopomer_spectrumAccuracyNormSum(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, accuracy, scan_type, True);
                                self.session.add(row);
            self.session.commit();

    