# System
import json
from .stage01_isotopomer_averages_query import stage01_isotopomer_averages_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from matplotlib_utilities.matplot import matplot
from ddt_python.ddt_container import ddt_container
from ddt_python.ddt_container_filterMenuAndChart2dAndTable import ddt_container_filterMenuAndChart2dAndTable
#Resources
from MDV_utilities.mass_isotopomer_distributions import mass_isotopomer_distributions

class stage01_isotopomer_averages_io(stage01_isotopomer_averages_query,sbaas_template_io):
    def import_dataStage01IsotopomerAverages_updateUsedAndComment(self,filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01IsotopomerAverages_usedAndComment(data.data);
        data.clear_data();

    def import_dataStage01IsotopomerAveragesNormSum_updateUsedAndComment(self,filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01IsotopomerAveragesNormSum_usedAndComment(data.data);
        data.clear_data();
    def export_dataStage01IsotopomerAveragesNormSum_js(self,experiment_id_I, time_points_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None,data_dir_I="tmp",
                                                  single_plot_I = True):
        '''Export data_stage01_isotopomer_averagesNormSum to js file'''
        
        mids = mass_isotopomer_distributions();
        
        print('plotting averagesNormSum...')
        data_O = [];
        data_dict_O = {};
        # get time points
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = [];
            time_points = self.get_timePoint_experimentID_dataStage01AveragesNormSum(experiment_id_I);
        for tp in time_points:
            print('Plotting product and precursor for time-point ' + str(tp));
            # get sample names and sample name abbreviations
            if sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                sample_types_lst = ['Unknown' for x in sample_abbreviations];
            else:
                sample_abbreviations = [];
                sample_types = ['Unknown'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01AveragesNormSum(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Plotting product and precursor for sample name abbreviation ' + sna);
                data_dict_O[sna] = [];
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
                    print('Plotting product and precursor for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Plotting product and precursor for metabolite ' + met);
                        # fragments
                        fragment_formulas = [];
                        fragment_formulas = self.get_fragmentFormula_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        for frag in fragment_formulas:
                            print('Plotting product and precursor for fragment ' + frag);
                            # data
                            data_mat = [];
                            data_mat_cv = [];
                            data_masses = [];
                            data_mat,data_mat_cv,data_masses = self.get_spectrum_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetIDAndFragmentFormula_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met,frag);
                            for i,d in enumerate(data_mat):
                                stdev = 0.0;
                                stderr = 0.0;
                                lb = None;
                                ub = None;
                                if data_mat_cv[i]: 
                                    stdev = data_mat[i]*data_mat_cv[i]/100;
                                    lb = data_mat[i]-stdev;
                                    ub = data_mat[i]+stdev;
                                fragment_id = mids.make_fragmentID(met,frag,data_masses[i]);
                                tmp = {
                                'experiment_id':experiment_id_I,
                                'sample_name_abbreviation':sna,
                                'sample_type':sample_types_lst[sna_cnt],
                                'time_point':tp,
                                'met_id':met,
                                'fragment_formula':frag,
                                'fragment_mass':data_masses[i],
                                'fragment_id':fragment_id,
                                'intensity_normalized_average':d,
                                'intensity_normalized_cv':data_mat_cv[i],
                                'intensity_normalized_lb':lb,
                                'intensity_normalized_ub':ub,
                                'intensity_normalized_units':"normSum",
                                'scan_type':scan_type,
                                'used_':True,
                                'comment_':None}
                                data_O.append(tmp);
                                data_dict_O[sna].append(tmp);

        print('tabulating averagesNormSum...')
        data_table_O = [];
        # get time points
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = [];
            time_points = self.get_timePoint_experimentID_dataStage01AveragesNormSum(experiment_id_I);
        for tp in time_points:
            print('Tabulating product and precursor for time-point ' + str(tp));
            # get sample names and sample name abbreviations
            if sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                sample_types_lst = ['Unknown' for x in sample_abbreviations];
            else:
                sample_abbreviations = [];
                sample_types = ['Unknown'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01AveragesNormSum(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Tabulating product and precursor for sample name abbreviation ' + sna);
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
                    print('Tabulating product and precursor for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Tabulating product and precursor for metabolite ' + met);
                        # get rows
                        rows = [];
                        rows = self.get_rows_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        if not rows: continue;
                        for d in rows:
                            d['fragment_id'] = mids.make_fragmentID(d['met_id'],d['fragment_formula'],d['fragment_mass']);
                        data_table_O.extend(rows);

        print('exporting averagesNormSum...');

        # visualization parameters
        data1_keys = ['sample_name_abbreviation',
                      'sample_type',
                      'met_id',
                      'time_point',
                      'fragment_formula',
                      'fragment_mass',
                      'scan_type',
                      'fragment_id'
                      ];
        data1_nestkeys = [
            #'fragment_id',
            'fragment_mass'
            ];
        data1_keymap = {
                #'xdata':'fragment_id',
                'xdata':'fragment_mass',
                'ydata':'intensity_normalized_average',
                'tooltiplabel':'sample_name_abbreviation',
                'serieslabel':'scan_type',
                #'featureslabel':'fragment_id',
                'featureslabel':'fragment_mass',
                'ydatalb':'intensity_normalized_lb',
                'ydataub':'intensity_normalized_ub'};

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
            for cnt,sn in enumerate(sample_abbreviations):
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
                    "svgfilters":{'sample_name_abbreviation':[sn]}               
                        };
                svgtileparameters1_O = {'tileheader':'Isotopomer distribution','tiletype':'svg',
                    'tileid':svgtileid,
                    'rowid':"row"+str(rowcnt),
                    'colid':"col"+str(colcnt),
                    'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
                svgtileparameters1_O.update(svgparameters1_O);
                parametersobject_O.append(svgtileparameters1_O);
                tile2datamap_O.update({svgtileid:[0]});
        else:
            cnt = 0;
            svgtileid = "tilesvg"+str(cnt);
            svgid = 'svg'+str(cnt);
            rowcnt = 2;
            colcnt = 1;
            # make the svg object
            svgparameters1_O = {"svgtype":'verticalbarschart2d_01',"svgkeymap":[data1_keymap],
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":500,"svgheight":350,"svgy1axislabel":"intensity (norm)",             
                    };
            svgtileparameters1_O = {'tileheader':'Isotopomer distribution','tiletype':'svg',
                'tileid':svgtileid,
                'rowid':"row"+str(rowcnt),
                'colid':"col"+str(colcnt),
                'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
            svgtileparameters1_O.update(svgparameters1_O);
            parametersobject_O.append(svgparameters1_O);
            tile2datamap_O.update({svgtileid:[0]});

        # make the table object
        tableparameters1_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    #"tableheaders":[],
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'tile1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters1_O = {'tileheader':'Isotopomer distribution','tiletype':'table','tileid':"tabletile1",
            'rowid':"row100",
            'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters1_O.update(tableparameters1_O);
        dataobject_O.append({"data":data_table_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(tabletileparameters1_O);
        tile2datamap_O.update({"tabletile1":[1]})

        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
                data_filtermenu=data_O,
                data_filtermenu_keys=data1_keys,
                data_filtermenu_nestkeys=data1_nestkeys,
                data_filtermenu_keymap=data1_keymap,
                data_svg_keys=data1_keys,
                data_svg_nestkeys=data1_nestkeys,
                data_svg_keymap=data1_keymap,
                data_table_keys=None,
                data_table_nestkeys=None,
                data_table_keymap=None,
                data_svg=data_dict_O,
                data_table=None,
                svgtype='verticalbarschart2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='',
                svgy1axislabel='',
                tablekeymap = [data1_keymap],
                svgkeymap = [], #calculated on the fly
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=[], #calculated on the fly
                svgfilters=None,
                svgtileheader='Isotopomer distribution',
                tablefilters=None,
                tableheaders=None
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());

        ## dump the data to a json file
        #data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        #parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        #tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        #if data_dir_I=='tmp':
        #    filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        #elif data_dir_I=='project':
        #    filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage01_isotopomer_normalized' + '.js'
        #elif data_dir_I=='data_json':
        #    data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
        #    return data_json_O;
        #with open(filename_str,'w') as file:
        #    file.write(data_str);
        #    file.write(parameters_str);
        #    file.write(tile2datamap_str);
    def plot_averageSpectrumNormSum(self,experiment_id_I, time_points_I = None, sample_name_abbreviations_I = None, met_ids_I = None, scan_types_I = None):
        '''calculate the average normalized intensity for all samples and scan types'''
        
        '''Assumptions:
        only a single fragment:spectrum is used_ per sample name abbreviation, time-point, replicate, scan_type
        (i.e. there are no multiple dilutions of the same precursor:spectrum that are used_)
        '''
        mids = mass_isotopomer_distributions();
        
        print('plot_averagesNormSum...')
        plot = matplot();
        # get time points
        if time_points_I:
            time_points = time_points_I;
        else:
            time_points = [];
            time_points = self.get_timePoint_experimentID_dataStage01AveragesNormSum(experiment_id_I);
        for tp in time_points:
            print('Plotting product and precursor for time-point ' + str(tp));
            # get sample names and sample name abbreviations
            if sample_name_abbreviations_I:
                sample_abbreviations = sample_name_abbreviations_I;
                sample_types_lst = ['Unknown' for x in sample_abbreviations];
            else:
                sample_abbreviations = [];
                sample_types = ['Unknown'];
                sample_types_lst = [];
                for st in sample_types:
                    sample_abbreviations_tmp = [];
                    sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01AveragesNormSum(experiment_id_I,st,tp);
                    sample_abbreviations.extend(sample_abbreviations_tmp);
                    sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
            for sna_cnt,sna in enumerate(sample_abbreviations):
                print('Plotting product and precursor for sample name abbreviation ' + sna);
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
                    print('Plotting product and precursor for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Plotting product and precursor for metabolite ' + met);
                        # fragments
                        fragment_formulas = [];
                        fragment_formulas = self.get_fragmentFormula_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        for frag in fragment_formulas:
                            print('Plotting product and precursor for fragment ' + frag);
                            # data
                            data_mat = [];
                            data_mat_cv = [];
                            data_masses = [];
                            data_mat,data_mat_cv,data_masses = self.get_spectrum_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetIDAndFragmentFormula_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met,frag);
                            data_stdev = [];
                            for i,d in enumerate(data_mat):
                                stdev = 0.0;
                                stderr = 0.0;
                                if data_mat_cv[i]: 
                                    stdev = data_mat[i]*data_mat_cv[i]/100;
                                data_stdev.append(stdev);
                            title = sna+'_'+met+'_'+frag;
                            plot.barPlot(title,data_masses,'intensity','m/z',data_mat,var_I=None,se_I=data_stdev,add_labels_I=True)
    def export_dataStage01IsotopomerAveragesNormSum_csv(self, experiment_id_I, filename_O,
                                                   sample_name_abbreviation_I='%',
                                                   time_point_I='%',
                                                   sample_type_I='%',
                                                   scan_type_I='%',
                                                   met_id_I='%'):
        '''export data_stage01_isotopomer_normalized to .csv'''

        data = [];
        data = self.get_rows_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum(experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I,met_id_I);
        if data:
            # write data to file
            export = base_exportData(data);
            export.write_dict2csv(filename_O);