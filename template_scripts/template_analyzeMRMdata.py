import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
#sys.path.append('C:/Users/dmccloskey/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_1.ini';
#filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_base/settings_2.ini';
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

##Analyze the MRM data

#make the results table to analyze the MRM data
from SBaaS_isotopomer.stage01_isotopomer_MQResultsTable_execute import stage01_isotopomer_MQResultsTable_execute
exmqrt01 = stage01_isotopomer_MQResultsTable_execute(session,engine,pg_settings.datadir_settings);
exmqrt01.drop_dataStage01_isotopomer_MQResultsTable();
exmqrt01.initialize_dataStage01_isotopomer_MQResultsTable();
exmqrt01.execute_deleteExperimentFromMQResultsTable('ALEsKOs01',sample_types_I = ['Quality Control','Unknown','Standard','Blank'])
exmqrt01.import_dataStage01IsotopomerMQResultsTable_add('data/tests/analysis_isotopomer/150911_Isotopomer_ALEsKOs01_tpiAEvo01-04_samples01.csv');
exmqrt01.export_dataStage01MQResultsTable_metricPlot_js('chemoCLim01',component_names_I = ['fdp.fdp_1.Light'],measurement_I='RT');

#make the normalized methods tables
from SBaaS_isotopomer.stage01_isotopomer_normalized_execute import stage01_isotopomer_normalized_execute
normalized01 = stage01_isotopomer_normalized_execute(session,engine,pg_settings.datadir_settings);
normalized01.drop_dataStage01_isotopomer_normalized();
normalized01.initialize_dataStage01_isotopomer_normalized();
normalized01.reset_dataStage01_isotopomer_normalized('ALEsKOs01');
# build the spectrums from MRM
normalized01.execute_buildSpectrumFromMRMs('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc',
    ],
    met_ids_I=[
              ]
    );

# export the data to .csv
normalized01.export_dataStage01IsotopomerNormalized_csv('ALEsKOs01',
        filename_O = 'data/tests/analysis_isotopomer/normalized_MRM.csv',
        sample_name_abbreviation_I='%',
        time_point_I='%',
        scan_type_I='%',
        met_id_I='%')
#export spectrums to js
normalized01.export_dataStage01IsotopomerNormalized_js('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['MRM'],
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
    scan_types_I=['MRM'],
    );
# update the DB from .csv
# NOTE: by_id = True should be used for most cases, but for this example, the row id's will do not match what is in the DB
normalized01.import_dataStage01IsotopomerNormalized_update('data/tests/analysis_isotopomer/150911_Isotopomer_ALEsKOs01_tpiAEvo01-04_normalizedUpdate01.csv',
                                                           by_id = False)

# update specific samples
normalized01.execute_updateNormalizedSpectrum('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['MRM']
    );

#make the averages methods tables
from SBaaS_isotopomer.stage01_isotopomer_averages_execute import stage01_isotopomer_averages_execute
ave01 = stage01_isotopomer_averages_execute(session,engine,pg_settings.datadir_settings);
ave01.drop_dataStage01_isotopomer_averages();
ave01.initialize_dataStage01_isotopomer_averages();
ave01.reset_dataStage01_isotopomer_averages('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'],
    scan_types_I = ['MRM']);

# calculate the spectrum averages for specific met_ids and/or scan_types
ave01.execute_analyzeAverages('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'],
    met_ids_I=[],
    scan_types_I = ['MRM']);

# calculate averages by normalizing the spectrum to 1.0 for specific met_ids and/or scan_types
ave01.execute_analyzeAveragesNormSum('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['MRM']
    );

# review the spectrums in excel
ave01.export_dataStage01IsotopomerAveragesNormSum_csv('ALEsKOs01',
            filename_O='data/tests/analysis_isotopomer/averagesNormSum.csv',
            sample_name_abbreviation_I='%',
            time_point_I='%',
            sample_type_I='%',
            scan_type_I='%',
            met_id_I='%')

# export the spectrums to matplotlib
ave01.plot_averageSpectrumNormSum('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['MRM']
    );
# export the spectrums to .js
ave01.export_dataStage01IsotopomerAveragesNormSum_js('ALEsKOs01',
    sample_name_abbreviations_I=[
    'OxicEvo04tpiAEvo01EPEcoli13CGlc',
    'OxicEvo04tpiAEvo02EPEcoli13CGlc',
    'OxicEvo04tpiAEvo03EPEcoli13CGlc',
    'OxicEvo04tpiAEvo04EPEcoli13CGlc'
    ],
    met_ids_I=[],
    scan_types_I=['MRM'],
    single_plot_I = False,
    );