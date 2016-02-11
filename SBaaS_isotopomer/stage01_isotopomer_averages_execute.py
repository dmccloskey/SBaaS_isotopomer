#SBaaS
from .stage01_isotopomer_averages_io import stage01_isotopomer_averages_io
from .stage01_isotopomer_normalized_query import stage01_isotopomer_normalized_query
#Resources
from MDV_utilities.mass_isotopomer_distributions import mass_isotopomer_distributions
#Remove after refactor
from .stage01_isotopomer_averages_postgresql_models import *
import numpy
import re
from molmass.molmass import Formula

class stage01_isotopomer_averages_execute(stage01_isotopomer_averages_io,
                                          stage01_isotopomer_normalized_query):
    def execute_analyzeAverages(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average normalized intensity for MRM samples'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''

        mids = mass_isotopomer_distributions();
        print('execute_analyzeAverages...')
        # get time points
        time_points = self.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Calculating average precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
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
                sample_types_lst = ['Unknown' for x in sample_abbreviations];
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
                print('Calculating average precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
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
                    print('Calculating average precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Calculating average precursor and product spectrum for metabolite ' + met);
                        ## get fragment formulas and masses
                        #fragment_formulas, fragment_masses = [],[];
                        #fragment_formulas,fragment_masses = self.get_fragmentFormulasAndMass_experimentIDAndSampleAbbreviationAndTimePointAndAndSampleTypeAndScanTypeAndMetID_dataStage01Normalized(experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        #for mass_cnt,mass in enumerate(fragment_masses):
                        #    print 'Calculating average precursor and product spectrum for fragment/mass ' + fragment_formulas[mass_cnt] + '/' + str(mass);
                        #    # get data
                        #    intensities = [];
                        #    intensities = self.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Normalized(experiment_id_I,sna,tp,sample_types_lst[sna_cnt],met,fragment_formulas[mass_cnt],mass,scan_type);
                        #    # calculate the average and cv
                        #    n_replicates = len(intensities);
                        #    intensities_average = 0.0;
                        #    intensities_var = 0.0;
                        #    intensities_cv = 0.0;
                        #    # calculate average and CV of intensities
                        #    if (not(intensities)): 
                        #        #continue
                        #        intensities_average = 0.0;
                        #        intensities_var = 0.0;
                        #        intensities_cv = 0.0;
                        #    elif n_replicates<2: # require at least 2 replicates
                        #        #continue
                        #        intensities_average = 0.0;
                        #        intensities_var = 0.0;
                        #        intensities_cv = 0.0;
                        #    else: 
                        #        intensities_average = numpy.mean(numpy.array(intensities));
                        #        intensities_var = numpy.var(numpy.array(intensities));
                        #        if (intensities_average <= 0.0): intensities_cv = 0.0;
                        #        else: intensities_cv = sqrt(intensities_var)/intensities_average*100;
                        #    # calculate the theoretical spectrum for the pecursor/mass
                        #    peakSpectrum_theoretical = mids.report_fragmentSpectrum_normMax([fragment_formulas[mass_cnt]],True);
                        #    # calculate the absolute deviation from the theoretical
                        #    intensity_theoretical = peakSpectrum_theoretical[fragment_formulas[mass_cnt]][mass];
                        #    if intensity_theoretical > 0.0:abs_devFromTheoretical = abs(intensity_theoretical-intensities_average)/intensity_theoretical*100;
                        #    else: abs_devFromTheoretical = None;
                        #    # add to data_stage01_isotopomer_averages
                        #    row = [];
                        #    row = data_stage01_isotopomer_averages(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,fragment_formulas[mass_cnt], mass,
                        #                                           n_replicates, intensities_average, intensities_cv,
                        #                                           'normMax', intensity_theoretical, abs_devFromTheoretical, scan_type, True)
                        #    self.session.add(row);
                        # get replicates
                        replicate_numbers = [];
                        replicate_numbers = self.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Calculating average precursor and product spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax(peakSpectrum_normalized_lst,True);
                        # update data_stage01_isotopomer_averages
                        for frag,spec in peakSpectrum_theoretical.items():
                            if spec:
                                fragment_str = re.sub('[+-]', '', frag);
                                fragment_mass =  Formula(fragment_str).isotope.mass;
                                for k,v in peakSpectrum_theoretical[frag].items():
                                    if v and k in peakSpectrum_stats[frag]:
                                        if peakSpectrum_stats[frag][k]['mean']> 0.0: intensities_cv = peakSpectrum_stats[frag][k]['stdDev']/peakSpectrum_stats[frag][k]['mean']*100;
                                        else: intensities_cv = 0.0;
                                        row = [];
                                        row = data_stage01_isotopomer_averages(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   peakSpectrum_stats[frag][k]['n'], peakSpectrum_stats[frag][k]['mean'], intensities_cv,
                                                                   'normMax', v, peakSpectrum_stats[frag][k]['absDev'], scan_type, True);
                                    elif v and k not in peakSpectrum_stats[frag]:
                                        intensities_cv = None;
                                        row = [];
                                        row = data_stage01_isotopomer_averages(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   None, None, intensities_cv,
                                                                   'normMax', v, None, scan_type, True);
                                    elif not v and k in peakSpectrum_stats[frag]:
                                        if peakSpectrum_stats[frag][k]['mean']> 0.0: intensities_cv = peakSpectrum_stats[frag][k]['stdDev']/peakSpectrum_stats[frag][k]['mean']*100;
                                        else: intensities_cv = 0.0;
                                        row = [];
                                        row = data_stage01_isotopomer_averages(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   peakSpectrum_stats[frag][k]['n'], peakSpectrum_stats[frag][k]['mean'], intensities_cv,
                                                                   'normMax', None, peakSpectrum_stats[frag][k]['absDev'], scan_type, True);
                                    self.session.add(row);
            self.session.commit();
    def execute_analyzeAveragesNormSum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average normalized intensity for all samples and scan types'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''

        mids = mass_isotopomer_distributions();
        
        print('execute_analyzeAveragesNormSum...')
        # get time points
        time_points = self.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Calculating average precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
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
                sample_types_lst = ['Unknown' for x in sample_abbreviations];
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
                print('Calculating average precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
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
                    print('Calculating average precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Calculating average precursor and product spectrum for metabolite ' + met);
                        # get replicates
                        replicate_numbers = [];
                        replicate_numbers = self.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Calculating average precursor and product spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normSum(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normSum(peakSpectrum_normalized_lst,True);
                        # update data_stage01_isotopomer_normalized
                        for frag,spec in peakSpectrum_theoretical.items():
                            if spec:
                                fragment_str = re.sub('[+-]', '', frag);
                                fragment_mass =  Formula(fragment_str).isotope.mass;
                                for k,v in peakSpectrum_theoretical[frag].items():
                                    if v and k in peakSpectrum_stats[frag]:
                                        if peakSpectrum_stats[frag][k]['mean']> 0.0: intensities_cv = peakSpectrum_stats[frag][k]['stdDev']/peakSpectrum_stats[frag][k]['mean']*100;
                                        else: intensities_cv = 0.0;
                                        row = [];
                                        row = data_stage01_isotopomer_averagesNormSum(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   peakSpectrum_stats[frag][k]['n'], peakSpectrum_stats[frag][k]['mean'], intensities_cv,
                                                                   'normSum', v, peakSpectrum_stats[frag][k]['absDev'], scan_type, True);
                                    elif v and k not in peakSpectrum_stats[frag]:
                                        intensities_cv = None;
                                        row = [];
                                        row = data_stage01_isotopomer_averagesNormSum(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   None, None, intensities_cv,
                                                                   'normSum', v, None, scan_type, True);
                                    elif not v and k in peakSpectrum_stats[frag]:
                                        if peakSpectrum_stats[frag][k]['mean']> 0.0: intensities_cv = peakSpectrum_stats[frag][k]['stdDev']/peakSpectrum_stats[frag][k]['mean']*100;
                                        else: intensities_cv = 0.0;
                                        row = [];
                                        row = data_stage01_isotopomer_averagesNormSum(experiment_id_I, sna, sample_types_lst[sna_cnt], tp, met,frag, k,
                                                                   peakSpectrum_stats[frag][k]['n'], peakSpectrum_stats[frag][k]['mean'], intensities_cv,
                                                                   'normSum', None, peakSpectrum_stats[frag][k]['absDev'], scan_type, True);
                                    self.session.add(row);
            self.session.commit();