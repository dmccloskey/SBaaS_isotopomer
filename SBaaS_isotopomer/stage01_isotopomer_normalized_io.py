# System
import json
from .stage01_isotopomer_normalized_query import stage01_isotopomer_normalized_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from matplotlib_utilities.matplot import matplot
from ddt_python.ddt_container import ddt_container
from MDV_utilities.mass_isotopomer_distributions import mass_isotopomer_distributions

class stage01_isotopomer_normalized_io(stage01_isotopomer_normalized_query,sbaas_template_io):
    def import_dataStage01IsotopomerNormalized_update(self,filename,by_id=True):
        '''table adds
        INPUT:
        filename: name of the update file
        by_id = if TRUE, update by row id
                if False, update by unique row constraint'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        if by_id:
            self.update_dataStage01IsotopomerNormalized(data.data);
        else:
            self.update_dataStage01IsotopomerNormalized_byUniqueConstraint(data.data);
        data.clear_data();

    def import_dataStage01IsotopomerNormalized_updateUsedAndComment(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.updateUsedAndComment_dataStage01IsotopomerNormalized(data.data);
        data.clear_data();

    def import_dataStage01IsotopomerNormalized_add(self,filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01IsotopomerNormalized(data.data);
        data.clear_data();
    def export_dataStage01IsotopomerNormalized_js(self,experiment_id_I,sample_names_I=[],sample_name_abbreviations_I=[],time_points_I=[],scan_types_I=[],met_ids_I=[],data_dir_I="tmp",
                                                  single_plot_I = True):
        """Export data_stage01_isotopomer_normalized to js file"""

        mids = mass_isotopomer_distributions();

        # get the data
        
        data_O = [];
        data_dict_O = {};
        sample_names_O = [];
        # get time points
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = self.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Plotting precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_name_abbreviations_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
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
                print('Plotting precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
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
                    print('Plotting precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Plotting precursor and product spectrum for metabolite ' + met);
                        if sample_names_I:
                            sample_names = sample_names_I;
                        else:
                            sample_names,replicate_numbers,sample_types = [],[],[];
                            sample_names,replicate_numbers,sample_types = self.get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndMetIDAndTimePointAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,met,tp,scan_type);
                        if not(replicate_numbers): continue; #no replicates found
                        for rep_cnt,rep in enumerate(replicate_numbers):
                        #if not(sample_names): continue; #no replicates found
                        #for sn_cnt,sn in enumerate(sample_names):
                            print('Plotting precursor and product spectrum for replicate_number ' + str(rep));
                            #print('Plotting precursor and product spectrum for sample_name ' + sn);
                            #sample_names_O.append(sn);
                            #get data
                            peakData_I = {};
                            peakData_I = self.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            #peakData_I = self.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndSampleName_dataStage01Normalized( \
                            #    experiment_id_I,sna,tp,scan_type,met,sn);
                            if peakData_I:
                                data_sample_names_tmp=[];
                                fragment_formulas = list(peakData_I.keys());
                                peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                    peakData_I, fragment_formulas, True);
                                for fragment_formula in fragment_formulas:
                                    for fragment_mass,intensity_normalized in peakSpectrum_normalized[fragment_formula].items():
                                        sample_name = sna + "_" + str(rep);
                                        sample_names_O.append(sample_name);
                                        fragment_id = mids.make_fragmentID(met,fragment_formula,fragment_mass);
                                        intensity = 0.0;
                                        if intensity_normalized:
                                            intensity = intensity_normalized;
                                        data_tmp = {
                                                    'experiment_id':experiment_id_I,
                                                    'sample_name':sample_name,
                                                    #'sample_name':sn,
                                                    'sample_name_abbreviation':sna,
                                                    'sample_type':sample_types_lst[sna_cnt],
                                                    'time_point':tp,
                                                    #'dilution':dil,
                                                    'replicate_number':rep,
                                                    'met_id':met,
                                                    'fragment_formula':fragment_formula,
                                                    'fragment_mass':fragment_mass,
                                                    'intensity_normalized':intensity,
                                                    'intensity_normalized_units':"normMax",
                                                    'scan_type':scan_type,
                                                    'fragment_id':fragment_id};
                                        data_O.append(data_tmp);
                                        if not sample_name in data_dict_O.keys():
                                            data_dict_O[sample_name] = [];
                                            data_dict_O[sample_name].append(data_tmp);
                                        else:
                                            data_dict_O[sample_name].append(data_tmp);

        # record the unique sample names:
        sample_names_unique = list(set(sample_names_O));
        sample_names_unique.sort();

        # get the table data
        data_table_O = [];
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = self.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Tabulating precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            dataListUpdated = [];
            # get dilutions
            dilutions = [];
            dilutions = self.get_sampleDilution_experimentIDAndTimePoint_dataStage01Normalized(experiment_id_I,tp);
            for dil in dilutions:
                print('Tabulating precursor and product spectrum from isotopomer normalized for dilution ' + str(dil));
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
                    print('Tabulating precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
                    # get the scan_types
                    if scan_types_I:
                        scan_types = scan_types_I;
                    else:
                        scan_types = [];
                        scan_types = self.get_scanTypes_experimentIDAndTimePointAndDilutionAndSampleAbbreviations_dataStage01Normalized(experiment_id_I,tp,dil,sna);
                    for scan_type in scan_types:
                        print('Tabulting precursor and product spectrum for scan type ' + scan_type)
                        # met_ids
                        if not met_ids_I:
                            met_ids = [];
                            met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanType_dataStage01Normalized( \
                                    experiment_id_I,sna,tp,dil,scan_type);
                        else:
                            met_ids = met_ids_I;
                        if not(met_ids): continue #no component information was found
                        for met in met_ids:
                            # get the data
                            data = [];
                            data = self.get_rows_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanTypeAndMetID_dataStage01Normalized( \
                                    experiment_id_I,sna,tp,dil,scan_type,met);
                            for d in data:
                                d['sample_name'] = d['sample_name_abbreviation']+"_"+str(d['replicate_number']);
                                d['fragment_id'] = mids.make_fragmentID(d['met_id'],d['fragment_formula'],d['fragment_mass']);
                            data_table_O.extend(data);
        # visualization parameters
        data1_keys = ['sample_name','sample_name_abbreviation',
                      'sample_type',
                      'met_id','time_point','fragment_formula','fragment_mass','scan_type','fragment_id'];
        data1_nestkeys = [
            #'fragment_id',
            'fragment_mass'
            ];
        data1_keymap = {
                #'xdata':'fragment_id',
                'xdata':'fragment_mass',
                'ydata':'intensity_normalized',
                'serieslabel':'scan_type',
                #'serieslabel':'sample_name', #single plot
                #'featureslabel':'fragment_id',
                'featureslabel':'fragment_mass',
                'tooltipdata':'sample_name_abbreviation',
                'ydatalb':None,
                'ydataub':None};

        # initialize the ddt objects
        dataobject_O = [];
        parametersobject_O = [];
        tile2datamap_O = {};

        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        dataobject_O.append({"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(formtileparameters_O);
        tile2datamap_O.update({"filtermenu1":[0]});
        if not single_plot_I:
            rowcnt = 1;
            colcnt = 1;
            cnt = 0;
            for sn in sample_names_unique:
                svgtileid = "tilesvg"+str(cnt);
                svgid = 'svg'+str(cnt);
                iter=cnt+1; #start at 1
                if (cnt % 2 == 0): 
                    rowcnt = rowcnt+1;#even 
                    colcnt = 1;
                else:
                    colcnt = colcnt+1;
                # make the svg object
                svgparameters1_O = {"svgtype":'verticalbarschart2d_01',"svgkeymap":[data1_keymap],
                    #'svgid':'svg1',
                    'svgid':'svg'+str(cnt),
                    "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "svgwidth":350,"svgheight":250,"svgy1axislabel":"intensity (norm)",            
                        };
                svgtileparameters1_O = {'tileheader':sn,'tiletype':'svg',
                    #'tileid':"tile2",
                    'tileid':svgtileid,
                    #'rowid':"row1",
                    'rowid':"row"+str(rowcnt),
                    #'colid':"col1",
                    'colid':"col"+str(colcnt),
                    'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
                svgtileparameters1_O.update(svgparameters1_O);
                parametersobject_O.append(svgtileparameters1_O);
                tile2datamap_O.update({svgtileid:[iter]});
                dataobject_O.append({"data":data_dict_O[sn],"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
                cnt+=1;
        else:
            cnt = 0;
            svgtileid = "tilesvg"+str(cnt);
            svgid = 'svg'+str(cnt);
            rowcnt = 2;
            colcnt = 1;
            # make the svg object
            svgparameters1_O = {"svgtype":'verticalbarschart2d_01',"svgkeymap":[data1_keymap],
                #'svgid':'svg1',
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":500,"svgheight":350,"svgy1axislabel":"intensity (norm)",         
                    };
            svgtileparameters1_O = {'tileheader':'Isotopomer distribution','tiletype':'svg',
                #'tileid':"tile2",
                'tileid':svgtileid,
                #'rowid':"row1",
                #'colid':"col1",
                'rowid':"row"+str(rowcnt),
                'colid':"col"+str(colcnt),
                'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
            svgtileparameters1_O.update(svgparameters1_O);
            parametersobject_O.append(svgparameters1_O);
            tile2datamap_O.update({svgtileid:[0]});
            iter+=1;

        # make the table object
        tableparameters1_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    #"tableheaders":[],
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'tile1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters1_O = {'tileheader':'Isotopomer distribution','tiletype':'table','tileid':"tabletile1",
            'rowid':"row"+str(rowcnt+1),
            'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters1_O.update(tableparameters1_O);
        #dataobject_O.append({"data":data_table_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(tabletileparameters1_O);
        tile2datamap_O.update({"tabletile1":[0]})

        #filtermenunsvgtable = ddt_container_filterMenuNSvgTable();
        #filtermenunsvgtable.make_filterMenuNSvgTable(
        #    data_filtermenu=data_O,
        #    data_filtermenu_keys=[data1_keymap],
        #    data_filtermenu_nestkeys=data1_nestkeys,
        #    data_filtermenu_keymap=[data1_keymap],
        #    data_svg_keys=[data1_keymap],
        #    data_svg_nestkeys=data1_nestkeys,
        #    data_svg_keymap=[data1_keymap],
        #    data_table_keys=data1_keys,
        #    data_table_nestkeys=data1_nestkeys,
        #    data_table_keymap=[data1_keymap],
        #    data_svg=data_dict_O,
        #    data_table=data_table_O,
        #    svgtype='verticalbarschart2d_01',
        #    tabletype='responsivetable_01',
        #    svgx1axislabel=None,
        #    svgy1axislabel="intensity (norm)",
        #    single_plot_I=True,
        #    formtile2datamap=[0],
        #    tabletile2datamap=[1],
        #    svgtile2datamap=None,
        #    svgfilters=None,
        #    svgtileheader='Isotopomer distribution',
        #    tablefilters=None,
        #    tableheaders=None
        #    );

        # dump the data to a json file
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());

    def plot_normalizedSpectrum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''plot the normalized spectrum'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''
        mids = mass_isotopomer_distributions();
        print('plot_normalizedSpectrum...')
        plot = matplot();
        # get time points
        time_points = self.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Plotting precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
            if sample_names_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_names_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            elif sample_name_abbreviations_I:
                sample_abbreviations = [];
                sample_types = ['Unknown','QC'];
                sample_types_lst = [];
                for sn in sample_name_abbreviations_I:
                    for st in sample_types:
                        sample_abbreviations_tmp = [];
                        sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,st,tp,sn);
                        sample_abbreviations.extend(sample_abbreviations_tmp);
                        sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
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
                print('Plotting precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
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
                    print('Plotting precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Plotting precursor and product spectrum for metabolite ' + met);
                        replicate_numbers = [];
                        replicate_numbers = self.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        fragment_formulas_lst = [];
                        if not(replicate_numbers): continue; #no replicates found
                        for rep in replicate_numbers:
                            print('Plotting precursor and product spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            if peakData_I:
                                fragment_formulas = list(peakData_I.keys());
                                fragment_formulas_lst.extend(fragment_formulas)
                                peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normMax(\
                                    peakData_I, fragment_formulas, True);
                                peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                                
                        # plot spectrum data for all replicates and fragments
                        fragment_formulas_unique = list(set(fragment_formulas_lst));
                        for fragment in fragment_formulas_unique:
                            panelLabels = [];
                            xticklabels = [];
                            mean = [];
                            xlabel = 'm/z'
                            ylabel = 'intensity'
                            for rep,spectrum in enumerate(peakSpectrum_normalized_lst):
                                panelLabels_tmp = sna+'_'+met+'_'+fragment+'_'+str(rep+1)
                                xticklabels_tmp = [];
                                mean_tmp = [];
                                if fragment not in spectrum: 
                                    print('no spectrum found for fragment ' + fragment);
                                    continue;
                                for mass,intensity in spectrum[fragment].items():
                                    intensity_tmp = intensity;
                                    if not intensity_tmp: intensity_tmp=0.0
                                    mean_tmp.append(intensity_tmp);
                                    xticklabels_tmp.append(mass);
                                panelLabels.append(panelLabels_tmp);
                                xticklabels.append(xticklabels_tmp);
                                mean.append(mean_tmp);
                            plot.multiPanelBarPlot('',xticklabels,xlabel,ylabel,panelLabels,mean);
    def plot_normalizedSpectrumNormSum(self,experiment_id_I, sample_names_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average normalized intensity for all samples and scan types'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''
        mids = mass_isotopomer_distributions();
        
        print('plot_normalizedSpectrumNormSum...')
        plot = matplot();
        # get time points
        time_points = self.get_timePoint_experimentID_dataStage01Normalized(experiment_id_I);
        for tp in time_points:
            print('Plotting precursor and product spectrum from isotopomer normalized for time-point ' + str(tp));
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
                print('Plotting precursor and product spectrum from isotopomer normalized for sample name abbreviation ' + sna);
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
                    print('Plotting precursor and product spectrum for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Plotting precursor and product spectrum for metabolite ' + met);
                        # get replicates
                        replicate_numbers = [];
                        replicate_numbers = self.get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met);
                        peakSpectrum_normalized_lst = [];
                        for rep in replicate_numbers:
                            print('Plotting precursor and product spectrum for replicate_number ' + str(rep));
                            #get data
                            peakData_I = {};
                            peakData_I = self.get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized( \
                                experiment_id_I,sna,tp,scan_type,met,rep);
                            fragment_formulas = list(peakData_I.keys());
                            peakSpectrum_corrected, peakSpectrum_normalized = mids.extract_peakList_normSum(\
                                peakData_I, fragment_formulas, True);
                            peakSpectrum_normalized_lst.append(peakSpectrum_normalized);
                        # plot spectrum data for all replicates and fragments
                        fragment_formulas_unique = list(set(fragment_formulas_lst));
                        for fragment in fragment_formulas_unique:
                            panelLabels = [];
                            xticklabels = [];
                            mean = [];
                            xlabel = 'm/z'
                            ylabel = 'intensity'
                            for rep,spectrum in enumerate(peakSpectrum_normalized_lst):
                                panelLabels_tmp = sna+'_'+met+'_'+fragment+'_'+str(rep+1)
                                xticklabels_tmp = [];
                                mean_tmp = [];
                                for mass,intensity in spectrum[fragment].items():
                                    intensity_tmp = intensity;
                                    if not intensity_tmp: intensity_tmp=0.0
                                    mean_tmp.append(intensity_tmp);
                                    xticklabels_tmp.append(mass);
                                panelLabels.append(panelLabels_tmp);
                                xticklabels.append(xticklabels_tmp);
                                mean.append(mean_tmp);
                            plot.multiPanelBarPlot('',xticklabels,xlabel,ylabel,panelLabels,mean);
        
    def export_dataStage01IsotopomerNormalized_csv(self, experiment_id_I, filename_O,
                                                   sample_name_abbreviation_I='%',
                                                   time_point_I='%',
                                                   scan_type_I='%',
                                                   met_id_I='%'):
        '''export data_stage01_isotopomer_normalized to .csv'''

        data = [];
        data = self.get_rows_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I)
        if data:
            # write data to file
            export = base_exportData(data);
            export.write_dict2csv(filename_O);