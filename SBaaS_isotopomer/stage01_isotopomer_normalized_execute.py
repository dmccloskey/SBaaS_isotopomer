#SBaaS
from .stage01_isotopomer_normalized_io import stage01_isotopomer_normalized_io
from .stage01_isotopomer_MQResultsTable_query import stage01_isotopomer_MQResultsTable_query
from SBaaS_LIMS.lims_msMethod_query import lims_msMethod_query
#Resources
from MDV_utilities.mass_isotopomer_distributions import mass_isotopomer_distributions
#Remove after refactor
from .stage01_isotopomer_normalized_postgresql_models import *
import numpy
import re
from molmass.molmass import Formula

class stage01_isotopomer_normalized_execute(stage01_isotopomer_normalized_io,
                                            stage01_isotopomer_MQResultsTable_query,
                                            lims_msMethod_query):
    def execute_buildSpectrumFromMRMs(self,experiment_id_I,ms_methodtype_I='isotopomer_13C',sample_name_abbreviations_I=[],sample_names_I=[],met_ids_I=[]):
        '''Extract peak spectrum for each fragment from MRMs'''
        # Input:
        #   experiment_id
        #   sample_names = (optional) list of specific samples
        # Output:
        #   sample_name
        #   sample_id
        #   component_group_name
        #   component_name
        #   calculated_concentration
        #   calculated_concentration_units
        #   used_

        # assumptions:
        #   1. there is only spectrum of MRMs for each components 

        mids = mass_isotopomer_distributions();
        
        print('build_precursorSpectrumFromMRMs...')
        # get time points
        time_points = self.get_timePoint_experimentID(experiment_id_I);
        for tp in time_points:
            print('Building precursor and product spectrum from MRMs for time-point ' + str(tp));
            # get dilutions
            dilutions = self.get_sampleDilution_experimentIDAndTimePoint(experiment_id_I,tp);
            for dil in dilutions:
                print('Building precursor and product spectrum from MRMs for dilution ' + str(dil));
                if sample_names_I:
                    sample_abbreviations = [];
                    for sn in sample_names_I:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleName(experiment_id_I,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                elif sample_name_abbreviations_I:
                    sample_abbreviations = sample_name_abbreviations_I;
                else:
                    # get sample names and sample name short
                    sample_abbreviations = [];
                    sample_types = ['Unknown','QC'];
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilution(experiment_id_I,st,tp,dil);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                for sna_cnt,sna in enumerate(sample_abbreviations):
                    print('Building precursor and product spectrum from MRMs for sample name abbreviation ' + sna);
                    ##BUG alert:
                    ##there is a potential bug whereby if the entire spectra per compound is not returned
                    ##e.g. one of the samples is not returned because "used_" is set to false in isotopomer_MQResultsTable
                    ##the spectra could potentially be shifted
                    ##get_componentsNamesAndOther_experimentIDAndSampleNameAndMSMethodTypeAndTimePointAndDilution has been adjusted to
                    ##return all component_names even if the sample from which it came is not "used_" as a temporary fix
                    ##this works for C12 validation experiments, but
                    ##the results of normalization will need to be monitored until a more robust method is established

                    ##UPDATE to BUG:
                    ##'met_cnt_max = len(component_names)-1' changed to 'met_cnt_max = len(component_names)' and 
                    ##get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndTimePointAndDilution added
                    ##so that the last component is included in the met/fragment spectra even when not all component names have "used_"
                    ##set to true in isotopomer_MQResultsTable 

                    # component names, group names, fragment formula, and fragment mass
                    if met_ids_I:
                        component_names,component_group_names,\
                            precursor_formulas_O, precursor_masses_O,\
                            product_formulas_O, product_masses_O = [],[],[],[],[],[];
                        for met in met_ids_I:
                            component_names_tmp,component_group_names_tmp,\
                                precursor_formulas_tmp, precursor_masses_tmp,\
                                product_formulas_tmp, product_masses_tmp = [],[],[],[],[],[];
                            component_names_tmp,component_group_names_tmp,\
                                precursor_formulas_tmp, precursor_masses_tmp,\
                                product_formulas_tmp, product_masses_tmp = \
                                self.get_componentsNamesAndOther_experimentIDAndSampleNameAndMSMethodTypeAndTimePointAndDilutionAndMetID( \
                                experiment_id_I,sna,ms_methodtype_I,tp,dil,met);
                            if not(component_names_tmp): continue #no component information was found
                            component_names.extend(component_names_tmp)
                            component_group_names.extend(component_group_names_tmp)
                            precursor_formulas_O.extend(precursor_formulas_tmp)
                            precursor_masses_O.extend(precursor_masses_tmp)
                            product_formulas_O.extend(product_formulas_tmp)
                            product_masses_O.extend(product_masses_tmp)
                    else:
                        component_names,component_group_names,\
                            precursor_formulas_O, precursor_masses_O,\
                            product_formulas_O, product_masses_O = [],[],[],[],[],[];
                        component_names,component_group_names,\
                            precursor_formulas_O, precursor_masses_O,\
                            product_formulas_O, product_masses_O = \
                            self.get_componentsNamesAndOther_experimentIDAndSampleNameAndMSMethodTypeAndTimePointAndDilution( \
                            experiment_id_I,sna,ms_methodtype_I,tp,dil);
                    if not(component_names): continue #no component information was found
                    # extract unique met ids and precursor formula id
                    met_ids_unique = [];
                    met_ids = [];
                    #precursor_formulas_unique = [];
                    #product_formulas_unique = [];
                    met_id = '';
                    met_id_old = '';
                    # algorithm works because lists are ordered by component_names
                    for i,cn in enumerate(component_names):
                        met_id = cn.split('.')[0];
                        met_ids.append(met_id);
                        if met_id != met_id_old:
                            met_id_old = met_id;
                            met_ids_unique.append(met_id);
                            #precursor_formulas_unique.append(precursor_formulas_O[i]);
                            #product_formulas_unique.append(product_formulas_O[i]);
                    # get precursor and productformulas for each unique met id:
                    precursor_formulas_unique = [];
                    product_formulas_unique = [];
                    for met in met_ids_unique:
                        precursor_formula,product_formula = None,None;
                        precursor_formula,product_formula = self.get_precursorFormulaAndProductFormula_metID(met,'-','isotopomer_13C')
                        precursor_formulas_unique.append(precursor_formula);
                        product_formulas_unique.append(product_formula);
                    # build precursor and spectrum for each met
                    met_all_cnt = 0;
                    met_cnt_max = len(component_names); # for use in a while loop
                    for i,met in enumerate(met_ids_unique):
                        print('Building precursor and product spectrum from MRMs for metabolite ' + met);
                        # get filtrate samples
                        precursorFiltrate_measured = {};
                        productFiltrate_measured = {};

                        #precursorFiltrate_measured[precursor_formulas_unique[i]] = None; #keep track of all met_ids

                        precursorFiltrate = {};
                        productFiltrate = {};
                        met_cnt = met_all_cnt;
                        # iterate through mets/fragments then sample names in order to calculate the average for each component_name (fragment/mass)
                        while met_cnt < met_cnt_max and met==met_ids[met_cnt]:
                            # get filtrate sample names
                            sample_names = [];
                            replicate_numbers = [];
                            sample_description = 'Filtrate';
                            sample_names,replicate_numbers,sample_types = self.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePointAndDilution(experiment_id_I,sna,sample_description,component_names[met_cnt],tp,dil);
                            intensities = [];
                            for sn_cnt,sn in enumerate(sample_names):
                                # get intensities
                                intensity = None;
                                intensity = self.get_peakHeight_sampleNameAndComponentName(sn,component_names[met_cnt]);
                                if not(intensity): continue
                                intensities.append(intensity);
                            n_replicates = len(intensities);
                            intensities_average_filtrate = 0.0;
                            intensities_var_filtrate = 0.0;
                            # calculate average and CV of the intensities
                            if (not(intensities)): intensities_average_filtrate = 0.0;
                            elif n_replicates<2: intensities_average_filtrate = intensities[0];
                            else: 
                                #intensities_average_filtrate, intensities_var_filtrate = self.calculate.calculate_ave_var_R(intensities);
                                intensities_average_filtrate = numpy.mean(numpy.array(intensities));
                                intensities_var_filtrate = numpy.var(numpy.array(intensities));
                            # append value to dictionary
                            precursorFiltrate[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = intensities_average_filtrate;
                            productFiltrate[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = intensities_average_filtrate;
                            met_cnt += 1;
                        precursorFiltrate_measured[precursor_formulas_unique[i]] = precursorFiltrate
                        productFiltrate_measured[product_formulas_unique[i]] = productFiltrate
                        # get broth samples
                        sample_names = [];
                        sample_description = 'Broth';
                        sample_names,replicate_numbers,sample_types = self.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndTimePointAndDilution(experiment_id_I,sna,sample_description,tp,dil);
                        #sample_names,replicate_numbers,sample_types = self.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePointAndDilution(experiment_id_I,sna,sample_description,component_names[met_cnt],tp,dil);
                        # iterate through sample names then mets/fragments in order to calculate the spectrum for each sample and component
                        for sn_cnt,sn in enumerate(sample_names):
                            print('Building precursor and product spectrum from MRMs for sample ' + sn);
                            precursorPeakSpectrum_measured = {};
                            precursorPeakSpectrum_corrected = {};
                            productPeakSpectrum_measured = {};
                            productPeakSpectrum_corrected = {};
                            #precursorPeakSpectrum_measured[precursor_formulas_unique[i]] = None; #keep track of all met_ids
                            #precursorPeakSpectrum_corrected[precursor_formulas_unique[i]] = None; #keep track of all met_ids
                            precursorMeasured = {};
                            precursorCorrected = {};
                            productMeasured = {};
                            productCorrected = {};
                            met_cnt = met_all_cnt;
                            while met_cnt < met_cnt_max and met==met_ids[met_cnt]:
                                # get intensities
                                intensity = None;
                                intensity = self.get_peakHeight_sampleNameAndComponentName(sn,component_names[met_cnt]);
                                if not(intensity):
                                    precursorMeasured[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = 0.0;
                                    productMeasured[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = 0.0;
                                else:
                                    precursorMeasured[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = intensity;
                                    productMeasured[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = intensity;
                                #if precursorFiltrate_measured[precursor_formulas_unique[i]][(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] < 0.5*intensity: 
                                #    corrected_intensity = intensity - precursorFiltrate_measured[precursor_formulas_unique[i]][(precursor_masses_O[met_cnt],product_masses_O[met_cnt])];
                                #else: corrected_intensity = 0.0;
                                #precursorCorrected[(precursor_masses_O[met_cnt],product_masses_O[met_cnt])] = corrected_intensity;
                                met_cnt += 1;
                            precursorPeakSpectrum_measured[precursor_formulas_unique[i]] = precursorMeasured;
                            productPeakSpectrum_measured[product_formulas_unique[i]] = productMeasured;

                            # generate normalized spectrum for the precursor:
                            precursorPeakSpectrum_measured, precursorPeakSpectrum_corrected, precursorPeakSpectrum_normalized \
                                = mids.build_precursorSpectrumFromMRMs(precursorPeakSpectrum_measured,precursorFiltrate_measured);
                            peakSpectrum_stats_O,precursorPeakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([precursorPeakSpectrum_normalized],True);
                            # update data_stage01_isotopomer_normalized
                            if precursorPeakSpectrum_theoretical[precursor_formulas_unique[i]]:
                                for k,v in precursorPeakSpectrum_theoretical[precursor_formulas_unique[i]].items():
                                    row1 = None;
                                    row1 = data_stage01_isotopomer_normalized(experiment_id_I,sn,sna,sample_types[sn_cnt],tp,dil,replicate_numbers[sn_cnt],
                                                                             met,precursor_formulas_unique[i],int(numpy.round(k)),
                                                                             precursorPeakSpectrum_measured[precursor_formulas_unique[i]][k],'cps',
                                                                             precursorPeakSpectrum_corrected[precursor_formulas_unique[i]][k],'cps',
                                                                             precursorPeakSpectrum_normalized[precursor_formulas_unique[i]][k],'normMax',
                                                                             v,peakSpectrum_stats_O[precursor_formulas_unique[i]][k]['absDev'],'MRM',True,None);
                                    self.session.add(row1);

                            # generate normalized spectrum for the product:
                            productPeakSpectrum_measured, productPeakSpectrum_corrected, productPeakSpectrum_normalized \
                                = mids.build_productSpectrumFromMRMs(productPeakSpectrum_measured,productFiltrate_measured);
                            peakSpectrum_stats_O,productPeakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([productPeakSpectrum_normalized],True);
                            # update data_stage01_isotopomer_normalized
                            if productPeakSpectrum_theoretical[product_formulas_unique[i]]:
                                for k,v in productPeakSpectrum_theoretical[product_formulas_unique[i]].items():
                                    row2 = None;
                                    row2 = data_stage01_isotopomer_normalized(experiment_id_I,sn,sna,sample_types[sn_cnt],tp,dil,replicate_numbers[sn_cnt],
                                                                             met,product_formulas_unique[i],int(numpy.round(k)),
                                                                             productPeakSpectrum_measured[product_formulas_unique[i]][k],'cps',
                                                                             productPeakSpectrum_corrected[product_formulas_unique[i]][k],'cps',
                                                                             productPeakSpectrum_normalized[product_formulas_unique[i]][k],'normMax',
                                                                             v,peakSpectrum_stats_O[product_formulas_unique[i]][k]['absDev'],'MRM',True,None);
                                    self.session.add(row2);

                        met_all_cnt = met_cnt
            self.session.commit();
    def execute_updateNormalizedSpectrum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''re-calculate intensity_normalized from intensity_corrected and used'''

        mids = mass_isotopomer_distributions();
        
        print('execute_updateNormalizedSpectrum...')
        # get time points
        time_points = self.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Building precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            dataListUpdated = [];
            # get dilutions
            dilutions = [];
            dilutions = self.get_sampleDilution_experimentIDAndTimePoint_dataStage01Normalized(experiment_id_I,tp);
            for dil in dilutions:
                print('Building precursor and product spectrum from isotopomer normalized for dilution ' + str(dil));
                if sample_names_I:
                    sample_abbreviations = [];
                    sample_types = ['Unknown','QC'];
                    for sn in sample_names_I:
                        for st in sample_types:
                            sample_abbreviations_tmp = [];
                            sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilutionAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,dil,sn);
                            sample_abbreviations.extend(sample_abbreviations_tmp);
                elif sample_name_abbreviations_I:
                    sample_abbreviations = sample_name_abbreviations_I;
                else:
                    # get sample names and sample name abbreviations
                    sample_abbreviations = [];
                    sample_types = ['Unknown','QC'];
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilution_dataStage01Normalized(experiment_id_I,st,tp,dil);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                for sna_cnt,sna in enumerate(sample_abbreviations):
                    print('Building precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
                    # get the scan_types
                    if scan_types_I:
                        scan_types = scan_types_I;
                    else:
                        scan_types = [];
                        scan_types = self.get_scanTypes_experimentIDAndTimePointAndDilutionAndSampleAbbreviations_dataStage01Normalized(experiment_id_I,tp,dil,sna);
                    for scan_type in scan_types:
                        print('Building precursor and product spectrum for scan type ' + scan_type)
                        # met_ids
                        if not met_ids_I:
                            met_ids = [];
                            met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanType_dataStage01Normalized( \
                                    experiment_id_I,sna,tp,dil,scan_type);
                        else:
                            met_ids = met_ids_I;
                        if not(met_ids): continue #no component information was found
                        for met in met_ids:
                            print('Building precursor and product spectrum from isotopomer normalized for metabolite ' + met);
                            # get sample names
                            sample_names = [];
                            sample_names,replicate_numbers,sample_types = self.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndMetIDAndTimePointAndDilutionAndScanType_dataStage01Normalized(experiment_id_I,sna,met,tp,dil,scan_type);
                            # iterate through sample names then mets/fragments in order to calculate the spectrum for each sample and component
                            for sn_cnt,sn in enumerate(sample_names):
                                print('Building precursor and product spectrum from isotopomer normalized for sample ' + sn);
                                # get peak data for the sample/met_id/scan_type
                                peak_data = [];
                                peak_data = self.get_data_experimentIDAndSampleNameAndMetIDAndAndScanType_normalized(experiment_id_I,sn,met,scan_type);
                                fragment_formulas = list(peak_data.keys());
                                peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                    peak_data, fragment_formulas, True);
                                peakSpectrum_stats,peakSpectrum_theoretical = mids.compare_peakSpectrum_normMax([peakSpectrum_normalized],True);
                                # update data_stage01_isotopomer_normalized
                                for frag,spec in peakSpectrum_theoretical.items():
                                    if spec:
                                        fragment_str = re.sub('[+-]', '', frag);
                                        fragment_mass =  Formula(fragment_str).isotope.mass;
                                        for k,v in peakSpectrum_theoretical[frag].items():
                                            dataListUpdated.append({'experiment_id':experiment_id_I,
                                                            'sample_name':sn,
                                                            'sample_name_abbreviation':sna,
                                                            'sample_type':sample_types[sn_cnt],
                                                            'time_point':tp,
                                                            'dilution':dil,
                                                            'replicate_number':replicate_numbers[sn_cnt],
                                                            'met_id':met,
                                                            'fragment_formula':frag,
                                                            'fragment_mass':int(numpy.round(k)),
                                                            'intensity_corrected':peakSpectrum_corrected[frag][k],
                                                            'intensity_corrected_units':'cps',
                                                            'intensity_normalized':peakSpectrum_normalized[frag][k],
                                                            'intensity_normalized_units':'normMax',
                                                            'intensity_theoretical':v,
                                                            'abs_devFromTheoretical':peakSpectrum_stats[frag][k]['absDev'],
                                                            'scan_type':scan_type});
            self.update_data_stage01_isotopomer_normalized(dataListUpdated);
    def execute_recombineNormalizedSpectrum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None):
        '''recombine intensity_normalized from a lower and higher dilution'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''

        mids = mass_isotopomer_distributions();

        print('execute_recombineNormalizedSpectrum...')
        # get time points
        time_points = self.get_timePoint_experimentIDAndComment_dataStage01Normalized(experiment_id_I,'Recombine');
        for tp in time_points:
            print('recombining spectrum for time-point ' + str(tp));
            dataListUpdated = [];
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleNameAndComment_dataStage01Normalized(experiment_id_I,st,tp,sn,'Recombine');
                        sample_abbreviations.extend(sample_abbreviations_tmp);
            elif sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
            else:
                # get sample names and sample name abbreviations
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndComment_dataStage01Normalized(experiment_id_I,st,tp,'Recombine');
                    sample_abbreviations.extend(sample_abbreviations_tmp);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('recombining spectrum for sample name abbreviation ' + sna);
                # get the scan_types
                scan_types = [];
                scan_types = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndComment_dataStage01Normalized(experiment_id_I,tp,sna,'Recombine');
                for scan_type in scan_types:
                    print('recombining spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndComment_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,'Recombine');
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('recombining spectrum for metabolite ' + met);
                        # get replicates
                        replicate_numbers = [];
                        replicate_numbers = self.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        for rep in replicate_numbers:
                            print('recombining spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.get_data_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            peakData_O,peakData_O_false,peakData_intensities_O = mids.recombine_dilutionsMRMs(peakData_I);
                            peakSpectrum_stats = mids.compare_peakSpectrum_normMax([peakData_intensities_O]);
                            # update data_stage01_isotopomer_normalized
                            for frag,spec in peakSpectrum_stats.items():
                                if spec:
                                    fragment_str = re.sub('[+-]', '', frag);
                                    fragment_mass =  Formula(fragment_str).isotope.mass;
                                    for k,v in peakSpectrum_stats[frag].items():
                                        if int(numpy.round(k)) in peakData_O[frag]:
                                            dataListUpdated.append({'experiment_id':experiment_id_I,
                                                        'sample_name_abbreviation':sna,
                                                        'time_point':tp,
                                                        'dilution':peakData_O[frag][int(numpy.round(k))]['dilution'],
                                                        'replicate_number':rep,
                                                        'met_id':met,
                                                        'fragment_formula':frag,
                                                        'fragment_mass':int(numpy.round(k)),
                                                        'intensity_normalized':peakData_O[frag][int(numpy.round(k))]['intensity'],
                                                        'intensity_normalized_units':'normMax',
                                                        'abs_devFromTheoretical':v['absDev'],
                                                        'scan_type':scan_type,
                                                        'used_':peakData_O[frag][int(numpy.round(k))]['used_'],
                                                        'comment_':peakData_O[frag][int(numpy.round(k))]['comment_']});
                            # update data_stage01_isotopomer_normalized (rows changed to false)
                            for frag,spec in peakData_O_false.items():
                                if spec:
                                    fragment_str = re.sub('[+-]', '', frag);
                                    fragment_mass =  Formula(fragment_str).isotope.mass;
                                    for k,v in peakData_O_false[frag].items():
                                        if v:
                                            dataListUpdated.append({'experiment_id':experiment_id_I,
                                                        'sample_name_abbreviation':sna,
                                                        'time_point':tp,
                                                        'dilution':v['dilution'],
                                                        'replicate_number':rep,
                                                        'met_id':met,
                                                        'fragment_formula':frag,
                                                        'fragment_mass':int(numpy.round(k)),
                                                        'intensity_normalized':v['intensity'],
                                                        'intensity_normalized_units':'normMax',
                                                        'abs_devFromTheoretical':None,
                                                        'scan_type':scan_type,
                                                        'used_':v['used_'],
                                                        'comment_':v['comment_']});
            self.update_data_stage01_isotopomer_normalized(dataListUpdated);
    #analyses not tested:
    def execute_removeDuplicateDilutions(self,experiment_id_I,component_names_dil_I = []):
        '''remove duplicate dilutions from data_stage01_isotopomer_normalized
        NOTE: rows are not removed, but the used value is changed to false
        NOTE: priority is given to the 1x dilution (i.e. 10x dilutions are removed
              if a 1x and 10x are both used'''
        # Input:
        #   experiment_id_I = experiment
        #   component_names_dil_I = component names for which the dilution will be prioritized
        
        print('execute_removeDuplicateDilutions...')
        # get sample names
        sample_ids = [];
        sample_ids = self.get_sampleIDs_experimentID_dataStage01Normalized(experiment_id_I);
        for si in sample_ids:
            # get component names
            component_names = [];
            component_names = self.get_componentsNames_experimentIDAndSampleID_dataStage01Normalized(experiment_id_I,si);
            for cn in component_names:
                # get dilutions
                sample_dilutions = [];
                sample_dilutions = self.get_sampleDilutions_experimentIDAndSampleIDAndComponentName_dataStage01Normalized(experiment_id_I,si,cn);
                if len(sample_dilutions)<2: continue;
                # find the minimum and maximum dilution
                min_sample_dilution = min(sample_dilutions);
                max_sample_dilution = max(sample_dilutions);
                for sd in sample_dilutions:
                    # prioritize undiluted samples if not in the dilution list
                    # i.e. diluted samples used_ are set to FALSE
                    if not(cn in component_names_dil_I) and not(sd == min_sample_dilution):
                        # get the sample name
                        sample_name = self.get_sampleName_experimentIDAndSampleIDAndSampleDilution_dataStage01Normalized(experiment_id_I,si,sd);
                        try:
                            data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                                    data_stage01_isotopomer_normalized.sample_name.like(sample_name),
                                    data_stage01_isotopomer_normalized.component_name.like(cn)).update(
                                    {'used_': False},synchronize_session=False);
                        except SQLAlchemyError as e:
                            print(e);
                    # prioritize diluted samples if in the dilution list
                    # i.e. undiluted samples used_ are set to FALSE
                    if (cn in component_names_dil_I) and not(sd == max_sample_dilution):
                        # get the sample name
                        sample_name = self.get_sampleName_experimentIDAndSampleIDAndSampleDilution_dataStage01Normalized(experiment_id_I,si,sd);
                        try:
                            data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                                    data_stage01_isotopomer_normalized.sample_name.like(sample_name),
                                    data_stage01_isotopomer_normalized.component_name.like(cn)).update(
                                    {'used_': False},synchronize_session=False);
                        except SQLAlchemyError as e:
                            print(e);
        self.session.commit();
    def execute_removeDuplicateComponents(self,experiment_id_I):
        '''remove duplicate components from data_stage01_isotopomer_normalized
        NOTE: rows are not removed, but the used value is changed to false
        NOTE: priority is given to the primary transition'''
        return

    