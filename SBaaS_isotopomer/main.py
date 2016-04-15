import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_isotopomer')
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/MDV_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')
sys.path.append(pg_settings.datadir_settings['github']+'/matplotlib_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/quantification_analysis')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')

# TODO:
# 1 control 12-C experiment (use: C:\Users\dmccloskey-sbrg\Documents\GitHub\sbaas_workspace\sbaas_workspace\workspace\isotopomer\WTEColi12C02.py)

#make the normalized methods tables
from SBaaS_isotopomer.stage01_isotopomer_normalized_execute import stage01_isotopomer_normalized_execute
normalized01 = stage01_isotopomer_normalized_execute(session,engine,pg_settings.datadir_settings);
## update the database from .csv
#normalized01.import_dataStage01IsotopomerNormalized_update('C:/Users/dmccloskey-sbrg/Desktop/dataStage01IsotopomerNormalized_WTEColi_113C80_U13C20_01_backup.csv');
## export the data to excel
#normalized01.export_dataStage01IsotopomerNormalized_csv('WTEColi_113C80_U13C20_01',
#        filename_O = pg_settings.datadir_settings['workspace_data']+'/_output/WTEColi_113C80_U13C20_01_averagesNormSum.csv',
#        sample_name_abbreviation_I='%',
#        time_point_I='%',
#        scan_type_I='EPI',
#        met_id_I='%')
#export spectrums to js
##TODO: bug in plots
#normalized01.export_dataStage01IsotopomerNormalized_js('ALEsKOs01',
#    sample_name_abbreviations_I=[
#        "OxicEvo04sdhCBEvo01EPEcoli13CGlc",
#    ],
#    met_ids_I=[],
#    scan_types_I=[],
#    single_plot_I = False,
#    );

#make the averages methods tables
from SBaaS_isotopomer.stage01_isotopomer_averages_execute import stage01_isotopomer_averages_execute
ave01 = stage01_isotopomer_averages_execute(session,engine,pg_settings.datadir_settings);
#ave01.import_dataStage01IsotopomerAveragesNormSum_updateUsedAndComment('C:/Users/dmccloskey-sbrg/Desktop/dataStage01IsotopomerAveragesNormSum_WTEColi_113C80_U13C20_01_update.csv');
## export the spectrums to .js
#ave01.export_dataStage01IsotopomerAveragesNormSum_csv('WTEColi_113C80_U13C20_01',pg_settings.datadir_settings['workspace_data']+'/_output/WTEColi_113C80_U13C20_01_averagesNormSum.csv');
# plot specific scan-types and met_ids
ave01.export_dataStage01IsotopomerAveragesNormSum_js('ALEsKOs01',
    sample_name_abbreviations_I=[
     "OxicEvo04ptsHIcrrEcoli13CGlc",
     "OxicEvo04ptsHIcrrEvo01EPEcoli13CGlc",
    ],
#     met_ids_I=[
#         #'fad',
#          'pyr',
#          'phpyr',
#     ],
    #scan_types_I=['EPI'],
    single_plot_I = False,
    );



##make the spectrumAccuracy methods tables
#from SBaaS_isotopomer.stage01_isotopomer_spectrumAccuracy_execute import stage01_isotopomer_spectrumAccuracy_execute
#specaccuracy01 = stage01_isotopomer_spectrumAccuracy_execute(session,engine,pg_settings.datadir_settings);
#specaccuracy01.drop_dataStage01_isotopomer_spectrumAccuracy();
#specaccuracy01.initialize_dataStage01_isotopomer_spectrumAccuracy();
#specaccuracy01.reset_dataStage01_isotopomer_spectrumAccuracy('chemoCLim01');

##make the QC methods tables
#from SBaaS_isotopomer.stage01_isotopomer_QCs_execute import stage01_isotopomer_QCs_execute
#exqcs01 = stage01_isotopomer_QCs_execute(session,engine,pg_settings.datadir_settings);
#exqcs01.drop_dataStage01_isotopomer_QCs();
#exqcs01.initialize_dataStage01_isotopomer_QCs();
#exqcs01.reset_dataStage01_isotopomer_QCs('chemoCLim01');