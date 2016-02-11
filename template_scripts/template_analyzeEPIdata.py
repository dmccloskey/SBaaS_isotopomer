import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_1.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_isotopomer')
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/calculate_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/MDV_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')
sys.path.append(pg_settings.datadir_settings['github']+'/matplotlib_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/quantification_analysis')

###Analyze the EPI data

#make the results table to analyze the EPI data
from io_utilities.base_importData import base_importData
from SBaaS_isotopomer.stage01_isotopomer_peakData_execute import stage01_isotopomer_peakData_execute
peakdata01 = stage01_isotopomer_peakData_execute(session,engine,pg_settings.datadir_settings);
peakdata01.drop_dataStage01_isotopomer_peakData();
peakdata01.initialize_dataStage01_isotopomer_peakData();
#import the raw peak data from data files
iobase = base_importData();
iobase.read_csv('C:/Users/dmccloskey-sbrg/Documents/GitHub/metabolomics/peakView/EPI/141104_Isotopomer_ALEsKOs01_tpiAEvo01EP_EPI/fileList.csv');
fileList = iobase.data;
# read in each data file
for file in fileList:
    print('processing file ' + file['filename'])
    peakdata01.import_peakData_add('C:/Users/dmccloskey-sbrg/Documents/GitHub/metabolomics/peakView/EPI/141104_Isotopomer_ALEsKOs01_tpiAEvo01EP_EPI/' + file['filename'],
                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type'],
                    add_data_I=True
                    );
iobase.clear_data();
iobase.read_csv('C:/Users/dmccloskey-sbrg/Documents/GitHub/metabolomics/peakView/EPI/141104_Isotopomer_ALEsKOs01_tpiAEvo02EP_EPI/fileList.csv');
fileList = iobase.data;
# read in each data file
for file in fileList:
    print('processing file ' + file['filename'])
    peakdata01.import_peakData_add('C:/Users/dmccloskey-sbrg/Documents/GitHub/metabolomics/peakView/EPI/141104_Isotopomer_ALEsKOs01_tpiAEvo02EP_EPI/' + file['filename'],
                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type'],
                    add_data_I=True
                    );
iobase.clear_data();
iobase.read_csv('C:/Users/dmccloskey-sbrg/Documents/GitHub/metabolomics/peakView/EPI/141104_Isotopomer_ALEsKOs01_tpiAEvo03EP_EPI/fileList.csv');
fileList = iobase.data;
# read in each data file
for file in fileList:
    print('processing file ' + file['filename'])
    peakdata01.import_peakData_add('C:/Users/dmccloskey-sbrg/Documents/GitHub/metabolomics/peakView/EPI/141104_Isotopomer_ALEsKOs01_tpiAEvo03EP_EPI/' + file['filename'],
                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type'],
                    add_data_I=True
                    );
iobase.clear_data();
iobase.read_csv('C:/Users/dmccloskey-sbrg/Documents/GitHub/metabolomics/peakView/EPI/141104_Isotopomer_ALEsKOs01_tpiAEvo04EP_EPI/fileList.csv');
fileList = iobase.data;
# read in each data file
for file in fileList:
    print('processing file ' + file['filename'])
    peakdata01.import_peakData_add('C:/Users/dmccloskey-sbrg/Documents/GitHub/metabolomics/peakView/EPI/141104_Isotopomer_ALEsKOs01_tpiAEvo04EP_EPI/' + file['filename'],
                    file['experiment_id'], file['sample_name'], file['precursor_formula'], file['met_id'],
                    mass_units_I='Da',intensity_units_I='cps', scan_type_I=file['scan_type'],
                    add_data_I=True
                    );
iobase.clear_data();

# TODO:
# export to .js (show the raw peak data)

#make the peakSpectrum methods tables
from SBaaS_isotopomer.stage01_isotopomer_peakSpectrum_execute import stage01_isotopomer_peakSpectrum_execute
peakspec01 = stage01_isotopomer_peakSpectrum_execute(session,engine,pg_settings.datadir_settings);
peakspec01.drop_dataStage01_isotopomer_peakSpectrum();
peakspec01.initialize_dataStage01_isotopomer_peakSpectrum();
peakspec01.reset_dataStage01_isotopomer_peakSpectrum('ALEsKOs01');

# build epi peak spectrum for specific samples/compounds
peakspec01.execute_buildSpectrumFromPeakData('ALEsKOs01','isotopomer_13C',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[
              ]
    );
# normalize the epi peak spectrum to the calculated precursor mrm spectrum for specific samples/met_ids
peakspec01.execute_normalizeSpectrumFromReference('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    use_mrm_ref = True,
    met_ids_I=[
              ]
    );
#make the normalized methods tables
from SBaaS_isotopomer.stage01_isotopomer_normalized_execute import stage01_isotopomer_normalized_execute
normalized01 = stage01_isotopomer_normalized_execute(session,engine,pg_settings.datadir_settings);
# export the data to excel
normalized01.export_dataStage01IsotopomerNormalized_csv('ALEsKOs01',
        filename_O = 'data/tests/analysis_isotopomer/normalized_EPI.csv',
        sample_name_abbreviation_I='%',
        time_point_I='%',
        scan_type_I='EPI',
        met_id_I='%')
#export spectrums to js
#TODO: bug in plots
normalized01.export_dataStage01IsotopomerNormalized_js('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['EPI'],
    single_plot_I = False,
    );
#export spectrums to matplotlib
normalized01.plot_normalizedSpectrum('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['EPI']
    );
# update the DB from the .csv
normalized01.import_dataStage01IsotopomerNormalized_update('data/tests/analysis_isotopomer/150911_Isotopomer_ALEsKOs01_tpiAEvo01-04_normalizedUpdate01.csv')

# update specific samples
normalized01.execute_updateNormalizedSpectrum('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['EPI']
    );

#make the averages methods tables
from SBaaS_isotopomer.stage01_isotopomer_averages_execute import stage01_isotopomer_averages_execute
ave01 = stage01_isotopomer_averages_execute(session,engine,pg_settings.datadir_settings);
#ave01.drop_dataStage01_isotopomer_averages();
#ave01.initialize_dataStage01_isotopomer_averages();
ave01.reset_dataStage01_isotopomer_averages('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'],
    scan_type_I=['EPI']);

# calculate the spectrum averages for specific met_ids and/or scan_types
ave01.execute_analyzeAverages('ALEsKOs01',
    met_ids_I=[],
    scan_types_I = ['EPI']);
# calculate averages by normalizing the spectrum to 1.0 for specific met_ids and/or scan_types
ave01.execute_analyzeAveragesNormSum('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['EPI']
    );

# review the spectrums in excel
ave01.export_dataStage01IsotopomerAveragesNormSum_csv('ALEsKOs01',
            filename_O='data/tests/analysis_isotopomer/averagesNormSum.csv',
            sample_name_abbreviation_I='%',
            time_point_I='%',
            sample_type_I='%',
            scan_type_I='EPI',
            met_id_I='%')
# export the spectrums to .js
ave01.export_dataStage01IsotopomerAveragesNormSum_js('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['EPI'],
    single_plot_I = False,
    );
# export the spectrums to matplotlib
ave01.plot_averageSpectrumNormSum('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['EPI']
    );