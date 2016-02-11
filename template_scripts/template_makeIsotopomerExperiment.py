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

# initialize the msMethod information
from SBaaS_LIMS.lims_msMethod_execute import lims_msMethod_execute
limssample = lims_msMethod_execute(session,engine,pg_settings.datadir_settings);
limssample.drop_lims_msMethod();
limssample.initialize_lims_msMethod();
limssample.reset_lims_msMethod();
# add in additional compounds

# export the new acquisition method

# initialize the sample information
from SBaaS_LIMS.lims_sample_execute import lims_sample_execute
limssample = lims_sample_execute(session,engine,pg_settings.datadir_settings);
limssample.drop_lims_sample();
limssample.initialize_lims_sample();
limssample.reset_lims_sample();

# initialize the experiment
from SBaaS_LIMS.lims_experiment_execute import lims_experiment_execute
limsexperiment = lims_experiment_execute(session,engine,pg_settings.datadir_settings);
limsexperiment.drop_lims_experimentTypes();
limsexperiment.initialize_lims_experimentTypes();
limsexperiment.reset_lims_experimentTypes();
limsexperiment.drop_lims_experiment();
limsexperiment.initialize_lims_experiment();
limsexperiment.reset_lims_experiment('chemoCLim01');
limsexperiment.execute_deleteExperiments(['ALEsKOs01'],["141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-2","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-2-10.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-2-100.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-2-1000.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-3","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-3-10.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-3-100.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-3-1000.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-5","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-5-10.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-5-100.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-5-1000.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-6","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-6-10.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-6-100.0x","141021_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-6-1000.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-1","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-1-10.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-1-100.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-1-1000.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-2","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-2-10.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-2-100.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-2-1000.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-3","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-3-10.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-3-100.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-3-1000.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-4","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-4-10.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-4-100.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-4-1000.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-5","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-5-10.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-5-100.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-5-1000.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-6","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-6-10.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-6-100.0x","141022_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Broth-6-1000.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-1","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-1-10.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-1-100.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-1-1000.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-2","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-2-10.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-2-100.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-2-1000.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-3","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-3-10.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-3-100.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-3-1000.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-4","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-4-10.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-4-100.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-4-1000.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-5","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-5-10.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-5-100.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-5-1000.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-6","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-6-10.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-6-100.0x","141022_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Broth-6-1000.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-1","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-1-10.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-1-100.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-1-1000.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-2","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-2-10.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-2-100.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-2-1000.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-3","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-3-10.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-3-100.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-3-1000.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-4","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-4-10.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-4-100.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-4-1000.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-5","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-5-10.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-5-100.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-5-1000.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-6","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-6-10.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-6-100.0x","141022_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Broth-6-1000.0x","141104_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Filtrate-1","141104_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Filtrate-1-10.0x","141104_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Filtrate-1-100.0x","141104_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Filtrate-1-1000.0x","141104_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Filtrate-4","141104_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Filtrate-4-10.0x","141104_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Filtrate-4-100.0x","141104_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Filtrate-4-1000.0x","141104_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Filtrate-1","141104_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Filtrate-1-10.0x","141104_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Filtrate-1-100.0x","141104_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Filtrate-1-1000.0x","141104_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Filtrate-4","141104_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Filtrate-4-10.0x","141104_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Filtrate-4-100.0x","141104_11_OxicEvo04tpiAEvo02EPEcoli13CGlcM9_Filtrate-4-1000.0x","141104_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Filtrate-1","141104_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Filtrate-1-10.0x","141104_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Filtrate-1-100.0x","141104_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Filtrate-1-1000.0x","141104_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Filtrate-4","141104_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Filtrate-4-10.0x","141104_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Filtrate-4-100.0x","141104_11_OxicEvo04tpiAEvo03EPEcoli13CGlcM9_Filtrate-4-1000.0x","141104_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Filtrate-1","141104_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Filtrate-1-10.0x","141104_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Filtrate-1-100.0x","141104_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Filtrate-1-1000.0x","141104_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Filtrate-4","141104_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Filtrate-4-10.0x","141104_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Filtrate-4-100.0x","141104_11_OxicEvo04tpiAEvo04EPEcoli13CGlcM9_Filtrate-4-1000.0x","141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1","141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1-10.0x","141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1-100.0x","141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-1-1000.0x","141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4","141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-10.0x","141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-100.0x","141125_11_OxicEvo04tpiAEvo01EPEcoli13CGlcM9_Broth-4-1000.0x"]);
limsexperiment.execute_makeExperimentFromSampleFile('data/tests/analysis_isotopomer/141104_Isotopomer_ALEsKOs01_sampleFile02.csv',
                                                 1,[10.0,100.0,1000.0]);
#TODO: link exp_type_id = 5 with isotopomer
#sample_name and sample_id are unique
#sample_name_short and sample_name_abbreviation are not and can come from multiple experiment types from within the same experiment
# export the analyst acquisition batch files
limsexperiment.execute_makeBatchFile('ALEsKOs01', '150408','data/tests/analysis_isotopomer/150408_Isotopomer_ALEsKOs01_samplFile05.txt',experiment_type_I=5);