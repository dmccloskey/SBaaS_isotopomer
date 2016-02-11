#SBaaS
from .stage01_isotopomer_peakSpectrum_io import stage01_isotopomer_peakSpectrum_io
from .stage01_isotopomer_peakData_query import stage01_isotopomer_peakData_query
from .stage01_isotopomer_normalized_query import stage01_isotopomer_normalized_query
from SBaaS_LIMS.lims_msMethod_query import lims_msMethod_query
#Resources
from MDV_utilities.mass_isotopomer_distributions import mass_isotopomer_distributions
#Remove after refactor
from .stage01_isotopomer_peakSpectrum_postgresql_models import *
from .stage01_isotopomer_normalized_postgresql_models import *
import numpy
import re
from molmass.molmass import Formula

class stage01_isotopomer_peakSpectrum_execute(stage01_isotopomer_peakSpectrum_io,
                                              stage01_isotopomer_peakData_query,
                                              stage01_isotopomer_normalized_query,
                                              lims_msMethod_query):
    def execute_buildSpectrumFromPeakData(self,experiment_id_I,ms_methodtype_I='isotopomer_13C',sample_name_abbreviations_I = None,met_ids_I = None):
        '''Build spectrum from raw peak data'''

        '''Assumptions:
        Only 1 precursur:spectrum per sample name and
        only 1 precursor:spectrum per dilution
        (i.e. the best/most representative precursor:spectrum was chose from the
        available EPI scans and dilutions of that particular precursor)
        '''

        mids = mass_isotopomer_distributions();

        # extract out the peakSpectrum
        # get sample names for the experiment
        print('execute_buildSpectrumFromPeakData...')
        if sample_name_abbreviations_I:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for sna in sample_name_abbreviations_I:
                for st in sample_types:
                    sample_names_tmp = [];
                    sample_names_tmp = self.get_sampleNames_experimentIDAndSampleTypeAndSampleNameAbbreviation_peakData(experiment_id_I,st,sna);
                    sample_names.extend(sample_names_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        else:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for st in sample_types:
                sample_names_tmp = [];
                sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType_peakData(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
                sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        # create database table
        for sn_cnt,sn in enumerate(sample_names):
            print('building spectrum for sample ' + sn);
            # get other information about the sample for later use
            sample_name_abbreviation,time_point,replicate_numbers = None,None,None;
            sample_name_abbreviation,time_point,replicate_numbers = self.get_sampleNameAbbreviationsAndOther_experimentIDAndSampleName_peakData(experiment_id_I,sn);
            # get met_id and precursor_formula for each sample
            scan_type = [];
            scan_type = self.get_scanType_experimentIDAndSampleName_peakData(experiment_id_I,sn);
            for scantype in scan_type:
                print('building spectrum for scan type ' + scantype);
                # get met_id and precursor formula for each sample
                if met_ids_I:
                    met_id, precursor_formula = [], [];
                    for met in met_ids_I:
                        met_id_tmp, precursor_formula_tmp = [], []
                        met_id_tmp, precursor_formula_tmp = self.get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanTypeAndMetID_peakData(experiment_id_I,sn,scantype,met);
                        met_id.extend(met_id_tmp);
                        precursor_formula.extend(precursor_formula_tmp);
                else:
                    met_id, precursor_formula = [], [];
                    met_id, precursor_formula = self.get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanType_peakData(experiment_id_I,sn,scantype);
                for precursor_cnt, precursor in enumerate(precursor_formula):
                    print('building spectrum for met_id/precursor ' + met_id[precursor_cnt] + '/' + precursor);
                    precursor_str = re.sub('[+-]', '', precursor);
                    precursor_mass =  Formula(precursor_str).isotope.mass
                    # get all product fragments for the met_id/precursor
                    precursor_formulas_monoisotopic, product_formulas = [], [];
                    precursor_formulas_monoisotopic, product_formulas = self.get_precursorAndProductFormulas_metID(met_id[precursor_cnt],'-','tuning');
                    product_formulas.append(precursor_formulas_monoisotopic[0]); # add precursor to list of fragments
                    # get peak data for the sample/met_id/precursor_formula
                    peak_data = [];
                    peak_data = self.get_data_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakData(experiment_id_I,sn,met_id[precursor_cnt],precursor,scantype);
                    peakSpectrum_measured,\
                        peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakData_normMax(\
                        peak_data, product_formulas, 0.3, True);
                    peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                    # update data_stage01_isotopomer_normalized
                    for frag,spec in peakSpectrum_theoretical.items():
                        if spec:
                            product_str = re.sub('[+-]', '', frag);
                            product_mass =  Formula(product_str).isotope.mass;
                            for k,v in peakSpectrum_theoretical[frag].items():
                                row1 = None;
                                row1 = data_stage01_isotopomer_peakSpectrum(experiment_id_I,sn,sample_name_abbreviation,
                                        sample_types_lst[sn_cnt],time_point,replicate_numbers,
                                        met_id[precursor_cnt],precursor,int(numpy.round(precursor_mass)),
                                        frag,int(numpy.round(k)),
                                        peakSpectrum_measured[frag][k],'cps',
                                        peakSpectrum_corrected[frag][k],'cps',
                                        peakSpectrum_normalized[frag][k],'normMax',
                                        v,peakSpectrum_stats[frag][k]['absDev'],scantype,True,None);
                                self.session.add(row1);
        self.session.commit();
    def execute_updatePeakSpectrum(self,experiment_id_I,sample_name_abbreviations_I = None):
        '''re-calculate intensity_normalized from intensity_corrected and used'''

        mids = mass_isotopomer_distributions();

        # extract out the peakSpectrum
        dataListUpdated = [];
        # get sample names for the experiment
        print('execute_updatePeakSpectrum...')
        if sample_name_abbreviations_I:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for sna in sample_name_abbreviations_I:
                for st in sample_types:
                    sample_names_tmp = [];
                    sample_names_tmp = self.get_sampleNames_experimentIDAndSampleTypeAndSampleNameAbbreviation_peakSpectrum(experiment_id_I,st,sna);
                    sample_names.extend(sample_names_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        else:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for st in sample_types:
                sample_names_tmp = [];
                sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType_peakSpectrum(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
                sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        # create database table
        for sn_cnt,sn in enumerate(sample_names):
            print('updating peak spectrum for sample ' + sn);
            # get other information about the sample for later use
            sample_name_abbreviation,time_point,replicate_numbers = None,None,None;
            sample_name_abbreviation,time_point,replicate_numbers = self.get_sampleNameAbbreviationsAndTimePointAndReplicateNumber_experimentIDAndSampleName_peakSpectrum(experiment_id_I,sn);
            # get met_id and precursor_formula for each sample
            scan_type = [];
            scan_type = self.get_scanType_experimentIDAndSampleName_peakSpectrum(experiment_id_I,sn);
            for scantype in scan_type:
                print('building spectrum for scan type ' + scantype);
                # get met_id and precursor formula for each sample
                met_id, precursor_formula = [], [];
                met_id, precursor_formula = self.get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanType_peakSpectrum(experiment_id_I,sn,scantype);
                for precursor_cnt, precursor in enumerate(precursor_formula):
                    print('updating peak spectrum for met_id/precursor ' + met_id[precursor_cnt] + '/' + precursor);
                    precursor_str = re.sub('[+-]', '', precursor);
                    precursor_mass =  Formula(precursor_str).isotope.mass
                    # get all product fragments for the met_id/precursor
                    precursor_formulas_monoisotopic, product_formulas = [], [];
                    precursor_formulas_monoisotopic, product_formulas = self.get_precursorAndProductFormulas_metID(met_id[precursor_cnt],'-','tuning');
                    product_formulas.append(precursor_formulas_monoisotopic[0]); # add precursor to list of fragments
                    # get peak data for the sample/met_id/precursor_formula
                    peak_data = [];
                    peak_data = self.get_data_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum(experiment_id_I,sn,met_id[precursor_cnt],precursor,scantype);
                    peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                        peak_data, product_formulas,True);
                    peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                    # update data_stage01_isotopomer_peakSpectrum
                    for frag,spec in peakSpectrum_theoretical.items():
                        if spec:
                            product_str = re.sub('[+-]', '', frag);
                            product_mass =  Formula(product_str).isotope.mass;
                            for k,v in peakSpectrum_theoretical[frag].items():
                                dataListUpdated.append({'experiment_id':experiment_id_I,
                                                'sample_name':sn,
                                                'sample_name_abbreviation':sample_name_abbreviation,
                                                'sample_type':sample_types_lst[sn_cnt],
                                                'time_point':time_point,
                                                'replicate_number':replicate_numbers,
                                                'met_id':met_id[precursor_cnt],
                                                'precursor_formula':precursor,
                                                'precursor_mass':int(numpy.round(precursor_mass)),
                                                'product_formula':frag,
                                                'product_mass':int(numpy.round(k)),
                                                'intensity_corrected':peakSpectrum_corrected[frag][k],
                                                'intensity_corrected_units':'cps',
                                                'intensity_normalized':peakSpectrum_normalized[frag][k],
                                                'intensity_normalized_units':'normMax',
                                                'intensity_theoretical':v,
                                                'abs_devFromTheoretical':peakSpectrum_stats[frag][k]['absDev'],
                                                'scan_type':scantype});
        self.update_data_stage01_isotopomer_peakSpectrum(dataListUpdated);
    def execute_filterValidatedFragments(self,experiment_id_I):
        '''Filter fragments that have been validated by a U12C reference experiment'''

        from .stage01_isotopomer_peakSpectrum_dependencies import isotopomer_13C_fragments_validated

        print('filtering validated met/fragment pairs...')
        dataUpdate_O = [];
        for k,v in isotopomer_13C_fragments_validated.items():
            for frag in v:
                dataUpdate_O.append({'experiment_id':experiment_id_I,'met_id':k,'product_formula':frag});
        self.update_validFragments_stage01_isotopomer_peakSpectrum(dataUpdate_O);
    def execute_normalizeSpectrumFromReference(self,experiment_id_I,sample_name_abbreviations_I = None, use_mrm_ref = True, met_ids_I = None):
        # 1. import used peak spectrum to normalized table after multiplying by measured
        #       scaling factor calculated from used MRM spectrum
        # 2. be sure that the MRMs in the normalized table have been finalized
        
        '''NOTES:
        cannot follow the forloop pattern used in buildSpectrumFromPeakData (i.e. starting with sample name)
        must use the forloop pattern similar to updateNormalizedSpectrum, but without a forloop for dilutions
        (i.e. time-point to sample name abbreviations to scan types to mets)
        buildSpectrumFromPeakData and updatePeakSpectrum methods process one product:spectrum from a single precursor at a time;
        each precursor:product:spectrum is associated with only one sample name
        However, because the entire range of precursor:product:spectrum for a given met can encompass multiple dilutions and therefore different 
        sample names, a more generic approach must be used'''

        '''Assumptions:
        only a single precursor:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''

        mids = mass_isotopomer_distributions();

        # extract out the peakSpectrum
        print('execute_normalizeSpectrumFromReference...')        
        # get time points
        time_points = [];
        time_points = self.get_timePoints_experimentID_peakSpectrum(experiment_id_I);
        for tp in time_points:
            print('normalizing peak spectrum from reference for time-point ' + tp);
            # get sample name abbreviations
            if sample_name_abbreviations_I:
                sample_name_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_name_abbreviations_tmp = [];
                    sample_name_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_peakSpectrum(experiment_id_I,st,tp);
                    sample_name_abbreviations.extend([sna for sna in sample_name_abbreviations_tmp if sna in sample_name_abbreviations_I]);
                    sample_types_lst.extend([st for sna in sample_name_abbreviations_tmp if sna in sample_name_abbreviations_I]);
            else:
                sample_name_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_name_abbreviations_tmp = [];
                    sample_name_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_peakSpectrum(experiment_id_I,st,tp);
                    sample_name_abbreviations.extend(sample_name_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_name_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_name_abbreviations):
                print('normalizing peak spectrum from reference for sample name abbreviation ' + sna);
                # get scan types
                scan_type = [];
                scan_type = self.get_scanType_experimentIDAndTimePointSampleNameAbbreviation_peakSpectrum(experiment_id_I,tp,sna);
                for scantype in scan_type:
                    print('normalizing peak spectrum from reference for scan type ' + scantype);
                    # get replicates
                    replicate_numbers = [];
                    replicate_numbers = self.get_replicateNumber_experimentIDAndTimePointAndSampleNameAbbreviationAndScanType_peakSpectrum(experiment_id_I,tp,sna,scantype);
                    for rep in replicate_numbers:
                        print('normalizing peak spectrum from reference for replicate ' + str(rep));
                        # get other information about the sample for later use
                        sample_name, dilution = None,None;
                        sample_name,dilution = self.get_sampleNameAndDilution_experimentIDAndTimePointAndSampleNameAbbreviationAndScanType_peakSpectrum(\
                                        experiment_id_I,tp,sna,scantype,rep);
                        # get met_id
                        if met_ids_I:
                            met_id = met_ids_I;
                        else:
                            med_id = [];
                            met_id = self.get_metID_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicate_peakSpectrum(\
                                        experiment_id_I,tp,sna,scantype,rep);
                        for met_cnt,met in enumerate(met_id):
                            print('normalizing peak spectrum from reference for met_id ' + met);
                            # get precursor formula and mass
                            precursor_formula, precursor_mass = [], [];
                            precursor_formula, precursor_mass = self.get_precursorFormulaAndMass_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicateAndMetID_peakSpectrum(\
                                        experiment_id_I,tp,sna,scantype,rep,met);
                            peak_data_all = {};
                            scaling_factors_all = {};
                            for precursor_cnt, precursor in enumerate(precursor_formula):
                                peak_data_all[precursor] = None;
                                scaling_factors_all[precursor] = None;
                                print('normalizing peak spectrum from reference for precursor ' + precursor);
                                precursor_str = re.sub('[+-]', '', precursor);
                                # get all product fragments for the met_id/precursor
                                product_formulas = [];
                                product_formulas = self.get_productFormulas_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicateAndMetIDAndPrecursorFormula_peakSpectrum(\
                                        experiment_id_I,tp,sna,scantype,rep,met,precursor);
                                # get the m+0 precursor_formula
                                precursor_formula_monoisotopic = self.get_precursorFormula_metID(met,'-','tuning');
                                precursor_monoisotopic_str = re.sub('[+-]', '', precursor_formula_monoisotopic);
                                precursor_monoisotpoic_mass = int(numpy.round(Formula(precursor_monoisotopic_str).isotope.mass));
                                # get peakSpectrum data
                                peak_data = {};
                                peak_data = self.get_data_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicateAndMetIDAndPrecursorFormula_peakSpectrum(\
                                    experiment_id_I,tp,sna,scantype,rep,met,precursor);
                                peak_data_all[precursor] = peak_data;
                                if scantype == 'ER': 
                                    scaling_factors_all[precursor] = 1.0; # there is no need to scale ER or other precursor ion scans
                                else:
                                    if use_mrm_ref:
                                        # get reference MRM spectrum scaling factor for the sample
                                        #scaling_factor,scaling_factor_cv = None,None; # will need to incorporate propogation of error
                                        #scaling_factor,scaling_factor_cv = self.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Averages(experiment_id_I,sample_name_abbreviation,time_point,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'MRM');
                                        scaling_factor = None; # does not require the propogation of error
                                        scaling_factor = self.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Normalized(experiment_id_I,sna,tp,rep,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'MRM');
                                        if scaling_factor: scaling_factors_all[precursor] = scaling_factor;
                                        else:
                                            scaling_factors_all[precursor] = 0.0;
                                            ## substitute with reference spectrum
                                            #refspec = mids.report_fragmentSpectrum_normMax([precursor_formula_monoisotopic],True);
                                            #scaling_factor = refspec[precursor_formula_monoisotopic][precursor_mass[precursor_cnt]];
                                            #scaling_factors_all[precursor] = scaling_factor;
                                    else:
                                        # get reference ER spectrum scaling factor for the sample
                                        scaling_factor = None;
                                        scaling_factor = self.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndPrecursorFormulaAndMassAndScanType_peakSpectrum(experiment_id_I,sna,tp,rep,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'ER');
                                        if scaling_factor: scaling_factors_all[precursor] = scaling_factor;
                                        else:
                                            scaling_factors_all[precursor] = 0.0;
                                            ## substitute with reference spectrum
                                            #refspec = mids.report_fragmentSpectrum_normMax([precursor_formula_monoisotopic],True);
                                            #scaling_factor = refspec[precursor_formula_monoisotopic][precursor_mass[precursor_cnt]];
                                            #scaling_factors_all[precursor] = scaling_factor;
                            # normalize spectrum to reference MRM for each precursor (m+0,m+1,...)
                            peakSpectrum_normalized = mids.normalize_peakSpectrum_normMax(peak_data_all,scaling_factors_all);
                            peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                            # update data_stage01_isotopomer_peakSpectrum
                            for frag,spec in peakSpectrum_theoretical.items():
                                if spec:
                                    product_str = re.sub('[+-]', '', frag);
                                    product_mass =  Formula(product_str).isotope.mass;
                                    for k,v in peakSpectrum_theoretical[frag].items():
                                        if k in peakSpectrum_normalized[frag]:
                                            row = None;
                                            row = data_stage01_isotopomer_normalized(experiment_id_I,sample_name,sna,sample_types_lst[sna_cnt],tp,dilution,rep,
                                                                                         met,frag,int(numpy.round(k)),
                                                                                         #None,'cps',None,'cps',
                                                                                         None,'cps',peakSpectrum_normalized[frag][k],'normMax', #allows for spectrum updates
                                                                                         peakSpectrum_normalized[frag][k],'normMax',
                                                                                         v,peakSpectrum_stats[frag][k]['absDev'],scantype,True,None);
                                            self.session.add(row);
        self.session.commit();
    def execute_normalizeSpectrumFromReference_v1(self,experiment_id_I,sample_name_abbreviations_I = None,use_mrm_ref = True):
        # 1. import used peak spectrum to normalized table after multiplying by measured
        #       scaling factor calculated from used MRM spectrum
        # 2. be sure that the MRMs in the normalized table have been finalized
        
        '''NOTES: Broken for the following reason:
        cannot follow the forloop pattern used in buildSpectrumFromPeakData (i.e. starting with sample name)
        must use the forloop pattern used in updateNormalizedSpectrum (i.e. time-point to dilutions to sample name abbreviations to scan types to mets)
        buildSpectrumFromPeakData and updatePeakSpectrum methods process one product:spectrum from a single precursor at a time;
        each precursor:product:spectrum is associated with only one sample name
        However, because the entire range of precursor:product:spectrum for a given met can encompass multiple dilutions and therefore different 
        sample names, a more generic approach must be used
        Please use current version'''

        mids = mass_isotopomer_distributions();
        
        # extract out the peakSpectrum
        # get sample name for the experiment
        print('execute_normalizeSpectrumFromReference...')
        if sample_name_abbreviations_I:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for sna in sample_name_abbreviations_I:
                for st in sample_types:
                    sample_names_tmp = [];
                    sample_names_tmp = self.get_sampleNames_experimentIDAndSampleTypeAndSampleNameAbbreviation_peakSpectrum(experiment_id_I,st,sna);
                    sample_names.extend(sample_names_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        else:
            sample_names = [];
            sample_types = ['Unknown','QC'];
            sample_types_lst = [];
            for st in sample_types:
                sample_names_tmp = [];
                sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType_peakSpectrum(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
                sample_types_lst.extend([st for i in range(len(sample_names_tmp))]);
        for sn_cnt,sn in enumerate(sample_names):
            print('normalizing peak spectrum for sample ' + sn);
            # get other information about the sample for later use
            sample_name_abbreviation,time_point,dilution,replicate_numbers = None,None,None,None;
            sample_name_abbreviation,time_point,dilution,replicate_numbers = self.get_sampleNameAbbreviationsAndOther_experimentIDAndSampleName_peakSpectrum(experiment_id_I,sn);
            # get met_id and precursor_formula for each sample
            scan_type = [];
            scan_type = self.get_scanType_experimentIDAndSampleName_peakSpectrum(experiment_id_I,sn);
            for scantype in scan_type:
                print('normalizing spectrum for scan type ' + scantype);
                # get met_id
                med_id = [];
                met_id = self.get_metID_experimentIDAndSampleNameAndScanType_peakSpectrum(experiment_id_I,sn,scantype);
                for met in met_id:
                    print('normalizing peak spectrum for met_id ' + met);
                    # get precursor formula and mass
                    precursor_formula, precursor_mass = [], [];
                    precursor_formula, precursor_mass = self.get_precursorFormulaAndMass_experimentIDAndSampleNameAndMetIDAndScanType_peakSpectrum(experiment_id_I,sn,met,scantype);
                    peak_data_all = {};
                    scaling_factors_all = {};
                    for precursor_cnt, precursor in enumerate(precursor_formula):
                        peak_data_all[precursor] = None;
                        scaling_factors_all[precursor] = None;
                        print('normalizing peak spectrum for precursor ' + precursor);
                        precursor_str = re.sub('[+-]', '', precursor);
                        # get all product fragments for the met_id/precursor
                        product_formulas = [];
                        product_formulas = self.get_productFormulas_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum(experiment_id_I,sn,met,precursor,scantype);
                        # get the m+0 precursor_formula
                        precursor_formula_monoisotopic = self.get_precursorFormula_metID(met,'-','tuning');
                        precursor_monoisotopic_str = re.sub('[+-]', '', precursor_formula_monoisotopic);
                        precursor_monoisotpoic_mass = int(numpy.round(Formula(precursor_monoisotopic_str).isotope.mass));
                        # get peakSpectrum data
                        peak_data = {};
                        #Change to sna+rep+timepoint:peak_data = self.get_normalizedIntensity_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum(experiment_id_I,sn,met,precursor,scantype);
                        peak_data_all[precursor] = peak_data;
                        if scantype == 'ER': 
                            scaling_factors_all[precursor] = 1.0; # there is no need to scale ER or other precursor ion scans
                        else:
                            if use_mrm_ref:
                                # get reference MRM spectrum scaling factor for the sample
                                #scaling_factor,scaling_factor_cv = None,None; # will need to incorporate propogation of error
                                #scaling_factor,scaling_factor_cv = self.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Averages(experiment_id_I,sample_name_abbreviation,time_point,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'MRM');
                                scaling_factor = None; # does not require the propogation of error
                                scaling_factor = self.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Normalized(experiment_id_I,sample_name_abbreviation,time_point,replicate_numbers,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'MRM');
                                if scaling_factor: scaling_factors_all[precursor] = scaling_factor;
                                else:
                                    scaling_factors_all[precursor] = 0.0;
                                    ## substitute with reference spectrum
                                    #refspec = mids.report_fragmentSpectrum_normMax([precursor_formula_monoisotopic],True);
                                    #scaling_factor = refspec[precursor_formula_monoisotopic][precursor_mass[precursor_cnt]];
                                    #scaling_factors_all[precursor] = scaling_factor;
                            else:
                                # get reference ER spectrum scaling factor for the sample
                                scaling_factor = None;
                                scaling_factor = self.get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndPrecursorFormulaAndMassAndScanType_peakSpectrum(experiment_id_I,sample_name_abbreviation,time_point,replicate_numbers,met,precursor_formula_monoisotopic,precursor_mass[precursor_cnt],'ER');
                                if scaling_factor: scaling_factors_all[precursor] = scaling_factor;
                                else:
                                    scaling_factors_all[precursor] = 0.0;
                                    ## substitute with reference spectrum
                                    #refspec = mids.report_fragmentSpectrum_normMax([precursor_formula_monoisotopic],True);
                                    #scaling_factor = refspec[precursor_formula_monoisotopic][precursor_mass[precursor_cnt]];
                                    #scaling_factors_all[precursor] = scaling_factor;
                    # normalize spectrum to reference MRM for each precursor (m+0,m+1,...)
                    peakSpectrum_normalized = mids.normalize_peakSpectrum_normMax(peak_data_all,scaling_factors_all);
                    peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                    # update data_stage01_isotopomer_peakSpectrum
                    for frag,spec in peakSpectrum_theoretical.items():
                        if spec:
                            product_str = re.sub('[+-]', '', frag);
                            product_mass =  Formula(product_str).isotope.mass;
                            for k,v in peakSpectrum_theoretical[frag].items():
                                if k in peakSpectrum_normalized[frag]:
                                    row = None;
                                    row = data_stage01_isotopomer_normalized(experiment_id_I,sn,sample_name_abbreviation,sample_types_lst[sn_cnt],time_point,dilution,replicate_numbers,
                                                                                 met,frag,int(numpy.round(k)),
                                                                                 None,'cps',None,'cps',
                                                                                 peakSpectrum_normalized[frag][k],'normMax',
                                                                                 v,peakSpectrum_stats[frag][k]['absDev'],scantype,True);
                                    self.session.add(row);
        self.session.commit();

    